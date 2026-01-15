#!/usr/bin/env python3
"""
Adaptive Distribution - Select question distribution based on content type

Provides different question type distributions for:
- conceptual: Heavy on Conceptual Distinction, Critical Evaluation
- procedural: Mixed with procedural focus
- coding: Heavy on Specification Design, Architecture Analysis
- mixed: Balanced default
"""

from dataclasses import dataclass
from typing import Dict
from enum import Enum


class ContentType(Enum):
    """Supported content types"""
    CONCEPTUAL = "conceptual"
    PROCEDURAL = "procedural"
    CODING = "coding"
    MIXED = "mixed"


@dataclass
class Distribution:
    """Question type distribution"""
    precision_recall: float  # 10%
    conceptual_distinction: float  # 15%
    decision_matrix: float  # 12.5%
    architecture_analysis: float  # 12.5%
    specification_design: float  # 10%
    critical_evaluation: float  # 12.5%
    strategic_synthesis: float  # 10%
    research_extension: float  # 7.5%
    economic_quantitative: float  # 10%

    def validate(self) -> bool:
        """Validate that all percentages sum to ~100%"""
        total = sum([
            self.precision_recall,
            self.conceptual_distinction,
            self.decision_matrix,
            self.architecture_analysis,
            self.specification_design,
            self.critical_evaluation,
            self.strategic_synthesis,
            self.research_extension,
            self.economic_quantitative
        ])
        return 99.0 <= total <= 101.0

    def to_dict(self) -> Dict[str, float]:
        """Convert to dictionary for display"""
        return {
            "Precision Recall": self.precision_recall,
            "Conceptual Distinction": self.conceptual_distinction,
            "Decision Matrix": self.decision_matrix,
            "Architecture Analysis": self.architecture_analysis,
            "Specification Design": self.specification_design,
            "Critical Evaluation": self.critical_evaluation,
            "Strategic Synthesis": self.strategic_synthesis,
            "Research Extension": self.research_extension,
            "Economic/Quantitative": self.economic_quantitative
        }


# Distribution Tables

DISTRIBUTION_CONCEPTUAL = Distribution(
    precision_recall=12.0,
    conceptual_distinction=22.0,  # +7% from default
    decision_matrix=10.0,
    architecture_analysis=10.0,
    specification_design=5.0,
    critical_evaluation=18.0,  # +5.5% from default
    strategic_synthesis=10.0,
    research_extension=7.0,
    economic_quantitative=6.0
)

DISTRIBUTION_PROCEDURAL = Distribution(
    precision_recall=10.0,
    conceptual_distinction=12.0,
    decision_matrix=13.0,
    architecture_analysis=13.0,
    specification_design=12.0,
    critical_evaluation=12.0,
    strategic_synthesis=11.0,
    research_extension=8.0,
    economic_quantitative=8.0
)

DISTRIBUTION_CODING = Distribution(
    precision_recall=8.0,
    conceptual_distinction=10.0,
    decision_matrix=15.0,
    architecture_analysis=15.0,  # +2.5% from default
    specification_design=18.0,  # +8% from default
    critical_evaluation=8.0,
    strategic_synthesis=10.0,
    research_extension=7.0,
    economic_quantitative=9.0
)

DISTRIBUTION_MIXED = Distribution(
    precision_recall=10.0,
    conceptual_distinction=15.0,
    decision_matrix=12.5,
    architecture_analysis=12.5,
    specification_design=10.0,
    critical_evaluation=12.5,
    strategic_synthesis=10.0,
    research_extension=7.5,
    economic_quantitative=10.0
)

# Map content types to distributions
DISTRIBUTIONS = {
    ContentType.CONCEPTUAL: DISTRIBUTION_CONCEPTUAL,
    ContentType.PROCEDURAL: DISTRIBUTION_PROCEDURAL,
    ContentType.CODING: DISTRIBUTION_CODING,
    ContentType.MIXED: DISTRIBUTION_MIXED,
}

# Validate all distributions on import
for dist in DISTRIBUTIONS.values():
    if not dist.validate():
        raise ValueError(f"Invalid distribution: {dist}")


def select_distribution(content_type: str) -> Distribution:
    """
    Select appropriate distribution for content type.

    Args:
        content_type: "conceptual", "procedural", "coding", or "mixed"

    Returns:
        Distribution object with question type percentages
    """
    try:
        content_enum = ContentType(content_type.lower())
    except ValueError:
        print(f"Warning: Unknown content type '{content_type}', using 'mixed'")
        content_enum = ContentType.MIXED

    return DISTRIBUTIONS[content_enum]


def calculate_recommended_questions(
    concept_count: int,
    lesson_count: int,
    content_type: str = "mixed"
) -> int:
    """
    Calculate recommended question count.

    Uses heuristic:
    - 1-3 concepts per lesson minimum
    - 2-3 questions per concept
    - Adjusted for content type

    Args:
        concept_count: Total concepts in content
        lesson_count: Number of lessons
        content_type: "conceptual", "procedural", "coding", or "mixed"

    Returns:
        Recommended question count (25-250 range)
    """
    if concept_count == 0:
        concept_count = max(1, lesson_count * 8)  # Estimate

    # Base calculation: 2 questions per concept
    base_questions = concept_count * 2

    # Type adjustments
    if content_type == "conceptual":
        # Conceptual needs more questions for deep understanding
        multiplier = 1.3
    elif content_type == "coding":
        # Coding needs practical verification
        multiplier = 1.2
    elif content_type == "procedural":
        # Procedural needs step verification
        multiplier = 1.1
    else:  # mixed
        multiplier = 1.0

    recommended = int(base_questions * multiplier)

    # Clamp to reasonable range
    recommended = max(25, min(250, recommended))

    return recommended


def get_distribution_rationale(content_type: str) -> str:
    """Get explanation of why this distribution was chosen"""
    rationales = {
        ContentType.CONCEPTUAL: """
Conceptual-focused content emphasizes deep understanding:
  • Conceptual Distinction +7% (distinguish related ideas)
  • Critical Evaluation +5.5% (judge trade-offs)
  Ideal for: Frameworks, paradigms, mental models""",
        ContentType.CODING: """
Coding-focused content emphasizes hands-on skills:
  • Specification Design +8% (apply patterns)
  • Architecture Analysis +2.5% (system understanding)
  Ideal for: Implementation, API design, deployment""",
        ContentType.PROCEDURAL: """
Procedural content balances understanding with application:
  • Even distribution across types
  • Emphasis on Decision Matrix, Architecture Analysis
  Ideal for: Tutorials, guides, step-by-step learning""",
        ContentType.MIXED: """
Balanced content uses default distribution:
  • Equal emphasis across all question types
  Ideal for: Comprehensive courses, multi-topic chapters"""
    }
    try:
        content_enum = ContentType(content_type.lower())
        return rationales[content_enum]
    except (ValueError, KeyError):
        return rationales[ContentType.MIXED]


def format_distribution_summary(content_type: str, question_count: int) -> str:
    """Format distribution selection for user display"""
    dist = select_distribution(content_type)
    rationale = get_distribution_rationale(content_type)

    summary = f"""Question Type Distribution:

Content Type: {content_type.upper()}
Question Count: {question_count}
{rationale}

Distribution breakdown:
"""
    for question_type, percentage in dist.to_dict().items():
        questions_of_type = int(question_count * percentage / 100)
        summary += f"  • {question_type}: {percentage:.1f}% ({questions_of_type} questions)\n"

    return summary


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: adaptive_distribution.py <content_type> [question_count]")
        print("Content types: conceptual, procedural, coding, mixed")
        sys.exit(1)

    content_type = sys.argv[1]
    question_count = int(sys.argv[2]) if len(sys.argv) > 2 else 150

    print(format_distribution_summary(content_type, question_count))

    # Show recommended count for different concept counts
    print("\nRecommended counts by concept size:")
    for concepts in [20, 50, 100]:
        recommended = calculate_recommended_questions(concepts, concepts // 8, content_type)
        print(f"  {concepts} concepts → {recommended} questions")

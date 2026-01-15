#!/usr/bin/env python3
"""
Content Classifier - Detect lesson content type

Classifies lessons as:
- "conceptual": Theory, frameworks, understanding-focused
- "procedural": Step-by-step guides, how-to content
- "coding": Code implementation, technical hands-on
- "mixed": Balanced mix of multiple types
"""

import re
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass
from collections import Counter


@dataclass
class LessonClassification:
    content_type: str  # "conceptual", "procedural", "coding", "mixed"
    scores: Dict[str, float]  # scores per type (0-100)
    indicators: Dict[str, int]  # raw indicator counts
    confidence: float  # 0-100


def extract_yaml_frontmatter(content: str) -> Dict:
    """
    Extract YAML frontmatter from markdown (simplified parsing without yaml library).

    Returns dict with basic frontmatter fields.
    """
    if not content.startswith("---"):
        return {}

    lines = content.split("\n")
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if not end_idx:
        return {}

    # Simple parsing: extract key: value pairs
    frontmatter = {}
    for line in lines[1:end_idx]:
        if ':' in line and not line.strip().startswith('#'):
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            # Try to parse as list or simple value
            if value.startswith('[') and value.endswith(']'):
                # Simple list parsing
                items = [item.strip() for item in value[1:-1].split(',')]
                frontmatter[key] = items
            elif value.lower() in ['true', 'false']:
                frontmatter[key] = value.lower() == 'true'
            else:
                frontmatter[key] = value

    return frontmatter


def count_code_blocks(content: str) -> int:
    """Count markdown code blocks (```...```  or ~~~...~~~)"""
    # Remove frontmatter first
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2]

    # Count backtick code blocks
    backtick_blocks = len(re.findall(r"```[\s\S]*?```", content))

    # Count tilde code blocks
    tilde_blocks = len(re.findall(r"~~~[\s\S]*?~~~", content))

    return backtick_blocks + tilde_blocks


def count_inline_code(content: str) -> int:
    """Count inline code snippets (`code`)"""
    # Remove code blocks first
    content = re.sub(r"```[\s\S]*?```", "", content)
    content = re.sub(r"~~~[\s\S]*?~~~", "", content)

    # Count backtick-enclosed text
    return len(re.findall(r"`[^`]+`", content))


def count_headings(content: str) -> Dict[int, int]:
    """Count headings by level (# ## ### etc)"""
    headings = Counter()
    for line in content.split("\n"):
        match = re.match(r"^(#+)\s+", line)
        if match:
            level = len(match.group(1))
            headings[level] += 1
    return dict(headings)


def count_keywords(content: str, keywords: List[str]) -> int:
    """Count occurrences of keyword list (case-insensitive)"""
    content_lower = content.lower()
    count = 0
    for keyword in keywords:
        count += len(re.findall(rf"\b{re.escape(keyword)}\b", content_lower))
    return count


def count_try_with_ai_sections(content: str) -> int:
    """Count 'Try With AI' or similar prompt sections"""
    patterns = [
        r"Try With AI",
        r"Try this in Claude",
        r"Prompt to try",
        r"Copy-paste this",
        r"## Try",
    ]
    count = 0
    for pattern in patterns:
        count += len(re.findall(pattern, content, re.IGNORECASE))
    return count


def extract_skills_from_frontmatter(frontmatter: Dict) -> List[str]:
    """Extract skill categories from YAML frontmatter"""
    skills = frontmatter.get("skills", [])
    if not isinstance(skills, list):
        return []

    categories = []
    for skill in skills:
        if isinstance(skill, dict):
            category = skill.get("category", "")
            if category:
                categories.append(category.lower())
        elif isinstance(skill, str):
            # Sometimes skills are just strings
            categories.append(skill.lower())

    return categories


def classify_single_lesson(lesson_path: Path) -> LessonClassification:
    """
    Classify a single lesson file.

    Returns LessonClassification with type and scores.
    """
    try:
        with open(lesson_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Warning: Could not read {lesson_path}: {e}")
        return LessonClassification("mixed", {}, {}, 0)

    # Extract frontmatter
    frontmatter = extract_yaml_frontmatter(content)

    # Count indicators
    indicators = {}

    # 1. Code blocks (>10 = coding)
    indicators["code_blocks"] = count_code_blocks(content)

    # 2. Inline code (high = coding/procedural)
    indicators["inline_code"] = count_inline_code(content)

    # 3. Try With AI sections (>5 = procedural)
    indicators["try_with_ai"] = count_try_with_ai_sections(content)

    # 4. Heading structure (deep nesting = procedural/coding)
    headings = count_headings(content)
    indicators["avg_heading_level"] = sum(
        level * count for level, count in headings.items()
    ) / max(sum(headings.values()), 1)

    # 5. Conceptual keywords
    conceptual_keywords = [
        "understand", "concept", "theory", "framework", "paradigm",
        "principles", "architecture", "design pattern", "model",
        "mental model", "why", "how it works"
    ]
    indicators["conceptual_keywords"] = count_keywords(content, conceptual_keywords)

    # 6. Procedural keywords
    procedural_keywords = [
        "step", "tutorial", "guide", "follow", "instructions",
        "how to", "setup", "configure", "install", "example",
        "exercise", "practice", "try", "implement"
    ]
    indicators["procedural_keywords"] = count_keywords(content, procedural_keywords)

    # 7. Technical keywords
    technical_keywords = [
        "function", "class", "variable", "loop", "condition",
        "algorithm", "api", "endpoint", "deploy", "server",
        "database", "framework", "library", "module", "package"
    ]
    indicators["technical_keywords"] = count_keywords(content, technical_keywords)

    # 8. Skills category from frontmatter
    skills = extract_skills_from_frontmatter(frontmatter)
    indicators["has_technical_skills"] = 1 if "technical" in skills else 0
    indicators["has_conceptual_skills"] = 1 if "conceptual" in skills else 0

    # Calculate scores (0-100)
    scores = {}

    # Conceptual score
    conceptual_score = 0
    conceptual_score += min(indicators.get("conceptual_keywords", 0) * 5, 30)
    conceptual_score += indicators.get("has_conceptual_skills", 0) * 20
    conceptual_score += max(0, 20 - indicators.get("code_blocks", 0) * 2)  # Inverse
    conceptual_score += max(0, 20 - indicators.get("try_with_ai", 0) * 2)  # Inverse
    scores["conceptual"] = min(100, conceptual_score)

    # Procedural score
    procedural_score = 0
    procedural_score += min(indicators.get("procedural_keywords", 0) * 3, 25)
    procedural_score += min(indicators.get("try_with_ai", 0) * 8, 30)
    procedural_score += min(indicators.get("code_blocks", 0) * 2, 25)
    procedural_score += max(0, 20 - indicators.get("technical_keywords", 0) * 0.5)
    scores["procedural"] = min(100, procedural_score)

    # Coding score
    coding_score = 0
    coding_score += min(indicators.get("code_blocks", 0) * 6, 40)
    coding_score += min(indicators.get("inline_code", 0) * 1.5, 20)
    coding_score += min(indicators.get("technical_keywords", 0) * 2, 30)
    coding_score += indicators.get("has_technical_skills", 0) * 10
    scores["coding"] = min(100, coding_score)

    # Normalize scores
    total = sum(scores.values())
    if total > 0:
        scores = {k: (v / total) * 100 for k, v in scores.items()}

    # Determine primary type and confidence
    max_score = max(scores.values())
    primary_type = max(scores, key=scores.get)

    # Confidence: how much higher is primary than second-best?
    sorted_scores = sorted(scores.values(), reverse=True)
    confidence = sorted_scores[0] - sorted_scores[1] if len(sorted_scores) > 1 else 50

    return LessonClassification(
        content_type=primary_type,
        scores=scores,
        indicators=indicators,
        confidence=confidence
    )


def detect_content_type(lesson_files: List[Path]) -> Dict:
    """
    Classify multiple lessons and aggregate.

    Returns:
    {
        "primary_type": "conceptual" | "procedural" | "coding" | "mixed",
        "percentages": {"conceptual": 70, "procedural": 20, "coding": 10},
        "lessons": [
            {"file": "...", "type": "conceptual", "scores": {...}, "confidence": ...},
            ...
        ],
        "confidence": 85  # Overall confidence
    }
    """
    if not lesson_files:
        return {
            "primary_type": "mixed",
            "percentages": {},
            "lessons": [],
            "confidence": 0
        }

    classifications = []
    for lesson_file in lesson_files:
        clf = classify_single_lesson(lesson_file)
        classifications.append({
            "file": lesson_file.name,
            "type": clf.content_type,
            "scores": clf.scores,
            "indicators": clf.indicators,
            "confidence": clf.confidence
        })

    # Aggregate: count types
    type_counts = Counter(c["type"] for c in classifications)
    total = len(classifications)
    percentages = {
        t: round(count / total * 100, 1)
        for t, count in type_counts.items()
    }

    # Determine primary type
    if percentages.get("conceptual", 0) > 60:
        primary_type = "conceptual"
    elif percentages.get("coding", 0) > 40:
        primary_type = "coding"
    elif percentages.get("procedural", 0) > 50:
        primary_type = "procedural"
    else:
        primary_type = "mixed"

    # Overall confidence: how dominant is primary type?
    primary_pct = percentages.get(primary_type, 0)
    overall_confidence = primary_pct if primary_type != "mixed" else 50

    return {
        "primary_type": primary_type,
        "percentages": percentages,
        "lessons": classifications,
        "confidence": overall_confidence,
        "lesson_count": total
    }


def format_classification_summary(result: Dict) -> str:
    """Format classification result for user display"""
    primary = result["primary_type"]
    percentages = result["percentages"]
    confidence = result["confidence"]
    lesson_count = result.get("lesson_count", 0)

    pct_str = " / ".join(
        f"{pct}% {t}" for t, pct in percentages.items()
    )

    summary = f"""Content Type Analysis:

Primary: {primary.upper()}
Distribution: {pct_str}
Lessons analyzed: {lesson_count}
Confidence: {confidence:.0f}%"""

    return summary


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: content_classifier.py <lesson_file_or_directory>")
        sys.exit(1)

    path = Path(sys.argv[1])

    if path.is_file():
        clf = classify_single_lesson(path)
        print(f"Content Type: {clf.content_type}")
        print(f"Scores: {clf.scores}")
        print(f"Confidence: {clf.confidence:.1f}%")
    elif path.is_dir():
        lesson_files = sorted(path.glob("*.md"))
        result = detect_content_type(lesson_files)
        print(format_classification_summary(result))
        print("\nDetailed breakdown:")
        for lesson in result["lessons"]:
            print(f"  {lesson['file']}: {lesson['type']} ({lesson['confidence']:.0f}% confidence)")

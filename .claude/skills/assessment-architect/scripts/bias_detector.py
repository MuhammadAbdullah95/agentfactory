#!/usr/bin/env python3
"""
Bias Detector - Detect and remediate three types of exam biases

Detects:
1. Length Bias: Correct answers consistently longest/shortest
2. Position Bias: Correct answers favor B/C over A/D
3. Specificity Bias: Correct answers more detailed than distractors
"""

import re
import json
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from collections import Counter

from config import (
    BIAS_THRESHOLDS,
    SPECIFICITY_WEIGHTS,
    SEQUENCES,
    get_sequence
)


@dataclass
class Question:
    """Parsed exam question"""
    number: int
    text: str
    options: List[str]  # [A, B, C, D]
    correct_option: int  # 0=A, 1=B, 2=C, 3=D
    explanation: str
    source_section: Optional[str] = None


@dataclass
class BiasReport:
    """Bias detection report"""
    bias_type: str
    bias_detected: bool
    severity: str  # "none", "low", "medium", "high"
    percentage: float  # % of questions affected
    issues: List[str]
    statistics: Dict
    remediation: Optional[str] = None
    remediation_applied: bool = False


class BiasDetector:
    """Detects and remediates exam biases"""

    def __init__(self, questions: List[Question]):
        self.questions = questions
        self.reports = []

    def detect_length_bias(self) -> BiasReport:
        """
        Detect if correct answers are consistently longest or shortest.

        Returns BiasReport with severity and statistics.
        """
        if not self.questions:
            return BiasReport("length", False, "none", 0, [], {})

        rankings = []
        for q in self.questions:
            # Rank options by word count
            word_counts = [(i, len(opt.split())) for i, opt in enumerate(q.options)]
            sorted_by_length = sorted(word_counts, key=lambda x: x[1])

            # Find rank of correct answer (0=shortest, 3=longest)
            for rank, (idx, _) in enumerate(sorted_by_length):
                if idx == q.correct_option:
                    rankings.append(rank)
                    break

        # Analyze distribution
        rank_counts = Counter(rankings)
        shortest_pct = rank_counts[0] / len(self.questions)
        longest_pct = rank_counts[3] / len(self.questions)
        middle_pct = (rank_counts[1] + rank_counts[2]) / len(self.questions)

        # Determine severity
        high_threshold = BIAS_THRESHOLDS['length']['high']
        medium_threshold = BIAS_THRESHOLDS['length']['medium']
        low_threshold = BIAS_THRESHOLDS['length']['low']

        issues = []
        if shortest_pct >= high_threshold:
            severity = "high"
            issues.append(f"Correct answers TOO SHORT: {shortest_pct:.1%}")
            bias_detected = True
        elif longest_pct >= high_threshold:
            severity = "high"
            issues.append(f"Correct answers TOO LONG: {longest_pct:.1%}")
            bias_detected = True
        elif shortest_pct >= medium_threshold or longest_pct >= medium_threshold:
            severity = "medium"
            if shortest_pct >= medium_threshold:
                issues.append(f"Correct answers tend SHORT: {shortest_pct:.1%}")
            if longest_pct >= medium_threshold:
                issues.append(f"Correct answers tend LONG: {longest_pct:.1%}")
            bias_detected = True
        elif shortest_pct >= low_threshold or longest_pct >= low_threshold:
            severity = "low"
            bias_detected = True
            if shortest_pct >= low_threshold:
                issues.append(f"Slight short bias: {shortest_pct:.1%}")
            if longest_pct >= low_threshold:
                issues.append(f"Slight long bias: {longest_pct:.1%}")
        else:
            severity = "none"
            bias_detected = False
            issues.append("No significant length bias detected")

        # Determine which is problematic
        if shortest_pct > longest_pct:
            max_pct = shortest_pct
        else:
            max_pct = longest_pct

        return BiasReport(
            bias_type="length",
            bias_detected=bias_detected,
            severity=severity,
            percentage=max(shortest_pct, longest_pct) * 100,
            issues=issues,
            statistics={
                "shortest_pct": round(shortest_pct, 3),
                "longest_pct": round(longest_pct, 3),
                "middle_pct": round(middle_pct, 3),
                "rank_distribution": dict(rank_counts)
            },
            remediation="Swap option texts to balance distribution" if bias_detected else None
        )

    def detect_position_bias(self) -> BiasReport:
        """
        Detect if correct answers cluster in middle (B/C) vs outer (A/D) positions.

        Uses thresholds from BIAS_THRESHOLDS['position'].
        Returns BiasReport with severity and statistics.
        """
        if not self.questions:
            return BiasReport("position", False, "none", 0, [], {})

        position_counts = {0: 0, 1: 0, 2: 0, 3: 0}  # A, B, C, D
        for q in self.questions:
            position_counts[q.correct_option] += 1

        n = len(self.questions)
        position_pcts = {pos: count / n for pos, count in position_counts.items()}

        # Middle vs outer analysis
        middle_pct = position_pcts[1] + position_pcts[2]  # B + C
        outer_pct = position_pcts[0] + position_pcts[3]   # A + D

        thresholds = BIAS_THRESHOLDS['position']
        issues = []
        severity = "none"
        bias_detected = False

        # Check middle/outer thresholds
        if middle_pct > thresholds['middle_max']:
            severity = "high"
            bias_detected = True
            issues.append(f"MIDDLE BIAS: B+C = {middle_pct:.1%} (threshold: ≤{thresholds['middle_max']:.0%})")

        if outer_pct < thresholds['outer_min']:
            if severity != "high":
                severity = "high"
            bias_detected = True
            issues.append(f"OUTER UNDERREP: A+D = {outer_pct:.1%} (threshold: ≥{thresholds['outer_min']:.0%})")

        # Check individual letter thresholds
        letter_names = ['A', 'B', 'C', 'D']
        individual_issues = []
        for pos, pct in position_pcts.items():
            if pct < thresholds['letter_min'] or pct > thresholds['letter_max']:
                bias_detected = True
                if severity == "none":
                    severity = "medium"
                letter = letter_names[pos]
                individual_issues.append(
                    f"{letter} = {pct:.1%} (acceptable: {thresholds['letter_min']:.0%}-{thresholds['letter_max']:.0%})"
                )

        if individual_issues and severity != "high":
            issues.extend(individual_issues)

        if not bias_detected:
            issues.append("No position bias detected")

        return BiasReport(
            bias_type="position",
            bias_detected=bias_detected,
            severity=severity,
            percentage=max(middle_pct, 1 - outer_pct) * 100,
            issues=issues,
            statistics={
                "position_distribution": {letter: round(pct, 3) for letter, pct in zip(letter_names, position_pcts.values())},
                "middle_pct": round(middle_pct, 3),
                "outer_pct": round(outer_pct, 3),
                "position_counts": position_counts
            },
            remediation="Apply pre-made sequence to redistribute" if bias_detected else None
        )

    def detect_specificity_bias(self) -> BiasReport:
        """
        Detect if correct answers are consistently more specific/detailed than distractors.

        Specificity score combines: word count, examples, qualifiers, technical density.
        Returns BiasReport with affected questions.
        """
        if not self.questions:
            return BiasReport("specificity", False, "none", 0, [], {})

        def calculate_specificity_score(option_text: str) -> float:
            """Calculate specificity score (0-100)"""
            score = 0.0

            # Factor 1: Word count
            word_count = len(option_text.split())
            score += min(word_count * SPECIFICITY_WEIGHTS['word_count']['weight'],
                        SPECIFICITY_WEIGHTS['word_count']['max_points'])

            # Factor 2: Examples
            example_count = sum(1 for p in SPECIFICITY_WEIGHTS['examples']['patterns']
                              if p in option_text.lower())
            score += min(example_count * SPECIFICITY_WEIGHTS['examples']['points_per_example'],
                        SPECIFICITY_WEIGHTS['examples']['max_points'])

            # Factor 3: Qualifiers
            qualifier_count = sum(1 for q in SPECIFICITY_WEIGHTS['qualifiers']['patterns']
                                if q in option_text.lower())
            score += min(qualifier_count * SPECIFICITY_WEIGHTS['qualifiers']['points_per_qualifier'],
                        SPECIFICITY_WEIGHTS['qualifiers']['max_points'])

            # Factor 4: Technical term density
            words = option_text.split()
            capitalized = sum(1 for w in words if len(w) > 1 and w[0].isupper())
            technical_density = capitalized / max(len(words), 1)
            score += technical_density * SPECIFICITY_WEIGHTS['technical_density']['weight']

            return min(score, 100)

        bias_count = 0
        affected_questions = []

        for idx, q in enumerate(self.questions):
            scores = [calculate_specificity_score(opt) for opt in q.options]
            correct_score = scores[q.correct_option]

            # Avg distractor score
            distractor_scores = [s for i, s in enumerate(scores) if i != q.correct_option]
            avg_distractor = sum(distractor_scores) / len(distractor_scores)

            # Check if correct significantly more specific
            if avg_distractor > 0:
                gap = (correct_score - avg_distractor) / avg_distractor
                if gap > BIAS_THRESHOLDS['specificity']['score_gap']:
                    bias_count += 1
                    affected_questions.append({
                        'question_num': idx + 1,
                        'correct_score': round(correct_score, 1),
                        'avg_distractor': round(avg_distractor, 1),
                        'gap_pct': f"{gap:.1%}"
                    })

        bias_pct = bias_count / len(self.questions) if self.questions else 0

        # Determine severity
        high_threshold = BIAS_THRESHOLDS['specificity']['question_pct_high']
        medium_threshold = BIAS_THRESHOLDS['specificity']['question_pct_medium']
        low_threshold = BIAS_THRESHOLDS['specificity']['question_pct_low']

        if bias_pct > high_threshold:
            severity = "high"
            issues = [f"CRITICAL: {bias_count} questions ({bias_pct:.1%}) show specificity bias"]
        elif bias_pct > medium_threshold:
            severity = "medium"
            issues = [f"WARNING: {bias_count} questions ({bias_pct:.1%}) show specificity bias"]
        elif bias_pct > low_threshold:
            severity = "low"
            issues = [f"INFO: {bias_count} questions ({bias_pct:.1%}) show specificity bias"]
        else:
            severity = "none"
            issues = ["No significant specificity bias detected"]

        if affected_questions and len(affected_questions) <= 5:
            issues.append(f"Affected questions: {[q['question_num'] for q in affected_questions]}")

        return BiasReport(
            bias_type="specificity",
            bias_detected=bias_pct > low_threshold,
            severity=severity,
            percentage=bias_pct * 100,
            issues=issues,
            statistics={
                "affected_count": bias_count,
                "affected_questions": affected_questions
            },
            remediation="Flag for manual review (semantic complexity)" if bias_pct > low_threshold else None
        )

    def remediate_length_bias(self, report: BiasReport) -> bool:
        """
        Remediate length bias by swapping option texts.

        Returns True if remediation successful, False if failed.
        """
        if not report.bias_detected:
            return True

        # Rank options by word count and reorder
        for q in self.questions:
            word_counts = [(i, len(opt.split())) for i, opt in enumerate(q.options)]
            sorted_indices = sorted(range(4), key=lambda i: word_counts[i][1])

            # If correct answer is at extreme (shortest or longest), move it to middle
            correct_rank = sorted_indices.index(q.correct_option)
            if correct_rank in [0, 3]:  # At extreme
                # Swap with middle position
                new_rank = 1 if correct_rank == 3 else 2
                swap_index = sorted_indices[new_rank]

                # Swap options
                q.options[q.correct_option], q.options[swap_index] = \
                    q.options[swap_index], q.options[q.correct_option]

                # Update correct option index
                q.correct_option = swap_index

        report.remediation_applied = True
        return True

    def remediate_position_bias(self, sequence_id: str = 'random') -> bool:
        """
        Remediate position bias by applying pre-made sequence.

        Returns True if successful.
        """
        try:
            sequence = get_sequence(sequence_id)
        except ValueError as e:
            print(f"Error getting sequence: {e}")
            return False

        # Apply sequence to questions
        for i, q in enumerate(self.questions):
            target_idx = sequence[i % len(sequence)]

            if q.correct_option != target_idx:
                # Swap option texts
                q.options[q.correct_option], q.options[target_idx] = \
                    q.options[target_idx], q.options[q.correct_option]

                # Update index
                q.correct_option = target_idx

        return True

    def run_validation(self, fix_auto: bool = False) -> Tuple[bool, List[BiasReport]]:
        """
        Run all bias detection and optional auto-remediation.

        Returns (passed, [BiasReport])
        """
        # Run all checks
        length_report = self.detect_length_bias()
        position_report = self.detect_position_bias()
        specificity_report = self.detect_specificity_bias()

        self.reports = [length_report, position_report, specificity_report]

        # Auto-fix if requested
        if fix_auto:
            if length_report.bias_detected and length_report.severity in ["medium", "high"]:
                self.remediate_length_bias(length_report)
            if position_report.bias_detected:
                self.remediate_position_bias()

            # Specificity always manual
            if specificity_report.bias_detected:
                specificity_report.issues.append("Manual review recommended")

        # Overall pass/fail
        passed = not any(r.bias_detected and r.severity == "high"
                        for r in self.reports)

        return passed, self.reports

    def format_report(self) -> str:
        """Format validation report for display"""
        lines = []
        lines.append("=" * 60)
        lines.append("BIAS DETECTION REPORT")
        lines.append("=" * 60)
        lines.append("")

        all_passed = True
        for report in self.reports:
            status_symbol = "✓" if not report.bias_detected else "⚠" if report.severity in ["low", "medium"] else "✗"
            lines.append(f"{status_symbol} {report.bias_type.upper()}: {report.severity.upper()}")
            lines.append(f"   {report.percentage:.1f}% affected")

            for issue in report.issues:
                lines.append(f"   • {issue}")

            if report.remediation_applied:
                lines.append(f"   ✓ Remediation applied")

            lines.append("")

            if report.severity == "high":
                all_passed = False

        lines.append("=" * 60)
        if all_passed:
            lines.append("OVERALL: PASS")
        else:
            lines.append("OVERALL: FAIL (critical issues detected)")
        lines.append("=" * 60)

        return "\n".join(lines)


def parse_exam_file(filepath: Path) -> List[Question]:
    """Parse exam markdown file into Question objects"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    questions = []
    question_blocks = re.split(r'\n## Q\d+:', content)

    for block_idx, block in enumerate(question_blocks[1:], 1):
        lines = block.strip().split('\n')
        if len(lines) < 6:
            continue

        # Parse question text (first lines until we hit **A)**)
        q_text_lines = []
        idx = 0
        for idx, line in enumerate(lines):
            if line.startswith('**A)') or line.startswith('**A **'):
                break
            q_text_lines.append(line)

        q_text = '\n'.join(q_text_lines).strip()

        # Parse options
        options = []
        correct_option = None
        for i, line in enumerate(lines[idx:]):
            if line.startswith(f"**{chr(65+len(options))})"):
                option_text = line.replace(f"**{chr(65+len(options))}) ", "").replace("**", "").strip()
                if " ✓" in option_text:
                    correct_option = len(options)
                    option_text = option_text.replace(" ✓", "")
                options.append(option_text)

        if len(options) == 4 and correct_option is not None:
            q = Question(
                number=block_idx,
                text=q_text,
                options=options,
                correct_option=correct_option,
                explanation=""
            )
            questions.append(q)

    return questions


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: bias_detector.py <exam_file.md> [--fix-auto] [--report-only]")
        sys.exit(1)

    filepath = Path(sys.argv[1])
    fix_auto = '--fix-auto' in sys.argv

    print(f"Analyzing {filepath}...")
    questions = parse_exam_file(filepath)
    print(f"Parsed {len(questions)} questions\n")

    detector = BiasDetector(questions)
    passed, reports = detector.run_validation(fix_auto=fix_auto)

    print(detector.format_report())

    sys.exit(0 if passed else 1)

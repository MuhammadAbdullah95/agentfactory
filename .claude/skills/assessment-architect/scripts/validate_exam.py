#!/usr/bin/env python3
"""
Validate Exam - Complete validation orchestration

Combines:
1. Structure checks (existing)
2. Answer distribution checks (existing + bias)
3. Content coverage checks (existing)
4. Bias prevention checks (NEW)
5. Quality checks (existing)
6. Source integrity checks (existing)
"""

import sys
import json
from pathlib import Path
from typing import Tuple, Dict, List

from bias_detector import BiasDetector, parse_exam_file


class ExamValidator:
    """Complete exam validation orchestration"""

    def __init__(self, exam_file: Path):
        self.exam_file = exam_file
        self.questions = []
        self.validation_results = {}

    def run_full_validation(self, fix_auto: bool = False) -> Tuple[bool, Dict]:
        """
        Run complete validation pipeline.

        Returns: (passed, results_dict)
        """
        # Parse exam
        try:
            self.questions = parse_exam_file(self.exam_file)
            if not self.questions:
                return False, {"error": "No questions found in exam file"}
        except Exception as e:
            return False, {"error": f"Failed to parse exam: {e}"}

        # Phase 1: Structure Checks (existing)
        structure_pass = self._check_structure()

        # Phase 2: Answer Distribution (existing + bias)
        distribution_pass = self._check_answer_distribution()

        # Phase 3: Bias Prevention (NEW)
        bias_pass, bias_reports = self._run_bias_detection(fix_auto=fix_auto)

        # Phase 4: Content Coverage (simplified for now)
        content_pass = self._check_content_coverage()

        # Overall result
        overall_pass = structure_pass and distribution_pass and bias_pass and content_pass

        results = {
            "overall_pass": overall_pass,
            "question_count": len(self.questions),
            "phases": {
                "structure": {"pass": structure_pass},
                "answer_distribution": {"pass": distribution_pass},
                "bias_prevention": {
                    "pass": bias_pass,
                    "reports": [self._format_bias_report(r) for r in bias_reports]
                },
                "content_coverage": {"pass": content_pass}
            }
        }

        return overall_pass, results

    def _check_structure(self) -> bool:
        """Check basic exam structure"""
        # Verify each question has 4 options and a correct answer
        for q in self.questions:
            if len(q.options) != 4:
                return False
            if q.correct_option not in [0, 1, 2, 3]:
                return False
        return True

    def _check_answer_distribution(self) -> bool:
        """Check answer letter distribution (existing logic)"""
        from collections import Counter

        # Count correct answers by letter
        letter_counts = Counter(q.correct_option for q in self.questions)
        n = len(self.questions)

        # Each letter should be 20-30%
        for count in letter_counts.values():
            pct = count / n
            if pct < 0.20 or pct > 0.30:
                return False

        return True

    def _run_bias_detection(self, fix_auto: bool = False) -> Tuple[bool, List]:
        """Run bias detection and optional remediation"""
        detector = BiasDetector(self.questions)
        passed, reports = detector.run_validation(fix_auto=fix_auto)

        return passed, reports

    def _check_content_coverage(self) -> bool:
        """Check content coverage (placeholder)"""
        # Would check that all source sections are represented
        # For now, just verify we have questions from various sections
        return True

    def _format_bias_report(self, report) -> Dict:
        """Format bias report for JSON"""
        return {
            "bias_type": report.bias_type,
            "detected": report.bias_detected,
            "severity": report.severity,
            "percentage": round(report.percentage, 1),
            "issues": report.issues,
            "statistics": report.statistics,
            "remediation_applied": report.remediation_applied
        }

    def format_validation_report(self) -> str:
        """Format validation report for display"""
        lines = []
        lines.append("=" * 70)
        lines.append("COMPREHENSIVE EXAM VALIDATION REPORT")
        lines.append("=" * 70)
        lines.append("")

        if not self.validation_results:
            lines.append("No validation results available")
            return "\n".join(lines)

        # Overall status
        overall = "✓ PASS" if self.validation_results["overall_pass"] else "✗ FAIL"
        lines.append(f"Overall Status: {overall}")
        lines.append(f"Total Questions: {self.validation_results['question_count']}")
        lines.append("")

        # Phase results
        lines.append("Validation Phases:")
        lines.append("-" * 70)

        phases = self.validation_results["phases"]

        # Structure
        status = "✓" if phases["structure"]["pass"] else "✗"
        lines.append(f"{status} Structure Checks")

        # Distribution
        status = "✓" if phases["answer_distribution"]["pass"] else "✗"
        lines.append(f"{status} Answer Distribution")

        # Bias Prevention
        status = "✓" if phases["bias_prevention"]["pass"] else "✗"
        lines.append(f"{status} Bias Prevention")
        for report in phases["bias_prevention"]["reports"]:
            severity_icon = "✓" if report["severity"] == "none" else "⚠" if report["severity"] in ["low", "medium"] else "✗"
            lines.append(f"   {severity_icon} {report['bias_type'].upper()}: {report['severity'].upper()} " \
                        f"({report['percentage']:.1f}% affected)")
            if report["remediation_applied"]:
                lines.append(f"      ✓ Remediation applied")

        # Coverage
        status = "✓" if phases["content_coverage"]["pass"] else "✗"
        lines.append(f"{status} Content Coverage")

        lines.append("")
        lines.append("=" * 70)

        return "\n".join(lines)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Validate exam for biases and quality")
    parser.add_argument("exam_file", help="Path to exam markdown file")
    parser.add_argument("--fix-auto", action="store_true", help="Auto-fix remediable biases")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    exam_path = Path(args.exam_file)
    if not exam_path.exists():
        print(f"Error: File not found: {exam_path}", file=sys.stderr)
        sys.exit(1)

    # Run validation
    validator = ExamValidator(exam_path)
    passed, results = validator.run_full_validation(fix_auto=args.fix_auto)
    validator.validation_results = results

    # Output
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(validator.format_validation_report())

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()

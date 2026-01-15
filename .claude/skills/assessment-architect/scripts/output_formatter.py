#!/usr/bin/env python3
"""
Output Formatter - Convert exam data to multiple formats

Supported formats:
- markdown: Standard markdown (default, easy to convert)
- docx: Microsoft Word (uses docx skill)
- pdf: PDF export (via markdown -> docx -> pdf)
"""

from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class ExamQuestion:
    """Structured exam question"""
    number: int
    text: str
    options: List[str]  # [A, B, C, D]
    correct_option: int  # 0=A, 1=B, 2=C, 3=D
    explanation: str
    source_section: str
    difficulty: str  # Remember, Understand, Apply, Analyze, Evaluate, Create
    bloom_level: str  # Same as above
    question_type: str


@dataclass
class Exam:
    """Complete exam structure"""
    title: str
    source_files: List[str]
    questions: List[ExamQuestion]
    duration_minutes: int
    content_type: str  # conceptual, procedural, coding, mixed
    difficulty_distribution: Dict[str, int]  # bloom_level -> count


def format_exam_markdown(exam: Exam) -> str:
    """
    Format exam as markdown.

    Output structure:
    - Header with metadata
    - Questions section (options only, no answers)
    - Answer key (table at end)
    - Explanations section
    """
    lines = []

    # Header
    lines.append(f"# {exam.title}")
    lines.append("## MIT PhD Qualifying Examination")
    lines.append("")
    lines.append(f"**Source:** {', '.join(exam.source_files)}")
    lines.append(f"**Questions:** {len(exam.questions)}")
    lines.append(f"**Duration:** {exam.duration_minutes} minutes")
    lines.append(f"**Content Type:** {exam.content_type}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Questions section (no answers shown)
    lines.append("## Questions")
    lines.append("")
    for q in exam.questions:
        lines.append(f"### Q{q.number}")
        lines.append("")
        lines.append(q.text)
        lines.append("")

        # Options without showing correct answer
        option_labels = ['A', 'B', 'C', 'D']
        for i, opt in enumerate(q.options):
            lines.append(f"**{option_labels[i]})** {opt}")
        lines.append("")

    # Answer key table (at end)
    lines.append("---")
    lines.append("")
    lines.append("## Answer Key")
    lines.append("")
    lines.append("| Q# | Answer | Section | Difficulty | Bloom Level | Type |")
    lines.append("|-----|--------|---------|------------|-------------|------|")

    for q in exam.questions:
        answer_letter = chr(65 + q.correct_option)  # A=65
        lines.append(
            f"| {q.number} | **{answer_letter}** | {q.source_section} | "
            f"{q.difficulty} | {q.bloom_level} | {q.question_type} |"
        )

    # Explanations section
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Explanations")
    lines.append("")

    for q in exam.questions:
        answer_letter = chr(65 + q.correct_option)
        lines.append(f"### Q{q.number}")
        lines.append("")
        lines.append(f"**Correct Answer: {answer_letter}**")
        lines.append("")
        lines.append(q.explanation)
        lines.append("")
        lines.append(f"**Source Section:** {q.source_section}")
        lines.append("")

    return "\n".join(lines)


def format_exam_docx_json(exam: Exam) -> Dict:
    """
    Format exam as JSON structure for docx skill conversion.

    Returns dict that can be passed to docx skill for document creation.
    """
    sections = []

    # Title section
    sections.append({
        "type": "heading",
        "level": 1,
        "text": exam.title
    })

    sections.append({
        "type": "heading",
        "level": 2,
        "text": "MIT PhD Qualifying Examination"
    })

    # Metadata
    metadata_text = (
        f"Source: {', '.join(exam.source_files)}\n"
        f"Questions: {len(exam.questions)}\n"
        f"Duration: {exam.duration_minutes} minutes\n"
        f"Content Type: {exam.content_type}"
    )
    sections.append({
        "type": "paragraph",
        "text": metadata_text,
        "style": "Normal"
    })

    # Questions
    sections.append({
        "type": "heading",
        "level": 2,
        "text": "Questions"
    })

    for q in exam.questions:
        sections.append({
            "type": "heading",
            "level": 3,
            "text": f"Q{q.number}"
        })

        sections.append({
            "type": "paragraph",
            "text": q.text
        })

        # Options
        option_labels = ['A', 'B', 'C', 'D']
        for i, opt in enumerate(q.options):
            sections.append({
                "type": "paragraph",
                "text": f"{option_labels[i]}) {opt}",
                "indent": 1
            })

        sections.append({"type": "paragraph", "text": ""})

    # Answer key table
    sections.append({"type": "page_break"})
    sections.append({
        "type": "heading",
        "level": 2,
        "text": "Answer Key"
    })

    answer_key_rows = [["Q#", "Answer", "Section", "Difficulty", "Bloom", "Type"]]
    for q in exam.questions:
        answer_letter = chr(65 + q.correct_option)
        answer_key_rows.append([
            str(q.number),
            answer_letter,
            q.source_section,
            q.difficulty,
            q.bloom_level,
            q.question_type
        ])

    sections.append({
        "type": "table",
        "rows": answer_key_rows
    })

    # Explanations
    sections.append({"type": "page_break"})
    sections.append({
        "type": "heading",
        "level": 2,
        "text": "Explanations"
    })

    for q in exam.questions:
        answer_letter = chr(65 + q.correct_option)
        sections.append({
            "type": "heading",
            "level": 3,
            "text": f"Q{q.number}"
        })

        sections.append({
            "type": "paragraph",
            "text": f"Correct Answer: {answer_letter}",
            "bold": True
        })

        sections.append({
            "type": "paragraph",
            "text": q.explanation
        })

        sections.append({
            "type": "paragraph",
            "text": f"Source Section: {q.source_section}",
            "italic": True
        })

    return {
        "title": exam.title,
        "sections": sections
    }


def format_exam(exam: Exam, format: str = "markdown") -> str:
    """
    Format exam in requested format.

    Args:
        exam: Exam object with questions
        format: "markdown" (default), "docx-json", or "pdf"

    Returns:
        Formatted exam string
    """
    if format.lower() == "markdown":
        return format_exam_markdown(exam)
    elif format.lower() in ["docx", "docx-json"]:
        import json
        return json.dumps(format_exam_docx_json(exam), indent=2)
    elif format.lower() == "pdf":
        # PDF would go through markdown -> docx -> pdf
        return format_exam_markdown(exam)
    else:
        raise ValueError(f"Unsupported format: {format}")


if __name__ == "__main__":
    # Test with sample exam
    exam = Exam(
        title="Sample Exam",
        source_files=["lesson1.md", "lesson2.md"],
        questions=[
            ExamQuestion(
                number=1,
                text="What is the capital of France?",
                options=["London", "Berlin", "Paris", "Madrid"],
                correct_option=2,
                explanation="Paris is the capital of France, located in northern France.",
                source_section="Geography Section",
                difficulty="Easy",
                bloom_level="Remember",
                question_type="Precision Recall"
            )
        ],
        duration_minutes=120,
        content_type="mixed",
        difficulty_distribution={"Remember": 1}
    )

    # Test markdown format
    md = format_exam(exam, "markdown")
    print("Markdown output (first 300 chars):")
    print(md[:300])
    print("\n...")

    # Test docx-json format
    docx_json = format_exam(exam, "docx-json")
    print("\nDocx-JSON output (first 300 chars):")
    print(docx_json[:300])

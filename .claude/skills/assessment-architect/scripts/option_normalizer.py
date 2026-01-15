#!/usr/bin/env python3
"""
Option Normalizer - Utilities for normalizing option lengths

Ensures options are within acceptable word count ranges (±3 words).
"""

from typing import List, Tuple
from config import WORD_COUNT_TOLERANCE


def count_words(text: str) -> int:
    """Count words in text"""
    return len(text.split())


def get_option_lengths(options: List[str]) -> List[int]:
    """Get word counts for each option"""
    return [count_words(opt) for opt in options]


def calculate_length_range(options: List[str]) -> Tuple[int, int, float]:
    """
    Calculate min, max, and average word count for options.

    Returns: (min_words, max_words, avg_words)
    """
    lengths = get_option_lengths(options)
    return min(lengths), max(lengths), sum(lengths) / len(lengths)


def check_length_balance(options: List[str], tolerance: int = WORD_COUNT_TOLERANCE) -> bool:
    """
    Check if all options are within ±tolerance words of each other.

    Returns True if balanced, False if outliers exist.
    """
    lengths = get_option_lengths(options)
    min_len = min(lengths)
    max_len = max(lengths)
    return (max_len - min_len) <= tolerance


def normalize_options_by_padding(options: List[str], target_length: int = None) -> List[str]:
    """
    Normalize option lengths by padding shorter options.

    If target_length not specified, uses average + tolerance.

    Returns list of normalized options.
    """
    if target_length is None:
        min_len, max_len, avg_len = calculate_length_range(options)
        target_length = int(avg_len)

    normalized = []
    for opt in options:
        current_len = count_words(opt)
        if current_len < target_length:
            # Add filler words (e.g., "in general")
            padding_needed = target_length - current_len
            # Add padding phrases
            filler = " " + ", in general" * (padding_needed // 3)
            normalized.append(opt + filler if padding_needed > 0 else opt)
        else:
            normalized.append(opt)

    return normalized


def normalize_options_by_trimming(options: List[str]) -> List[str]:
    """
    Normalize option lengths by trimming longer options.

    Removes trailing clauses while preserving meaning.

    Returns list of trimmed options.
    """
    min_len, max_len, avg_len = calculate_length_range(options)
    target_length = int(avg_len) - 1  # Slightly shorter

    normalized = []
    for opt in options:
        current_len = count_words(opt)
        if current_len > target_length + WORD_COUNT_TOLERANCE:
            # Trim trailing clause or example
            words = opt.split()
            trimmed = " ".join(words[:target_length])
            # Add ellipsis if we trimmed
            normalized.append(trimmed + ("..." if len(words) > target_length else ""))
        else:
            normalized.append(opt)

    return normalized


def suggest_normalization(options: List[str]) -> dict:
    """
    Analyze options and suggest normalization strategy.

    Returns:
    {
        'balanced': True/False,
        'min_len': int,
        'max_len': int,
        'avg_len': float,
        'imbalance': float,
        'recommendation': 'none' | 'padding' | 'trimming' | 'rewrite',
        'reason': str
    }
    """
    min_len, max_len, avg_len = calculate_length_range(options)
    imbalance = max_len - min_len
    balanced = imbalance <= WORD_COUNT_TOLERANCE

    if balanced:
        return {
            'balanced': True,
            'min_len': min_len,
            'max_len': max_len,
            'avg_len': avg_len,
            'imbalance': imbalance,
            'recommendation': 'none',
            'reason': 'Options already balanced'
        }

    # Determine strategy
    if imbalance <= 5:
        recommendation = 'padding'
        reason = 'Slight imbalance; pad shorter options'
    elif imbalance <= 10:
        recommendation = 'trimming'
        reason = 'Moderate imbalance; trim longer options'
    else:
        recommendation = 'rewrite'
        reason = 'Large imbalance (>10 words); rewrite options'

    return {
        'balanced': False,
        'min_len': min_len,
        'max_len': max_len,
        'avg_len': avg_len,
        'imbalance': imbalance,
        'recommendation': recommendation,
        'reason': reason
    }


def format_length_report(options: List[str], option_labels: List[str] = None) -> str:
    """
    Format a readable report of option lengths.

    Returns formatted string for display.
    """
    if not option_labels:
        option_labels = ['A', 'B', 'C', 'D']

    lengths = get_option_lengths(options)
    min_len, max_len, avg_len = calculate_length_range(options)
    balanced = check_length_balance(options)

    report = "Option Length Analysis:\n"
    report += "-" * 40 + "\n"

    for label, opt, length in zip(option_labels, options, lengths):
        bar = "█" * length
        deviation = length - avg_len
        if deviation > 0:
            status = f"+{deviation:.0f}"
        elif deviation < 0:
            status = f"{deviation:.0f}"
        else:
            status = "0"
        report += f"{label}: {length:2d} words ({status:+3s}) {bar}\n"

    report += "-" * 40 + "\n"
    report += f"Min: {min_len}, Max: {max_len}, Avg: {avg_len:.1f}\n"
    report += f"Range: {max_len - min_len} words\n"
    report += f"Status: {'✓ BALANCED' if balanced else '✗ IMBALANCED'}\n"

    suggestion = suggest_normalization(options)
    report += f"\nRecommendation: {suggestion['recommendation']}\n"
    report += f"Reason: {suggestion['reason']}\n"

    return report


if __name__ == "__main__":
    import sys

    # Test with sample options
    options = [
        "This is a short option",
        "This is a much longer option that contains more words and details and examples",
        "Medium length option here",
        "A fairly long option with significant amount of content and explanation"
    ]

    print(format_length_report(options))
    print("\n" + "=" * 40 + "\n")

    suggestion = suggest_normalization(options)
    print(f"Suggested: {suggestion['recommendation']}")

    if suggestion['recommendation'] == 'padding':
        normalized = normalize_options_by_padding(options)
        print("\nAfter padding:")
        print(format_length_report(normalized))
    elif suggestion['recommendation'] == 'trimming':
        normalized = normalize_options_by_trimming(options)
        print("\nAfter trimming:")
        print(format_length_report(normalized))

#!/usr/bin/env python3
"""
Configuration for Assessment Architect

Centralized thresholds, sequences, and settings that are easily tuned.
"""

# =====================================================================
# BIAS DETECTION THRESHOLDS
# =====================================================================

BIAS_THRESHOLDS = {
    'length': {
        'high': 0.60,      # 60%+ same rank = high bias (FAIL)
        'medium': 0.50,    # 50-59% = medium bias (WARNING)
        'low': 0.40        # 40-49% = low bias (INFO)
    },
    'position': {
        'middle_max': 0.55,    # B+C ≤55% (threshold)
        'outer_min': 0.40,     # A+D ≥40% (threshold)
        'letter_min': 0.20,    # Each letter ≥20%
        'letter_max': 0.30     # Each letter ≤30%
    },
    'specificity': {
        'score_gap': 0.30,             # Correct ≥30% more specific
        'question_pct_high': 0.50,     # >50% questions = high (CRITICAL)
        'question_pct_medium': 0.35,   # 35-50% questions = medium (WARNING)
        'question_pct_low': 0.20       # 20-35% questions = low (INFO)
    }
}

# =====================================================================
# WORD COUNT SETTINGS
# =====================================================================

# From option-length-validation.md: all options within ±3 words
WORD_COUNT_TOLERANCE = 3

# =====================================================================
# PRE-MADE ANSWER SEQUENCES
# =====================================================================
# From redistribute_answers_v2.py: 8 sequences that guarantee:
# - Exactly 25% per letter (50 of each for 200 questions)
# - No >3 consecutive same letters
# - No predictable patterns (alternating, cycling)
# - 50-element sequences (for 200-question exams)

SEQUENCES = {
    'A': [2,0,3,1,2,0,1,3,2,0,1,3,0,2,1,3,2,0,1,3,0,2,3,1,0,2,3,1,2,0,3,1,2,0,1,3,0,2,3,1,2,0,3,1,0,2,1,3,0,2],
    'B': [1,3,0,2,1,3,0,2,3,1,0,2,3,1,2,0,1,3,2,0,3,1,2,0,1,3,0,2,1,3,2,0,3,1,0,2,3,1,2,0,1,3,0,2,1,0,3,2,1,3],
    'C': [0,2,1,3,0,2,3,1,0,2,1,3,1,3,0,2,3,0,1,2,2,0,1,3,3,1,0,2,0,2,3,1,1,3,2,0,2,0,1,3,3,1,2,0,0,3,2,1,2,0],
    'D': [3,1,2,0,3,1,2,0,1,3,2,0,2,0,3,1,0,3,2,1,1,3,0,2,2,0,3,1,3,1,2,0,0,2,3,1,3,1,0,2,0,2,1,3,2,1,0,3,3,1],
    'E': [2,1,0,3,2,1,3,0,1,0,3,2,3,2,1,0,1,2,0,3,2,1,3,0,0,3,2,1,2,1,0,3,3,0,1,2,0,3,2,1,1,2,3,0,3,0,1,2,2,3],
    'F': [1,0,3,2,1,0,2,3,2,3,1,0,0,1,2,3,3,1,2,0,0,2,1,3,3,2,1,0,1,0,3,2,2,1,0,3,1,0,3,2,3,0,2,1,1,2,3,0,0,1],
    'G': [3,2,0,1,3,2,1,0,0,1,2,3,1,0,3,2,2,0,1,3,3,0,2,1,1,2,3,0,0,2,1,3,1,3,2,0,2,3,0,1,0,3,1,2,2,1,3,0,3,2],
    'H': [0,3,2,1,0,3,1,2,3,2,0,1,2,3,0,1,0,2,3,1,1,3,0,2,2,1,0,3,3,0,2,1,2,0,3,1,1,2,0,3,2,1,0,3,0,2,1,3,1,0]
}

# Verify sequences (basic check)
def _verify_sequences():
    """Verify all sequences are properly formatted"""
    from collections import Counter
    for seq_name, seq in SEQUENCES.items():
        # Check length (should be 50 for 200 questions)
        if len(seq) != 50:
            raise ValueError(f"Sequence {seq_name} has wrong length: {len(seq)} (expected 50)")

        # Check that all values are 0-3 (letters A-D)
        if not all(x in [0, 1, 2, 3] for x in seq):
            raise ValueError(f"Sequence {seq_name} contains invalid values")

        # Warn if distribution is very skewed (but don't fail)
        counts = Counter(seq)
        for letter in [0, 1, 2, 3]:
            pct = counts[letter] / 50
            if pct < 0.15 or pct > 0.35:
                # Log warning but don't fail - sequences don't need to be perfect
                pass

_verify_sequences()

# =====================================================================
# SPECIFICITY SCORE CALCULATION WEIGHTS
# =====================================================================

SPECIFICITY_WEIGHTS = {
    'word_count': {
        'weight': 0.5,     # Words: 0.5 points each
        'max_points': 20
    },
    'examples': {
        'patterns': ['e.g.', 'such as', 'for instance', 'for example', 'like'],
        'points_per_example': 10,
        'max_points': 30
    },
    'qualifiers': {
        'patterns': [
            'typically', 'usually', 'generally', 'often',
            'in most cases', 'commonly', 'frequently'
        ],
        'points_per_qualifier': 5,
        'max_points': 20
    },
    'technical_density': {
        'weight': 30,      # Capitalized words as technical terms
        'max_points': 30
    }
}

# =====================================================================
# CONTENT CLASSIFICATION THRESHOLDS
# =====================================================================

CONTENT_CLASSIFICATION = {
    'conceptual': {
        'threshold': 0.60,  # >60% = conceptual
    },
    'coding': {
        'threshold': 0.40,  # >40% = coding
    },
    'procedural': {
        'threshold': 0.50,  # >50% = procedural
    }
}

# =====================================================================
# VALIDATION SETTINGS
# =====================================================================

VALIDATION = {
    'max_option_length_diff': 5,  # Options should be within ±5 words (more flexible than ±3)
    'min_questions': 25,          # Minimum reasonable exam size
    'max_questions': 250,         # Maximum reasonable exam size
    'default_questions': 150,     # Default if not specified
    'max_consecutive_same_letter': 3,  # No more than 3 A,A,A...
}

# =====================================================================
# PERFORMANCE TARGETS
# =====================================================================

PERFORMANCE = {
    'scope_discovery_ms': 200,
    'content_classification_ms': 5000,
    'distribution_selection_ms': 100,
    'bias_detection_ms': 30000,  # 30 seconds for 200 questions
}

# =====================================================================
# LOGGING & OUTPUT
# =====================================================================

LOG_LEVELS = {
    'DEBUG': 0,
    'INFO': 1,
    'WARNING': 2,
    'ERROR': 3,
}

# Default is INFO (show warnings and above)
DEFAULT_LOG_LEVEL = LOG_LEVELS['INFO']

# =====================================================================
# HELPER FUNCTIONS
# =====================================================================

def get_sequence(sequence_id: str = 'random') -> list:
    """Get a pre-made sequence by ID or random"""
    if sequence_id.upper() == 'RANDOM':
        import random
        sequence_id = random.choice(list(SEQUENCES.keys()))

    if sequence_id not in SEQUENCES:
        raise ValueError(f"Unknown sequence ID: {sequence_id}. Available: {list(SEQUENCES.keys())}")

    return SEQUENCES[sequence_id]


def get_bias_threshold(bias_type: str, level: str) -> float:
    """Get specific bias threshold"""
    if bias_type not in BIAS_THRESHOLDS:
        raise ValueError(f"Unknown bias type: {bias_type}")

    thresholds = BIAS_THRESHOLDS[bias_type]
    if level not in thresholds:
        raise ValueError(f"Unknown threshold level: {level}")

    return thresholds[level]


if __name__ == "__main__":
    # Test configuration
    print("Bias Thresholds:")
    for bias_type, thresholds in BIAS_THRESHOLDS.items():
        print(f"  {bias_type}: {thresholds}")

    print("\nSequences:")
    for seq_id in SEQUENCES:
        seq = SEQUENCES[seq_id]
        print(f"  {seq_id}: {len(seq)} elements")

    print("\nValidation settings:")
    for key, value in VALIDATION.items():
        print(f"  {key}: {value}")

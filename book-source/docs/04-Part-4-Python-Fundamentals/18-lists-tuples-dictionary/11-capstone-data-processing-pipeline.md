---
title: "Capstone - Data Processing Pipeline"
chapter: 18
lesson: 11
duration_minutes: 240

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Data Pipeline Architecture"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can design and build a complete data processing application that ingests, transforms, and aggregates data using multiple data structures appropriately"

  - name: "List and Dict Comprehension Application"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information"
    measurable_at_this_level: "Student applies comprehensions with filtering and transformation logic to real data processing scenarios"

  - name: "Data Structure Integration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student chooses and justifies appropriate combinations of lists, tuples, and dicts for complex data tasks and explains tradeoffs"

  - name: "AI-Driven Problem Solving"
    proficiency_level: "B1"
    category: "Soft"
    bloom_level: "Apply"
    digcomp_area: "Communication"
    measurable_at_this_level: "Student uses AI effectively to debug errors, validate designs, and extend functionality in a real application context"

learning_objectives:
  - objective: "Design and build a complete data processing pipeline that ingests, transforms, and outputs data using lists, tuples, and dictionaries appropriately"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Capstone project execution with architectural justification"

  - objective: "Apply list and dict comprehensions with filtering and transformation logic to real data"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Code implementation showing comprehensions handling multiple filtering conditions"

  - objective: "Debug data structure errors by analyzing error messages and asking AI targeted diagnostic questions"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Error resolution process with AI partnership during capstone"

cognitive_load:
  new_concepts: 0
  assessment: "Lesson 11 is pure integration (0 new concepts). Students synthesize all 46+ concepts from Lessons 1-10 in a single cohesive application. Cognitive load is managed through step-by-step scaffolding and AI partnership, not volume. ✓"

differentiation:
  extension_for_advanced: "Extend the pipeline: add multiple filtering criteria (AND/OR logic), implement sorting by multiple fields, add data validation, handle malformed records gracefully, or build a mini statistical analysis module (mean, median, standard deviation)."
  remedial_for_struggling: "Focus on core pipeline only (ingest → parse → filter → aggregate → output). Use the provided data structure templates. Pair with AI to debug step-by-step. Skip extensions. Ask instructor or AI for scaffolded hints."

# Generation metadata
generated_by: "lesson-writer v3.0.0"
source_spec: "specs/001-part-4-chapter-18/spec.md"
created: "2025-11-09"
last_modified: "2025-11-09"
git_author: "Claude Code"
workflow: "/sp.implement lesson-11"
version: "1.0.0"
---

# Lesson 11: Capstone - Data Processing Pipeline

## The Challenge: From Data to Insight

You've now mastered three fundamental Python data structures: **lists** (ordered, mutable sequences), **tuples** (ordered, immutable sequences), and **dictionaries** (fast key-value lookups). But mastery means more than understanding each structure in isolation. The real test is this: **Can you combine all three to solve a realistic, end-to-end data processing problem?**

This is what data engineers, analysts, and backend developers do every day. They receive raw data—messy, unstructured, often in text format—and transform it into meaningful insights. A student dataset. A transaction log. A sensor reading stream. The pattern is always the same:

1. **Ingest** the data (get it into a usable format)
2. **Parse** it (structure it as objects you can work with)
3. **Filter** it (select only what matters)
4. **Aggregate** it (calculate summaries, patterns, counts)
5. **Output** it (present results to humans or systems)

In this lesson, you'll build a **Data Processing Pipeline** that demonstrates this entire workflow. You'll parse student records, filter by major and GPA, aggregate statistics by program, and output a professional summary report.

**The Learning Goal**: Prove you can think architecturally about data structures and build a complete application that combines all three collections intelligently. This is not a toy exercise—this is the foundation of real-world data work.

---

## The Pipeline Architecture: Planning Before Code

#### 💬 AI Colearning Prompt
> "Design the data structure for this pipeline. We're processing student records (name, major, GPA). Should each record be a dict or a tuple? Why? What structure should we use for aggregating counts by major?"

Before you write a single line of code, understand the design. The best developers sketch their data structures first—on paper, in a notebook, or discussing with their AI partner.

Here's the structure we'll use:

### Step 1: Raw Data (String Format)

```python
raw_data: str = """
name,major,gpa
Alice,Computer Science,3.8
Bob,Mathematics,3.2
Carol,Computer Science,3.9
David,Physics,3.1
Eve,Computer Science,3.5
Frank,Mathematics,3.6
Grace,Physics,3.8
"""
```

This simulates reading a CSV file (we'll learn actual file I/O in Chapter 22). For now, it's just a multi-line string.

### Step 2: Parsed Data (List of Dicts)

```python
students: list[dict[str, str | float]] = [
    {"name": "Alice", "major": "Computer Science", "gpa": 3.8},
    {"name": "Bob", "major": "Mathematics", "gpa": 3.2},
    # ... more records
]
```

Each student is a **dict** (key-value mapping for field access by name), stored in a **list** (ordered collection of all records).

### Step 3: Filtered Data (List Comprehension)

```python
cs_students: list[dict[str, str | float]] = [
    student for student in students
    if student["major"] == "Computer Science" and student["gpa"] >= 3.5
]
```

We use a **list comprehension with if conditions** to select only records matching our criteria.

### Step 4: Aggregated Results (Dict of Counts/Stats)

```python
major_stats: dict[str, dict[str, float | int]] = {
    "Computer Science": {
        "count": 3,
        "average_gpa": 3.733,
    },
    "Mathematics": {
        "count": 2,
        "average_gpa": 3.4,
    },
    # ...
}
```

We use a **dict mapping major names to summary stats** (another dict containing counts and averages).

#### 🎓 Instructor Commentary

> In AI-native development, you don't just code—you design. Notice how we chose list for "ordered records" (we care about having all students), dict for "key-value lookup by student field", and dict again for "meaningful keys in aggregations". Structure choice is communication. When future you (or a teammate) reads this code, the structures tell the story.

---

## Phase 1: Parse Raw Data into List of Dicts

Let's start with the foundation. You have a CSV-like string, and your job is to convert it into a list of dicts, where each dict represents one student record.

**Specification**:
- Input: Multi-line string with headers on first line, data on remaining lines
- Output: list[dict[str, str | float]] where keys are column names
- Each dict = one record
- Handle missing values gracefully (skip malformed rows)

#### Code Example: Data Parsing

```python
def parse_csv_data(raw: str) -> list[dict[str, str | float]]:
    """Parse CSV-like string into list of dicts.

    Each dict represents one student record with keys: name, major, gpa.
    Returns empty list if no valid records found.
    """
    lines: list[str] = raw.strip().split('\n')

    # First line is headers
    if not lines:
        return []

    headers: list[str] = lines[0].split(',')
    students: list[dict[str, str | float]] = []

    # Parse remaining lines (skip first line and empty lines)
    for line in lines[1:]:
        if not line.strip():  # Skip empty lines
            continue

        values: list[str] = line.split(',')

        # Create dict with header -> value pairs
        record: dict[str, str | float] = {}
        for i, header in enumerate(headers):
            header_clean = header.strip()
            value_raw = values[i].strip() if i < len(values) else ""

            # Convert GPA to float if it's the GPA column
            if header_clean.lower() == 'gpa':
                try:
                    record[header_clean] = float(value_raw)
                except ValueError:
                    continue  # Skip row with invalid GPA
            else:
                record[header_clean] = value_raw

        students.append(record)

    return students

# Usage
raw_data: str = """name,major,gpa
Alice,Computer Science,3.8
Bob,Mathematics,3.2
Carol,Computer Science,3.9
David,Physics,3.1
Eve,Computer Science,3.5
Frank,Mathematics,3.6
Grace,Physics,3.8"""

parsed_students: list[dict[str, str | float]] = parse_csv_data(raw_data)
print(f"Parsed {len(parsed_students)} students")
```

#### ✨ Teaching Tip
> When debugging this parsing step, ask your AI: "Why is my list empty?" or "Show me what each dict contains after parsing". AI can help you visualize the structure and spot issues. Use `print(parsed_students[0])` to inspect the first record.

---

## Phase 2: Filter Data with Comprehensions

Now that you have structured data, filter it. Let's find all Computer Science students with a GPA of 3.5 or higher.

**Specification**:
- Input: list[dict[str, str | float]] of all students
- Criteria: major == "Computer Science" AND gpa >= 3.5
- Output: list[dict] containing only matching records
- Use comprehension (not a loop)

#### Code Example: Filtering with List Comprehension

```python
# Filter: Computer Science students with GPA >= 3.5
cs_high_achievers: list[dict[str, str | float]] = [
    student for student in parsed_students
    if student["major"] == "Computer Science" and student["gpa"] >= 3.5
]

print(f"Found {len(cs_high_achievers)} CS students with GPA >= 3.5")
for student in cs_high_achievers:
    print(f"  - {student['name']}: {student['gpa']}")
```

Notice the **two conditions in the if clause**:
- `student["major"] == "Computer Science"` (exact match)
- `student["gpa"] >= 3.5` (numeric comparison)

Both must be true for the student to be included.

#### 💬 AI Colearning Prompt
> "Show me how to write a list comprehension that filters students from multiple majors (Computer Science OR Mathematics). How would the condition change?"

#### 🚀 CoLearning Challenge

Ask your AI Co-Teacher:
> "Given the student data, write a comprehension that finds all students with GPA between 3.5 and 3.9 (inclusive). Then explain what each part of the comprehension does."

**Expected Outcome**: You'll understand how to combine multiple conditions in comprehensions and apply range-based filtering to numerical data.

---

## Phase 3: Aggregate Data with Dictionaries

Filtering is useful, but aggregation is powerful. Now calculate statistics **by major**:
- How many students in each major?
- What's the average GPA per major?

**Specification**:
- Input: list[dict[str, str | float]] of all students
- Output: dict[str, dict[str, float | int]] where:
  - Outer key = major name
  - Inner dict = `{"count": N, "average_gpa": X.XX}`
- Use dict to accumulate counts and sums

#### Code Example: Aggregation with Dict

```python
def aggregate_by_major(
    students: list[dict[str, str | float]]
) -> dict[str, dict[str, float | int]]:
    """Aggregate student statistics by major.

    Returns dict mapping major → {count, average_gpa}.
    """
    stats: dict[str, dict[str, float | int]] = {}

    for student in students:
        major: str = student["major"]
        gpa: float = student["gpa"]

        # Initialize major dict if not seen before
        if major not in stats:
            stats[major] = {
                "count": 0,
                "total_gpa": 0.0,
                "average_gpa": 0.0
            }

        # Accumulate
        stats[major]["count"] += 1
        stats[major]["total_gpa"] += gpa

    # Calculate averages
    for major in stats:
        total_gpa: float = stats[major]["total_gpa"]
        count: int = stats[major]["count"]
        stats[major]["average_gpa"] = round(total_gpa / count, 2)
        # Remove temporary field
        del stats[major]["total_gpa"]

    return stats

# Usage
major_statistics: dict[str, dict[str, float | int]] = aggregate_by_major(parsed_students)
print("Statistics by Major:")
for major, data in major_statistics.items():
    print(f"{major}: {data['count']} students, avg GPA {data['average_gpa']}")
```

Notice the pattern:
1. **Check if key exists**: `if major not in stats`
2. **Initialize if needed**: `stats[major] = {...}`
3. **Accumulate**: `stats[major]["count"] += 1`
4. **Calculate final value**: `average_gpa = total_gpa / count`

#### 🎓 Instructor Commentary

> This aggregation pattern appears everywhere: calculating totals, counting occurrences, tracking minimums/maximums. You're learning a skill that applies to data analysis, reporting, analytics dashboards, and more. The dict-based accumulator is fundamental. Syntax is cheap—understanding this pattern is gold.

#### 🚀 CoLearning Challenge

Ask your AI:
> "I need to find the student with the highest GPA in each major. How would I modify this aggregation to also track the top student's name in each major?"

**Expected Outcome**: You'll extend the aggregation pattern to track multiple values per group.

---

## Phase 4: Output Formatted Results

Raw dicts are great for computation, but humans need readable output. Format your results as a professional summary report.

**Specification**:
- Input: dict[str, dict[str, float | int]] of aggregated statistics
- Output: Formatted string suitable for printing or saving
- Include: Major name, student count, average GPA
- Format clearly with spacing and alignment

#### Code Example: Formatted Output

```python
def format_report(
    stats: dict[str, dict[str, float | int]],
    title: str = "Student Statistics by Major"
) -> str:
    """Format aggregation results as readable report."""
    lines: list[str] = [
        title,
        "=" * 50,
        ""
    ]

    # Sort majors alphabetically for consistent output
    sorted_majors: list[str] = sorted(stats.keys())

    for major in sorted_majors:
        count: int = stats[major]["count"]
        avg_gpa: float = stats[major]["average_gpa"]

        # Format with alignment
        lines.append(f"{major:25s} | Count: {count:2d} | Avg GPA: {avg_gpa:.2f}")

    lines.append("")
    lines.append("=" * 50)

    return '\n'.join(lines)

# Usage
report: str = format_report(major_statistics)
print(report)

# Output looks like:
# Student Statistics by Major
# ==================================================
#
# Computer Science      | Count:  3 | Avg GPA: 3.73
# Mathematics           | Count:  2 | Avg GPA: 3.40
# Physics               | Count:  2 | Avg GPA: 3.45
#
# ==================================================
```

Notice the formatting techniques:
- `{major:25s}` — left-align major name in 25 characters
- `{count:2d}` — right-align integer in 2 characters
- `{avg_gpa:.2f}` — float with 2 decimal places
- `'\n'.join(lines)` — combine list of strings with newlines

#### ✨ Teaching Tip
> When your output doesn't look quite right, show it to your AI: "Here's my output. The columns don't line up. How can I fix the formatting?" AI can suggest better alignment and explain f-string formatting codes.

---

## Putting It All Together: The Complete Pipeline

Now integrate all phases into one cohesive application:

```python
# PHASE 1: Parse raw data
raw_student_data: str = """name,major,gpa
Alice,Computer Science,3.8
Bob,Mathematics,3.2
Carol,Computer Science,3.9
David,Physics,3.1
Eve,Computer Science,3.5
Frank,Mathematics,3.6
Grace,Physics,3.8"""

students: list[dict[str, str | float]] = parse_csv_data(raw_student_data)
print(f"✓ Parsed {len(students)} student records\n")

# PHASE 2: Filter (optional - show CS students)
cs_students: list[dict[str, str | float]] = [
    s for s in students
    if s["major"] == "Computer Science"
]
print(f"✓ Found {len(cs_students)} Computer Science students\n")

# PHASE 3: Aggregate
statistics: dict[str, dict[str, float | int]] = aggregate_by_major(students)
print("✓ Calculated statistics by major\n")

# PHASE 4: Output
report: str = format_report(statistics)
print(report)
```

#### Validation Checklist

- [ ] Data parses correctly (right number of students, correct field values)
- [ ] Filtering works (CS students match expected records)
- [ ] Aggregation is accurate (counts and averages are correct)
- [ ] Output is readable (aligned columns, no errors)
- [ ] Code runs without exceptions

---

## Common Pitfalls and How to Debug Them

### Pitfall 1: KeyError When Accessing Dict Values

**Error**: `KeyError: 'major'`

**Cause**: The dict doesn't have the expected key (field name misspelled, or data parsing failed).

**Debug approach**:
1. Print the first dict to see what keys actually exist: `print(students[0].keys())`
2. Check if your header parsing is correct
3. Ask AI: "Why is my key 'major' not in the dict after parsing?"

### Pitfall 2: Type Errors in Aggregation

**Error**: `TypeError: '>' not supported between instances of 'str' and 'float'`

**Cause**: You're trying to compare GPA but it's stored as a string instead of float.

**Debug approach**:
1. Print a student record: `print(students[0]['gpa'], type(students[0]['gpa']))`
2. Check your parsing function—is it converting to float?
3. Ask AI: "How do I convert string '3.8' to float in Python?"

### Pitfall 3: Comprehension Syntax Error

**Error**: `SyntaxError: invalid syntax`

**Cause**: Missing colon, wrong if placement, or unbalanced brackets.

**Debug approach**:
1. Break the comprehension into a loop to verify logic:
   ```python
   # Instead of: [x for x in data if x > 3.5]
   # Try this first:
   result = []
   for x in data:
       if x > 3.5:
           result.append(x)
   ```
2. Once the loop works, convert back to comprehension
3. Ask AI: "Convert this loop to a list comprehension and explain each part"

#### ✨ Teaching Tip

> When debugging, **never** just ask AI to fix your code. Instead, ask AI to explain what you're seeing: "I got this error. What does it mean?" Then work with AI to diagnose. This builds your debugging skills—the most valuable skill in professional development.

---

## Extensions: Making It Real

Your basic pipeline works. Now make it more sophisticated. Choose one or more extensions:

### Extension 1: Multi-Criteria Filtering

Filter students who are Computer Science OR Mathematics majors with GPA above 3.4:

```python
stem_students: list[dict[str, str | float]] = [
    s for s in students
    if (s["major"] in ["Computer Science", "Mathematics"])
    and s["gpa"] > 3.4
]
```

### Extension 2: Sort Results

Sort students by GPA (highest first) before output:

```python
top_students: list[dict[str, str | float]] = sorted(
    students,
    key=lambda s: s["gpa"],
    reverse=True
)
```

### Extension 3: Find Outliers

Find students whose GPA is significantly different from their major's average:

```python
def find_outliers(
    students: list[dict[str, str | float]],
    stats: dict[str, dict[str, float | int]],
    threshold: float = 0.3
) -> list[dict[str, str | float]]:
    """Find students with GPA > threshold above their major's average."""
    outliers: list[dict[str, str | float]] = []

    for student in students:
        major: str = student["major"]
        avg: float = stats[major]["average_gpa"]
        difference: float = student["gpa"] - avg

        if difference > threshold:
            outliers.append(student)

    return outliers
```

---

## Capstone Validation: Am I Done?

Check yourself against these criteria:

**Core Functionality** (Required):
- [ ] Code parses raw CSV string into list[dict] ✓
- [ ] Filtering works with at least one comprehension ✓
- [ ] Aggregation calculates correct counts and averages ✓
- [ ] Output is formatted and readable ✓
- [ ] No runtime errors when processing data ✓

**Code Quality** (Expected):
- [ ] Type hints present on all function signatures ✓
- [ ] Variable names are descriptive (not `x`, `data1`, etc.) ✓
- [ ] Comments explain non-obvious logic ✓
- [ ] Code follows consistent indentation ✓

**Understanding** (Critical):
- [ ] I can explain why each data structure (list, dict) was chosen ✓
- [ ] I can justify the comprehension logic ✓
- [ ] I could modify this for a different data format (products, employees, transactions) ✓
- [ ] I asked AI when I was stuck and learned from the explanation ✓

**Stretch Goals** (Optional):
- [ ] Implemented at least one extension ✓
- [ ] Data handles edge cases (empty records, missing fields) ✓
- [ ] Code is organized and easy to read ✓

---

## Try With AI

Use your preferred AI companion (Claude Code, Gemini CLI, or ChatGPT web).

### Prompt 1: Recall Architecture (Remember)
> "I'm building a data pipeline to process student records. Should I store each record as a dict or a tuple? Should I use a list or a dict to aggregate statistics? Explain your reasoning for each choice."

**Expected Outcome**: You'll verify your understanding of structure selection. AI reinforces why list[dict] works for records and why dict is natural for aggregations.

---

### Prompt 2: Understand the Pattern (Understand)
> "Explain how list comprehensions with if conditions work. Show me a concrete example that filters students by major and GPA, then explain each part of the comprehension syntax."

**Expected Outcome**: You'll deepen your understanding of comprehension syntax and be able to read/write more complex filtering logic independently.

---

### Prompt 3: Apply to New Data (Apply)
> "Here's my student data pipeline working. Now I need to process employee records instead (name, department, salary). How would I modify my parsing, filtering, and aggregation functions for this new data? Show me the modified code with the same structure."

**Expected Outcome**: You'll prove you can transfer the pipeline pattern to different domains. This demonstrates true competency—not just following steps, but understanding the underlying pattern.

---

### Prompt 4: Debug and Extend (Analyze)
> "I'm getting a KeyError when filtering by department. [Paste your code]. Why is this happening? Help me debug it. Then, show me how to add a feature that calculates average salary per department."

**Expected Outcome**: You'll practice debugging with AI as a partner, moving from error to understanding. You'll also extend the pipeline with new aggregations—real-world application building.

---

**Safety & Ethics Note**: When AI suggests code, validate that it:
- Correctly handles the data you're working with
- Doesn't skip error handling for edge cases (empty lists, missing keys, type mismatches)
- Uses type hints appropriately
- Matches your project's style and structure

Ask AI: "Why did you choose this approach? Are there tradeoffs I should consider?" This builds critical thinking alongside coding skills.

---

## Capstone Success

You've now completed the full journey from raw data to insights. You've:
- **Designed** data structures strategically
- **Parsed** text into structured Python objects
- **Filtered** data with comprehensions
- **Aggregated** results using dict-based accumulators
- **Output** professional summaries

This is real work. Data engineers, backend developers, analytics engineers do this every day. You've demonstrated the core competency: **architectural thinking combined with execution**.

Congratulations on completing Chapter 18. You're ready for Chapter 19 (Sets and Frozen Sets) and beyond. The collection structures you've mastered form the foundation for everything that comes next—from functions that operate on collections to objects that contain collections as attributes.

**What's next**: In Chapter 20, you'll learn how to encapsulate this pipeline logic into reusable functions. In Chapter 21, you'll handle exceptions robustly when data is malformed. In Chapter 22, you'll read/write data from actual files. But the core pattern—ingest, transform, aggregate, output—remains your north star.

Keep building. Keep asking your AI partner. Keep validating. You're thinking like a developer now.

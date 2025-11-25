---
sidebar_position: 8
title: "Chapter 15 Quiz"
chapter: 15
lesson: 8
duration_minutes: 20

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 4"
layer_progression: "L4 capstone assessment"
layer_4_capstone: "Assesses SDD-RI workflow, intelligence accumulation, and skill creation mastery"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "SDD-RI Workflow Understanding"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify correct SDD-RI workflow sequence and explain rationale"

  - name: "Intelligence Accumulation Comprehension"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain why Feature 4 builds faster than Feature 1 and what causes acceleration"

  - name: "P+Q+P Framework Application"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can identify when patterns should be formalized into skills using P+Q+P framework"

  - name: "Pipeline Architecture Understanding"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain how feature outputs feed into downstream feature inputs"

learning_objectives:
  - objective: "Demonstrate understanding of constitution-based quality standards"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Multiple choice questions on constitution purpose and quality gates"

  - objective: "Explain intelligence accumulation and its measurable effects"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Questions on 50% target and acceleration causes"

  - objective: "Apply P+Q+P framework criteria for skill formalization"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Questions on when and how to create reusable skills"

cognitive_load:
  new_concepts: 0
  reused_concepts: 12
  assessment: "Quiz assesses 12 concepts from Lessons 1-7; no new concepts introduced ✓"

# Generation metadata
generated_by: "content-implementer v3.0.0"
source_spec: "specs/015-chapter-15-redesign/spec.md"
created: "2025-11-25"
last_modified: "2025-11-25"
git_author: "Claude Code"
workflow: "/sp.loopflow.v2"
version: "3.0.0"
---

# Chapter 15 Quiz

Test your understanding of constitution-based development, intelligence accumulation, and skill creation through the Personal AI Business Intelligence capstone.

---

## Questions

### Question 1

What is the primary purpose of creating a constitution before building features in the Personal BI System?

A) To document the project for future developers
B) To establish quality gates and decision standards that apply consistently across all features
C) To create marketing documentation for stakeholders
D) To satisfy project management requirements

---

### Question 2

What does the "50% target" in the Personal BI capstone represent?

A) Half of all features should use AI tools
B) Feature 4 should take approximately 50% of the time required for Feature 1
C) The acceleration should reduce errors by half
D) At least 50% of outputs should be reusable

---

### Question 3

True or False: In the Personal BI System, Feature 2 (Market Intelligence Scanner) uses NotebookLM because it excels at synthesizing information from multiple uploaded sources with citations.

---

### Question 4

Why does the Content Strategy Generator (Feature 3) receive inputs from BOTH Feature 1 AND Feature 2, rather than just Feature 2?

A) To increase the complexity of the feature
B) Content pillars must connect personal strengths (F1) to market trends (F2), requiring both inputs
C) It makes the AI prompts more efficient
D) Feature 1 output is needed for error handling

---

### Question 5

In the P+Q+P framework for creating reusable skills, what do these three components represent?

A) Process, Questions, Procedures
B) Plan, Queries, Practices
C) Persona, Questions, Principles
D) Purpose, Quality, Patterns

---

### Question 6

Which of the following is a valid quality gate from the constitution for the Personal Brand Profiler (Feature 1)?

A) "The feature should work well and produce useful output"
B) "Users will find the brand analysis helpful"
C) "Must cite specific phrases from your profile as evidence for each strength"
D) "Analysis will take less than an hour to complete"

---

### Question 7

Why is Feature 4 (Action Dashboard) typically faster to build than Feature 1 (Brand Profiler)?

A) Feature 4 requires simpler AI prompts
B) The constitution is no longer needed by Feature 4
C) Patterns from F1-F3 (structured prompting, validation, quality gates) transfer directly, reducing cognitive load
D) Feature 4 uses a different AI tool that is faster

---

### Question 8

True or False: Skills created using P+Q+P should be specific to a single project and should not be reused in other contexts.

---

### Question 9

In the Personal BI System, what is the primary purpose of the Action Dashboard (Feature 4)?

A) To generate new brand analysis data
B) To aggregate outputs from all upstream features (F1 + F2 + F3) into a unified view with priority actions
C) To replace the market intelligence brief
D) To automatically post content to social media

---

### Question 10

A pattern becomes worth formalizing into a reusable skill when it:

A) Uses advanced AI techniques or sophisticated algorithms
B) Appears in 2+ features AND involves multiple decision points or variations in application
C) Was difficult to implement initially in any single feature
D) Is suggested by an AI assistant during prompting

---

### Question 11

Which of the following represents a constitution principle being applied effectively across the Personal BI features?

A) Each feature interprets output format differently based on its unique context
B) Feature 1 outputs plain text, Feature 2 outputs JSON, Feature 3 outputs CSV—maximum flexibility
C) All features output structured markdown, ensuring upstream outputs can be validated against quality gates consistently
D) Each feature includes its own documentation format to suit its specific purpose

---

### Question 12

What should an honest retrospective document capture about feature development?

A) Only successful implementations and positive outcomes
B) Which AI tools performed best and which should be avoided
C) Specific patterns that accelerated development, friction points encountered, and learnings transferable to future projects
D) Timelines and resource plans for the next project

---

### Question 13 (Short Answer)

Explain in 2-3 sentences why the constitution is created BEFORE any features are built, and how this differs from documenting quality standards after the project is complete.

---

### Question 14 (Short Answer)

You've built Features 1-4 and identified a recurring pattern: "structured AI prompting with explicit output format and validation." This pattern appears with 5+ decision points (output format, input context, quality gates, examples, iteration approach). Should you formalize this as a reusable skill? Explain your reasoning using the 2+ features + 5+ decision points criteria.

---

## Answers

<details>
<summary>Click to reveal answers</summary>

**1. B** - To establish quality gates and decision standards that apply consistently across all features. The constitution defines what "good" looks like before you start building, preventing quality drift and ensuring each feature meets the same standards.

**2. B** - Feature 4 should take approximately 50% of the time required for Feature 1. This 50% target demonstrates that accumulated patterns, reusable workflows, and intelligence compound—each subsequent feature builds faster due to prior work.

**3. True** - NotebookLM is specifically chosen for Feature 2 because it excels at uploading multiple sources (company pages, job postings, articles) and synthesizing insights with citations. This is different from Gemini App which is better for single-context analysis and generation.

**4. B** - Content pillars must connect personal strengths (F1) to market trends (F2), requiring both inputs. This is the pipeline architecture principle—Feature 3 synthesizes two upstream outputs to create content strategy that bridges personal brand and market opportunity.

**5. C** - Persona, Questions, Principles.
- **Persona** defines who applies this skill and what they value
- **Questions** guide critical decisions before implementation
- **Principles** constrain how the skill should be applied and why

**6. C** - "Must cite specific phrases from your profile as evidence for each strength." Quality gates must be measurable and testable—not subjective statements like "work well" or "be helpful." This gate can be verified by checking if each strength includes a quoted phrase.

**7. C** - Patterns from F1-F3 (structured prompting, validation, quality gates) transfer directly, reducing cognitive load. Intelligence accumulation means you're not re-solving similar problems from scratch; you inherit proven approaches and can focus on Feature 4's unique aggregation task.

**8. False** - Skills should be designed for reuse across multiple projects and domains. The entire value of formalizing a pattern using P+Q+P is to make it applicable beyond the immediate context. This is why the pattern must recur in 2+ contexts and have 5+ decision points—criteria that ensure general applicability.

**9. B** - To aggregate outputs from all upstream features (F1 + F2 + F3) into a unified view with priority actions. The dashboard serves as the final integration point that makes the entire personal BI pipeline actionable—combining brand summary, market opportunities, content calendar, and synthesized actions.

**10. B** - It appears in 2+ features AND involves multiple decision points or variations in application. Patterns that recur and require judgment calls are worth capturing in a reusable skill; isolated, one-time patterns are not. The 5+ decision points criterion ensures the skill captures meaningful complexity worth encoding.

**11. C** - All features output structured markdown, ensuring upstream outputs can be validated against quality gates consistently. This demonstrates the constitution principle of "Structured Outputs" being applied uniformly. It enables composition: F1 output becomes F3 input, F2 output becomes F3 input, all three become F4 input.

**12. C** - Specific patterns that accelerated development, friction points encountered, and learnings transferable to future projects. Honest retrospectives balance celebrating successes with capturing honest feedback about what worked, what didn't, and what you learned. This honesty is how intelligence accumulates—you capture not just wins but friction points that future projects should anticipate.

**13. Sample Answer:** The constitution is created BEFORE features to establish quality gates upfront, ensuring every feature is built to the same standard. This differs from post-project documentation because it guides decisions during development—you reference the constitution when validating outputs, not write it after the fact when standards may have drifted. Pre-defining quality prevents "good enough" compromises during implementation.

**14. Sample Answer:** Yes, formalize this as a reusable skill. The pattern appears in Features 1, 2, 3, and 4 (4 features exceeds the 2+ threshold), and the 5+ decision points (output format, input context, quality gates, examples, iteration approach) exceed the complexity threshold. This pattern has sufficient generality—it applies whenever you need structured output from an AI tool—making it valuable for future projects beyond Personal BI.

</details>

---

## Scoring Guide

**Total Points:** 14 (12 MC @ 1 point each, 2 SA @ 1 point each)

**Passing Score:** 10/14 (71%)

### Grade Breakdown

- **13-14 points (93-100%):** Mastery — Deep understanding of constitution-based development, intelligence accumulation, and skill formalization
- **11-12 points (79-86%):** Proficient — Solid understanding of core concepts with minor gaps
- **10-11 points (71-79%):** Developing — Meets baseline, some concepts need reinforcement
- **Below 10 (Below 71%):** Needs Support — Review Chapter 14-15 before proceeding

### Key Concept Mapping

| Concept | Questions | Weight |
|---------|-----------|--------|
| Constitution Purpose | Q1, Q13 | 14% |
| Intelligence Accumulation | Q2, Q7, Q14 | 21% |
| Tool Selection | Q3 | 7% |
| Pipeline Architecture | Q4, Q9 | 14% |
| P+Q+P Framework | Q5, Q10 | 14% |
| Quality Gates | Q6, Q11 | 14% |
| Retrospective Value | Q12 | 7% |
| Skill Formalization | Q8, Q14 | 14% |

### Individual Question Difficulty

- **Easy (80%+ expected pass):** Q1, Q2, Q3, Q5, Q9
- **Medium (60-80%):** Q4, Q6, Q7, Q8, Q10, Q11, Q12
- **Hard (Below 60%):** Q13, Q14 (short answers require synthesis)

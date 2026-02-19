# Frontmatter-to-Teaching Reference

How to use each frontmatter field from lesson content to drive teaching behavior.

## Field Mapping

| Frontmatter Field             | Teaching Behavior                                                    |
| ----------------------------- | -------------------------------------------------------------------- |
| `title`                       | Lesson heading — announce at the start                               |
| `description`                 | Set context: "In this lesson you'll learn..."                        |
| `skills`                      | What they'll be able to DO — preview upfront as learning goals       |
| `skills[].proficiency_level`  | Calibrate depth: A1=introduce, B1=apply, C1=analyze                  |
| `skills[].bloom_level`        | Quiz at this level: Remember=recall, Apply=scenario, Analyze=compare |
| `learning_objectives`         | What they'll UNDERSTAND — quiz against these after teaching          |
| `cognitive_load`              | `low`: explain fully. `medium`: guided. `high`: scaffold into chunks |
| `cognitive_load.new_concepts` | Number of new concepts — if >5, break into sub-sessions              |
| `practice_exercise`           | If present, use for hands-on practice after explaining               |
| `teaching_guide`              | Teacher notes: key_points, misconceptions, discussion_prompts        |
| `differentiation`             | Advanced/struggling learner adaptations                              |
| `duration_minutes`            | Pace the session — don't rush a 30-min lesson into 5 minutes         |
| `keywords`                    | Define these terms explicitly during teaching                        |
| `hide_table_of_contents`      | If true, teach linearly without offering to skip ahead               |

## Skills Object Structure

Skills come as structured objects, not strings:

```json
{
  "name": "Recognizing AI Capability Breakthroughs",
  "proficiency_level": "A1",
  "category": "Conceptual",
  "bloom_level": "Remember",
  "digcomp_area": "Information Literacy",
  "measurable_at_this_level": "Student can identify concrete evidence..."
}
```

Use `measurable_at_this_level` as your acceptance criterion — if the learner can do this, they've mastered the skill.

## Cognitive Load Handling

```json
{
  "new_concepts": 7,
  "assessment": "7 concepts at upper limit of A1-A2 range (5-7)"
}
```

- 1-3 concepts: teach in one pass
- 4-5 concepts: check understanding halfway through
- 6-7 concepts: break into 2-3 chunks with comprehension checks between each
- 8+: split across multiple teaching sessions

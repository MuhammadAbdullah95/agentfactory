interface ExerciseConfig {
  repo: string;
  releaseTag: string;
  description?: string;
}

const EXERCISE_REGISTRY: Record<string, ExerciseConfig> = {
  "ch3-basics": {
    repo: "panaversity/claude-code-basic-exercises",
    releaseTag: "latest",
    description:
      "Claude Code Basic Exercises — prompting, file operations, debugging",
  },
  "ch3-skills": {
    repo: "panaversity/claude-code-skills-exercises",
    releaseTag: "latest",
    description: "Claude Code Skills Exercises — custom skills creation",
  },
  "ch3-plugins": {
    repo: "panaversity/claude-code-plugins-exercises",
    releaseTag: "latest",
    description: "Claude Code Plugins Exercises — MCP and tool integration",
  },
  "ch3-agent-teams": {
    repo: "panaversity/claude-code-agent-teams-exercises",
    releaseTag: "latest",
    description: "Claude Code Agent Teams Exercises — multi-agent workflows",
  },
  "ch4-context": {
    repo: "panaversity/context-engineering-exercises",
    releaseTag: "latest",
    description:
      "Context Engineering Exercises — CLAUDE.md, memory, prompt design",
  },
  "ch5-sdd": {
    repo: "panaversity/sdd-exercises",
    releaseTag: "latest",
    description:
      "Spec-Driven Development Exercises — specs, plans, tasks workflows",
  },
  "ch6-principles": {
    repo: "panaversity/seven-principles-exercises",
    releaseTag: "latest",
    description:
      "Seven Principles Exercises — bash, verification, decomposition",
  },
};

export function getExercise(exerciseId: string): ExerciseConfig | undefined {
  return EXERCISE_REGISTRY[exerciseId];
}

export function listExercises(): Record<string, ExerciseConfig> {
  return { ...EXERCISE_REGISTRY };
}

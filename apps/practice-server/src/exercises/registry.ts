interface ExerciseConfig {
  repo: string;
  releaseTag: string;
  description?: string;
}

const EXERCISE_REGISTRY: Record<string, ExerciseConfig> = {
  "ch3-basics": {
    repo: "panaversity/claude-code-basic-exercises",
    releaseTag: "latest",
    description: "Claude Code Basic Exercises — prompting, file operations, debugging",
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
};

export function getExercise(exerciseId: string): ExerciseConfig | undefined {
  return EXERCISE_REGISTRY[exerciseId];
}

export function listExercises(): Record<string, ExerciseConfig> {
  return { ...EXERCISE_REGISTRY };
}

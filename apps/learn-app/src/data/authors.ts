export interface Author {
  name: string;
  role: string;
  avatar: string;
  link: string;
  bio: string;
  isAI: boolean;
  initials: string;
}

export const authors: Author[] = [
  {
    name: "Zia Khan",
    role: "Lead Author",
    avatar: "/img/authors/zia-khan.jpg",
    link: "https://www.linkedin.com/in/ziaukhan/",
    bio: "CEO of Panaversity, leading the mission to democratize AI-native education. Architect of the Agent Factory methodology and the Spec-Driven Development paradigm.",
    isAI: false,
    initials: "ZK",
  },
  {
    name: "Wania Kazmi",
    role: "Co-Author",
    avatar: "/img/authors/wania.jpeg",
    link: "https://www.linkedin.com/in/waniakazmi/",
    bio: "AI educator and curriculum designer at Panaversity. Specializes in making complex AI concepts accessible through structured learning progressions.",
    isAI: false,
    initials: "WK",
  },
  {
    name: "Muhammad Junaid",
    role: "Co-Author",
    avatar: "/img/authors/junaid.jpeg",
    link: "https://www.linkedin.com/in/mrjunaid/",
    bio: "CTO at Panaversity, building governed, reliable, and measurable AI agents. Leads technical implementation of production-ready examples and cloud-native deployment patterns throughout the book.",
    isAI: false,
    initials: "MJ",
  },
  {
    name: "Rehan Ul Haq",
    role: "Co-Author",
    avatar: "/img/authors/rehan.jpeg",
    link: "https://www.linkedin.com/in/m-rehan-ul-haq-333bb6363/",
    bio: "Systems architect specializing in agentic AI infrastructure. Contributor to the Kubernetes, Docker, and production deployment chapters.",
    isAI: false,
    initials: "RH",
  },
  {
    name: "Claude Code",
    role: "AI Co-Author",
    avatar: "/img/authors/claude-code.png",
    link: "https://github.com/panaversity/agentfactory/tree/main/.claude",
    bio: "Anthropic's AI coding agent. Co-authored content, generated examples, and validated technical accuracy across all chapters using spec-driven workflows.",
    isAI: true,
    initials: "CC",
  },
  {
    name: "SpecKitPlus",
    role: "AI Co-Author",
    avatar: "/img/authors/speckitplus.png",
    link: "https://github.com/panaversity/spec-kit-plus",
    bio: "An SDD-RI (Specification-Driven Development with Reusable Intelligence) framework built around one core idea: capture intelligence, not just deliver code. Powers the book's spec templates, curriculum architecture, and quality validation pipelines.",
    isAI: true,
    initials: "SK",
  },
];

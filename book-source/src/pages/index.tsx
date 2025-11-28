import type { ReactNode } from "react";
import clsx from "clsx";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import Heading from "@theme/Heading";

import styles from "./index.module.css";

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={styles.heroBanner}>
      <div className={styles.heroGradient} />
      <div className="container">
        <div className={styles.heroContent}>
          {/* Left side - Book Cover */}
          <div className={styles.heroImageContainer}>
            <img
              src="/robolearn/img/book-cover-page.png"
              alt="RoboLearn: Physical AI & Humanoid Robotics"
              className={styles.heroBookCover}
            />
          </div>

          {/* Right side - Content */}
          <div className={styles.heroTextContent}>
            <div className={styles.heroLabel}>
              Panaversity Hackathon Project
            </div>
            <Heading as="h1" className={styles.heroTitle}>
              RoboLearn
              <br />
              <span className={styles.heroTitleAccent}>
                Physical AI & Humanoid Robotics –{" "}
                <strong>Bridging Digital Brain & Physical Body</strong>
              </span>
            </Heading>

            <div className={styles.heroBadges}>
              <span className={styles.badge}>
                <span className={styles.badgeIcon}>🤖</span>
                ROS 2
              </span>
              <span className={styles.badge}>
                <span className={styles.badgeIcon}>🎮</span>
                Gazebo & Unity
              </span>
              <span className={styles.badge}>
                <span className={styles.badgeIcon}>🧠</span>
                NVIDIA Isaac
              </span>
            </div>

            <div className={styles.heroButtons}>
              <Link
                className={clsx(
                  "button button--primary button--md",
                  styles.ctaButton
                )}
                to="/docs/preface-agent-native"
              >
                <span className={styles.buttonContent}>
                  <span className={styles.buttonText}>Start Learning</span>
                  <span className={styles.buttonIcon}>→</span>
                </span>
              </Link>
              <Link
                className={clsx(
                  "button button--outline button--md",
                  styles.secondaryButton
                )}
                href="https://github.com/mjunaidca/robolearn"
                target="_blank"
                rel="noopener noreferrer"
              >
                <span className={styles.buttonContent}>
                  <span className={styles.buttonText}>View on GitHub</span>
                  <span className={styles.buttonIcon}>⭐</span>
                </span>
              </Link>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}

function Feature({
  title,
  description,
  icon,
  featured,
}: {
  title: string;
  description: string;
  icon: string;
  featured?: boolean;
}) {
  return (
    <div className={clsx(styles.feature, featured && styles.featureFeatured)}>
      {featured && <div className={styles.featureBadge}>Core Module</div>}
      <div className={styles.featureIconWrapper}>
        <div className={styles.featureIcon}>{icon}</div>
      </div>
      <h3 className={styles.featureTitle}>{title}</h3>
      <p className={styles.featureDescription}>{description}</p>
      <div className={styles.featureAccent} />
    </div>
  );
}

function ModulesSection() {
  return (
    <section className={styles.spectrumSection}>
      <div className="container">
        <div className={styles.spectrumHeader}>
          <div className={styles.spectrumLabel}>
            Course Curriculum
          </div>
          <Heading as="h2" className={styles.spectrumTitle}>
            Four Modules to Physical AI Mastery
          </Heading>
          <p className={styles.spectrumSubtitle}>
            From robot middleware to autonomous humanoids with voice control
          </p>
        </div>

        <div className={styles.spectrumCards}>
          {/* Module 1 */}
          <div className={styles.spectrumCard}>
            <div className={styles.spectrumCardHeader}>
              <div className={styles.spectrumIcon}>🔌</div>
              <h3 className={styles.spectrumCardTitle}>Module 1</h3>
              <div className={styles.spectrumCardSubtitle}>ROS 2 Fundamentals</div>
            </div>
            <p className={styles.spectrumCardDescription}>
              Master the robotic nervous system with ROS 2 middleware for robot control.
            </p>
            <ul className={styles.spectrumCardList}>
              <li>Nodes, Topics, and Services</li>
              <li>Python Agents with rclpy</li>
              <li>URDF for Humanoids</li>
            </ul>
            <div className={styles.spectrumCardExample}>
              <strong>Weeks 1-5</strong>
            </div>
          </div>

          {/* Module 2 */}
          <div className={styles.spectrumCard}>
            <div className={styles.spectrumCardHeader}>
              <div className={styles.spectrumIcon}>🎮</div>
              <h3 className={styles.spectrumCardTitle}>Module 2</h3>
              <div className={styles.spectrumCardSubtitle}>Digital Twins</div>
            </div>
            <p className={styles.spectrumCardDescription}>
              Build physics simulations and high-fidelity environments.
            </p>
            <ul className={styles.spectrumCardList}>
              <li>Gazebo Physics Simulation</li>
              <li>Unity Visualization</li>
              <li>Sensor Simulation (LiDAR, IMU)</li>
            </ul>
            <div className={styles.spectrumCardExample}>
              <strong>Weeks 6-7</strong>
            </div>
          </div>

          {/* Module 3 */}
          <div
            className={clsx(styles.spectrumCard, styles.spectrumCardHighlight)}
          >
            <div className={styles.spectrumBadge}>AI-Powered</div>
            <div className={styles.spectrumCardHeader}>
              <div className={styles.spectrumIcon}>🧠</div>
              <h3 className={styles.spectrumCardTitle}>Module 3</h3>
              <div className={styles.spectrumCardSubtitle}>NVIDIA Isaac</div>
            </div>
            <p className={styles.spectrumCardDescription}>
              Advanced perception, navigation, and sim-to-real transfer.
            </p>
            <ul className={styles.spectrumCardList}>
              <li>Isaac Sim & Synthetic Data</li>
              <li>VSLAM & Navigation</li>
              <li>Reinforcement Learning</li>
            </ul>
            <div className={styles.spectrumCardExample}>
              <strong>Weeks 8-10</strong>
            </div>
          </div>

          {/* Module 4 */}
          <div
            className={clsx(styles.spectrumCard, styles.spectrumCardHighlight)}
          >
            <div className={styles.spectrumBadge}>Capstone</div>
            <div className={styles.spectrumCardHeader}>
              <div className={styles.spectrumIcon}>🗣️</div>
              <h3 className={styles.spectrumCardTitle}>Module 4</h3>
              <div className={styles.spectrumCardSubtitle}>Vision-Language-Action</div>
            </div>
            <p className={styles.spectrumCardDescription}>
              Convergence of LLMs and Robotics for conversational control.
            </p>
            <ul className={styles.spectrumCardList}>
              <li>Voice-to-Action (Whisper)</li>
              <li>LLM Cognitive Planning</li>
              <li>Autonomous Humanoid Capstone</li>
            </ul>
            <div className={styles.spectrumCardExample}>
              <strong>Weeks 11-13</strong>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function FeaturesSection() {
  return (
    <section className={styles.features}>
      <div className="container">
        {/* Section Header */}
        <div className={styles.featuresHeader}>
          <div className={styles.featuresLabel}>Why Physical AI</div>
          <Heading as="h2" className={styles.featuresHeading}>
            The Future of Human-Robot Collaboration
          </Heading>
          <p className={styles.featuresSubheading}>
            Humanoid robots share our form and can work in human environments
          </p>
        </div>

        {/* Features Grid */}
        <div className={styles.featuresGrid}>
          <Feature
            icon="🤖"
            title="Embodied Intelligence"
            description="AI that operates in physical space, not just digital environments. Robots that understand physics and interact with the real world."
            featured={true}
          />
          <Feature
            icon="🔧"
            title="Human-Centered Design"
            description="Humanoid robots navigate our world without modification. They use human tools, interfaces, and learn from demonstrations."
          />
          <Feature
            icon="🎯"
            title="Production-Ready Skills"
            description="ROS 2, Gazebo, NVIDIA Isaac, and VLA models. The complete stack for modern robotics development."
          />
          <Feature
            icon="🗣️"
            title="Conversational Robotics"
            description="Natural language commands translated to robot actions. 'Clean the room' becomes a sequence of coordinated movements."
          />
          <Feature
            icon="🌐"
            title="Sim-to-Real Transfer"
            description="Train in simulation, deploy to reality. Photorealistic environments and domain randomization bridge the gap."
          />
          <Feature
            icon="🚀"
            title="Interactive Learning"
            description="RAG-powered chat, personalized content, and hands-on exercises. Learn by doing, not just reading."
            featured={true}
          />
        </div>
      </div>
    </section>
  );
}

function HardwareSection() {
  return (
    <section className={styles.maturitySection}>
      <div className="container">
        <div className={styles.maturityHeader}>
          <div className={styles.maturityLabel}>Getting Started</div>
          <Heading as="h2" className={styles.maturityTitle}>
            Hardware & Setup Options
          </Heading>
          <p className={styles.maturitySubtitle}>
            Choose your path based on available resources
          </p>
        </div>

        <div className={styles.maturityLevels}>
          {/* Option 1 */}
          <div className={styles.maturityLevel}>
            <div className={styles.maturityLevelNumber}>1</div>
            <div className={styles.maturityLevelHeader}>
              <div>
                <h3 className={styles.maturityLevelTitle}>Workstation</h3>
                <div className={styles.maturityLevelSubtitle}>
                  Full Local Setup
                </div>
              </div>
              <div className={styles.maturityLevelImpact}>
                Best Experience
              </div>
            </div>
            <p className={styles.maturityLevelDescription}>
              RTX 4070 Ti+, 64GB RAM, Ubuntu 22.04. Run Isaac Sim locally with full performance.
            </p>
            <div className={styles.maturityLevelApproach}>
              <strong>Cost:</strong> ~$2,500+ hardware
            </div>
          </div>

          {/* Option 2 */}
          <div
            className={clsx(
              styles.maturityLevel,
              styles.maturityLevelHighlight
            )}
          >
            <div className={styles.maturityBadge}>RECOMMENDED</div>
            <div className={styles.maturityLevelNumber}>2</div>
            <div className={styles.maturityLevelHeader}>
              <div>
                <h3 className={styles.maturityLevelTitle}>Cloud + Edge</h3>
                <div className={styles.maturityLevelSubtitle}>
                  Hybrid Approach
                </div>
              </div>
              <div className={styles.maturityLevelImpact}>
                Flexible
              </div>
            </div>
            <p className={styles.maturityLevelDescription}>
              AWS/Azure GPU instances for simulation. Jetson kit for physical deployment.
            </p>
            <div className={styles.maturityLevelApproach}>
              <strong>Cost:</strong> ~$200/quarter cloud + $700 Jetson
            </div>
          </div>

          {/* Option 3 */}
          <div className={styles.maturityLevel}>
            <div className={styles.maturityLevelNumber}>3</div>
            <div className={styles.maturityLevelHeader}>
              <div>
                <h3 className={styles.maturityLevelTitle}>Simulation Only</h3>
                <div className={styles.maturityLevelSubtitle}>
                  Learning Focus
                </div>
              </div>
              <div className={styles.maturityLevelImpact}>
                Lowest Cost
              </div>
            </div>
            <p className={styles.maturityLevelDescription}>
              Cloud-based simulation without physical hardware. Complete the theory and simulation modules.
            </p>
            <div className={styles.maturityLevelApproach}>
              <strong>Cost:</strong> Cloud compute only
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function CTASection() {
  return (
    <section className={styles.paradigmSection}>
      <div className="container">
        <div className={styles.paradigmContent}>
          <div className={styles.paradigmHeader}>
            <div className={styles.paradigmLabel}>Ready to Begin?</div>
            <Heading as="h2" className={styles.paradigmTitle}>
              The Future is Physical AI
              <br />
              <span className={styles.paradigmTitleAccent}>
                Robots That Think, Move, and Collaborate
              </span>
            </Heading>
            <p className={styles.paradigmSubtitle}>
              Join the transition from AI confined to screens to AI that shapes the physical world alongside us.
            </p>
          </div>

          <div className={styles.paradigmCTA}>
            <div className={styles.paradigmCTAContent}>
              <div className={styles.paradigmCTAIcon}>🤖</div>
              <div className={styles.paradigmCTAText}>
                <h3 className={styles.paradigmCTATitle}>
                  Start Your Physical AI Journey
                </h3>
                <p className={styles.paradigmCTADescription}>
                  From ROS 2 basics to autonomous humanoids with voice control
                </p>
              </div>
              <Link
                className={clsx(
                  "button button--primary button--lg",
                  styles.paradigmCTAButton
                )}
                to="/docs/preface-agent-native"
              >
                Begin Learning
              </Link>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title="RoboLearn: Physical AI & Humanoid Robotics"
      description="Physical AI & Humanoid Robotics – Bridging the Digital Brain and the Physical Body. Learn ROS 2, Gazebo, NVIDIA Isaac, and Vision-Language-Action systems."
    >
      <HomepageHeader />
      <ModulesSection />
      <FeaturesSection />
      <HardwareSection />
      <CTASection />
    </Layout>
  );
}

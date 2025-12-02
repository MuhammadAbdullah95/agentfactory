import React, { ReactNode, useState, useEffect } from 'react';
import { useAuth } from '@/contexts/AuthContext';
import { getOAuthAuthorizationUrl } from '@/lib/auth-client';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './ContentGate.module.css';

export type GateType = 'quiz' | 'summary' | 'exercise' | 'premium';

interface ContentGateProps {
  children: ReactNode;
  type: GateType;
  /** Preview content to show in blurred state (optional - defaults to children) */
  preview?: ReactNode;
  /** Custom title for the gate */
  title?: string;
  /** Custom description for the gate */
  description?: string;
  /** Whether to show the gate even when authenticated (for testing) */
  forceGate?: boolean;
}

// Gate configuration per content type
const gateConfig: Record<GateType, {
  title: string;
  description: string;
  icon: string;
  benefit: string;
}> = {
  quiz: {
    title: 'Test Your Knowledge',
    description: 'Sign in to access chapter quizzes and track your learning progress.',
    icon: '🎯',
    benefit: 'Get instant feedback and see how you compare',
  },
  summary: {
    title: 'Quick Reference',
    description: 'Sign in to unlock lesson summaries for quick review and revision.',
    icon: '📋',
    benefit: 'Save hours with condensed key takeaways',
  },
  exercise: {
    title: 'Hands-On Practice',
    description: 'Sign in to access coding exercises with guided solutions.',
    icon: '💻',
    benefit: 'Build real skills through practical application',
  },
  premium: {
    title: 'Premium Content',
    description: 'Sign in to unlock this exclusive learning material.',
    icon: '✨',
    benefit: 'Get the complete learning experience',
  },
};

export function ContentGate({
  children,
  type,
  preview,
  title,
  description,
  forceGate = false,
}: ContentGateProps) {
  const { session, isLoading } = useAuth();
  const { siteConfig } = useDocusaurusContext();
  const authUrl = (siteConfig.customFields?.authUrl as string) || 'http://localhost:3001';
  const oauthClientId = (siteConfig.customFields?.oauthClientId as string) || 'ai-native-public-client';

  const [isUnlocking, setIsUnlocking] = useState(false);
  const [isSigningIn, setIsSigningIn] = useState(false);

  const config = gateConfig[type];
  const displayTitle = title || config.title;
  const displayDescription = description || config.description;

  // OAuth config
  const oauthConfig = {
    authUrl,
    clientId: oauthClientId,
  };

  // Handle sign in
  const handleSignIn = async () => {
    setIsSigningIn(true);
    try {
      const authorizationUrl = await getOAuthAuthorizationUrl('signin', oauthConfig);
      await new Promise(resolve => setTimeout(resolve, 50));
      window.location.href = authorizationUrl;
    } catch (error) {
      console.error('Sign in failed:', error);
      setIsSigningIn(false);
    }
  };

  // Handle sign up
  const handleSignUp = async () => {
    setIsSigningIn(true);
    try {
      const oauthUrl = await getOAuthAuthorizationUrl('signup', oauthConfig);
      const signupUrl = `${authUrl}/auth/sign-up?redirect=${encodeURIComponent(oauthUrl)}`;
      window.location.href = signupUrl;
    } catch (error) {
      console.error('Sign up failed:', error);
      setIsSigningIn(false);
    }
  };

  // Unlock animation when session becomes available
  useEffect(() => {
    if (session && !isLoading) {
      setIsUnlocking(true);
      const timer = setTimeout(() => setIsUnlocking(false), 800);
      return () => clearTimeout(timer);
    }
  }, [session, isLoading]);

  // Show loading state
  if (isLoading) {
    return (
      <div className={styles.gateContainer}>
        <div className={styles.loadingState}>
          <div className={styles.loadingSpinner} />
          <span>Checking access...</span>
        </div>
      </div>
    );
  }

  // User is authenticated - show content (with optional unlock animation)
  if (session && !forceGate) {
    return (
      <div className={`${styles.contentWrapper} ${isUnlocking ? styles.unlocking : ''}`}>
        {children}
      </div>
    );
  }

  // User is not authenticated - show gate
  return (
    <div className={styles.gateContainer}>
      {/* Blurred preview */}
      <div className={styles.previewContainer}>
        <div className={styles.blurredContent} aria-hidden="true">
          {preview || children}
        </div>
        <div className={styles.blurOverlay} />
      </div>

      {/* Gate card */}
      <div className={styles.gateCard}>
        <div className={styles.gateIcon}>{config.icon}</div>

        <h3 className={styles.gateTitle}>{displayTitle}</h3>

        <p className={styles.gateDescription}>{displayDescription}</p>

        <div className={styles.benefitBadge}>
          <svg className={styles.checkIcon} viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
          </svg>
          <span>{config.benefit}</span>
        </div>

        <div className={styles.gateActions}>
          <button
            onClick={handleSignIn}
            className={styles.signInButton}
            disabled={isSigningIn}
          >
            {isSigningIn ? (
              <>
                <div className={styles.buttonSpinner} />
                Signing in...
              </>
            ) : (
              <>
                <svg className={styles.buttonIcon} viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M3 3a1 1 0 011 1v12a1 1 0 11-2 0V4a1 1 0 011-1zm7.707 3.293a1 1 0 010 1.414L9.414 9H17a1 1 0 110 2H9.414l1.293 1.293a1 1 0 01-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0z" clipRule="evenodd" />
                </svg>
                Sign In
              </>
            )}
          </button>

          <button
            onClick={handleSignUp}
            className={styles.signUpButton}
            disabled={isSigningIn}
          >
            Create Free Account
          </button>
        </div>

        <p className={styles.gateFooter}>
          Free forever. No credit card required.
        </p>
      </div>
    </div>
  );
}

export default ContentGate;

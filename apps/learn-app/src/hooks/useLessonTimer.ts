import { useEffect, useRef, useState } from "react";

/**
 * Tracks active reading time on a lesson page.
 * Pauses when the tab/window is hidden (visibilitychange API).
 * Returns the number of seconds the user has been actively reading.
 */
export function useLessonTimer() {
  const [activeSeconds, setActiveSeconds] = useState(0);
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null);

  useEffect(() => {
    const startTimer = () => {
      if (intervalRef.current === null) {
        intervalRef.current = setInterval(() => {
          setActiveSeconds((s) => s + 1);
        }, 1000);
      }
    };

    const stopTimer = () => {
      if (intervalRef.current !== null) {
        clearInterval(intervalRef.current);
        intervalRef.current = null;
      }
    };

    const handleVisibilityChange = () => {
      if (document.visibilityState === "hidden") {
        stopTimer();
      } else {
        startTimer();
      }
    };

    // Start immediately if visible
    if (document.visibilityState === "visible") {
      startTimer();
    }

    document.addEventListener("visibilitychange", handleVisibilityChange);

    return () => {
      stopTimer();
      document.removeEventListener("visibilitychange", handleVisibilityChange);
    };
  }, []);

  return activeSeconds;
}

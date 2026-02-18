"use client";

import { useSearchParams } from "next/navigation";
import { useState, Suspense } from "react";
import { authClient, useSession } from "@/lib/auth-client";

function DeviceApproveContent() {
  const searchParams = useSearchParams();
  const userCode = searchParams.get("user_code") || "";
  const { data: session, isPending } = useSession();
  const [isProcessing, setIsProcessing] = useState(false);
  const [result, setResult] = useState<{
    type: "success" | "denied" | "error";
    message: string;
  } | null>(null);

  const handleApprove = async () => {
    setIsProcessing(true);
    try {
      await authClient.device.approve({ userCode });
      setResult({
        type: "success",
        message:
          "Device authorized successfully. You can close this page and return to your CLI.",
      });
    } catch {
      setResult({
        type: "error",
        message: "Failed to authorize device. The code may have expired.",
      });
    } finally {
      setIsProcessing(false);
    }
  };

  const handleDeny = async () => {
    setIsProcessing(true);
    try {
      await authClient.device.deny({ userCode });
      setResult({
        type: "denied",
        message: "Device authorization denied.",
      });
    } catch {
      setResult({
        type: "error",
        message: "Failed to deny device authorization.",
      });
    } finally {
      setIsProcessing(false);
    }
  };

  if (isPending) {
    return (
      <div className="flex items-center justify-center py-8">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-pana-500"></div>
      </div>
    );
  }

  if (!session) {
    // Redirect to sign-in, preserving the return URL
    const currentUrl = `/device/approve?user_code=${encodeURIComponent(userCode)}`;
    window.location.href = `/auth/sign-in?redirect=${encodeURIComponent(currentUrl)}`;
    return null;
  }

  if (!userCode) {
    return (
      <div className="max-w-md mx-auto">
        <div className="bg-white rounded-2xl shadow-lg p-8 text-center">
          <p className="text-gray-600">
            No device code provided. Please go back and enter your code.
          </p>
          <a
            href="/device"
            className="inline-block mt-4 text-pana-500 hover:text-pana-600 font-medium"
          >
            Enter device code
          </a>
        </div>
      </div>
    );
  }

  if (result) {
    return (
      <div className="max-w-md mx-auto">
        <div className="bg-white rounded-2xl shadow-lg p-8 text-center">
          {result.type === "success" && (
            <div className="inline-flex items-center justify-center w-12 h-12 rounded-full bg-green-50 mb-4">
              <svg
                className="w-6 h-6 text-green-500"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M5 13l4 4L19 7"
                />
              </svg>
            </div>
          )}
          {result.type === "denied" && (
            <div className="inline-flex items-center justify-center w-12 h-12 rounded-full bg-gray-100 mb-4">
              <svg
                className="w-6 h-6 text-gray-500"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </div>
          )}
          {result.type === "error" && (
            <div className="inline-flex items-center justify-center w-12 h-12 rounded-full bg-red-50 mb-4">
              <svg
                className="w-6 h-6 text-red-500"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z"
                />
              </svg>
            </div>
          )}
          <h2 className="text-xl font-semibold text-gray-900 mb-2">
            {result.type === "success" && "Device Authorized"}
            {result.type === "denied" && "Authorization Denied"}
            {result.type === "error" && "Authorization Failed"}
          </h2>
          <p className="text-gray-600 text-sm">{result.message}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-md mx-auto">
      <div className="bg-white rounded-2xl shadow-lg p-8">
        <div className="text-center mb-6">
          <div className="inline-flex items-center justify-center w-12 h-12 rounded-full bg-yellow-50 mb-4">
            <svg
              className="w-6 h-6 text-yellow-600"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"
              />
            </svg>
          </div>
          <h2 className="text-2xl font-semibold text-gray-900 mb-2">
            Authorize Device
          </h2>
          <p className="text-gray-600 text-sm">
            A CLI application is requesting access to your account.
          </p>
        </div>

        <div className="bg-gray-50 rounded-lg p-4 mb-6">
          <p className="text-sm text-gray-500 mb-1">Device code</p>
          <p className="text-lg font-mono font-semibold text-gray-900 tracking-wider">
            {userCode}
          </p>
        </div>

        <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-3 mb-6">
          <p className="text-xs text-yellow-800">
            Only authorize this device if you initiated the request from your
            CLI. If you did not request this, click Deny.
          </p>
        </div>

        <div className="flex gap-3">
          <button
            onClick={handleDeny}
            disabled={isProcessing}
            className="flex-1 py-2.5 px-4 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500 disabled:opacity-50"
          >
            Deny
          </button>
          <button
            onClick={handleApprove}
            disabled={isProcessing}
            className="flex-1 py-2.5 px-4 border border-transparent rounded-lg text-sm font-medium text-white bg-pana-500 hover:bg-pana-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pana-500 disabled:opacity-50"
          >
            {isProcessing ? "Processing..." : "Authorize"}
          </button>
        </div>

        <p className="text-xs text-gray-500 text-center mt-4">
          Signed in as {session.user.email}
        </p>
      </div>
    </div>
  );
}

export default function DeviceApprovePage() {
  return (
    <Suspense
      fallback={
        <div className="flex items-center justify-center py-8">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-pana-500"></div>
        </div>
      }
    >
      <DeviceApproveContent />
    </Suspense>
  );
}

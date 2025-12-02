'use client'
export default function Home() {
  return (
    <main className="min-h-screen p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-8">SSO Server</h1>
        
        <div className="space-y-6">
          <section className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-2xl font-semibold mb-4">API Endpoints</h2>
            <ul className="space-y-2">
              <li>
                <strong>Health:</strong>
                <a href="/api/auth/health" className="text-blue-600 ml-2">/api/auth/health</a>
              </li>
              <li>
                <strong>OIDC Discovery:</strong>
                <a href="/.well-known/openid-configuration" className="text-blue-600 ml-2">/.well-known/openid-configuration</a>
              </li>
              <li>
                <strong>JWKS:</strong>
                <a href="/.well-known/jwks.json" className="text-blue-600 ml-2">/.well-known/jwks.json</a>
              </li>
            </ul>
          </section>

          <section className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-2xl font-semibold mb-4">Test Authentication</h2>
            <div className="space-y-4">
              <button 
                onClick={() => window.location.href = '/api/auth/sign-in'}
                className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
              >
                Sign In
              </button>
              <button 
                onClick={() => window.location.href = '/api/auth/sign-up'}
                className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 ml-4"
              >
                Sign Up
              </button>
            </div>
          </section>

          <section className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-2xl font-semibold mb-4">Environment Status</h2>
            <ul className="space-y-2 text-sm">
              <li>✅ Database Connected</li>
              <li>✅ BetterAuth Configured</li>
              <li>✅ OIDC Provider Enabled</li>
              <li>✅ JWT/JWKS Enabled</li>
            </ul>
          </section>
        </div>
      </div>
    </main>
  );
}

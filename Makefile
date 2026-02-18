.PHONY: dev dev-services dev-book dev-learn

dev-services:
	nx serve sso & \
	nx serve study-mode-api & \
	nx serve token-metering-api & \
	wait

dev-book:
	nx serve learn-app & \
	wait

# Local stack for learn-agentfactory skill testing
# Requires: brew services start postgresql@17 && brew services start redis
dev-learn:
	@echo "Starting SSO (3001) + Content API (8001) + Progress API (8002)..."
	nx serve sso & \
	nx serve content-api & \
	DATABASE_URL="postgresql+asyncpg://$(USER)@localhost:5432/progress" \
	REDIS_URL="redis://localhost:6379" \
	REDIS_PASSWORD="" \
	SSO_URL="http://localhost:3001" \
	DEV_MODE="false" \
	nx serve progress-api & \
	wait
-- Initialize token-metering-api database
-- Run this to create tables and seed initial data

-- Create tables (SQLModel creates these, but here for reference)
CREATE TABLE IF NOT EXISTS token_account (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL UNIQUE,
    balance INTEGER NOT NULL DEFAULT 0,
    total_granted INTEGER NOT NULL DEFAULT 0,
    total_used INTEGER NOT NULL DEFAULT 0,
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    last_activity_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS pricing (
    id SERIAL PRIMARY KEY,
    model VARCHAR(100) NOT NULL,
    pricing_version VARCHAR(20) NOT NULL,
    effective_date DATE NOT NULL DEFAULT CURRENT_DATE,
    input_cost_per_1k DECIMAL(10, 6) NOT NULL,
    output_cost_per_1k DECIMAL(10, 6) NOT NULL,
    max_tokens INTEGER NOT NULL DEFAULT 128000,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS token_allocation (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    allocation_type VARCHAR(20) NOT NULL,
    tokens INTEGER NOT NULL,
    reason VARCHAR(255),
    admin_id VARCHAR(36),
    payment_reference VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS token_transaction (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    request_id VARCHAR(100) NOT NULL UNIQUE,
    transaction_type VARCHAR(20) NOT NULL,
    model VARCHAR(100),
    input_tokens INTEGER NOT NULL DEFAULT 0,
    output_tokens INTEGER NOT NULL DEFAULT 0,
    total_tokens INTEGER NOT NULL DEFAULT 0,
    base_cost_usd DECIMAL(10, 6) NOT NULL DEFAULT 0,
    markup_usd DECIMAL(10, 6) NOT NULL DEFAULT 0,
    total_cost_usd DECIMAL(10, 6) NOT NULL DEFAULT 0,
    pricing_version VARCHAR(20),
    thread_id VARCHAR(100),
    context JSONB,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_token_account_user_id ON token_account(user_id);
CREATE INDEX IF NOT EXISTS idx_pricing_model ON pricing(model);
CREATE INDEX IF NOT EXISTS idx_pricing_active ON pricing(model, is_active);
CREATE INDEX IF NOT EXISTS idx_token_transaction_user_id ON token_transaction(user_id);
CREATE INDEX IF NOT EXISTS idx_token_transaction_thread_id ON token_transaction(thread_id);
CREATE INDEX IF NOT EXISTS idx_token_allocation_user_id ON token_allocation(user_id);

-- Seed pricing data
-- Clear existing pricing (for fresh setup)
DELETE FROM pricing;

-- DeepSeek Chat (study-mode-api ask agent) - $0.14/$0.28 per 1M tokens
INSERT INTO pricing (model, input_cost_per_1k, output_cost_per_1k, max_tokens, pricing_version, is_active)
VALUES ('deepseek-chat', 0.00014, 0.00028, 64000, 'deepseek-v3.2', true);

-- GPT-5 Nano (study-mode-api triage agent) - $0.15/$0.60 per 1M tokens
INSERT INTO pricing (model, input_cost_per_1k, output_cost_per_1k, max_tokens, pricing_version, is_active)
VALUES ('gpt-5-nano-2025-08-07', 0.00015, 0.00060, 128000, 'gpt5-nano-v1', true);

-- Claude Sonnet 4 - $3/$15 per 1M tokens
INSERT INTO pricing (model, input_cost_per_1k, output_cost_per_1k, max_tokens, pricing_version, is_active)
VALUES ('claude-sonnet-4-20250514', 0.003, 0.015, 200000, 'claude-sonnet-4-v1', true);

-- Claude Opus 4 - $15/$75 per 1M tokens
INSERT INTO pricing (model, input_cost_per_1k, output_cost_per_1k, max_tokens, pricing_version, is_active)
VALUES ('claude-opus-4-20250514', 0.015, 0.075, 200000, 'claude-opus-4-v1', true);

-- Verify
SELECT model, input_cost_per_1k as "$/1k in", output_cost_per_1k as "$/1k out", max_tokens, pricing_version
FROM pricing WHERE is_active = true ORDER BY model;

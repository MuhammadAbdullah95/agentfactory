#!/bin/bash
# generate-codeowners.sh - Generate CODEOWNERS from directory structure
# Usage: ./generate-codeowners.sh [--dry-run]

set -euo pipefail

DRY_RUN=false
if [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN=true
fi

OUTPUT_FILE=".github/CODEOWNERS"
ROOT_DIR=$(git rev-parse --show-toplevel 2>/dev/null || pwd)

echo "=== CODEOWNERS Generator ==="
echo "Root: $ROOT_DIR"
echo ""

# Create output directory
mkdir -p "$(dirname "$OUTPUT_FILE")"

# Generate CODEOWNERS content
generate_codeowners() {
    cat << 'EOF'
# CODEOWNERS - Auto-generated
# This file defines code ownership for the monorepo
# https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners

# ============================================
# DEFAULT OWNER (fallback for unmatched paths)
# ============================================
* @team-platform

# ============================================
# APPLICATIONS
# ============================================
EOF

    # Generate app ownership
    if [[ -d "apps" ]]; then
        for app in apps/*/; do
            if [[ -d "$app" ]]; then
                name=$(basename "$app")
                echo "/$app* @team-$name"
            fi
        done
    fi

    cat << 'EOF'

# ============================================
# PACKAGES / LIBRARIES
# ============================================
EOF

    # Generate package ownership
    if [[ -d "packages" ]]; then
        for pkg in packages/*/; do
            if [[ -d "$pkg" ]]; then
                name=$(basename "$pkg")
                echo "/$pkg* @team-$name"
            fi
        done
    fi

    cat << 'EOF'

# ============================================
# DOMAINS (if using domain-based structure)
# ============================================
EOF

    # Generate domain ownership
    if [[ -d "domains" ]]; then
        for domain in domains/*/; do
            if [[ -d "$domain" ]]; then
                name=$(basename "$domain")
                echo "/$domain* @team-$name"
            fi
        done
    fi

    cat << 'EOF'

# ============================================
# SERVICES
# ============================================
EOF

    # Generate service ownership
    if [[ -d "services" ]]; then
        for svc in services/*/; do
            if [[ -d "$svc" ]]; then
                name=$(basename "$svc")
                echo "/$svc* @team-$name"
            fi
        done
    fi

    cat << 'EOF'

# ============================================
# INFRASTRUCTURE & PLATFORM
# ============================================
/.github/             @team-platform
/infrastructure/      @team-platform @team-sre
/scripts/             @team-platform

# ============================================
# CONFIGURATION (Require senior/platform)
# ============================================
turbo.json            @team-platform
pnpm-workspace.yaml   @team-platform
tsconfig.base.json    @team-platform
*.lock                @team-platform

# ============================================
# SENSITIVE PATHS (Multiple reviewers required)
# ============================================
# /packages/auth/       @team-auth @security-leads
# /services/payments/   @team-payments @security-leads

# ============================================
# AI / AUTOMATION
# ============================================
/.claude/             @team-ai @team-platform

# ============================================
# DOCUMENTATION
# ============================================
/docs/                @team-docs
*.md                  @team-docs

EOF
}

if $DRY_RUN; then
    echo "=== DRY RUN - Would generate: ==="
    echo ""
    generate_codeowners
else
    echo "Generating $OUTPUT_FILE..."
    generate_codeowners > "$OUTPUT_FILE"
    echo ""
    echo "Generated: $OUTPUT_FILE"
    echo ""
    echo "=== Generated Content ==="
    cat "$OUTPUT_FILE"
fi

echo ""
echo "=== Notes ==="
echo "1. Replace @team-* placeholders with actual GitHub teams"
echo "2. Add @security-leads to sensitive paths"
echo "3. Ensure all GitHub teams exist in your organization"
echo "4. Test with: gh api repos/{owner}/{repo}/codeowners/errors"

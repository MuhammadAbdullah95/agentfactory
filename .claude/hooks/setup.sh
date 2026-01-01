#!/usr/bin/env bash
# ============================================================================
# Claude Code Hooks Setup Script
# Cross-platform setup for Windows (Git Bash), macOS, and Linux
# ============================================================================

set -e

# Colors (if terminal supports them)
if [ -t 1 ]; then
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    NC='\033[0m' # No Color
else
    RED=''
    GREEN=''
    YELLOW=''
    BLUE=''
    NC=''
fi

echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}  Claude Code Hooks Setup${NC}"
echo -e "${BLUE}============================================${NC}"
echo ""

# ============================================================================
# Detect Operating System
# ============================================================================

detect_os() {
    case "$(uname -s)" in
        Linux*)
            if grep -qi microsoft /proc/version 2>/dev/null; then
                echo "wsl"
            else
                echo "linux"
            fi
            ;;
        Darwin*)
            echo "macos"
            ;;
        CYGWIN*|MINGW*|MSYS*)
            echo "windows"
            ;;
        *)
            echo "unknown"
            ;;
    esac
}

OS=$(detect_os)

case "$OS" in
    windows)
        echo -e "Detected: ${GREEN}Windows (Git Bash/MSYS2)${NC}"
        ;;
    macos)
        echo -e "Detected: ${GREEN}macOS${NC}"
        ;;
    linux)
        echo -e "Detected: ${GREEN}Linux${NC}"
        ;;
    wsl)
        echo -e "Detected: ${GREEN}Windows Subsystem for Linux (WSL)${NC}"
        ;;
    *)
        echo -e "Detected: ${YELLOW}Unknown OS${NC}"
        ;;
esac
echo ""

# ============================================================================
# Check for jq
# ============================================================================

echo -e "${BLUE}Checking dependencies...${NC}"
echo ""

check_jq() {
    if command -v jq &>/dev/null; then
        local version=$(jq --version 2>/dev/null || echo "unknown")
        echo -e "  jq: ${GREEN}✓ Installed${NC} ($version)"
        return 0
    else
        echo -e "  jq: ${RED}✗ Not installed${NC}"
        return 1
    fi
}

check_python() {
    if command -v python3 &>/dev/null; then
        local version=$(python3 --version 2>/dev/null || echo "unknown")
        echo -e "  Python: ${GREEN}✓ Installed${NC} ($version)"
        return 0
    elif command -v python &>/dev/null; then
        local version=$(python --version 2>/dev/null || echo "unknown")
        echo -e "  Python: ${GREEN}✓ Installed${NC} ($version)"
        return 0
    elif command -v py &>/dev/null; then
        local version=$(py -3 --version 2>/dev/null || echo "unknown")
        echo -e "  Python: ${GREEN}✓ Installed${NC} (py launcher: $version)"
        return 0
    else
        echo -e "  Python: ${YELLOW}✗ Not installed${NC} (optional fallback)"
        return 1
    fi
}

JQ_INSTALLED=false
PYTHON_INSTALLED=false

if check_jq; then
    JQ_INSTALLED=true
fi

if check_python; then
    PYTHON_INSTALLED=true
fi

echo ""

# ============================================================================
# Install jq if missing
# ============================================================================

install_jq_windows() {
    echo -e "${BLUE}Select installation method for Windows:${NC}"
    echo "  1) winget (Windows Package Manager)"
    echo "  2) choco (Chocolatey)"
    echo "  3) scoop"
    echo "  4) Show manual instructions"
    echo "  5) Skip installation"
    echo ""
    read -p "Enter choice [1-5]: " choice

    case "$choice" in
        1)
            echo -e "${BLUE}Installing with winget...${NC}"
            if command -v winget &>/dev/null; then
                winget install jqlang.jq && echo -e "${GREEN}✓ jq installed successfully!${NC}" || echo -e "${RED}Installation failed${NC}"
            else
                echo -e "${RED}winget not found. Please install it or choose another method.${NC}"
            fi
            ;;
        2)
            echo -e "${BLUE}Installing with Chocolatey...${NC}"
            if command -v choco &>/dev/null; then
                choco install jq -y && echo -e "${GREEN}✓ jq installed successfully!${NC}" || echo -e "${RED}Installation failed. Try running as Administrator.${NC}"
            else
                echo -e "${RED}Chocolatey not found. Install from: https://chocolatey.org/install${NC}"
            fi
            ;;
        3)
            echo -e "${BLUE}Installing with scoop...${NC}"
            if command -v scoop &>/dev/null; then
                scoop install jq && echo -e "${GREEN}✓ jq installed successfully!${NC}" || echo -e "${RED}Installation failed${NC}"
            else
                echo -e "${RED}scoop not found. Install from: https://scoop.sh/${NC}"
            fi
            ;;
        4)
            echo ""
            echo -e "${YELLOW}Manual installation instructions:${NC}"
            echo "  1. Download jq from: https://jqlang.github.io/jq/download/"
            echo "  2. Download the Windows 64-bit executable"
            echo "  3. Rename it to 'jq.exe'"
            echo "  4. Move it to a folder in your PATH (e.g., C:\\Windows\\System32)"
            echo "  5. Restart your terminal"
            ;;
        5)
            echo -e "${YELLOW}Skipping jq installation. Hooks will use Python fallback.${NC}"
            ;;
        *)
            echo -e "${YELLOW}Invalid choice. Skipping installation.${NC}"
            ;;
    esac
}

install_jq_macos() {
    echo -e "${BLUE}Install jq using Homebrew?${NC}"
    read -p "Proceed? [y/N]: " confirm

    if [[ "$confirm" =~ ^[Yy]$ ]]; then
        if command -v brew &>/dev/null; then
            echo -e "${BLUE}Installing with Homebrew...${NC}"
            brew install jq && echo -e "${GREEN}✓ jq installed successfully!${NC}" || echo -e "${RED}Installation failed${NC}"
        else
            echo -e "${RED}Homebrew not found.${NC}"
            echo "Install Homebrew first: /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
            echo "Then run: brew install jq"
        fi
    else
        echo -e "${YELLOW}Skipping jq installation. Hooks will use Python fallback.${NC}"
    fi
}

install_jq_linux() {
    echo -e "${BLUE}Select your package manager:${NC}"
    echo "  1) apt (Debian/Ubuntu)"
    echo "  2) dnf (Fedora)"
    echo "  3) yum (CentOS/RHEL)"
    echo "  4) pacman (Arch)"
    echo "  5) zypper (openSUSE)"
    echo "  6) apk (Alpine)"
    echo "  7) Skip installation"
    echo ""
    read -p "Enter choice [1-7]: " choice

    case "$choice" in
        1)
            echo -e "${BLUE}Installing with apt...${NC}"
            sudo apt update && sudo apt install -y jq && echo -e "${GREEN}✓ jq installed successfully!${NC}" || echo -e "${RED}Installation failed${NC}"
            ;;
        2)
            echo -e "${BLUE}Installing with dnf...${NC}"
            sudo dnf install -y jq && echo -e "${GREEN}✓ jq installed successfully!${NC}" || echo -e "${RED}Installation failed${NC}"
            ;;
        3)
            echo -e "${BLUE}Installing with yum...${NC}"
            sudo yum install -y jq && echo -e "${GREEN}✓ jq installed successfully!${NC}" || echo -e "${RED}Installation failed${NC}"
            ;;
        4)
            echo -e "${BLUE}Installing with pacman...${NC}"
            sudo pacman -S --noconfirm jq && echo -e "${GREEN}✓ jq installed successfully!${NC}" || echo -e "${RED}Installation failed${NC}"
            ;;
        5)
            echo -e "${BLUE}Installing with zypper...${NC}"
            sudo zypper install -y jq && echo -e "${GREEN}✓ jq installed successfully!${NC}" || echo -e "${RED}Installation failed${NC}"
            ;;
        6)
            echo -e "${BLUE}Installing with apk...${NC}"
            sudo apk add jq && echo -e "${GREEN}✓ jq installed successfully!${NC}" || echo -e "${RED}Installation failed${NC}"
            ;;
        7)
            echo -e "${YELLOW}Skipping jq installation. Hooks will use Python fallback.${NC}"
            ;;
        *)
            echo -e "${YELLOW}Invalid choice. Skipping installation.${NC}"
            ;;
    esac
}

if [ "$JQ_INSTALLED" = false ]; then
    echo -e "${YELLOW}jq is not installed.${NC}"
    echo "jq provides the best performance for JSON parsing in hooks."
    echo "Without jq, hooks will fall back to Python (if available)."
    echo ""

    if [ "$PYTHON_INSTALLED" = true ]; then
        echo -e "${GREEN}Python is available as fallback.${NC}"
        echo ""
    else
        echo -e "${RED}Warning: Neither jq nor Python is installed!${NC}"
        echo "Hooks may not work correctly without at least one of these."
        echo ""
    fi

    read -p "Would you like to install jq now? [y/N]: " install_confirm

    if [[ "$install_confirm" =~ ^[Yy]$ ]]; then
        echo ""
        case "$OS" in
            windows)
                install_jq_windows
                ;;
            macos)
                install_jq_macos
                ;;
            linux|wsl)
                install_jq_linux
                ;;
            *)
                echo -e "${YELLOW}Unknown OS. Please install jq manually:${NC}"
                echo "  https://jqlang.github.io/jq/download/"
                ;;
        esac
    else
        echo -e "${YELLOW}Skipping jq installation.${NC}"
    fi
else
    echo -e "${GREEN}jq is already installed. No action needed.${NC}"
fi

echo ""

# ============================================================================
# Verify hook files have correct line endings
# ============================================================================

echo -e "${BLUE}Checking hook file line endings...${NC}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HOOKS_FIXED=0

for script in "$SCRIPT_DIR"/*.sh; do
    if [ -f "$script" ]; then
        # Check for CRLF (carriage return)
        if file "$script" 2>/dev/null | grep -q "CRLF"; then
            echo -e "  $(basename "$script"): ${YELLOW}CRLF detected, fixing...${NC}"
            # Fix CRLF -> LF
            sed -i 's/\r$//' "$script" 2>/dev/null || sed -i '' 's/\r$//' "$script" 2>/dev/null
            HOOKS_FIXED=$((HOOKS_FIXED + 1))
        else
            echo -e "  $(basename "$script"): ${GREEN}✓ OK${NC}"
        fi
    fi
done

if [ $HOOKS_FIXED -gt 0 ]; then
    echo ""
    echo -e "${GREEN}Fixed line endings in $HOOKS_FIXED file(s).${NC}"
fi

echo ""

# ============================================================================
# Clear warning flag (so hooks can show fresh status)
# ============================================================================

rm -f "$SCRIPT_DIR/.jq-warning-shown" 2>/dev/null

# ============================================================================
# Summary
# ============================================================================

echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}  Setup Complete${NC}"
echo -e "${BLUE}============================================${NC}"
echo ""

# Re-check jq after potential installation
if command -v jq &>/dev/null; then
    echo -e "  jq: ${GREEN}✓ Ready${NC}"
else
    if command -v python3 &>/dev/null || command -v python &>/dev/null || command -v py &>/dev/null; then
        echo -e "  jq: ${YELLOW}Not installed (using Python fallback)${NC}"
    else
        echo -e "  jq: ${RED}Not installed (no fallback available!)${NC}"
    fi
fi

echo ""
echo "Hooks are ready to use. Restart Claude Code to apply changes."
echo ""

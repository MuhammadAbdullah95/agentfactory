#!/usr/bin/env bash
# Common functions for Claude Code hooks
# Cross-platform compatible (Windows Git Bash, macOS, Linux)

# Flag file to track if we've shown jq warning
JQ_WARNING_FLAG=".claude/hooks/.jq-warning-shown"

# Detect available Python command (actually test it works, not just exists)
get_python_cmd() {
    # Test each Python command by actually running it
    # This handles Windows Store aliases that exist but don't work in Git Bash
    if python3 --version &>/dev/null 2>&1; then
        echo "python3"
    elif python --version &>/dev/null 2>&1; then
        echo "python"
    elif py -3 --version &>/dev/null 2>&1; then
        echo "py -3"
    else
        echo ""
    fi
}

# Show jq missing warning (only once)
warn_jq_missing() {
    if [ ! -f "$JQ_WARNING_FLAG" ]; then
        echo "⚠️  jq not found. For best performance, run: .claude/hooks/setup.sh" >&2
        mkdir -p "$(dirname "$JQ_WARNING_FLAG")" 2>/dev/null
        touch "$JQ_WARNING_FLAG" 2>/dev/null
    fi
}

# Parse JSON field with fallbacks: jq -> python3 -> python -> py
# Usage: parse_json "$json_string" "field_name"
# For nested: parse_json "$json_string" "parent.child"
parse_json() {
    local json="$1"
    local field="$2"
    local result=""

    # Try jq first (fastest)
    if command -v jq &>/dev/null; then
        result=$(echo "$json" | jq -r ".$field // empty" 2>/dev/null)
        if [ $? -eq 0 ]; then
            echo "$result"
            return 0
        fi
    else
        warn_jq_missing
    fi

    # Fallback to Python
    local py_cmd=$(get_python_cmd)
    if [ -n "$py_cmd" ]; then
        result=$(echo "$json" | $py_cmd -c "
import sys, json
try:
    data = json.loads(sys.stdin.read())
    keys = '$field'.split('.')
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, '')
        else:
            data = ''
            break
    print(data if data is not None else '')
except:
    print('')
" 2>/dev/null)
        echo "$result"
        return 0
    fi

    # Last resort: basic grep for simple top-level string fields
    # Only works for: "field": "value" (not nested, not arrays)
    result=$(echo "$json" | grep -o "\"$field\"[[:space:]]*:[[:space:]]*\"[^\"]*\"" 2>/dev/null | \
        sed 's/.*:[[:space:]]*"\([^"]*\)".*/\1/' 2>/dev/null | head -1)
    echo "$result"
}

# Parse JSON boolean field
# Returns "true" or "false" as string
parse_json_bool() {
    local json="$1"
    local field="$2"
    local result=""

    if command -v jq &>/dev/null; then
        result=$(echo "$json" | jq -r ".$field // false" 2>/dev/null)
        echo "$result"
        return 0
    fi

    local py_cmd=$(get_python_cmd)
    if [ -n "$py_cmd" ]; then
        result=$(echo "$json" | $py_cmd -c "
import sys, json
try:
    data = json.loads(sys.stdin.read())
    keys = '$field'.split('.')
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, False)
        else:
            data = False
            break
    print(str(data).lower())
except:
    print('false')
" 2>/dev/null)
        echo "$result"
        return 0
    fi

    echo "false"
}

# Validate JSON input
validate_json() {
    local json="$1"

    if command -v jq &>/dev/null; then
        echo "$json" | jq -e . >/dev/null 2>&1
        return $?
    fi

    local py_cmd=$(get_python_cmd)
    if [ -n "$py_cmd" ]; then
        echo "$json" | $py_cmd -c "import sys,json; json.loads(sys.stdin.read())" 2>/dev/null
        return $?
    fi

    # Can't validate without jq or python, assume valid
    return 0
}

# Get ISO timestamp (cross-platform)
# Prefers date command (reliable in Git Bash), falls back to Python
get_timestamp() {
    # Try date command first (most reliable across platforms)
    if date -u +"%Y-%m-%dT%H:%M:%SZ" 2>/dev/null; then
        return 0
    fi

    # Fallback to Python
    local py_cmd=$(get_python_cmd)
    if [ -n "$py_cmd" ]; then
        $py_cmd -c "from datetime import datetime,timezone; print(datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))" 2>/dev/null
        return 0
    fi

    # Last resort: local time without -u flag
    date +"%Y-%m-%dT%H:%M:%SZ" 2>/dev/null || echo "1970-01-01T00:00:00Z"
}

# Write JSONL log entry
# Usage: write_jsonl "file.jsonl" '{"key": "value"}'
write_jsonl() {
    local file="$1"
    local entry="$2"
    local dir=$(dirname "$file")

    mkdir -p "$dir" 2>/dev/null || return 1
    echo "$entry" >> "$file" 2>/dev/null
}

# Create JSON object (cross-platform)
# Usage: create_json "key1" "value1" "key2" "value2" ...
create_json() {
    local py_cmd=$(get_python_cmd)

    if command -v jq &>/dev/null; then
        local args=""
        local jq_expr="{"
        local first=true
        while [ $# -ge 2 ]; do
            local key="$1"
            local value="$2"
            shift 2
            args="$args --arg $key \"$value\""
            if [ "$first" = true ]; then
                jq_expr="$jq_expr\"$key\": \$$key"
                first=false
            else
                jq_expr="$jq_expr, \"$key\": \$$key"
            fi
        done
        jq_expr="$jq_expr}"
        eval "jq -nc $args '$jq_expr'" 2>/dev/null
        return $?
    fi

    if [ -n "$py_cmd" ]; then
        local py_dict="{"
        local first=true
        while [ $# -ge 2 ]; do
            local key="$1"
            local value="$2"
            shift 2
            # Escape quotes in value
            value=$(echo "$value" | sed 's/"/\\"/g')
            if [ "$first" = true ]; then
                py_dict="$py_dict\"$key\": \"$value\""
                first=false
            else
                py_dict="$py_dict, \"$key\": \"$value\""
            fi
        done
        py_dict="$py_dict}"
        echo "$py_dict" | $py_cmd -c "import sys,json; print(json.dumps(json.loads(sys.stdin.read())))" 2>/dev/null
        return $?
    fi

    # Manual JSON construction (last resort)
    local result="{"
    local first=true
    while [ $# -ge 2 ]; do
        local key="$1"
        local value="$2"
        shift 2
        value=$(echo "$value" | sed 's/"/\\"/g')
        if [ "$first" = true ]; then
            result="$result\"$key\": \"$value\""
            first=false
        else
            result="$result, \"$key\": \"$value\""
        fi
    done
    result="$result}"
    echo "$result"
}

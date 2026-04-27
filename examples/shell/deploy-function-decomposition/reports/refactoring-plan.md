# Monolithic Script → Function Decomposition

Refactored from a linear script to a structured script with functions, error handling, and idempotent steps.

## Design Pressure

- No functions — every step was inline, impossible to reuse or test.
- Error handling was minimal — `set -e` would abort mid-deployment.
- Rollback was inline and duplicated.
- Adding a new step required inserting code in the middle of the script.

## Applied Pattern

**Function decomposition + trap-based cleanup** — each deployment step is a named function. `trap` ensures rollback on any failure.

## After Code

```bash
#!/bin/bash
set -euo pipefail

APP_DIR="/var/www/myapp"
BACKUP_DIR="/var/backups/myapp"
BACKUP_FILE=""

# --- Utility functions ---

log() {
    echo "[$(date +%H:%M:%S)] $*"
}

cleanup() {
    if [ $? -ne 0 ] && [ -n "$BACKUP_FILE" ]; then
        log "Deployment failed. Restoring backup..."
        tar -xzf "$BACKUP_FILE" -C "$APP_DIR"
        systemctl restart myapp
        log "Rolled back to previous version."
    fi
}

# --- Deployment steps ---

backup() {
    local timestamp
    timestamp=$(date +%Y%m%d_%H%M%S)
    BACKUP_FILE="$BACKUP_DIR/backup_${timestamp}.tar.gz"
    log "Creating backup: $BACKUP_FILE"
    tar -czf "$BACKUP_FILE" -C "$APP_DIR" .
}

pull_code() {
    log "Pulling latest code..."
    git -C "$APP_DIR" pull origin main
}

install_deps() {
    log "Installing dependencies..."
    npm --prefix "$APP_DIR" install
}

build_app() {
    log "Running build..."
    npm --prefix "$APP_DIR" run build
}

restart_server() {
    log "Restarting server..."
    systemctl restart myapp
}

health_check() {
    log "Running health check..."
    sleep 5
    local status
    status=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/health)
    if [ "$status" != "200" ]; then
        log "Health check failed (HTTP $status)"
        return 1
    fi
    log "Health check passed."
}

# --- Main ---

trap cleanup EXIT

backup
pull_code
install_deps
build_app
restart_server
health_check

log "Deployment complete!"
```

## Key Changes

| Before | After |
|--------|-------|
| Linear script | Function decomposition |
| No error handling | `trap cleanup EXIT` — automatic rollback |
| Inline rollback | Centralized `cleanup()` function |
| No logging | `log()` with timestamps |
| `set -e` only | `set -euo pipefail` — strict mode |
| Hard to test | Each function is independently testable |

## Verification

- Same deployment behavior for success case.
- On any failure, rollback is automatic via `trap`.
- Adding a new step is a one-line addition to the main sequence.
- Each function can be tested in isolation.
- `set -euo pipefail` catches unset variables and pipe failures.

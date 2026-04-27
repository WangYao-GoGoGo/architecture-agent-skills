#!/bin/bash
# Before: Monolithic script — no functions, no error handling, no structure.

set -e

APP_DIR="/var/www/myapp"
BACKUP_DIR="/var/backups/myapp"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "Starting deployment..."

cd "$APP_DIR"

echo "Creating backup..."
tar -czf "$BACKUP_DIR/backup_$TIMESTAMP.tar.gz" .

echo "Pulling latest code..."
git pull origin main

echo "Installing dependencies..."
npm install

echo "Running build..."
npm run build

echo "Restarting server..."
systemctl restart myapp

echo "Running health check..."
sleep 5
STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/health)
if [ "$STATUS" != "200" ]; then
    echo "Health check failed! Restoring backup..."
    tar -xzf "$BACKUP_DIR/backup_$TIMESTAMP.tar.gz" -C "$APP_DIR"
    systemctl restart myapp
    echo "Rolled back to previous version."
    exit 1
fi

echo "Deployment complete!"

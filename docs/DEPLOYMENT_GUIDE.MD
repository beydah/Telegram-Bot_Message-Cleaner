# region -------------------- HEADER --------------------------------------------------------------------------------
# DEPLOYMENT_GUIDE.MD - Production Deployment Procedures
# endregion

# Deployment Guide

Follow these procedures to deploy the Message Cleaner in a production environment.

## 1. Environment Preparation
Ensure the host system has Python 3.8+ installed.

```bash
# Update system and install dependencies
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
```

## 2. Configuration Hardening
1. Copy `config/.env.example` to `config/.env`.
2. Restrict file permissions: `chmod 600 config/.env`.
3. Populate production tokens.

## 3. Process Management
It is recommended to use `systemd` or `pm2` for continuous execution.

Example Systemd Unit:
```ini
[Unit]
Description=Telegram Message Cleaner Bot
After=network.target

[Service]
WorkingDirectory=/path/to/project
ExecStart=/usr/bin/python3 backend/main.py
Restart=always
User=botuser

[Install]
WantedBy=multi-user.target
```

## 4. Monitoring
Monitor the bot using standard logging:
`tail -f /var/log/syslog | grep MessageCleanerBot`

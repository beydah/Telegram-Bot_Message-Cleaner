# Security Policy

## Supported Versions

We actively maintain and provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of our Telegram bot seriously. If you discover a security vulnerability, please follow these guidelines:

### How to Report

**Please do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report security vulnerabilities by:

1. **Creating a private security advisory** on GitHub:

   - Go to the repository's Security tab
   - Click "Report a vulnerability"
   - Fill out the advisory form

2. **Email us directly** (if private advisory is not available):
   - Send details to the repository maintainer
   - Include "SECURITY" in the subject line
   - Provide detailed information about the vulnerability

### What to Include

When reporting a vulnerability, please include:

- **Type of issue** (e.g., authentication bypass, data exposure, etc.)
- **Full paths** of source file(s) related to the vulnerability
- **Step-by-step instructions** to reproduce the issue
- **Proof-of-concept or exploit code** (if possible)
- **Impact assessment** - what an attacker could achieve
- **Suggested fix** (if you have one)

### Response Timeline

- **Initial Response**: Within 48 hours of report
- **Status Update**: Within 7 days with preliminary assessment
- **Resolution**: Security fixes will be prioritized and released as soon as possible

## Security Considerations

### Bot Token Security

**Critical**: Your bot token is equivalent to a password and must be protected:

- ✅ **DO**: Store bot tokens in environment variables
- ✅ **DO**: Use secure configuration management
- ✅ **DO**: Rotate tokens if compromised
- ❌ **DON'T**: Commit tokens to version control
- ❌ **DON'T**: Share tokens in public channels
- ❌ **DON'T**: Log tokens in console output

### Recommended Token Storage

Instead of hardcoding in `main.py`:

```python
import os
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GROUP_ID = int(os.getenv('TELEGRAM_GROUP_ID', '-100'))
```

### Group ID Protection

- Group IDs are sensitive information
- Don't expose them in logs or public repositories
- Use environment variables for production deployments

### Permission Management

**Bot Permissions**:

- Only grant minimum required permissions
- Regularly audit bot permissions in groups
- Remove unused permissions

**Required Permissions**:

- ✅ Delete messages (essential)
- ✅ Read messages (essential)
- ❌ Admin rights (not required beyond message deletion)

### Network Security

**API Communication**:

- All communication with Telegram API uses HTTPS
- The bot uses official `python-telegram-bot` library
- No custom HTTP implementations that could introduce vulnerabilities

**Rate Limiting**:

- Built-in rate limit handling prevents API abuse
- Automatic backoff on rate limit errors
- No aggressive polling that could trigger blocks

### Data Privacy

**Message Handling**:

- Bot only processes service messages for deletion
- No user message content is stored or logged
- Minimal logging of message metadata (IDs only)

**User Data**:

- No personal user information is collected
- No message content is persisted
- Bot operates with minimal data retention

### Input Validation

**Message Processing**:

- All message types are validated before processing
- Safe handling of malformed messages
- No execution of user-provided code or commands

**Configuration Validation**:

- Bot token format validation
- Group ID format validation
- Graceful handling of invalid configurations

## Security Best Practices for Users

### Deployment Security

1. **Environment Variables**:

   ```bash
   export TELEGRAM_BOT_TOKEN="your_bot_token_here"
   export TELEGRAM_GROUP_ID="-1001234567890"
   ```

2. **File Permissions**:

   ```bash
   chmod 600 main.py  # Restrict file access
   ```

3. **Process Management**:
   - Run bot with minimal system privileges
   - Use process managers like systemd for production
   - Implement proper logging without sensitive data

### Monitoring and Auditing

**Regular Security Checks**:

- Monitor bot activity logs
- Review group member changes
- Audit bot permissions periodically
- Check for unauthorized API usage

**Incident Response**:

- Have a plan for token compromise
- Know how to quickly revoke bot access
- Maintain backup configurations

### Production Deployment

**Server Security**:

- Keep Python and dependencies updated
- Use virtual environments
- Implement proper firewall rules
- Regular security updates

**Container Security** (if using Docker):

- Use official Python base images
- Run as non-root user
- Minimize container attack surface
- Regular image updates

## Known Security Considerations

### Telegram API Limitations

- **Message Age**: Telegram limits deletion of messages older than 48 hours
- **Admin Messages**: Some admin messages cannot be deleted
- **Rate Limits**: Aggressive deletion may trigger temporary blocks

### Bot Limitations

- **Group Only**: Bot only works in groups with admin permissions
- **Permission Dependent**: Functionality depends on granted permissions
- **API Dependent**: Security relies on Telegram's API security

## Vulnerability Disclosure Policy

### Coordinated Disclosure

We follow responsible disclosure practices:

1. **Report received** - We acknowledge receipt within 48 hours
2. **Investigation** - We investigate and validate the report
3. **Fix development** - We develop and test a fix
4. **Release** - We release the fix and security advisory
5. **Public disclosure** - Details are made public after fix is available

### Recognition

Security researchers who responsibly disclose vulnerabilities will be:

- Credited in security advisories (if desired)
- Listed in our security acknowledgments
- Notified when fixes are released

## Security Updates

### Notification Channels

Stay informed about security updates:

- **GitHub Security Advisories**: Automatic notifications for repository watchers
- **Release Notes**: Security fixes are highlighted in releases
- **Issues**: Security-related issues are tagged appropriately

### Update Process

When security updates are released:

1. **Immediate**: Critical security fixes
2. **Priority**: High-impact vulnerabilities
3. **Regular**: Low-impact security improvements

## Contact Information

For security-related questions or concerns:

- **Security Issues**: Use GitHub Security Advisories
- **General Security Questions**: Create an issue with `security` label
- **Urgent Security Matters**: Contact repository maintainers directly

## Security Checklist for Contributors

Before contributing code, ensure:

- [ ] No hardcoded secrets or tokens
- [ ] Proper input validation
- [ ] Safe error handling without information disclosure
- [ ] No introduction of new dependencies without security review
- [ ] Code follows secure coding practices
- [ ] No logging of sensitive information

## Compliance and Standards

This project aims to follow:

- **OWASP** secure coding practices
- **Python** security best practices
- **Telegram Bot API** security guidelines
- **Open source** security standards

---

**Remember**: Security is a shared responsibility. Users, contributors, and maintainers all play a role in keeping this project secure.

For the latest security information, always refer to the repository's Security tab and recent releases.

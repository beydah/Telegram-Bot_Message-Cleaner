# Telegram Service Message Cleaner Bot

A Python-based Telegram bot that automatically detects and deletes service messages in group chats to keep your conversations clean and focused.

## Features

- **Real-time Service Message Deletion**: Automatically removes service messages as they appear
- **Bulk Cleanup**: Clean up to 1000 old service messages with `/cleanup` command
- **Permission Checking**: Verifies bot has necessary permissions before attempting deletions
- **Comprehensive Service Message Detection**: Handles all types of Telegram service messages
- **Rate Limit Handling**: Built-in protection against Telegram API rate limits
- **Detailed Logging**: Console output for monitoring bot activity

## Service Messages Detected

The bot automatically detects and removes these types of service messages:

- New member joins
- Member leaves
- Pinned messages
- Chat photo changes
- Chat title changes
- Auto-delete timer changes
- Forum topic events (created, closed, reopened, edited)
- Video chat events (started, ended, participants invited)
- Group/supergroup/channel creation messages
- Chat migration messages
- And more...

## Requirements

- Python 3.7+
- `python-telegram-bot` library
- A Telegram Bot Token
- Admin permissions in target group

## Installation

1. **Clone or download this repository**

2. **Install required dependencies**:

   ```bash
   pip install python-telegram-bot
   ```

3. **Create a Telegram Bot**:

   - Message [@BotFather](https://t.me/botfather) on Telegram
   - Use `/newbot` command and follow instructions
   - Copy your bot token

4. **Get your Group ID**:

   - Add your bot to the target group
   - Make the bot an admin with "Delete messages" permission
   - Send a message in the group
   - Visit `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Find your group ID (it will be negative, like `-1001234567890`)

5. **Configure the bot**:
   - Open `main.py`
   - Replace `BOT_TOKEN = ""` with your actual bot token
   - Replace `GROUP_ID = -100` with your actual group ID

## Usage

1. **Run the bot**:

   ```bash
   python main.py
   ```

2. **Available Commands**:

   - `/test` - Check if bot is working
   - `/cleanup` - Delete up to 1000 old service messages

3. **Automatic Operation**:
   - The bot will automatically delete service messages as they appear
   - No manual intervention required for real-time cleaning

## Configuration

### Bot Token

```python
BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
```

### Group ID

```python
GROUP_ID = -1001234567890  # Your group's ID (negative number)
```

## Bot Permissions Required

Make sure your bot has these permissions in the target group:

- ✅ Delete messages
- ✅ Read messages

## Code Structure

```
main.py
├── INFO Region - Project information
├── LIBRARY Region - Import statements
├── VARIABLE Region - Configuration variables
├── FUNCTION Region - Core bot functions
│   ├── F_Delete_Service_Message() - Real-time deletion
│   ├── F_Cleanup_Old_Messages() - Bulk cleanup
│   └── F_Test_Command() - Bot status check
└── MAIN Region - Bot initialization and startup
```

## Functions Overview

### F_Delete_Service_Message()

- Monitors all incoming messages
- Detects service messages automatically
- Deletes them with a 0.5-second delay
- Provides detailed logging

### F_Cleanup_Old_Messages()

- Scans up to 1000 previous messages
- Attempts to delete old service messages
- Shows progress updates
- Handles rate limits gracefully

### F_Test_Command()

- Simple command to verify bot functionality
- Responds with confirmation message

## Error Handling

The bot includes comprehensive error handling for:

- Missing permissions
- Rate limiting
- Network issues
- Message deletion failures
- Invalid configurations

## Logging

Console output includes:

- 🗑️ Successfully deleted messages
- ⚠️ Permission warnings
- ❌ Unexpected errors
- 📊 Cleanup progress
- ℹ️ Normal message info (for messages under 30 characters)

## Troubleshooting

### Bot not responding

- Check if bot token is correct
- Verify bot is added to the group
- Ensure bot has admin permissions

### Messages not being deleted

- Confirm bot has "Delete messages" permission
- Check if group ID is correct (should be negative)
- Some service messages may be protected by Telegram

### Rate limiting

- The bot includes automatic rate limit handling
- If you see "Too many requests" errors, the bot will wait automatically

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions, please create an issue in the repository.

---

**Note**: This bot only works in groups where it has admin permissions. It cannot delete messages in private chats or channels where it lacks proper permissions.

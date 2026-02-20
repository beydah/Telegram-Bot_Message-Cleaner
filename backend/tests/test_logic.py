import unittest
from unittest.mock import MagicMock, AsyncMock
from src.config import Config
from src.handlers.admin import is_admin

class TestBotLogic(unittest.IsolatedAsyncioTestCase):
    
    def setUp(self):
        Config.BOT_TOKEN = "test_token"
        Config.GROUP_ID = -100123456789
        
    def test_config_validation_success(self):
        """Passes when BOT_TOKEN is set."""
        try:
            Config.validate()
        except ValueError:
            self.fail("Config.validate() raised ValueError unexpectedly!")

    def test_config_validation_failure(self):
        """Raises ValueError when BOT_TOKEN is missing."""
        Config.BOT_TOKEN = None
        with self.assertRaises(ValueError):
            Config.validate()

    async def test_admin_check_unauthorized(self):
        """is_admin returns False for non-admin users."""
        mock_update = MagicMock()
        mock_context = MagicMock()
        mock_context.bot.get_chat_member = AsyncMock()
        
        # Mock a non-admin member
        mock_member = MagicMock()
        mock_member.status = "member"
        mock_context.bot.get_chat_member.return_return_value = mock_member
        
        # We need to set up the return value for the awaitable
        mock_context.bot.get_chat_member.return_value = mock_member
        
        result = await is_admin(mock_update, mock_context)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

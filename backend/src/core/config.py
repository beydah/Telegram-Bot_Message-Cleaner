# region -------------------- HEADER --------------------------------------------------------------------------------
# config.py - Enterprise Production Configuration
# endregion

# region -------------------- LIBRARIES --------------------------------------------------------------------------------
import os
import re
from dotenv import load_dotenv
# endregion

# region -------------------- CLASSES --------------------------------------------------------------------------------
class C_Config:
    # Central configuration controller with production-grade validation
    
    load_dotenv()
    
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    GROUP_ID = os.getenv("GROUP_ID", "-100")

    @classmethod
    def F_Validate(cls):
        # Validates that required environment variables are correctly populated for production
        if not cls.BOT_TOKEN:
            raise ValueError("❌ Production Error: BOT_TOKEN is missing!")
            
        # Basic regex check for Telegram Bot Token format
        token_pattern = re.compile(r"^\d+:[\w-]{35}$")
        if not token_pattern.match(cls.BOT_TOKEN):
            raise ValueError("❌ Production Error: BOT_TOKEN format is invalid!")

        try:
            cls.GROUP_ID = int(cls.GROUP_ID)
            if cls.GROUP_ID == -100:
                pass # Default ID handled by system
        except (ValueError, TypeError):
            raise ValueError("❌ Production Error: GROUP_ID must be a valid integer!")
# endregion

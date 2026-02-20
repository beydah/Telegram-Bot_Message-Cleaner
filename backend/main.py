# region -------------------- HEADER --------------------------------------------------------------------------------
# main.py - Enterprise Application Entry Point
# endregion

# region -------------------- LIBRARIES --------------------------------------------------------------------------------
import sys
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from src.core.config import C_Config
from src.core.logger import F_Setup_Logging, L_Logger
from src.cleaner.logic import F_Delete_Service_Message, F_Cleanup_Old_Messages, F_Test_Command
# endregion

# region -------------------- FUNCTIONS --------------------------------------------------------------------------------
def F_Main():
    # Application startup and handler registration
    try:
        F_Setup_Logging()
        C_Config.F_Validate()
        
        app = ApplicationBuilder().token(C_Config.BOT_TOKEN).build()
        
        app.add_handler(CommandHandler("cleanup", F_Cleanup_Old_Messages))
        app.add_handler(CommandHandler("test", F_Test_Command))
        app.add_handler(MessageHandler(filters.ALL, F_Delete_Service_Message))
        
        L_Logger.info("🚀 Bot is starting with Governance...")
        app.run_polling()
        
    except ValueError as ve:
        L_Logger.error(ve)
        sys.exit(1)
    except Exception as e:
        L_Logger.critical(f"💥 Fatal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    F_Main()
# endregion

# region -------------------- CLASSES --------------------------------------------------------------------------------
# Classes region required by structural rules
# endregion

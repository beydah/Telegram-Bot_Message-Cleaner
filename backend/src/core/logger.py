# region -------------------- HEADER --------------------------------------------------------------------------------
# logger.py - Enterprise Logging Governance
# endregion

# region -------------------- LIBRARIES --------------------------------------------------------------------------------
import logging
import sys
# endregion

# region -------------------- VARIABLES --------------------------------------------------------------------------------
# Global logger instance configured for the application
L_Logger = logging.getLogger("MessageCleanerBot")
# endregion

# region -------------------- FUNCTIONS --------------------------------------------------------------------------------
def F_Setup_Logging():
    # Initializes the global logging configuration for console output
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)]
    )

def F_Get_Logger(p_name):
    # Returns a child logger instance for specific modular domains
    return logging.getLogger(f"MessageCleanerBot.{p_name}")
# endregion

# region -------------------- CLASSES --------------------------------------------------------------------------------
# Classes region required by structural rules
# endregion

# region -------------------- HEADER --------------------------------------------------------------------------------
# logic.py - Cleaner Domain Business Logic
# endregion

# region -------------------- LIBRARIES --------------------------------------------------------------------------------
import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from src.core.config import C_Config
from src.core.logger import F_Get_Logger
# endregion

# region -------------------- VARIABLES --------------------------------------------------------------------------------
L_Logger = F_Get_Logger("Cleaner")
# endregion

# region -------------------- FUNCTIONS --------------------------------------------------------------------------------
async def F_Is_Admin(p_update, p_context):
    # Verifies if the triggering user has administrative privileges
    try:
        user = await p_context.bot.get_chat_member(C_Config.GROUP_ID, p_update.effective_user.id)
        return user.status in ["administrator", "creator"]
    except Exception as e:
        L_Logger.error(f"❌ Admin check failed: {e}")
        return False

async def F_Delete_Service_Message(p_update, p_context):
    # Detects and deletes service messages in real-time
    message = p_update.message
    if not message or message.chat.id != C_Config.GROUP_ID:
        return

    is_service = bool(
        message.new_chat_members or 
        message.left_chat_member or 
        message.message_auto_delete_timer_changed or
        message.pinned_message or 
        message.new_chat_photo or 
        message.new_chat_title or
        message.delete_chat_photo or 
        message.group_chat_created or 
        message.supergroup_chat_created or
        message.channel_chat_created or 
        message.migrate_to_chat_id or 
        message.migrate_from_chat_id or
        message.forum_topic_created or
        message.forum_topic_closed or
        message.forum_topic_reopened or
        message.forum_topic_edited or
        message.general_forum_topic_hidden or
        message.general_forum_topic_unhidden or
        message.video_chat_started or
        message.video_chat_ended or
        message.video_chat_participants_invited or
        message.web_app_data
    )

    if is_service:
        try:
            await asyncio.sleep(0.5)
            await message.delete()
            L_Logger.info(f"🗑️ Deleted service message: {message.message_id}")
        except Exception as e:
            L_Logger.warning(f"⚠️ Failed to delete: {e}")

async def F_Cleanup_Old_Messages(p_update, p_context):
    # Scans and removes historical service messages (Admin Only)
    if p_update.effective_chat.id != C_Config.GROUP_ID:
        return

    if not await F_Is_Admin(p_update, p_context):
        await p_update.message.reply_text("⛔ Restricted to administrators.")
        return

    status_msg = await p_update.message.reply_text("🔍 Scanning...")
    deleted_count = 0
    current_id = p_update.message.message_id
    
    for i in range(1, 1001):
        msg_id = current_id - i
        if msg_id <= 0:
            break
        try:
            await p_context.bot.delete_message(C_Config.GROUP_ID, msg_id)
            deleted_count += 1
            await asyncio.sleep(0.3)
        except:
            pass
        if i % 50 == 0:
            try:
                await status_msg.edit_text(f"🔍 Progress: {i}/1000\n🗑️ Deleted: {deleted_count}")
            except:
                pass

    await status_msg.edit_text(f"✅ Cleanup finished. Deleted: {deleted_count}")

async def F_Test_Command(p_update, p_context):
    # Verifies bot responsiveness
    await p_update.message.reply_text("✅ Governance refactor complete!")
# endregion

# region -------------------- CLASSES --------------------------------------------------------------------------------
# Classes region required by structural rules
# endregion

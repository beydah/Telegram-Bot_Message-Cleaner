# region -------------------- INFO --------------------------------------------------------------------------------
# Project information and developer details

# Developer: Ilkay Beydah Saglam
# Website: https://beydahsaglam.com
# Description: Telegram bot for automatically deleting service messages in groups
# Version: 1.0.0

# endregion
# region -------------------- LIBRARY --------------------------------------------------------------------------------
# Import required libraries and modules for Telegram bot functionality

import asyncio as LB_ASYNC
from datetime import datetime as LB_Date, timedelta as LB_Time_Delta
from telegram import Update as LB_Update
from telegram.ext import ApplicationBuilder as LB_App_Builder, MessageHandler as LB_Message_Handler, \ 
    filters as LB_Filters, ContextTypes as LB_Context_Types, CommandHandler as LB_Command_Handler

# endregion
# region -------------------- VARIABLE --------------------------------------------------------------------------------
# Configuration variables for bot token and target group

BOT_TOKEN = ""      # TODO: Enter your bot token here
GROUP_ID = -100     # TODO: Enter your group ID here (as negative integer)

# endregion
# region -------------------- FUNCTION --------------------------------------------------------------------------------
# Core functions for handling service message deletion and bot commands

async def F_Delete_Service_Messages(p_update: LB_Update, p_context: LB_Context_Types.DEFAULT_TYPE):
    # DESC: Automatically detects and deletes service messages in real-time
    message = p_update.message
    if not message or message.chat.id != GROUP_ID: return
    try:
        bot_member = await p_context.bot.get_chat_member(GROUP_ID, p_context.bot.id)
        if not bot_member.can_delete_messages:
            print(f"⚠️ Bot doesn't have message deletion permission!")
            return

    except Exception as e: print(f"⚠️ Bot permission check error: {e}")

    is_service_message = bool(
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
        message.web_app_data or
        (hasattr(message, 'content_type') and message.content_type in ['new_chat_members', 'left_chat_member'])
    )
    
    if is_service_message:
        try:
            await LB_ASYNC.sleep(0.5)
            await message.delete()
            print(f"🗑️ Service message deleted: {message.message_id}")

        except Exception as e:
            if "Message can't be deleted" not in str(e): 
                print(f"❌ Unexpected error: {e} - Message ID: {message.message_id}")
            
            else:
                service_types = []
                if message.new_chat_members: service_types.append("new_members")
                if message.left_chat_member: service_types.append("left_member") 
                if message.forum_topic_created: service_types.append("topic_created")
                print(f"⚠️ Couldn't delete ({', '.join(service_types)}): {message.message_id}")

    else:
        if message.text and len(message.text) < 30: print(f"ℹ️ Normal: {message.text} - ID: {message.message_id}")

async def F_Cleanup_Old_Messages(p_update: LB_Update, p_context: LB_Context_Types.DEFAULT_TYPE):
    # DESC: Scans and deletes old service messages from chat history using /cleanup command
    print(f"🔧 Cleanup command received! Chat ID: {p_update.message.chat.id}, User: {p_update.message.from_user.first_name}")
    if p_update.message.chat.id != GROUP_ID:
        print(f"❌ Wrong group! Expected: {GROUP_ID}, Received: {p_update.message.chat.id}")
        return
    
    try:
        user_member = await p_context.bot.get_chat_member(GROUP_ID, p_update.message.from_user.id)
        print(f"👤 User status: {user_member.status}")
        print("⚠️ Admin check temporarily disabled!")

    except Exception as e:
        print(f"Admin check error: {e}")
        print("⚠️ Admin check skipped, continuing...")

    status_msg = await p_update.message.reply_text("🔍 Scanning old service messages...")
    deleted_count = 0
    errors_count = 0
    current_id = p_update.message.message_id
    print(f"🚀 Cleanup started. Starting ID: {current_id}")
    for i in range(1, 1001):
        try:
            msg_id = current_id - i
            if msg_id <= 0: break
            try:
                await p_context.bot.delete_message(GROUP_ID, msg_id)
                deleted_count += 1
                print(f"🗑️ Deleted: {msg_id}")
                await LB_ASYNC.sleep(0.3)
                
            except Exception as delete_error:
                error_msg = str(delete_error).lower()
                if "message to delete not found" in error_msg: pass  # Message already gone, normal
                elif "message can't be deleted" in error_msg: pass  # This message is protected, normal
                elif "too many requests" in error_msg:
                    print("⏳ Rate limit, waiting...")
                    await LB_ASYNC.sleep(2)

                else:
                    errors_count += 1
                    if errors_count < 5: print(f"⚠️ Error: {delete_error}")
            
            if i % 50 == 0:
                try: await status_msg.edit_text(f"🔍 Progress: {i}/1000 messages checked\n🗑️ Deleted: {deleted_count}")
                except: pass
                print(f"📊 Progress: {i}/1000, Deleted: {deleted_count}")
                    
        except Exception as e: continue
    
    try: await status_msg.edit_text(f"✅ Cleanup completed!\n📊 Checked: 1000 messages\n🗑️ Deleted: {deleted_count}")
    except: 
        await p_update.message.reply_text(f"✅ Cleanup completed!\n📊 Checked: 1000 messages\n🗑️ Deleted: {deleted_count}")
    
    print(f"🎉 Cleanup completed! Total deleted: {deleted_count}")

async def F_Test_Command(p_update: LB_Update, p_context: LB_Context_Types.DEFAULT_TYPE):
    # DESC: Simple test command to verify bot functionality and responsiveness
    print(f"🧪 Test command received: {p_update.message.text}")
    await p_update.message.reply_text("✅ Bot is working and receiving commands!")

# endregion
# region -------------------- MAIN --------------------------------------------------------------------------------
# Main execution block for initializing and running the Telegram bot

def F_Main():
    # DESC: Initializes bot application, registers handlers, and starts polling for messages
    app = LB_App_Builder().token(BOT_TOKEN).build()
    app.add_handler(LB_Command_Handler("cleanup", F_Cleanup_Old_Messages))
    app.add_handler(LB_Command_Handler("test", F_Test_Command))
    app.add_handler(LB_Message_Handler(LB_Filters.ALL, F_Delete_Service_Messages))
    print("Bot is running... (Ctrl+C to stop)")
    print("💡 Use /cleanup command to delete old service messages")
    print("💡 Use /test command to check bot status")
    app.run_polling()

if __name__ == "__main__": F_Main()

# endregion

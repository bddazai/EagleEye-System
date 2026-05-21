import os
import telebot
from datetime import datetime

# EagleEye Tactical Alert Bot
# Integrates with the Ground Station to send real-time coordinates to security groups.

TOKEN = os.getenv('EAGLEEYE_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

def send_tactical_alert(chat_id, lat, lon, target_type, image_path=None):
    """
    Sends a tactical alert to a specific Telegram group.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    alert_msg = (
        f"🚨 **EAGLEEYE TACTICAL ALERT** 🚨\n"
        f"---------------------------\n"
        f"🕒 Time: {timestamp}\n"
        f"📍 Coordinates: {lat}, {lon}\n"
        f"🎯 Target: {target_type}\n"
        f"🔗 Map: https://www.google.com/maps?q={lat},{lon}\n"
        f"---------------------------\n"
        f"ACTION: Dispatch ground patrol to interception point."
    )
    
    if image_path and os.path.exists(image_path):
        with open(image_path, 'rb') as photo:
            bot.send_photo(chat_id, photo, caption=alert_msg, parse_mode='Markdown')
    else:
        bot.send_message(chat_id, alert_msg, parse_mode='Markdown')

if __name__ == "__main__":
    print("EagleEye Alert Bot Initialized...")
    # Example usage:
    # send_tactical_alert("-100XXXXXXXXX", 10.5105, 7.4165, "Suspected Bandit Camp")

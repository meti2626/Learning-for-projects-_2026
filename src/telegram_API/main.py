import asyncio
import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

# Load environment variables
load_dotenv(override=True)

TELEGRAM_API_ID = os.environ.get('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.environ.get('TELEGRAM_API_HASH')

async def main():
    # 'session_name' will be the name of the session file created
    client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)
    
    @client.on(events.NewMessage)
    async def handle_message(event):
        if event.message.text:
            print(f"Received: {event.message.text}")
            await event.reply(event.message.text)
            
    print("Starting Telegram Client...")
    await client.start()
    
    # Send a message to yourself ('me') to verify connection
    try:
        await client.send_message('me', 'Hello, myself! The client is running.')
        print("Test message sent to 'Saved Messages'.")
    except Exception as e:
        print(f"Could not send test message: {e}")

    print("Listening for messages...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
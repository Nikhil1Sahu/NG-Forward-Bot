# bot developer @OwnerofNG
from bot import Bot
from keep_alive import keep_alive

# start the tiny Flask server (for Render port binding)
keep_alive()

# start your Telegram bot
app = Bot()
app.run()

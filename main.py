import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from spy import log

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

app = ApplicationBuilder().token("5767897712:AAEnsMEY9J3eqyzVicNPIHf7x5O0XuPjQeg").build()

start_handler = CommandHandler('Start', start)
app.add_handler(start_handler)

app.add_handler(CommandHandler("Hi", hi_command))
app.add_handler(CommandHandler("Help", help_command))
app.add_handler(CommandHandler("Time", time_command))

echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    
app.add_handler(start_handler)
app.add_handler(echo_handler)



app.run_polling()
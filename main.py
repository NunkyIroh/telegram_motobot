from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token("5767897712:AAEnsMEY9J3eqyzVicNPIHf7x5O0XuPjQeg").build()

app.add_handler(CommandHandler("Hi", hi_command))
app.add_handler(CommandHandler("Help", help_command))
app.add_handler(CommandHandler("Time", time_command))



app.run_polling()
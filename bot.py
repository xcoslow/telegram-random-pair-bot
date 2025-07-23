

\f0\fs24 \cf0 from telegram import Update\
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes\
\
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    await update.message.reply_text("\uc0\u1055 \u1088 \u1080 \u1074 \u1077 \u1090 ! \u1071  \u1088 \u1072 \u1073 \u1086 \u1090 \u1072 \u1102 .")\
\
app = ApplicationBuilder().token("
\f1\fs26 \cf2 7526689928:AAEbPbLt4kl1lhQdj7HlorTKPFjZuYojdNM
\f0\fs24 \cf0 ").build()\
app.add_handler(CommandHandler("start", start))\
\
app.run_polling()\
}

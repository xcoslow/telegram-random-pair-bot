{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 .AppleSystemUIFontMonospaced-Medium;}
{\colortbl;\red255\green255\blue255;\red40\green146\blue255;}
{\*\expandedcolortbl;;\cspthree\c33218\c64182\c97252;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

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
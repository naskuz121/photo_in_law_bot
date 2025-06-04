from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

main_buttons = [['📥 Отримати гайд', 'ℹ️ Детальніше про курс']]
more_button = [['🔥 Хочу!']]
payment_buttons = [['💳 Тарифи'], ['➡️ Перейти до оплати', '❓ Задати питання']]
keyboard_main = ReplyKeyboardMarkup(main_buttons, resize_keyboard=True)
keyboard_more = ReplyKeyboardMarkup(more_button, resize_keyboard=True)
keyboard_payment = ReplyKeyboardMarkup(payment_buttons, resize_keyboard=True)

guide_link = "https://drive.google.com/uc?export=download&id=1Tp9DIgYJQHk_8g8NpQwkfga6BOk7penK"
guide_message = (
    "Привіт, фотограф!\n\n"
    f"🎁 [Скачати гайд «Захист авторського права для фотографа»]({guide_link})\n\n"
    "Ти вже зробив перший крок до впевненості у своїх правах.\n"
    "А тепер — давай по-справжньому розберемося, як ЗАХИСТИТИ себе, свої фото і свої гроші.\n\n"
    "Запрошую тебе на мій онлайн-курс «Фотограф в законі» — це юридичний захист, який не зітреться фільтром.\n\n"
    "Хочеш більше інформації про курс або дізнатися вартість участі?"
)

course_program = "Програма курсу Фотограф в законі 1.0\n\n..."

tariffs = "🟢 Базовий пакет — 2 500 грн\n..."

payment_reply = "Щоб отримати реквізити для оплати — напишіть «оплата» сюди 👉 @anastasiia_ful"
question_reply = "Щоб задати питання, пиши мені сюди 👉 @anastasiia_ful"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Обери опцію нижче:", reply_markup=keyboard_main)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in ['📥 Отримати гайд', 'ℹ️ Детальніше про курс']:
        await update.message.reply_text(guide_message, reply_markup=keyboard_more, parse_mode="Markdown")
    elif text == '🔥 Хочу!':
        await update.message.reply_text(course_program, reply_markup=keyboard_payment)
    elif text == '💳 Тарифи':
        await update.message.reply_text(tariffs)
    elif text == '➡️ Перейти до оплати':
        await update.message.reply_text(payment_reply)
    elif text == '❓ Задати питання':
        await update.message.reply_text(question_reply)
    else:
        await update.message.reply_text("Обери, будь ласка, варіант з меню 👇")

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
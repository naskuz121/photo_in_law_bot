
from telegram import Update, ReplyKeyboardMarkup, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

main_buttons = [['📥 Отримати гайд', 'ℹ️ Детальніше про курс']]
more_button = [['🔥 Хочу!']]
payment_buttons = [['💳 Тарифи'], ['➡️ Перейти до оплати', '❓ Задати питання']]
keyboard_main = ReplyKeyboardMarkup(main_buttons, resize_keyboard=True)
keyboard_more = ReplyKeyboardMarkup(more_button, resize_keyboard=True)
keyboard_payment = ReplyKeyboardMarkup(payment_buttons, resize_keyboard=True)

guide_message = (
    "Привіт, фотограф!\n"
    "Ти щойно завантажив безкоштовний гайд — отже, вже зробив перший крок до впевненості у своїх правах.\n\n"
    "А тепер — давай по-справжньому розберемося, як ЗАХИСТИТИ себе, свої фото і свої гроші.\n"
    "Запрошую тебе на мій онлайн-курс «Фотограф в законі» — це юридичний захист, який не зітреться фільтром.\n\n"
    "Хочеш більше інформації про курс або дізнатися вартість участі?"
)

course_program = (
    "📚 *Програма курсу «Фотограф в законі 1.0»*\n\n"
    "*1 модуль*\nАвторське право фотографа, особисті права, ©, водяний знак, кейси\n"
    "*2 модуль*\nСпівавторство, замовлення, мавпа-фотограф\n"
    "*3 модуль*\nКопіювання стилю, поз\n"
    "*4 модуль*\nЗйомка клієнтів, згода\n"
    "*5 модуль*\nПередплата, кейси незадоволених клієнтів\n"
    "*6 модуль*\nДоговори, оферти, згода. Кейс: Instagram без згоди\n"
    "✅ Відео, презентації, бонуси: гайд, реєстрація в е-суді, моральна шкода, чекліст"
)

tariffs = (
    "🟢 *Базовий — 2 500 грн*\n• Відео, презентації, бонуси, сертифікат\n\n"
    "🟡 *Стандартний — 3 500 грн*\n• Додано: Zoom, чат, перевірка тесту\n\n"
    "🔴 *Преміум — 5 000 грн*\n• Додано: консультація, шаблони, знижки, рекомендації"
)

payment_reply = "Щоб отримати реквізити для оплати — напишіть «оплата» сюди 👉 @anastasiia_ful"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Обери опцію нижче:", reply_markup=keyboard_main)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in ['📥 Отримати гайд', 'ℹ️ Детальніше про курс']:
        await update.message.reply_document(InputFile("DMCA_Guide_Final.docx"))
        await update.message.reply_text(guide_message, reply_markup=keyboard_more)
    elif text == '🔥 Хочу!':
        await update.message.reply_text(course_program, reply_markup=keyboard_payment, parse_mode="Markdown")
    elif text == '💳 Тарифи':
        await update.message.reply_text(tariffs, parse_mode="Markdown")
    elif text in ['➡️ Перейти до оплати', '❓ Задати питання']:
        await update.message.reply_text(payment_reply)
    else:
        await update.message.reply_text("Обери, будь ласка, варіант з меню 👇")

import os
app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()


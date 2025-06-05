from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

keyboard_main = ReplyKeyboardMarkup([['📥 Отримати гайд', 'ℹ️ Детальніше про курс']], resize_keyboard=True)
keyboard_more = ReplyKeyboardMarkup([['🔥 Хочу!']], resize_keyboard=True)
keyboard_payment = ReplyKeyboardMarkup([['💳 Тарифи'], ['➡️ Перейти до оплати', '❓ Задати питання']], resize_keyboard=True)

guide_message = """Привіт, фотограф!
Ти щойно завантажив безкоштовний гайд — отже, вже зробив перший крок до впевненості у своїх правах.
А тепер — давай по-справжньому розберемося, як ЗАХИСТИТИ себе, свої фото і свої гроші.
Запрошую тебе на мій онлайн-курс «Фотограф в законі» — це юридичний захист, який не зітреться фільтром.
Хочеш більше інформації про курс або дізнатися вартість участі?
"""

course_program = """📚 Програма курсу «Фотограф в законі 1.0»

1. Авторське право фотографа.
1.1. Особисті немайнові права автора. Недоторканість твору.
1.2. Особисті майнові права автора.
1.3. Які твори захищаються авторським правом.
1.4. Способи захисту авторського права:
• розміщення знаку ©
• водяний знак
• реєстрація авторського права
1.5. Об’єкти, що не охороняються авторським правом.

2. Права інших осіб на твір. Виконання роботи на замовлення:
• співавторство
• службовий твір
• твір за замовленням

3. Копіювання стилю, поз, обстановки. Надихання чужими фото.

4. Кому належить право на фото клієнта? Зйомка у публічних місцях, згода на зйомку.

5. Взаємодія з клієнтами:
• ЦКУ і ЗУ «Про захист прав споживачів»
• Що вказати в договорі про надання послуг
• Як оформити передплату
• Що робити, якщо клієнт незадоволений

6. Договір, оферта, згода на публікацію фото — що обрати?

✅ Усе це — у форматі:
• Відеоуроки
• Презентації зі статтями закону
• Судові справи
+ Бонуси: гайд, е-суд, моральна шкода, чекліст
"""

tariffs = """🟢 Базовий пакет — 2 500 грн
• Відеоуроки, доступ 2 міс., презентації, сертифікат

🟡 Стандартний пакет — 3 500 грн
• Все з базового
• Zoom, чат, перевірка тесту

🔴 Преміум пакет — 5 000 грн
• Все зі стандартного
• Консультація, шаблони, знижки, рекомендації
"""

payment_reply = "Щоб задати питання або отримати реквізити для оплати, пиши 👉 @anastasiia_ful"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Обери опцію нижче:", reply_markup=keyboard_main)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in ['📥 Отримати гайд', 'ℹ️ Детальніше про курс']:
        await update.message.reply_text(guide_message, reply_markup=keyboard_more)
    elif text == '🔥 Хочу!':
        await update.message.reply_text(course_program, reply_markup=keyboard_payment)
    elif text == '💳 Тарифи':
        await update.message.reply_text(tariffs)
    elif text in ['➡️ Перейти до оплати', '❓ Задати питання']:
        await update.message.reply_text(payment_reply)
    else:
        await update.message.reply_text("Обери, будь ласка, варіант з меню 👇")

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()

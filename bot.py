
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

keyboard_main = ReplyKeyboardMarkup([['📥 Отримати гайд', 'ℹ️ Детальніше про курс']], resize_keyboard=True)
keyboard_more = ReplyKeyboardMarkup([['🔥 Хочу!']], resize_keyboard=True)
keyboard_payment = ReplyKeyboardMarkup([['💳 Тарифи'], ['➡️ Перейти до оплати', '❓ Задати питання']], resize_keyboard=True)

guide_message = (
    "Привіт, фотограф!
"
    "Ти щойно завантажив безкоштовний гайд — отже, вже зробив перший крок до впевненості у своїх правах.

"
    "А тепер — давай по-справжньому розберемося, як ЗАХИСТИТИ себе, свої фото і свої гроші.
"
    "Запрошую тебе на мій онлайн-курс «Фотограф в законі» — це юридичний захист, який не зітреться фільтром.

"
    "Хочеш більше інформації про курс або дізнатися вартість участі?"
)

course_program = (
    "Програма курсу Фотограф в законі 1.0

"
    "1. Авторське право фотографа.
"
    "1.2. Особисті немайнові права автора. Недоторканість твору.
"
    "1.2. Особисті майнові права автора.
"
    "1.2. Які твори захищаються авторським правом.
"
    "1.3. Способи захисту авторського права.
"
    "1.3.1. Розміщення знаку ©
"
    "1.3.2. Водяний знак.
"
    "1.3.3. Реєстрація авторського права.
"
    "1.4. Об’єкти, що не охороняються авторським правом.

"
    "2. Права інших осіб на твір. Виконання роботи на замовлення.
"
    "2.1. Співавторство
"
    "2.2. Авторське право на службовий твір
"
    "2.3. Авторське право на твір, створений за замовленням
"
    "2.4. Підстави для захисту авторського права і суміжних прав

"
    "3. Копіювання стилю, поз, обстановки. Надихання чужими фото.

"
    "4. Кому належить право на фото клієнта? Зйомка у публічних місцях, згода на зйомку

"
    "5. Взаємодія з клієнтами.
"
    "5.1. Загальні положення ЦКУ та ЗУ «Про права споживачів».
"
    "5.2. На що звернути увагу фотографу в договорі про надання послуг.
"
    "5.3. Як оформити передплату правильно і вигідно?
"
    "5.4. Клієнту не подобається результат.

"
    "6. Механізми оформлення стосунків з клієнтом: договір, оферта, згода публікацію фото, що краще обрати? Порівняння.

"
    "6 модулів включають:
"
    "• відео уроки по кожному модулю;
"
    "• презентація до уроків, із зазначенням статей законів;
"
    "• приклади – реальні судові справи по темі.
"
    "+ Бонуси: гайд, е-суд, моральна шкода, чек-ліст по референсах.
"
)

tariffs = (
    "🟢 Базовий пакет — 2 500 грн
"
    "• Відео уроки, доступ на 2 місяці, презентації, сертифікат

"
    "🟡 Стандартний пакет — 3 500 грн
"
    "• Все з базового пакету
"
    "• Zoom-сесія, чат, письмові питання, перевірка тесту

"
    "🔴 Преміум пакет — 5 000 грн
"
    "• Все зі стандартного пакету
"
    "• Консультація, шаблони, знижки, пріоритет"
)

payment_reply = "Щоб задати питання або отримати реквізити для оплати, пиши сюди 👉 @anastasiia_ful"

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

import os
app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()

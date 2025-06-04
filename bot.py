from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

main_buttons = [[' Отримати гайд', ' Детальніше про курс']]
more_button = [[' Хочу!']]
payment_buttons = [[' Тарифи'], [' Перейти до оплати', ' Задати питання']]
keyboard_main = ReplyKeyboardMarkup(main_buttons, resize_keyboard=True)
keyboard_more = ReplyKeyboardMarkup(more_button, resize_keyboard=True)
keyboard_payment = ReplyKeyboardMarkup(payment_buttons, resize_keyboard=True)

guide_link = "https://drive.google.com/uc?export=download&id=1Tp9DIgYJQHk_8g8NpQwkfga6BOk7penK"
guide_message = (
    "Привіт, фотограф!\n\n"
    f" [Скачати гайд «Захист авторського права для фотографа»]({guide_link})\n\n"
    "Ти вже зробив перший крок до впевненості у своїх правах.\n"
    "А тепер — давай по-справжньому розберемося, як ЗАХИСТИТИ себе, свої фото і свої гроші.\n\n"
    "Запрошую тебе на мій онлайн-курс «Фотограф в законі» — це юридичний захист, який не зітреться фільтром.\n\n"
    "Хочеш більше інформації про курс або дізнатися вартість участі?"
)

course_program = (
    "Програма курсу Фотограф в законі 1.0\n\n"
    "1. Авторське право фотографа.\n"
    "  1.1. Особисті немайнові права автора. Недоторканість твору.\n"
    "  1.2. Особисті майнові права автора.\n"
    "  1.3. Які твори захищаються авторським правом.\n"
    "  1.4. Способи захисту авторського права: ©, водяний знак, реєстрація.\n"
    "  1.5. Об’єкти, що не охороняються авторським правом.\n\n"
    "2. Права інших осіб на твір. Виконання роботи на замовлення.\n"
    "  2.1. Співавторство, службовий твір, твір за замовленням, захист суміжних прав.\n\n"
    "3. Копіювання стилю, поз, обстановки. Натхнення чужими фото.\n\n"
    "4. Кому належить фото клієнта? Публічні місця, згода на зйомку.\n\n"
    "5. Взаємодія з клієнтами.\n"
    "  5.1. Права споживачів.\n"
    "  5.2. Договір на надання послуг.\n"
    "  5.3. Як оформити передплату правильно.\n"
    "  5.4. Клієнту не подобається результат.\n\n"
    "6. Як оформити відносини: договір, оферта, згода. Що краще?\n"
    "   + Відео, презентації, реальні судові справи\n"
    "   + Бонус: гайд, чекліст, моральна шкода, реєстрація в е-суді"
)

tariffs = (
    " Базовий пакет — 2 500 грн\n"
    "• Відео уроки\n• Презентації та бонуси\n• Доступ 2 міс.\n• Сертифікат\n\n"
    " Стандартний пакет — 3 500 грн\n"
    "• Все з базового\n• Zoom-сесія\n• Чат, питання, перевірка тесту\n\n"
    " Преміум пакет — 5 000 грн\n"
    "• Все зі стандарту\n• Консультація\n• Шаблони договорів\n"
    "• Рекомендація, знижки, курс на 6 міс."
)

payment_reply = "Щоб отримати реквізити для оплати — напишіть «оплата» сюди  @anastasiia_ful"
question_reply = "Щоб задати питання, пиши мені сюди  @anastasiia_ful"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Обери опцію нижче:", reply_markup=keyboard_main)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in [' Отримати гайд', ' Детальніше про курс']:
        await update.message.reply_text(guide_message, reply_markup=keyboard_more, parse_mode="Markdown")
    elif text == ' Хочу!':
        await update.message.reply_text(course_program, reply_markup=keyboard_payment)
    elif text == ' Тарифи':
        await update.message.reply_text(tariffs)
    elif text == ' Перейти до оплати':
        await update.message.reply_text(payment_reply)
    elif text == ' Задати питання':
        await update.message.reply_text(question_reply)
    else:
        await update.message.reply_text("Обери, будь ласка, варіант з меню ")

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()


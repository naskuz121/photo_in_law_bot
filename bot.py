
naskuz121@gmail.com12:22 AM (0 minutes ago)

to me
import os
from telegram import Update, ReplyKeyboardMarkup, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Клавіатури
main_buttons = [[' Отримати гайд', ' Детальніше про курс']]
more_button = [[' Хочу!']]
payment_buttons = [[' Тарифи'], [' Перейти до оплати', ' Задати питання']]
keyboard_main = ReplyKeyboardMarkup(main_buttons, resize_keyboard=True)
keyboard_more = ReplyKeyboardMarkup(more_button, resize_keyboard=True)
keyboard_payment = ReplyKeyboardMarkup(payment_buttons, resize_keyboard=True)

# Повідомлення
guide_message = (
    "Привіт, фотограф!\n"
    "Ти щойно завантажив безкоштовний гайд — отже, вже зробив перший крок до впевненості у своїх правах.\n\n"
    "А тепер — давай по-справжньому розберемося, як ЗАХИСТИТИ себе, свої фото і свої гроші.\n"
    "Запрошую тебе на мій онлайн-курс «Фотограф в законі» — це юридичний захист, який не зітреться фільтром.\n\n"
    "Хочеш більше інформації про курс або дізнатися вартість участі?"
)

course_program = (
    " *Програма курсу Фотограф в законі 1.0*\n\n"
    "*1. Авторське право фотографа.*\n"
    "1.1. Особисті немайнові права автора. Недоторканість твору\n"
    "1.2. Особисті майнові права автора\n"
    "1.3. Які твори захищаються авторським правом\n"
    "1.4. Способи захисту авторського права\n"
    "  • Розміщення знаку ©\n"
    "  • Водяний знак\n"
    "  • Реєстрація авторського права\n"
    "1.5. Об’єкти, що не охороняються авторським правом\n\n"
    "*2. Права інших осіб на твір. Виконання роботи на замовлення.*\n"
    "  • Співавторство\n"
    "  • Авторське право на службовий твір\n"
    "  • Авторське право на твір, створений за замовленням\n"
    "  • Підстави для захисту авторського права і суміжних прав\n\n"
    "*3. Копіювання стилю, поз, обстановки. Надихання чужими фото.*\n\n"
    "*4. Кому належить право на фото клієнта? Зйомка у публічних місцях, згода на зйомку.*\n\n"
    "*5. Взаємодія з клієнтами.*\n"
    "  • Права споживача, передплата, відмова від послуг\n"
    "  • Як оформити передплату правильно і вигідно?\n"
    "  • Клієнту не подобається результат\n\n"
    "*6. Механізми оформлення стосунків з клієнтом.*\n"
    "  • Договір, оферта, згода на публікацію фото — що краще?\n\n"
    " *У кожному модулі:*\n"
    "• Відео урок\n"
    "• Презентація з вказаними нормами закону\n"
    "• Реальні судові приклади\n\n"
    " *Бонуси:*\n"
    "• Гайд про захист в соцмережах\n"
    "• Інструкція з реєстрації в е-суді\n"
    "• Гайд з моральної шкоди\n"
    "• Чек-ліст: «Як знімати по референсу без порушення авторського права»"
)

tariffs = (
    " *Базовий пакет — 2 500 грн*\n"
    "Підійде тим, хто хоче отримати основну інформацію без додаткових сервісів.\n"
    "• Доступ до відео уроків\n"
    "• Доступ до курсу на 2 місяці\n"
    "• Презентації та письмові бонуси\n"
    "• Сертифікат\n"
    "• Без участі в Zoom-сесії\n\n"

    " *Стандартний пакет — 3 500 грн*\n"
    "База + зворотній зв’язок\n"
    "• Все з базового пакету\n"
    "• Участь у Zoom-сесії з відповідями на запитання\n"
    "• Чат з учасниками\n"
    "• Можливість задати письмове запитання\n"
    "• Сертифікат + перевірка фінального тесту\n\n"

    " *Преміум пакет — 5 000 грн*\n"
    "Для тих, хто хоче максимум практичної цінності та персональної уваги\n"
    "• Все зі стандартного пакету\n"
    "• Індивідуальна 30-хв консультація з юристом Анастасією\n"
    "• Пріоритетний розгляд питань\n"
    "• Доступ до курсу на півроку\n"
    "• Рекомендація у ваших соцмережах / сертифікат з відзнакою\n"
    " Готові шаблони:\n"
    "• Договір з клієнтом\n"
    "• Згода на публікацію фото\n"
    " Знижка 20–30% на документи:\n"
    "• Публічна оферта (замість 5 000 грн — 3 500 грн)\n"
    "• Політика конфіденційності (замість 3 000 грн — 2 400 грн)\n"
    "• Індивідуальний договір (замість 3 000 грн — 2 400 грн)"
)

payment_reply = "Щоб отримати реквізити для оплати — напишіть «оплата» сюди  @anastasiia_ful"
question_reply = "Щоб задати питання, пиши мені сюди  @anastasiia_ful"

# Хендлери
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Обери опцію нижче:", reply_markup=keyboard_main)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in [' Отримати гайд', ' Детальніше про курс']:
        await update.message.reply_document(InputFile("DMCA_Guide_Final.docx"))
        await update.message.reply_text(guide_message, reply_markup=keyboard_more)
    elif text == ' Хочу!':
        await update.message.reply_text(course_program, reply_markup=keyboard_payment, parse_mode="Markdown")
    elif text == ' Тарифи':
        await update.message.reply_text(tariffs, parse_mode="Markdown")
    elif text == ' Перейти до оплати':
        await update.message.reply_text(payment_reply)
    elif text == ' Задати питання':
        await update.message.reply_text(question_reply)
    else:
        await update.message.reply_text("Обери, будь ласка, варіант з меню ")

# Запуск
app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()


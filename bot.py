
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters

# Увімкнення логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Посилання на гайд
GUIDE_LINK = "https://docs.google.com/document/d/1Tp9DIgYJQHk_8g8NpQwkfga6BOk7penK/uc?export=download"

# Повідомлення після отримання гайду
guide_message = (
    "Привіт, фотограф!\n\n"
    "Ти щойно завантажив безкоштовний гайд — отже, вже зробив перший крок до впевненості у своїх правах.\n\n"
    "🔍 У гайді ти знайдеш:\n"
    "• Що робити, якщо твої фото вкрали;\n"
    "• Як реагувати, коли клієнт не платить або скасовує зйомку;\n"
    "• Які документи захищають фотографа і коли саме вони потрібні;\n"
    "• + бонус — перелік статей законів, які знадобляться фотографу.\n\n"
    "Гайд — це лише 10% того, що чекає тебе на онлайн-курсі «Фотограф в законі».\n"
    "Хочеш більше? 😉"
)

# Повна програма курсу
course_program = (
    "📚 *Програма курсу Фотограф в законі 1.0*\n\n"
    "1. Авторське право фотографа.\n"
    "1.1. Особисті немайнові права автора. Недоторканість твору.\n"
    "1.2. Особисті майнові права автора.\n"
    "1.3. Які твори захищаються авторським правом.\n"
    "1.4. Способи захисту авторського права:\n"
    "   • Розміщення знаку ©\n"
    "   • Водяний знак\n"
    "   • Реєстрація авторського права\n"
    "1.5. Об’єкти, що не охороняються авторським правом.\n\n"
    "2. Права інших осіб на твір. Виконання роботи на замовлення.\n"
    "   • Співавторство\n"
    "   • Авторське право на службовий твір\n"
    "   • Авторське право на твір, створений за замовленням\n"
    "   • Підстави для захисту авторського права і суміжних прав\n\n"
    "3. Копіювання стилю, поз, обстановки. Надихання чужими фото.\n\n"
    "4. Кому належить право на фото клієнта? Зйомка у публічних місцях, згода на зйомку.\n\n"
    "5. Взаємодія з клієнтами.\n"
    "   • Загальні положення ЦКУ та ЗУ «Про права споживачів».\n"
    "   • На що звернути увагу фотографу в договорі про надання послуг.\n"
    "   • Як оформити передплату правильно і вигідно?\n"
    "   • Клієнту не подобається результат.\n\n"
    "6. Механізми оформлення стосунків з клієнтом: договір, оферта, згода на публікацію фото — що краще обрати? Порівняння.\n\n"
    "У кожному модулі:\n"
    "• Відео уроки\n"
    "• Презентація зі статтями законів\n"
    "• Приклади реальних судових справ\n\n"
    "*Бонуси:*\n"
    "• Гайд – захист авторського права в соцмережах\n"
    "• Урок – реєстрація в електронному суді\n"
    "• Гайд з моральної шкоди\n"
    "• Чек-ліст — “Як знімати по референсу без порушення авторських прав”"
)

# Тарифи курсу
tariffs = (
    "💵 *Тарифи:*\n\n"
    "🟢 *Базовий пакет — 2 500 грн*\n"
    "Підійде тим, хто хоче отримати основну інформацію без додаткових сервісів.\n"
    "• Доступ до відео уроків\n"
    "• Доступ до курсу на 2 місяці\n"
    "• Презентації та письмові бонуси\n"
    "• Сертифікат\n"
    "• Без участі в Zoom-сесії\n\n"
    "🟡 *Стандартний пакет — 3 500 грн*\n"
    "• Все з базового пакету\n"
    "• Участь у Zoom-сесії\n"
    "• Чат з учасниками\n"
    "• Можливість задати письмове запитання\n"
    "• Сертифікат + перевірка фінального тесту\n\n"
    "🔴 *Преміум пакет — 5 000 грн*\n"
    "• Все зі стандартного пакету\n"
    "• Індивідуальна консультація\n"
    "• Пріоритетний розгляд питань\n"
    "• Доступ до курсу на півроку\n"
    "• Рекомендація у соцмережах / сертифікат з відзнакою\n"
    "• Шаблони документів\n"
    "• Знижка 20–30% на індивідуальні документи"
)

# Відповідь на "Задати питання"
ask_question = "Щоб задати питання, пиши мені сюди 👉 @anastasiia_ful"

# Обробка старту
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_document(GUIDE_LINK)
    await update.message.reply_text(guide_message, reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("🔎 Програма курсу", callback_data="program")],
        [InlineKeyboardButton("💵 Тарифи", callback_data="tariffs")],
        [InlineKeyboardButton("✉️ Задати питання", callback_data="question")]
    ]))

# Обробка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "program":
        await query.message.reply_text(course_program, parse_mode="Markdown")
    elif query.data == "tariffs":
        await query.message.reply_text(tariffs, parse_mode="Markdown")
    elif query.data == "question":
        await query.message.reply_text(ask_question)

# Основний запуск
if __name__ == '__main__':
    import os
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

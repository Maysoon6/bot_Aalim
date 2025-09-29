from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7952506661:AAEFIbkpBvEMdifwBVv7WZMQbUzHyKci9gI"

# دالة /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("المستوى التمهيدي", callback_data="level1")],
        [InlineKeyboardButton("📗 المستوى الثاني", callback_data="level2")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("اختر المستوى:", reply_markup=reply_markup)

# التعامل مع الأزرار
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "level1":
        keyboard = [
            [InlineKeyboardButton("📂 مادة الرياضيات", callback_data="math")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="back_main")]
        ]
        await query.edit_message_text("مستوى 1 - اختر المادة:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "math":
        keyboard = [
            [InlineKeyboardButton("📄 ملخص", callback_data="math_pdf")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="level1")]
        ]
        await query.edit_message_text("📘 مادة الرياضيات:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "math_pdf":
        await query.message.reply_document(document=open("سمية.pdf", "rb"), filename="math.pdf")
        await query.answer("📄 تم إرسال الملف!")

    elif query.data == "back_main":
        await start(update, context)

# تشغيل البوت
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()

if __name__ == "__main__":
    main()

import logging

from telegram.utils import helpers

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    
    chat = update.effective_chat

    print(chat.id)

    keyboard = [
        [InlineKeyboardButton("Маргарита", callback_data='11'),InlineKeyboardButton("Четыре сыра", callback_data='22')],
        [InlineKeyboardButton("Американо", callback_data='33'),InlineKeyboardButton("Кальцоне", callback_data='44'),InlineKeyboardButton("Падана", callback_data='55'),],
        [InlineKeyboardButton("Индивидуальный заказ", callback_data='8')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите Пиццу:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    
    query = update.callback_query

    keyboard_16p = [[InlineKeyboardButton("M\n 45см\n 60грн", callback_data='1')],
    [InlineKeyboardButton("L\n 60см\n 80грн", callback_data='2')],
    [InlineKeyboardButton("XL\n 90см \n 120грн", callback_data='3')],]

    reply_markup_16p = InlineKeyboardMarkup(keyboard_16p)

    query.answer()
    print(query.data)

    if query.data == '11':
        query.edit_message_text(text=f"Выбирете размер вашей пиццы", reply_markup=reply_markup_16p)
    elif query.data == '22':
        query.edit_message_text(text=f"Выбирете размер вашей пиццы", reply_markup=reply_markup_16p)
    elif query.data == '33':
        query.edit_message_text(text=f"Выбирете размер вашей пиццы", reply_markup=reply_markup_16p)
    elif query.data == '44':
        query.edit_message_text(text=f"Выбирете размер вашей пиццы", reply_markup=reply_markup_16p)
    elif query.data == '55':
        query.edit_message_text(text=f"Выбирете размер вашей пиццы", reply_markup=reply_markup_16p)
    elif query.data == '8':
        query.edit_message_text(text=f"Мы перезвоним Вам в течении 5 минут")
    elif query.data == '1':
        query.edit_message_text(text=f"Введите свой номер и мы Вам перезвоним!")
    elif query.data == '2':
        query.edit_message_text(text=f"Введите свой номер и мы Вам перезвоним!")
    elif query.data == '3':
        query.edit_message_text(text=f"Введите свой номер и мы Вам перезвоним!")

    else:
        query.edit_message_text(text=f"Ссылка на оплату")

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("/call - Для того что бы позвонить нам\n /sale - акиции\n /friend - приведи друга получи скидку 10%")

def call_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("+380660137220")

def sale_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("✅Покупая 5 и более штук - 1 пицца по индивидуальному заказу беспланто!\n ✅Купи сегодня пиццу с ананасом и участвуй в розиграше целого ананаса!\n ✅Завтра для всех посетителей пиццерии напитки бесплатно, при условии покупки большого стакана!")

def friend_command(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.username)
    text = "Вот твоя ссылка:\n\n" + url
    update.message.reply_text(text)

def geophone(message) -> None:
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "Предоставь мне свои данные!", reply_markup=keyboard)


def main() -> None:
    updater = Updater("2026797713:AAFzOVBw_3sRrpsI0QSrJx36AYdmd4oMXEA")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(CommandHandler('call', call_command))
    updater.dispatcher.add_handler(CommandHandler('sale', sale_command))
    updater.dispatcher.add_handler(CommandHandler('friend', friend_command))
    updater.dispatcher.add_handler(CommandHandler('geophone', geophone))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

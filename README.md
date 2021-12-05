# Pizza_times_bot 
 
Бот который помогает выбрать пиццу  


## Список команд  

 * /start - Начало работы 
 * /pizza - начать выбирать пиццу 
 * /help - список команд  
 * /friend - реферальная ссылка  
 * /sale - скидка  
 * /call - можно нам позвонить  
 * /give_data - Ваш телефон или локация 
 * /change - смена времени получения рассылки
 * /stp - отписка от рассылки

### <a href = 'https://docs.google.com/presentation/d/1GerdPr9hSjaubdAfxp6TVD-6hv3LmJ4GR4FUErWguDc/edit#slide=id.p'>Призентация(старая)</a>

Если Вам срочно захотелось пиццу, но нету времени искать сайты и номера телефонов, то мой Бот Вам в этом поможет!)

<a href = 'https://t.me/Pizza_times_bot'>**Ссылочка на ботика**</a>

<a href = 'https://github.com/Sergiychik/bot/blob/main/picture/bot.mp4'>**Видео**</a>

![Picture](https://github.com/Sergiychik/bot/blob/main/picture/%D0%B1%D0%BE%D1%82.PNG)

## Код Бота

```python
from telegram.utils import helpers

from telegram import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    Update, 
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    keyboardbutton, 
    LabeledPrice, 
    ShippingOption, 
    Update
)
from telegram.ext import (
    Updater, 
    CommandHandler, 
    CallbackQueryHandler, 
    CallbackContext, 
    MessageHandler, 
    Filters, 
    PreCheckoutQueryHandler, 
    ShippingQueryHandler, 
    CallbackContext
)
from datetime import time
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
                    )
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    b = time(10, 00, 00)
    context.job_queue.run_daily(info, b, context=chat_id, name=str(chat_id))
    update.message.reply_text('Спасибо за подписку!🥳\n Теперь я буду тебя оповещать о новых скидках и акциях😎\n\n Если не хочешь их получать, то просто отпишись😢 /stp\n\n Хочешь изменить время получения👌😁 \n /change  Вводим команду вручную\n A дальше время по гринвичу\n Например:\n/change 10 00 00 = 12:00 у нас!')

    chat = update.effective_chat
    print(chat.id)

def pizza(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Маргарита", callback_data='11'),InlineKeyboardButton("Падана", callback_data='55')],
        [InlineKeyboardButton("Американо", callback_data='33'),InlineKeyboardButton("Кальцоне", callback_data='44')],
        [InlineKeyboardButton("Четыре сыра", callback_data='22')],
        [InlineKeyboardButton("Индивидуальный заказ", callback_data='8')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите Пиццу:', reply_markup=reply_markup)

def give_data(update: Update, context: CallbackContext) -> None:
    keyboard_r = [
        [
            KeyboardButton("Номер ☎️", request_contact=True),
            KeyboardButton("Локация 🗺️", request_location=True),
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard_r)
    update.message.reply_text("Предоставь мне свои данные для уточения заказа!🤠", reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    
    query = update.callback_query

    keyboard_16p = [[InlineKeyboardButton("📏Размер - 45см 💵Цена - 60грн", callback_data='111')],
    [InlineKeyboardButton("📏Размер - 60см 💵Цена - 80грн", callback_data='222')],
    [InlineKeyboardButton("📏Размер - 90см 💵Цена - 120грн", callback_data='333')]]

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
        query.edit_message_text(text=f"Введите свой номер☎️\n И мы перезвоним Вам в течении 5 минут\n /give_data")
    elif query.data == '1':
        query.edit_message_text(text=f"Введите свой номер☎️ и мы Вам перезвоним! - /give_data")
    elif query.data == '111':
        query.edit_message_text(text=f"Отправь мне свои данные ☎️ 🗺️\n Спец команда - /give_data")
    elif query.data == '222':
        query.edit_message_text(text=f"Отправь мне свои данные ☎️ 🗺️\n Спец команда - /give_data")
    elif query.data == '333':
        query.edit_message_text(text=f"Отправь мне свои данные ☎️ 🗺️\n Спец команда - /give_data")

    else:
        query.edit_message_text(text=f"Ссылка на оплату")

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("/call - Для того что бы позвонить нам\n /sale - акиции\n /friend - приведи друга получи скидку 10%\n /pizza - для выбора пиццы\n /give_data - поделиться своими данными")
#/p - оплата\n \

def call_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Вот мой номер: +380660137220\n Звони в любое рабочее время!😏\n Я всегда отечу!🤙")

def sale_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("✅Покупая 5 и более штук - 1 пицца по индивидуальному заказу беспланто!\n ✅Купи сегодня пиццу с ананасом и участвуй в розиграше целого ананаса!\n ✅Завтра для всех посетителей пиццерии напитки бесплатно, при условии покупки большого стакана!")

def friend_command(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.username)
    text = "Вот твоя ссылка:\n\n" + url
    update.message.reply_text(text)



def info(context: CallbackContext) -> None:
    job = context.job
    context.bot.send_message(job.context, text='Купи одну получи две со скидкой!')

def remove_job_if_exists(name: str, context: CallbackContext) -> bool:
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True

def stp(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = 'Вы успешно отписались!' if job_removed else 'Вы не подписаны на акции'
    update.message.reply_text(text)

def change(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    b = time(int(context.args[0]), int(context.args[1]), int(context.args[2]))
    context.job_queue.run_daily(info, b, context=chat_id, name=str(chat_id))
    text = 'Гринвич: '+ context.args[0] +' '+ context.args[1] +' '+ context.args[2]
    if job_removed:
        text += ' Время было успешно изменено!'
    update.message.reply_text(text)

def main() -> None:
    updater = Updater("2026797713:AAFzOVBw_3sRrpsI0QSrJx36AYdmd4oMXEA")
    a = updater.dispatcher.add_handler
    a(CommandHandler('start', start))
    a(CommandHandler('pizza', pizza))
    a(CallbackQueryHandler(button))
    a(CommandHandler('help', help_command))
    a(CommandHandler('call', call_command))
    a(CommandHandler('sale', sale_command))
    a(CommandHandler('friend', friend_command))
    a(CommandHandler("stp", stp))
    a(CommandHandler("change", change))
    a(CommandHandler('give_data', give_data))

    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```


# А вот и QR CODE
![Picture](https://github.com/Sergiychik/bot/blob/main/picture/qrchimpX2048%20(1).png)

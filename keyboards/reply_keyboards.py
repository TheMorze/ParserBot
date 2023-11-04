from aiogram.types import ReplyKeyboardMarkup, \
                          KeyboardButton
                          
async def get_news_keyboard_on() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text='✅ Включить рассылку')]
    ]
    reply_keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
    
    return reply_keyboard

async def get_news_keyboard_off() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text='❌ Отключить рассылку')]
    ]
    reply_keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
    
    return reply_keyboard
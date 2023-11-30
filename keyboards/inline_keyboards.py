from aiogram.types import InlineKeyboardMarkup, \
                          InlineKeyboardButton
                          
async def get_news_setting() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Sports.ru', callback_data='source_1'),
         InlineKeyboardButton(text='✅', callback_data='off_1')],
    ])
    
    return ikb
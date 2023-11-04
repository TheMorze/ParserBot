from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart, \
                            StateFilter

from lexicon.lexicon import LEXICON
from keyboards.reply_keyboards import get_news_keyboard_on, \
                                      get_news_keyboard_off

from database.service import Database
from filters.newsletter_filter import IsNewsletter

router: Router = Router()

@router.message(CommandStart(), ~IsNewsletter())
async def process_command_start(message: Message):
    
    Database.set_user(user_id=message.from_user.id,
                      first_name=message.from_user.first_name)
    await message.answer(text=LEXICON['/start'],
                         reply_markup=await get_news_keyboard_on())
    
@router.message(Command('help'))
async def process_command_help(message: Message):
    
    await message.answer(text=LEXICON['/help'])

@router.message(F.text.lower().in_(['✅ включить рассылку', '/newsletter_on']), \
                ~IsNewsletter())
async def process_news_on(message: Message):
    
    Database.set_user_newsletter(message.from_user.id, True)
    await message.answer(text=LEXICON['on_successful'],
                         reply_markup=await get_news_keyboard_off())
    
@router.message(F.text.lower().in_(['✅ включить рассылку', '/newsletter_on']))
async def news_already_on(message: Message):
    
    await message.answer(text=LEXICON['already_on'])
    
@router.message(F.text.lower().in_(['❌ отключить рассылку', '/newsletter_off']), \
                IsNewsletter())
async def process_news_off(message: Message):
    
    Database.set_user_newsletter(message.from_user.id, False)
    await message.answer(text=LEXICON['off_successful'],
                         reply_markup=await get_news_keyboard_on())
    
@router.message(F.text.lower().in_(['❌ отключить рассылку', '/newsletter_off']))
async def news_already_off(message: Message):
    
    await message.answer(text=LEXICON['already_off'])
    
@router.message(IsNewsletter())
async def process_others_on(message: Message):
    
    await message.answer(text=LEXICON['not_understand_on'])

@router.message(~IsNewsletter())
async def process_others_off(message: Message):
    
    await message.answer(text=LEXICON['not_understand_off'])
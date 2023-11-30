from aiogram import Router, F
from aiogram.types import Message

from lexicon.lexicon import LEXICON
from keyboards.inline_keyboards import *

from database.service import Database
from filters.newsletter_filter import IsNewsletter

router: Router = Router()

@router.message(F.text.lower().in_(['настройки', '/settings']))
async def process_settings_start(message: Message):
    await message.answer(text=LEXICON['/settings'])
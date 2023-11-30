from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon import LEXICON

from filters.newsletter_filter import IsNewsletter

router: Router = Router()

@router.message(IsNewsletter())
async def process_others_on(message: Message):
    
    await message.answer(text=LEXICON['not_understand_on'])

@router.message(~IsNewsletter())
async def process_others_off(message: Message):
    
    await message.answer(text=LEXICON['not_understand_off'])
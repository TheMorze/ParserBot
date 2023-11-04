from aiogram.filters import BaseFilter
from aiogram.types import Message

from database.service import Database

class IsNewsletter(BaseFilter):
        
    async def __call__(self, message: Message) -> bool:
        user_ids = Database.get_users_newsletter()
        
        return message.from_user.id in user_ids
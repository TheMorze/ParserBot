import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis

from config_data.config import Config, load_config
from config_data.menu import set_main_menu

from handlers import user_handlers, settings_handlers, \
                     other_handlers
from database.service import Database

from parsers.sports_ru import check_sports_ru

# Инициализируем логгер
logger = logging.getLogger(__name__)

# Функция конфигурации и запуска бота
async def main() -> None:
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s ' \
               '[%(asctime)s] - %(name)s - %(message)s'
    )
    
    logger.info('Starting bot')
    Database.create_users_table()
    
    config: Config = load_config()
    
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    redis = Redis(host='localhost')
    dp = Dispatcher(redis=redis)
    
    dp.include_router(user_handlers.router)
    dp.include_router(settings_handlers.router)
    
    dp.include_router(other_handlers.router)
    
    asyncio.create_task(check_sports_ru(bot))
    # Задаем боту меню с командами
    await set_main_menu(bot)
    
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
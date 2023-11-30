import asyncio
from loader import dp, bot
import handlers  # noqa
from database.models import Base
from database.db import engine


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

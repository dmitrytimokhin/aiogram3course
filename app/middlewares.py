# Есть два типа:
## Outer - внешний, который выполняется до фильтра. Он еще не знает какой handler будет выполнен, однако уже выполняет задачи, прописанные в middleware
## Inner - внутренний выполняется после того, как диспетчер выбрал нужный handler. И мы можем выполнять какие то действия до или после handler.
### В проекте можно и без них обойтись, но иногда очень полезны

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any, Awaitable
class TestMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        print('Действия до обработчика')
        result = await handler(event, data)
        print('Действия после обработчика')
        return result

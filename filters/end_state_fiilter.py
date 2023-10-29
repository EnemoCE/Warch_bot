import re 
from typing import Union, Dict, Any

from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject
from handlers.states import UniversalEndState



class EndStateFilter(BaseFilter):
    async def __call__(self, obj: TelegramObject,  state: FSMContext) -> bool:
        user_state = await state.get_state()
        if user_state is UniversalEndState.end_state:
            return True
        return False
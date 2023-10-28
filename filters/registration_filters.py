import re 
from typing import Union, Dict, Any

from aiogram.filters import BaseFilter
from aiogram.types import Message




class PasswordFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        password = message.text
        if not (12 <= len(password) <= 50):
            return False
        if not re.search(r'\d', password):
            return False
        if not re.search(r'[A-Z]', password):
            return False
        return {"password": message.text}
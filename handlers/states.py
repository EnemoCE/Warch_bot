from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    waiting_for_name = State()
    waiting_for_password = State()

class UniversalEndState(StatesGroup):
    end_state = State()

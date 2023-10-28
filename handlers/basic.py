from aiogram import Bot, types, Dispatcher
from aiogram import Router, F
from aiogram.types import Message
#executor
#from aiogram.utils.executor import start_webhook
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
#from aiogram.utils.keyboard import ReplyKeyboardBuilder
from filters.end_state_fiilter import EndStateFilter

router = Router()


@router.message(Command(commands=["cancel"]))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
    )

@router.message(EndStateFilter())
async def show_main_menu(message: Message):
    """
    builder = ReplyKeyboardBuilder()
    for i in range(1, 17):
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(4)
    await message.answer(
        "Выберите число:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )
    """
    kb = [
        [
            types.KeyboardButton(text="Add Links"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)
    await message.answer("Main Menu:", reply_markup=keyboard)
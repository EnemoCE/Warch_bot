from aiogram import Router, F
from aiogram.types import Message
#executor
#from aiogram.utils.executor import start_webhook
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from filters.registration_filters import PasswordFilter
from db.ops import user_exists, create_user
from aiogram.utils.markdown import hbold


router = Router()

class Registration(StatesGroup):
    waiting_for_name = State()
    waiting_for_password = State()


@router.message(Command("start"))
async def on_start(message: Message, state: FSMContext, session_maker):
    await state.clear()
    user = await user_exists(message.chat.id, session_maker)
    if user is None:
        await message.answer("Please enter your name:")
        await state.set_state(Registration.waiting_for_name)
    else:
        message.reply(f"Hello, {hbold(message.from_user.full_name)}!")


@router.message(lambda message: message.text, Registration.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await message.reply("Please enter your password:")
    await state.set_state(Registration.waiting_for_password)


router.message(lambda message: not message.text, Registration.waiting_for_name)
async def process_name_invalid(message: Message):
    return await message.reply("User name should not be empty!")


@router.message(lambda message: message.text, 
                Registration.waiting_for_password,
                PasswordFilter())
async def process_password(message: Message, state: FSMContext, session_maker):
    chat_id = message.chat.id
    user_data = await state.get_data()
    user_name = user_data['name']
    password = message.text
    await create_user(chat_id, user_name, password, session_maker)
    await state.clear()

router.message(lambda message: not message.text, Registration.waiting_for_password)
async def process_password_invalid(message: Message):
    return await message.reply("Incorrect password format!")

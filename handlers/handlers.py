from aiogram import Router, F
from aiogram.filters import Text, Command, StateFilter
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from FSM import FSM
from aiogram.fsm.state import default_state
from keyboards.keyboards import *
import datetime
from lexicon import lex

router: Router = Router()

# Хэндлер на команду /start
@router.message(Command(commands='start'))
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(text=f'Привет, {message.chat.username}!\n'
                              f'Выберите вид упражнения:', reply_markup=keyboard_type)
    with open('log.log', 'a', encoding='utf-8') as file:
        file.write(f'{datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")} ID: {message.chat.id} '
                   f'USERNAME: {message.chat.username} FIRST NAME: {message.chat.first_name} '
                   f'LAST NAME: {message.chat.last_name}\n')
    await state.set_state(FSM.fill_group)

# Хэндлер на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=lex['help'], parse_mode='MarkdownV2')

# Хэндлер на кнопки выбора типа упражнения
@router.callback_query(StateFilter(FSM.fill_group), Text(text=['speed_button', 'strong_button', 'endurance-button']))
async def group_button_pressed(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'speed_button':
        await callback.message.edit_text(text='Выбери упражнение:', reply_markup=keyboard_speed)
    elif callback.data == 'strong_button':
        await callback.message.edit_text(text='Выбери упражнение:', reply_markup=keyboard_strong)
    elif callback.data == 'endurance-button':
        await callback.message.edit_text(text='Выбери упражнение:', reply_markup=keyboard_endurance)
    await state.set_state(FSM.fill_type)

# Хэндлер на любое другое сообщение кроме нажатия кнопки выбора типа упражнения
@router.message(StateFilter(FSM.fill_group))
async def no_group_button_pressed(message: Message):
    await message.answer(text='Пожалуйста, пользуйтесь кнопками при выборе вида упражнений')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)

# Хэндлер на кнопки выбора упражнения
@router.callback_query(StateFilter(FSM.fill_type), Text(text=['button_100m', 'button_60m', 'button_10x10', 'button_swim100m',
                                                              'button_podt', 'button_vihod', 'button_podem', 'button_otzhim',
                                                              ]))
async def type_button_pressed(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'button_100m':
        await callback.message.edit_text(text=f'{lex["input_100m"]}')
        await state.set_state(FSM.fill_100m)
    elif callback.data == 'button_60m':
        await callback.message.edit_text(text=f'{lex["input_60m"]}')
        await state.set_state(FSM.fill_60m)
    elif callback.data == 'button_10x10':
        await callback.message.edit_text(text=f'{lex["input_10x10"]}')
        await state.set_state(FSM.fill_10x10)
    elif callback.data == 'button_swim100m':
        await callback.message.edit_text(text=f'{lex["input_swim100m"]}')
        await state.set_state(FSM.fill_swim100m)
    elif callback.data == 'button_podt':
        await callback.message.edit_text(text=f'{lex["input_podt"]}')
        await state.set_state(FSM.fill_podt)
    elif callback.data == 'button_vihod':
        await callback.message.edit_text(text=f'{lex["input_vihod"]}')
        await state.set_state(FSM.fill_vihod)
    elif callback.data == 'button_podem':
        await callback.message.edit_text(text=f'{lex["input_podem"]}')
        await state.set_state(FSM.fill_podem)
    elif callback.data == 'button_otzhim':
        await callback.message.edit_text(text=f'{lex["input_otzhim"]}')
        await state.set_state(FSM.fill_otzhim)


# Хэндлер при выборе 1км, 3 км
@router.callback_query(StateFilter(FSM.fill_type), Text(text=['button_1km', 'button_3km']))
async def press_1_or_3_km(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'button_1km':
        await callback.message.edit_text(text='Выбери возрастную группу:', reply_markup=keyboard_age)
        await state.set_state(FSM.fill_age_1km)
    elif callback.data == 'button_3km':
        await callback.message.edit_text(text='Выбери возрастную группу:', reply_markup=keyboard_age)
        await state.set_state(FSM.fill_age_3km)

@router.callback_query(StateFilter(FSM.fill_age_1km), Text(text=['button_before35', 'button_after35', 'button_back']))
async def age_button_pressed_1km(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'button_before35':
        await callback.message.edit_text(text=f'{lex["input_1km"]}')
        await state.set_state(FSM.fill_1km_before35)
    elif callback.data == 'button_after35':
        await callback.message.edit_text(text=f'{lex["input_1km"]}')
        await state.set_state(FSM.fill_1km_after35)
    elif callback.data == 'button_back':
        await callback.message.edit_text(text='Выбери упражнение:', reply_markup=keyboard_endurance)
        await state.set_state(FSM.fill_type)

@router.callback_query(StateFilter(FSM.fill_age_3km), Text(text=['button_before35', 'button_after35', 'button_back']))
async def age_button_pressed_3km(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'button_before35':
        await callback.message.edit_text(text=f'{lex["input_3km"]}')
        await state.set_state(FSM.fill_3km_before35)
    elif callback.data == 'button_after35':
        await callback.message.edit_text(text=f'{lex["input_3km"]}')
        await state.set_state(FSM.fill_3km_after35)
    elif callback.data == 'button_back':
        await callback.message.edit_text(text='Выбери упражнение:', reply_markup=keyboard_endurance)
        await state.set_state(FSM.fill_type)

# Хэндлер на кнопку Назад
@router.callback_query(Text(text=['button_back']), ~StateFilter(default_state))
async def strong_button_pressed(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text='Выберите вид упражнения:', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)











from aiogram import Router, F
from aiogram.filters import Text, Command, StateFilter
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from FSM import FSM
# from aiogram.fsm.state import default_state
from keyboards.keyboards import *
import datetime
from lexicon import lex

router: Router = Router()

@router.message(Command(commands='start'))
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(text=f'Привет, {message.chat.username}!\n'
                              f'{lex["choose_mode"]}', reply_markup=keyboard_mode)
    with open('log.log', 'a', encoding='utf-8') as file:
        file.write(f'{datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")} ID: {message.chat.id} '
                   f'USERNAME: {message.chat.username} FIRST NAME: {message.chat.first_name} '
                   f'LAST NAME: {message.chat.last_name}\n')
    await state.set_state(FSM.fill_mode)

# Хэндлер на режим Одиночных упражнений
@router.callback_query(StateFilter(FSM.fill_mode), Text(text=['simply_count', 'sum_count']))
async def choose_mode(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'simply_count':
        await callback.message.edit_text(text=lex['choose_type'], reply_markup=keyboard_type)
        await state.set_state(FSM.fill_group)
    elif callback.data == 'sum_count':
        await callback.message.edit_text(text=f'‼ Этот режим в процессе разработки\nВыберите режим работы:',
                                         reply_markup=keyboard_mode)
        await state.set_state(FSM.fill_mode)

# Хэндлер на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=lex['help'], parse_mode='MarkdownV2')

# Хэндлер на команду /help
@router.message(Command(commands='history'))
async def process_help_command(message: Message):
    await message.answer(text=lex['history'], parse_mode='MarkdownV2')

# Хэндлер на кнопки выбора типа упражнения
@router.callback_query(StateFilter(FSM.fill_group), Text(text=['speed_button', 'strong_button', 'endurance_button',
                                                               'agility_button', 'choose_mode']))
async def group_button_pressed(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'speed_button':
        await callback.message.edit_text(text=lex['choose_exersize'], reply_markup=keyboard_speed)
        await state.set_state(FSM.fill_speed)
    elif callback.data == 'strong_button':
        await callback.message.edit_text(text=lex['choose_exersize'], reply_markup=keyboard_strong)
        await state.set_state(FSM.fill_strong)
    elif callback.data == 'endurance_button':
        await callback.message.edit_text(text=lex['choose_exersize'], reply_markup=keyboard_endurance)
        await state.set_state(FSM.fill_endurance)
    elif callback.data == 'agility_button':
        await callback.message.edit_text(text=lex['choose_exersize'], reply_markup=keyboard_agility)
        await state.set_state(FSM.fill_agility)
    elif callback.data == 'choose_mode':
        await callback.message.edit_text(text=lex['choose_mode'], reply_markup=keyboard_mode)
        await state.set_state(FSM.fill_mode)

# Хэндлер на выбор упражнений на скорость
@router.callback_query(StateFilter(FSM.fill_speed), Text(text=['button_100m', 'button_60m', 'button_10x10', 'button_swim100m']))
async def speed_button_pressed(callback: CallbackQuery, state: FSMContext):
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

# Хэндлер на выбор упражнений на силу
@router.callback_query(StateFilter(FSM.fill_strong), Text(text=['button_podt', 'button_vihod', 'button_podem', 'button_otzhim']))
async def strong_button_pressed(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'button_podt':
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

# Хэндлер на выбор упражнений на выносливость
@router.callback_query(StateFilter(FSM.fill_endurance), Text(text=['button_1km', 'button_3km', 'button_back']))
async def endurance_button_pressed(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'button_1km':
        await callback.message.edit_text(text=lex['choose_age'], reply_markup=keyboard_age)
        await state.set_state(FSM.fill_age_1km)
    elif callback.data == 'button_3km':
        await callback.message.edit_text(text=lex['choose_age'], reply_markup=keyboard_age)
        await state.set_state(FSM.fill_age_3km)
    elif callback.data == 'button_back':
        await callback.message.edit_text(text=lex['choose_type'], reply_markup=keyboard_type)
        await state.set_state(FSM.fill_group)

# Хэндлер на выбор упражнений на ловкость
@router.callback_query(StateFilter(FSM.fill_agility), Text(text=['button_jump3', 'button_brevno', 'button_mark']))
async def endurance_button_pressed(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'button_jump3':
        await callback.message.edit_text(text=f'{lex["input_jump3"]}')
        await state.set_state(FSM.fill_jump3)
    elif callback.data == 'button_brevno':
        await callback.message.edit_text(text=f'{lex["input_brevno"]}')
        await state.set_state(FSM.fill_brevno)
    elif callback.data == 'button_mark':
        await callback.message.edit_text(text=lex['input_mark'], reply_markup=keyboard_mark)
        await state.set_state(FSM.fill_mark)
    elif callback.data == 'button_back':
        await callback.message.edit_text(text=lex['choose_type'], reply_markup=keyboard_type)
        await state.set_state(FSM.fill_group)

# Хэндлер на выбор возраста на 1 км
@router.callback_query(StateFilter(FSM.fill_age_1km), Text(text=['button_before35', 'button_after35', 'button_back']))
async def age_button_pressed_1km(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'button_before35':
        await callback.message.edit_text(text=f'{lex["input_1km"]}')
        await state.set_state(FSM.fill_1km_before35)
    elif callback.data == 'button_after35':
        await callback.message.edit_text(text=f'{lex["input_1km"]}')
        await state.set_state(FSM.fill_1km_after35)
    elif callback.data == 'button_back':
        await callback.message.edit_text(text=lex['choose_type'], reply_markup=keyboard_endurance)
        await state.set_state(FSM.fill_endurance)

# Хэндлер на выбор возраста на 3 км
@router.callback_query(StateFilter(FSM.fill_age_3km), Text(text=['button_before35', 'button_after35', 'button_back']))
async def age_button_pressed_3km(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'button_before35':
        await callback.message.edit_text(text=f'{lex["input_3km"]}')
        await state.set_state(FSM.fill_3km_before35)
    elif callback.data == 'button_after35':
        await callback.message.edit_text(text=f'{lex["input_3km"]}')
        await state.set_state(FSM.fill_3km_after35)
    elif callback.data == 'button_back':
        await callback.message.edit_text(text=lex['choose_type'], reply_markup=keyboard_endurance)
        await state.set_state(FSM.fill_endurance)

# Хэндлер на кнопку назад из режима выбора упражнений
@router.callback_query(StateFilter(FSM.fill_speed, FSM.fill_strong, FSM.fill_endurance, FSM.fill_agility),
                       Text(text=['button_back']))
async def press_back(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=f'{lex["choose_type"]}', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)














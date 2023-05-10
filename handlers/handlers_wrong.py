from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message
from FSM import FSM
from lexicon import lex
from aiogram.fsm.context import FSMContext
from keyboards.keyboards import *

router: Router = Router()

# Хэндлер на неправильный воод формата результата
@router.message(StateFilter(FSM.fill_otzhim, FSM.fill_100m, FSM.fill_60m, FSM.fill_10x10, FSM.fill_swim100m, FSM.fill_podt,
                            FSM.fill_podem, FSM.fill_vihod, FSM.fill_1km_before35, FSM.fill_1km_after35,
                            FSM.fill_3km_before35, FSM.fill_3km_after35, FSM.fill_brevno, FSM.fill_jump3,
                            FSM.fill_shtanga_before70, FSM.fill_shtanga_after70, FSM.fill_swim500))
async def incorrect_input(message: Message):
    await message.answer(text=f'{lex["wrong_input"]}')

# Хэндлер на ненажатие кнопок в режиме нажатия кнопок
@router.message(StateFilter(FSM.fill_speed, FSM.fill_strong, FSM.fill_endurance, FSM.fill_agility, FSM.fill_VPN,
                            FSM.fill_group, FSM.fill_mode, FSM.fill_mark))
async def no_button_pressed(message: Message, state: FSMContext):
    current_state = await state.get_state()
    raw_state = current_state.split(':')[1]
    await message.answer(text=lex['button_only'])
    if raw_state == 'fill_speed':
        await message.answer(text=lex['choose_type'], reply_markup=keyboard_speed)
    elif raw_state == 'fill_strong':
        await message.answer(text=lex['choose_type'], reply_markup=keyboard_strong)
    elif raw_state == 'fill_endurance':
        await message.answer(text=lex['choose_type'], reply_markup=keyboard_endurance)
    elif raw_state == 'fill_agility':
        await message.answer(text=lex['choose_type'], reply_markup=keyboard_agility)
    elif raw_state == 'fill_group':
        await message.answer(text=lex['choose_type'], reply_markup=keyboard_type)
    elif raw_state == 'fill_mode':
        await message.answer(text=lex['choose_mode'], reply_markup=keyboard_mode)
    elif raw_state == 'fill_mark':
        await message.answer(text=lex['input_mark'], reply_markup=keyboard_mark)


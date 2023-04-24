from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards.keyboards import keyboard_type
from data.data_strong import *
from FSM import FSM
from lexicon import lex

router: Router = Router()

# Хэндлер на подтягивания
@router.message(StateFilter(FSM.fill_podt), lambda x: x.text.isdigit() and int(x.text) >= 0)
async def rezult_podt(message: Message, state: FSMContext):
    if float(message.text) > 30:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif float(message.text) < 6:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_podt[float(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)

# Хэндлер на выход силой
@router.message(StateFilter(FSM.fill_vihod), lambda x: x.text.isdigit() and int(x.text) >= 0)
async def rezult_vihod(message: Message, state: FSMContext):
    if float(message.text) > 14:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif float(message.text) < 1:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_vihod[float(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)

# Хэндлер на подъем переворотом
@router.message(StateFilter(FSM.fill_podem), lambda x: x.text.isdigit() and int(x.text) >= 0)
async def rezult_podem(message: Message, state: FSMContext):
    if float(message.text) > 31:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif float(message.text) < 1:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_podem[float(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)

# Хэндлер на отжимания
@router.message(StateFilter(FSM.fill_otzhim), lambda x: x.text.isdigit() and int(x.text) >= 0)
async def rezult_otzhim(message: Message, state: FSMContext):
    if float(message.text) > 99:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif float(message.text) < 13:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_otzhim[float(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)


from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards.keyboards import keyboard_endurance
from data.data_endurance import *
from FSM import FSM
from lexicon import lex
import re

router: Router = Router()
router.message.filter(lambda x: int(x.text.split('.')[1]) <= 59)

# Хэндлер на 1 км до 35 лет
@router.message(StateFilter(FSM.fill_1km_before35), lambda x: re.fullmatch(r'\d[.]\d{2}', x.text))
async def rezult_1km_before35(message: Message, state: FSMContext):
    if float(message.text) <= 2.55:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif float(message.text) > 5.55:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_1km_before35[float(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text=f'{lex["choose_exersize"]}', reply_markup=keyboard_endurance)
    await state.set_state(FSM.fill_endurance)

# Хэндлер на 1 км после 35 лет
@router.message(StateFilter(FSM.fill_1km_after35), lambda x: re.fullmatch(r'\d[.]\d{2}', x.text))
async def rezult_1km_after35(message: Message, state: FSMContext):
    if float(message.text) <= 3.10:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif float(message.text) > 6.00:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_1km_after35[float(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text=f'{lex["choose_exersize"]}', reply_markup=keyboard_endurance)
    await state.set_state(FSM.fill_endurance)

# Хэндлер на 3 км до 35 лет
@router.message(StateFilter(FSM.fill_3km_before35), lambda x: re.fullmatch(r'\d{1,2}[.]\d{2}', x.text))
async def rezult_3km_before35(message: Message, state: FSMContext):
    if float(message.text) <= 10.30:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif float(message.text) > 16.24:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_3km_before35[float(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text=f'{lex["choose_exersize"]}', reply_markup=keyboard_endurance)
    await state.set_state(FSM.fill_endurance)

# Хэндлер на 3 км после 35 лет
@router.message(StateFilter(FSM.fill_3km_after35), lambda x: re.fullmatch(r'\d{1,2}[.]\d{2}', x.text))
async def rezult_3km_after35(message: Message, state: FSMContext):
    if float(message.text) <= 12.00:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif float(message.text) > 19.50:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_3km_after35[float(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text=f'{lex["choose_exersize"]}', reply_markup=keyboard_endurance)
    await state.set_state(FSM.fill_endurance)

# Хэндлер на плавание 500 м
@router.message(StateFilter(FSM.fill_swim500), lambda x: re.fullmatch(r'\d{1,2}[.]\d{2}', x.text))
async def rezult_swim500(message: Message, state: FSMContext):
    if float(message.text) <= 9.00:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif float(message.text) > 16.50:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_swim500[float(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text=f'{lex["choose_exersize"]}', reply_markup=keyboard_endurance)
    await state.set_state(FSM.fill_endurance)
from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards.keyboards import keyboard_type
from data.data_speed import *
from FSM import FSM
import re
from lexicon import lex

router: Router = Router()

# Хэндлер на 100 метров
@router.message(StateFilter(FSM.fill_100m), lambda x: re.fullmatch(r'\d{1,2}[.]\d', x.text))
async def rezult_100m(message: Message, state: FSMContext):
    if float(message.text) > 18.9:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    elif float(message.text) < 11.9:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_100m[float(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)

# Хэндлер на 60 метров
@router.message(StateFilter(FSM.fill_60m), lambda x: re.fullmatch(r'\d{1,2}[.]\d', x.text))
async def rezult_60m(message: Message, state: FSMContext):
    if float(message.text) > 11.0:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    elif float(message.text) <= 7.4:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_60m[float(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)

# Хэндлер на 10 по 10 метров
@router.message(StateFilter(FSM.fill_10x10), lambda x: re.fullmatch(r'\d{2}[.]\d', x.text))
async def rezult_10x10(message: Message, state: FSMContext):
    if float(message.text) > 34.4:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    elif float(message.text) <= 24.1:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_10x10[float(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)

# Хэндлер на плавание 100 метров
@router.message(StateFilter(FSM.fill_swim100m),
                lambda x: re.fullmatch(r'\d[.]\d{2}', x.text) and int(x.text.split('.')[1]) <= 59)
async def rezult_swim100m(message: Message, state: FSMContext):
    if float(message.text) > 3.04:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    elif float(message.text) <= 1.01:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_swim100m[float(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)


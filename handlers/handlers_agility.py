from aiogram import Router
from aiogram.filters import StateFilter, Text
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.keyboards import keyboard_type, keyboard_agility
from data.data_agility import *
from FSM import FSM
from lexicon import lex
import re

router: Router = Router()

# Хэндлер на тройной прыжок
@router.message(StateFilter(FSM.fill_jump3), lambda x: re.fullmatch(r'\d{3}', x.text))
async def rezult_jump3(message: Message, state: FSMContext):
    if int(message.text) >= 850:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif int(message.text) < 442:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_jump3[int(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)

# Хэндлер на перемещение по бревну
@router.message(StateFilter(FSM.fill_brevno), lambda x: re.fullmatch(r'\d{1,2}[.]\d', x.text))
async def rezult_brevno(message: Message, state: FSMContext):
    if float(message.text) <= 9.0:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif float(message.text) > 18.4:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_brevno[float(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)

# Хэндлер на оценку
@router.callback_query(StateFilter(FSM.fill_mark), Text(text=['mark_2', 'mark_3', 'mark_4', 'mark_5', 'button_back']))
async def button2_pressed(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'mark_2':
        await callback.message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
        await callback.message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
        await state.set_state(FSM.fill_group)
    elif callback.data == 'mark_3':
        await callback.message.answer(text=f'{lex["rez"]}*{d_mark[3]}*', parse_mode='MarkdownV2')
        await callback.message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
        await state.set_state(FSM.fill_group)
    elif callback.data == 'mark_4':
        await callback.message.answer(text=f'{lex["rez"]}*{d_mark[4]}*', parse_mode='MarkdownV2')
        await callback.message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
        await state.set_state(FSM.fill_group)
    elif callback.data == 'mark_5':
        await callback.message.answer(text=f'{lex["rez"]}*{d_mark[5]}*', parse_mode='MarkdownV2')
        await callback.message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
        await state.set_state(FSM.fill_group)
    elif callback.data == 'button_back':
        await callback.message.edit_text(text=lex['choose_type'], reply_markup=keyboard_agility)
        await state.set_state(FSM.fill_agility)

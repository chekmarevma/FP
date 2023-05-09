from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards.keyboards import keyboard_type
from data.data_strong import *
from FSM import FSM
from lexicon import lex

router: Router = Router()
router.message.filter(lambda x: x.text.isdigit() and int(x.text) >= 0)

# Хэндлер на подтягивания
@router.message(StateFilter(FSM.fill_podt))
async def rezult_podt(message: Message, state: FSMContext):
    if int(message.text) > 30:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif int(message.text) < 6:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_podt[int(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)

# Хэндлер на выход силой
@router.message(StateFilter(FSM.fill_vihod))
async def rezult_vihod(message: Message, state: FSMContext):
    if int(message.text) > 14:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif int(message.text) < 1:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_vihod[int(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)

# Хэндлер на подъем переворотом
@router.message(StateFilter(FSM.fill_podem))
async def rezult_podem(message: Message, state: FSMContext):
    if int(message.text) > 31:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif int(message.text) < 1:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_podem[int(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)

# Хэндлер на отжимания
@router.message(StateFilter(FSM.fill_otzhim))
async def rezult_otzhim(message: Message, state: FSMContext):
    if int(message.text) >= 100:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif int(message.text) < 13:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_otzhim[int(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)

# Хэндлер на штангу до 70 кг
@router.message(StateFilter(FSM.fill_shtanga_before70))
async def rezult_otzhim(message: Message, state: FSMContext):
    if int(message.text) >= 21:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif int(message.text) < 1:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_shtanga_before70[int(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)

# Хэндлер на штангу после 70 кг
@router.message(StateFilter(FSM.fill_shtanga_after70))
async def rezult_otzhim(message: Message, state: FSMContext):
    if int(message.text) >= 29:
        await message.answer(text=f'{lex["rez"]}\n{lex["100_balls"]}')
    elif int(message.text) < 1:
        await message.answer(text=f'{lex["rez"]}\n{lex["0_balls"]}')
    else:
        await message.answer(text=f'{lex["rez"]}*{d_shtanga_after70[int(message.text)]}*', parse_mode='MarkdownV2')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)


from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message
from FSM import FSM
from lexicon import lex
from aiogram.fsm.context import FSMContext
from keyboards.keyboards import *

router: Router = Router()

@router.message(StateFilter(FSM.fill_otzhim, FSM.fill_100m, FSM.fill_60m, FSM.fill_10x10, FSM.fill_swim100m, FSM.fill_podt,
                            FSM.fill_podem, FSM.fill_vihod, FSM.fill_1km_before35, FSM.fill_1km_after35,
                            FSM.fill_3km_before35, FSM.fill_3km_after35))
async def incorrect_input(message: Message):
    await message.answer(text=f'{lex["wrong_input"]}')

# Хэндлер на любое другое сообщение кроме нажатия кнопки выбора упражнения
@router.message(StateFilter(FSM.fill_type, FSM.fill_age_1km, FSM.fill_age_3km))
async def no_group_button_pressed(message: Message, state: FSMContext):
    await message.answer(text='Пользуйтесь кнопками при выборе упражнения')
    await message.answer(text='Выберите вид упражнения', reply_markup=keyboard_type)
    await state.set_state(FSM.fill_group)





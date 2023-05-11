from aiogram.filters.state import State, StatesGroup

# Класс состояний
class FSM(StatesGroup):
    fill_mode = State()              # Выбор режима
    fill_group = State()             # Выбор типа упражнения
    fill_speed = State()             # Выбор упражнения на скорость
    fill_strong = State()            # Выбор упражнения на силу
    fill_endurance = State()         # Выбор упражнения на выносливость
    fill_agility = State()           # Выбор упражнений на ловкость
    fill_VPN = State()               # Выбор военно-прикладных упражнений
    fill_100m = State()              # 100 м
    fill_60m = State()               # 60 м
    fill_10x10 = State()             # Челночный бег
    fill_swim100m = State()          # Плавание 100м
    fill_podt = State()              # Подтягивания
    fill_vihod = State()             # Выход силой
    fill_podem = State()             # Подъем переворотом
    fill_otzhim = State()            # Отжимания
    fill_shtanga_before70 = State()  # Штанга до 70 кг
    fill_shtanga_after70 = State()   # Штанга свыше 70 кг
    fill_1km_before35 = State()      # 1 км до 35 лет
    fill_1km_after35 = State()       # 1 км после 35 лет
    fill_3km_before35 = State()      # 3 км до 35 лет
    fill_3km_after35 = State()       # 3 км после 35 лет
    fill_jump3 = State()             # Тройной прыжок
    fill_brevno = State()            # Перемещение по бревну
    fill_mark = State()              # Оценка за упражнение
    fill_swim500 = State()           # Плавание 500 м
    fill_feedback = State()

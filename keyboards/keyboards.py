from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Клавиатура для выбора типов упражнений
speed_button: InlineKeyboardButton = InlineKeyboardButton(
    text='Скорость ⏱', callback_data='speed_button')
strong_button: InlineKeyboardButton = InlineKeyboardButton(
    text='Сила 💪', callback_data='strong_button')
endurance_button: InlineKeyboardButton = InlineKeyboardButton(
    text='Выносливость 🏃 🏃‍', callback_data='endurance-button')
keyboard_type: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[speed_button], [strong_button], [endurance_button]])

# Клавиатура для выбора упражнений на скорость
button_100m: InlineKeyboardButton = InlineKeyboardButton(
    text='100 метров', callback_data='button_100m')
button_60m: InlineKeyboardButton = InlineKeyboardButton(
    text='60 метров', callback_data='button_60m')
button_10x10: InlineKeyboardButton = InlineKeyboardButton(
    text='Челночный бег‍', callback_data='button_10x10')
button_swim100m: InlineKeyboardButton = InlineKeyboardButton(
    text='Плавание 100 метров', callback_data='button_swim100m')
button_back: InlineKeyboardButton = InlineKeyboardButton(
    text='Назад', callback_data='button_back')
keyboard_speed: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_100m], [button_60m], [button_10x10], [button_swim100m], [button_back]])

# Клавиатура для выбора упражнений на силу
button_podt: InlineKeyboardButton = InlineKeyboardButton(
    text='Подтягивание на перекладине', callback_data='button_podt')
button_vihod: InlineKeyboardButton = InlineKeyboardButton(
    text='Подъем силой на перекладине', callback_data='button_vihod')
button_podem: InlineKeyboardButton = InlineKeyboardButton(
    text='Подъем переворотом на перекладине', callback_data='button_podem')
# button_giri: InlineKeyboardButton = InlineKeyboardButton(
#     text='Гири', callback_data='button_giri')
# button_shtanga: InlineKeyboardButton = InlineKeyboardButton(
#     text='Штанга', callback_data='button_shtanga')
button_otzhim: InlineKeyboardButton = InlineKeyboardButton(
    text='Сгибания и разгибания рук в упоре лежа', callback_data='button_otzhim')
button_back: InlineKeyboardButton = InlineKeyboardButton(
    text='Назад', callback_data='button_back')
keyboard_strong: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_podt], [button_vihod], [button_podem], [button_otzhim], [button_back]])

# Клавиатура для выбора упражнений на выносливость
button_1km: InlineKeyboardButton = InlineKeyboardButton(
    text='Бег 1 км', callback_data='button_1km')
button_3km: InlineKeyboardButton = InlineKeyboardButton(
    text='Бег 3 км', callback_data='button_3km')
# button_500m_swim: InlineKeyboardButton = InlineKeyboardButton(
#     text='Плавание 500 метров', callback_data='button_500m_swim')
button_back: InlineKeyboardButton = InlineKeyboardButton(
    text='Назад', callback_data='button_back')
keyboard_endurance: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_1km], [button_3km], [button_back]]) # [button_500m_swim]

# Клавиатура для выбора возрастной группы
button_before35: InlineKeyboardButton = InlineKeyboardButton(
    text='До 35 лет', callback_data='button_before35')
button_after35: InlineKeyboardButton = InlineKeyboardButton(
    text='После 35 лет', callback_data='button_after35')
button_back: InlineKeyboardButton = InlineKeyboardButton(
    text='Назад', callback_data='button_back')
keyboard_age: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_before35], [button_after35], [button_back]])

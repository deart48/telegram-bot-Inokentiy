
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


kb = ReplyKeyboardMarkup(keyboard =[ 
        [KeyboardButton(text = 'Расписание'), KeyboardButton(text = 'Замены')],
        [KeyboardButton(text = 'Мероприятия'), KeyboardButton(text = 'Заявка на питание, Посещаемость')] 
    ],
                             resize_keyboard=True, 
                             input_field_placeholder=" Выберите пункт" 
                             )

ref = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Открыть ссылку', url = 'https://disk.yandex.ru/d/gCqmY1cM4AIhNA')]
])
ref2 = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Открыть ссылку', url = 'https://disk.yandex.ru/d/mVe-IcIoqaVbhg')]
])
ref3 = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Открыть ссылку', url = 'https://disk.yandex.ru/d/gCqmY1cM4AIhNA')]
])
ref4 = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Открыть ссылку', url = 'https://disk.yandex.ru/d/gCqmY1cM4AIhNA')]
])
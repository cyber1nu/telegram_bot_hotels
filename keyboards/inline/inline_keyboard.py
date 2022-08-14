from typing import Any, Dict
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time


def inline_button(text: str, callback_data: Any) -> InlineKeyboardButton:
    # макет создания кнопки
    the_button = InlineKeyboardButton(text=text, callback_data=callback_data)

    return the_button


def inline_button_2(text: str, url: str) -> InlineKeyboardButton:
    # макет создания кнопки
    the_button = InlineKeyboardButton(text=text, url=url)

    return the_button


def cancel_button() -> InlineKeyboardButton:
    cncl_btn = InlineKeyboardButton(text='Выйти из режима поиска', callback_data='/cancel')

    return cncl_btn


def cities_keyboard(cities_dict: Dict) -> InlineKeyboardMarkup:
    # макет создания клавиатуры на основании макета создания кнопки
    kb = InlineKeyboardMarkup(row_width=1)
    for i_id, i_name in cities_dict.items():
        kb.insert(button=inline_button(text=i_name, callback_data=i_id))
    kb.add(cancel_button())
    return kb


def year_calendar_keyboard() -> InlineKeyboardMarkup:
    # клавиатура выбора года
    kb = InlineKeyboardMarkup(row_width=3)
    cur_year = time.strftime('%Y-%m-%d').split('-')
    for i_year in range(int(cur_year[0]), int(cur_year[0]) + 3):
        kb.insert(inline_button(f'{i_year}', callback_data=f'{str(i_year)}'))

    kb.add(cancel_button())
    return kb


def month_calendar_keyboard(cur_year: int) -> InlineKeyboardMarkup:
    # клавиатура выбора месяца
    months = {
        'Январь': '01', 'Февраль': '02', 'Март': '03', 'Апрель': '04',
        'Май': '05', 'Июнь': '06', 'Июль': '07', 'Август': '08',
        'Сентябрь': '09', 'Октябрь': '10', 'Ноябрь': '11', 'Декабрь': '12',
        }
    kb = InlineKeyboardMarkup(row_width=4)
    if cur_year > int(time.strftime('%Y-%m-%d').split('-')[0]):
        for i_month, i_value in months.items():
            kb.insert(inline_button(f'{i_month}', callback_data=f'{i_value}'))
    else:
        for i_month, i_value in months.items():
            if int(i_value) >= int(time.strftime('%Y-%m-%d').split('-')[1]):
                kb.insert(inline_button(f'{i_month}', callback_data=f'{i_value}'))
    kb.add(cancel_button())
    return kb


def day_calendar_keyboard(month: str, year: str) -> InlineKeyboardMarkup:
    # клавиатура выбора дня
    months_31 = ['01', '03', '05', '07', '08', '10', '12']
    months_30 = ['04', '06', '09', '11']

    kb = InlineKeyboardMarkup(row_width=7)
    if month in months_31:
        for i_day in range(1, 32):
            if i_day < 10:
                day = f'0{i_day}'
            else:
                day = i_day
            kb.insert(inline_button(f'{i_day}', callback_data=f'{day}'))
    elif month in months_30:
        for i_day in range(1, 31):
            if i_day < 10:
                day = f'0{i_day}'
            else:
                day = i_day
            kb.insert(inline_button(f'{i_day}', callback_data=f'{day}'))
    elif month == '02' and (int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0):
        for i_day in range(1, 30):
            if i_day < 10:
                day = f'0{i_day}'
            else:
                day = i_day
            kb.insert(inline_button(f'{i_day}', callback_data=f'{day}'))
    elif month == '02':
        for i_day in range(1, 29):
            if i_day < 10:
                day = f'0{i_day}'
            else:
                day = i_day
            kb.insert(inline_button(f'{i_day}', callback_data=f'{day}'))

    kb.add(cancel_button())
    return kb


def yes_or_no_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(inline_button(text='Да', callback_data='photo_yes'), inline_button(text='Нет', callback_data='photo_no'))

    return kb


def set_photo_quantity_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=5)
    for i_num in range(1, 11):
        kb.insert(inline_button(str(i_num), callback_data=f'{i_num}'))
    kb.add(cancel_button())

    return kb


def hotel_url(name: str, url: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(inline_button_2(text=name, url=url))
    kb.add(inline_button(text='OK', callback_data='OK'))
    kb.insert(inline_button(text='DELETE', callback_data='delete'))

    return kb


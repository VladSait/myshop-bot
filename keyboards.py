from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Главное меню (нижние кнопки)
def main_menu():
    kb = [
        [KeyboardButton(text="🛒 Купить UC"), KeyboardButton(text="⭐ Купить Stars")],
        [KeyboardButton(text="💰 Пополнить баланс"), KeyboardButton(text="🛍️ Корзина")],
        [KeyboardButton(text="📞 Поддержка")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# Кнопки выбора количества UC
def uc_quantity_keyboard():
    builder = InlineKeyboardBuilder()
    from config import UC_PRICES
    for amount in UC_PRICES.keys():
        builder.button(text=f"{amount} UC", callback_data=f"uc_{amount}")
    builder.button(text="🔙 Назад", callback_data="back_to_main")
    builder.adjust(2)
    return builder.as_markup()

# Кнопки выбора количества Stars
def stars_quantity_keyboard():
    builder = InlineKeyboardBuilder()
    from config import STARS_PRICES
    for amount in STARS_PRICES.keys():
        builder.button(text=f"{amount} ⭐", callback_data=f"stars_{amount}")
    builder.button(text="🔙 Назад", callback_data="back_to_main")
    builder.adjust(2)
    return builder.as_markup()

# Кнопки для товара
def item_actions_keyboard(item_id: str, item_type: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="➕ В корзину", callback_data=f"add_{item_type}_{item_id}")
    builder.button(text="💰 Купить сейчас", callback_data=f"buy_{item_type}_{item_id}")
    builder.button(text="🔙 Назад", callback_data=f"back_to_{item_type}")
    builder.adjust(1)
    return builder.as_markup()
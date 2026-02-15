import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN, ADMIN_IDS, UC_PRICES, STARS_PRICES
from keyboards import main_menu, uc_quantity_keyboard, stars_quantity_keyboard, item_actions_keyboard

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Создаем бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Команда /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        f"🔥 Здесь можно купить UC для PUBG и Telegram Stars\n"
        f"👇 Выбери что нужно:",
        reply_markup=main_menu()
    )

# Кнопка "Купить UC"
@dp.message(lambda message: message.text == "🛒 Купить UC")
async def buy_uc(message: Message):
    text = "🔫 *Выбери количество UC:*\n\n"
    for amount, price in UC_PRICES.items():
        text += f"{amount} UC — {price}₽\n"
    
    await message.answer(
        text,
        reply_markup=uc_quantity_keyboard(),
        parse_mode="Markdown"
    )

# Кнопка "Купить Stars"
@dp.message(lambda message: message.text == "⭐ Купить Stars")
async def buy_stars(message: Message):
    text = "✨ *Выбери количество Telegram Stars:*\n\n"
    for amount, price in STARS_PRICES.items():
        text += f"{amount} ⭐ — {price}₽\n"
    
    await message.answer(
        text,
        reply_markup=stars_quantity_keyboard(),
        parse_mode="Markdown"
    )

# Кнопка "Поддержка"
@dp.message(lambda message: message.text == "📞 Поддержка")
async def support(message: Message):
    await message.answer(
        "📞 *Служба поддержки*\n\n"
        "По всем вопросам пиши: @your_support\n"
        "Время ответа: 5-10 минут",
        parse_mode="Markdown"
    )

# Обработка выбора UC
@dp.callback_query(lambda c: c.data.startswith("uc_"))
async def process_uc(callback: CallbackQuery):
    amount = callback.data.split("_")[1]
    price = UC_PRICES[int(amount)]
    
    await callback.message.edit_text(
        f"🔫 *{amount} UC*\n\n"
        f"💰 Цена: {price}₽\n\n"
        f"Выбери действие:",
        reply_markup=item_actions_keyboard(amount, "uc"),
        parse_mode="Markdown"
    )

# Обработка выбора Stars
@dp.callback_query(lambda c: c.data.startswith("stars_"))
async def process_stars(callback: CallbackQuery):
    amount = callback.data.split("_")[1]
    price = STARS_PRICES[int(amount)]
    
    await callback.message.edit_text(
        f"✨ *{amount} Telegram Stars*\n\n"
        f"💰 Цена: {price}₽\n\n"
        f"Выбери действие:",
        reply_markup=item_actions_keyboard(amount, "stars"),
        parse_mode="Markdown"
    )

# Запуск бота
async def main():
    print("🤖 Бот запущен на телефоне!")
    print("👑 Админ ID:", ADMIN_IDS[0])
    print("📱 Termux можно свернуть, но НЕ ЗАКРЫВАЙ!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
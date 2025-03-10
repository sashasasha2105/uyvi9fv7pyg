# handlers.py
import user_data
from steps import steps
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Я чат-бот по сборке вашего персонального компьютера. У вас есть все необходимые компоненты для сборки ПК? "
        "Пожалуйста, проверьте наличие следующих компонентов:\n"
        "- Материнская плата\n"
        "- Процессор\n"
        "- Охлаждение процессора\n"
        "- Оперативная память\n"
        "- Накопитель\n"
        "- Блок питания\n"
        "- Корпус\n"
        "- Видеокарта (если у процессора нет встроенного видеоядра)\n"
        "- Небольшой набор отверток\n"
        "- Термопаста\n"
        "Выберите вариант:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Я готов", callback_data='ready')],
            [InlineKeyboardButton("Еще нужно подготовиться", callback_data='not_ready')]
        ])
    )

async def handle_preparation_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'ready':
        await query.edit_message_text("*Шаг 1:\n"
    "*Разложите комплектующие на ровной, просторной и непроводящей поверхности. Убедитесь, что у вас есть достаточно места для работы и все инструменты под рукой. Расположите комплектующие так, чтобы они были легко доступны:\n"
    "* Корпус: Положите егiygy9vpvy[vyvypvyvvyо на бок, открыв доступ к материнской плате.\n"
    "* Материнская плата: Можно положить ее на антистатический пакет рядом с корпусом.\n"
    "* Процессор, кулер и оперативная память: Держите их рядом с материнской платой для удобства установки.\n"
    "* Видеокарта, SSD/HDD: Пока отложите в сторону, они устанавливаются позже.\n"
    "* Блок питания: Также можно отложить, его устанавливают после материнской платы..)\n")
        await query.message.reply_text("Нажмите 'Следующий шаг', чтобы продолжить.",
                                       reply_markup=InlineKeyboardMarkup([
                                           [InlineKeyboardButton("Следующий шаг", callback_data='next_step')]
                                       ]))

# Добавьте остальные обработчики здесь...rgrgr
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

register_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Register",
            callback_data='register'
            )]
        ]
    )

main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="User",
            callback_data='user_role'
            )],
        [InlineKeyboardButton(
            text="Admin",
            callback_data='admin_role',
            style='success'
            )],
        [InlineKeyboardButton(
            text="Developer",
            callback_data='dev_role',
            style='primary'
            )]
        ]
    )

back_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text = "Back",
            callback_data='back_from_help'
            )]
        ]
    )
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

list_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Get list",
            callback_data='dList'
            )]
        ]
    )

delete_user_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Delete User",
            callback_data='dUser',
            style='danger'
            )]
        ]
    )

reject_del = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Reject",
            callback_data='dDel'
            )]
        ]
    )

back_to_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Back",
            callback_data='dBack'
            )]
        ]
    )
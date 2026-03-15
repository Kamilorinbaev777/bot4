from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

dev_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Get list",
            callback_data='dList'
            )],
        [InlineKeyboardButton(
            text="Broadcast",
            callback_data='dBroadcast'
            )]
        ]
    )

""" for list buttons """
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
""" end """

""" for broadcast buttons """
broadcast_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Broadcast Text",
            callback_data='dBcast_text',
            style="primary"
            )],
        [InlineKeyboardButton(
            text="Broadcast Image",
            callback_data='dBcast_img',
            style="primary"
            )],
        [InlineKeyboardButton(
            text="Broadcast Document",
            callback_data='dBcast_doc',
            style="primary"
            )]
        ]
    )
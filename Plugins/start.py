from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from config import ADMINS



# Start Message
@Client.on_message(filters.user(ADMINS) & filters.command("channel") & ~filters.channel)
async def start(bot, msg):
	user = await bot.get_me()
	mention = user["mention"]
	await bot.send_message(
		msg.chat.id,
		"Silahkan plih opsi mana yang ingin anda lakukan, silahkan tekan Tombol keyboard yang ada".format(msg.from_user.mention, mention),
                reply_markup=ReplyKeyboardMarkup(
			[
				['+ Add Channels +'],
				['Manage Channels'],
			],
			one_time_keyboard=True,
			resize_keyboard=True
		)
	)

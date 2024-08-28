import logging
from telegram import Bot, InputMediaPhoto, Poll
from telegram.ext import Application, CommandHandler, CallbackContext
import schedule
from decouple import config
import time
import helpers.worker as w

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


TOKEN = config('TELEGRAM_API')
CHANNEL_ID = '@char_bt'

async def send_message_poll(context):
    bot = context.bot

    #Step 1
    image_path = 'post/answer/pic_2.png'
    
    with open(image_path, 'rb') as image:
        await bot.send_photo(chat_id=CHANNEL_ID, photo=image, caption="Visit CharBT https://charbt.com - Historical Data Trading Simulator\n[Answer]")
    
    #Step 2
    await w.create_next_poll_pic()

    #Step 3
    image_path = 'post/question/pic_1.png'
    
    with open(image_path, 'rb') as image:
        await bot.send_photo(chat_id=CHANNEL_ID, photo=image, caption="Vote and visit CharBT https://charbt.com - Historical Data Trading Simulator\n[Question]")
    
    question = "Where will the price go?"
    options = ["Up", "Flat", "Down"]
    await bot.send_poll(chat_id=CHANNEL_ID, question=question, options=options, is_anonymous=True, allows_multiple_answers=False)


def main():
    application = Application.builder().token(TOKEN).build()
    
    job_queue = application.job_queue
    job_queue.run_repeating(send_message_poll, interval=86400, first=0)
    
    application.run_polling()

if __name__ == '__main__':
    main()

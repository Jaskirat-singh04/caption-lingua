import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from youtube_transcript_api import YouTubeTranscriptApi

# Replace 5713513900:AAE8T2-6M55Q2f_cFP3Cn77jsgxJQoiyxEg with your actual bot token
bot = telegram.Bot(token='5713513900:AAE8T2-6M55Q2f_cFP3Cn77jsgxJQoiyxxx')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm a YouTube transcript bot. Send me a YouTube video URL and the language you want the transcript in. For example: /transcript https://www.youtube.com/watch?v=dQw4w9WgXcQ en")

def get_transcript(update, context):
    try:
        args = context.args
        video_id = args[0]
        language_name = args[1]
        # language_code = Languages.get_language_code(language_name)
        transcript = YouTubeTranscriptApi.get_transcript(video_id,languages=[language_name])
        text = '\n'.join([line['text'] for line in transcript])
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, there was an error. Please check your input and try again.")

updater = Updater(token='5713513900:AAE8T2-6M55Q2f_cFP3Cn77jsgxJQoiyxEg', use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
transcript_handler = CommandHandler('transcript', get_transcript)
dispatcher.add_handler(transcript_handler)
updater.start_polling()

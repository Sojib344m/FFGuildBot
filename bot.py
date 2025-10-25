import os
from telegram.ext import Updater, CommandHandler

# এটি আপনার BotFather টোকেন Render থেকে নেবে
BOT_TOKEN = os.environ.get('BOT_TOKEN')

def start(update, context):
    update.message.reply_text('স্বাগতম! আমি আপনার গিল্ড বুস্টার বট। /ff_group 5 লিখে চেষ্টা করুন।')

def ff_group(update, context):
    # /ff_group <সংখ্যা> কমান্ডটি হ্যান্ডেল করা
    if not context.args:
        update.message.reply_text("ব্যবহার: /ff_group <সংখ্যা>। যেমন: /ff_group 5")
        return

    try:
        group_size = context.args[0]
        
        # এখানে অস্থায়ী গ্রুপ তৈরির লজিক দেখানোর জন্য একটি মেসেজ দেওয়া হচ্ছে 
        message = f"✅ প্রস্তুত! {group_size} জনের জন্য লাইক বুস্ট শুরু হলো। আপনার গিল্ড মেম্বারদের লাইক দিতে বলুন।"
        update.message.reply_text(message)
        
    except Exception as e:
        update.message.reply_text(f"ক্ষমা করবেন, কোনো ত্রুটি হয়েছে।")


def main():
    # এখানে পরিবর্তন করা হয়েছে
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    # কমান্ড যুক্ত করা
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ff_group", ff_group))

    # বট চালানো
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

import re
from datetime import datetime
from mmpy_bot.bot import respond_to
from mmpy_bot.scheduler import schedule

@respond_to('remind me \"(.*)\" at (.*)', re.IGNORECASE)
def reply_specific_time(message, content, trigger_time):
    try:
        t_time = datetime.strptime(trigger_time, '%b-%d-%Y_%H:%M:%S')
        message.reply("I will remind you: " + content + " at " + trigger_time)
        schedule.once(t_time).do(message.reply, content)
    except:
        message.reply("Wrong time format:\n right example: Feb-02-2020_23:59:59")
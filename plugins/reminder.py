import re
from datetime import datetime
from mmpy_bot.bot import respond_to, listen_to
from mmpy_bot.scheduler import schedule
import json
import logging
import time


@respond_to('remind me \"(.*)\" at (.*)', re.IGNORECASE)
def reply_specific_time(message, content, trigger_time):
    try:
        t_time = datetime.strptime(trigger_time, '%b-%d-%Y_%H:%M:%S')
        message.reply("I will remind you: " + content + " at " + trigger_time)
        schedule.once(t_time).do(message.reply, content)
    except:
        message.reply(
            "Wrong time format:\n right example: Feb-02-2020_23:59:59")


@respond_to('remind \"(.*)\" \"(.*)\" at \"(.*)\" every \"(.*)\"', re.IGNORECASE)
def create_reminder(message, people, content, trigger_time, freq):
    for user in list(people.split()):
        if int(freq) <= 0:
            t_time = datetime.strptime(trigger_time, '%b-%d-%Y_%H:%M:%S')
            schedule.once(t_time).do(
                message.send, "Hey, %s! It's time to do some work:\n %s" % (user, content))
        else:
            schedule.every(int(freq)).seconds.do(
                message.send, "Hey, %s! It's time to do some work again:\n %s" % (user, content))

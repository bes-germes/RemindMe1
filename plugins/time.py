from mmpy_bot.bot import respond_to, listen_to
import time

@respond_to('time')
@listen_to('time')
def help_request(message):
    localtime = time.asctime( time.localtime(time.time()) )
    message.send("Local current time :    "+ localtime)

import pytz
from flask import Flask
from mysql.connector import errorcode
from twitchio.ext import commands
from twitchio.ext.commands.errors import CommandNotFound
import mysql.connector
import datetime

app = Flask(__name__)

IST = pytz.timezone('America/Sao_Paulo')

@app.route("/")
def hello_world():
    return ""

try:
    cnx = mysql.connector.connect(user='felipearruda', password='felipejf34',
                                  host='mysql-twitch.cf7idmglqggw.sa-east-1.rds.amazonaws.com',
                                  database='twitch')
    print("Conectado")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

def pushEventMessage(data_event_message):
    add_event_message = ("INSERT INTO twitch.event_message "
                         "(user, channel, message, date, created_at) "
                         "VALUES (%s, %s, %s, %s, %s)")
    # user = usuario que mandou a msg,
    # channel = canal em que foi mandado a msg,
    # message = mensagem,
    # date = data/hora do servidor da twitch,
    # created_at = data/hora da insercao no BD

    cursor = cnx.cursor()
    cursor.execute(add_event_message, data_event_message)
    cnx.commit()
    cursor.close()



class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        # super().__init__(token='67qpusn45w05rniu5t5gj83c0a1p9d', prefix='?',
        #                  initial_channels=['gaules', 'yoda', 'summit1g', 'casimito', 'mch_agg', 'ale_apoka',
        #                                    'hasanabi', 'mizkif', 'elspreen', 'rubius', 'kamet0', 'xqcow'])
        # super().__init__(token='67qpusn45w05rniu5t5gj83c0a1p9d', prefix='?', initial_channels=['sudo4root'])
        super().__init__(token='67qpusn45w05rniu5t5gj83c0a1p9d', prefix='?',
                         initial_channels=['gaules', 'casimito', 'mch_agg', 'ale_apoka', 'gafallen', 'bt0tv', 'fnxlntc', 'vinicsgo'])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message, initial_channels=None):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        # print(message.channel.name + " - " +message.author.name + " - " + message.content + " - " + message.timestamp.strftime("%Y-%m-%d %H:%M:%S"), datetime.datetime.now(IST))


        data_event_message = (message.author.name, message.channel.name, message.content,
                              message.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                              datetime.datetime.now(IST))
        pushEventMessage(data_event_message)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        if not CommandNotFound:
            await self.handle_commands(message)



if __name__ == "__main__":
    bot = Bot().run()

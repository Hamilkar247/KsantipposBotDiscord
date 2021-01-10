import logging
import argparse
import os
import random
import discord
from dotenv import load_dotenv

def def_params():
    parser = argparse.ArgumentParser(
            description="Description to fill"
    )
    parser.add_argument("-l", "--loghami", action='store_true', help="set debug")
    args = parser.parse_args()
    if args.loghami:
        logging.basicConfig(level=logging.DEBUG)
        print("args:" + str(args))
    return args

class KsantipposBot:

    def __init__(self):
        super().__init__()
        self.TOKEN = None
        self.GUILD = None
        self.dotenvConfig()
        self.clientDiscord()

    def dotenvConfig(self):
        load_dotenv()
        self.TOKEN = os.getenv('DISCORD_TOKEN')
        self.GUILD = os.getenv('DISCORD_GUILD')

    def clientDiscord(self):
        client = discord.Client()

        self.readDiscordGuildMember(client)
        self.newMemberMessage(client)
        self.messageToAnswerUser(client)

        client.run(self.TOKEN)

    def readDiscordGuildMember(self, client):

        @client.event
        async def on_ready():

            #guild = discord.utils.find(lambda g: g.name == self.GUILD, client.guilds)
            guild = discord.utils.get(client.guilds, name=self.GUILD)

            print(
                f'{client.user} is connected to to the following guild:\n'
                f'{guild.name}(id: {guild.id})'
            )

            members = '\n - '.join([member.name for member in guild.members])
            print(f'Guild Members:\n - {members}')

    def newMemberMessage(self, client):

        @client.event
        async def on_member_join(member):
            await member.create_dm()
            await member.dm_channel.send(
                f'Hi {member.name}, welcome to my Discord server!'
            )

    def messageToAnswerUser(self, client):

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return

            brooklyn_99_quotes = [
               'I\'m the human form of the 💯 emoji.',
               'Bingpot!',
               (
                   '''
                   I am young, I am twenty years old; yet I know nothing of life but despair, death, fear,
                   and fatuous superficiality cast over an abyss of sorrow. I see how peoples are set against
                   one another, and in silence, unknowingly, foolishly, obediently, innocently slay one another.
                   ― Erich Maria Remarque, All Quiet on the Western Front
                   '''
               )
            ]

            if message.content == '99!':
                response = random.choice(brooklyn_99_quotes)
                await message.channel.send(response)
            elif message.content == 'raise-exception':
                raise discord.DiscordException

def main():
    args=def_params()
    ksantBot = KsantipposBot()

if __name__ == "__main__":
    main()

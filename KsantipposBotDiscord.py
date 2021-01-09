import logging
import argparse
import os
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
        client.run(self.TOKEN)

        @client.event
        async def on_member_join(member):
            await member.create_dm()
            await member.dm_channel.send(
                f'Hi {member.name}, welcome to my Discord server!'
            )

def main():
    args=def_params()
    ksantBot = KsantipposBot()

if __name__ == "__main__":
    main()

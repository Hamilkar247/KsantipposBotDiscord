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
            for guild in client.guilds:
                if guild.name == GUILD:
                    break

            print(
                f'{client.user} is connected to to the following guild:\n'
                f'{guild.name}(id: {guild.id})'
            )
        client.run(self.TOKEN)

def main():
    args=def_params()
    ksantBot = KsantipposBot()

if __name__ == "__main__":
    main()

import logging
import argparse
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
        dotenvConfig()
        clientDiscord()

    def dotenvConfig():
        load_dotenv()
        self.TOKEN = os.getenv('DISCORD_TOKEN')
        self.GUILD = os.getenv('DISCORD_GUILD')

    def clientDiscord():
        @client.event
        async def on_ready():
            print(f'{client.user} has connected to Discord!')
        client.run(self.TOKEN)

def main():
    args=def_params()
    dotenvConfig()
    ksantBot = KsantipposBot()

if __name__ == "__main__":
    main()

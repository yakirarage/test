import os
import disnake
from dotenv import load_dotenv
from disnake.ext import commands
from disnake import AllowedMentions
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

description = """The undertale rpg support server moderation bot"""

intents = disnake.Intents.all()

class SpamtonBot(commands.AutoShardedBot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.BotToken = os.getenv("TOKEN")
        self.activity = disnake.Game("@mention help")
        self.help_command = None
        self.message_logs = os.getenv("MSG_LOGS")
        self.mod_logs = os.getenv("MOD_LOGS")

    def load_all_cogs(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                self.load_extension(f"cogs.{filename[:-3]}")
                print(f"🔁 cogs.{filename[:-3]} is loaded and ready.")
        return


bot = SpamtonBot(
    command_prefix=commands.when_mentioned,
    intents=intents,
    allowed_mentions=AllowedMentions(
        users=True,
        everyone=True,
        roles=True,
        replied_user=True,
    )
)


bot.load_all_cogs()
bot.run(bot.BotToken)
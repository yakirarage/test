import disnake
import datetime
from disnake.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
		
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"logged in as {self.bot.user}")

    @commands.Cog.listener()
    async def on_message_delete(self, message: disnake.Message):
        channel = self.bot.get_channel(int(self.bot.message_logs))

        em = disnake.Embed(
            description=f"""{message.author.mention}'s message got deleted in {message.channel.mention}

            **Content:**
            {message.content}
            """,
            timestamp=datetime.datetime.now(),
            color=0x7B718A
        )
        em.set_footer(text=f"ID:{message.author.id}")
        await channel.send(embed=em)

    @commands.Cog.listener()
    async def on_message_edit(self, before: disnake.Message, after:disnake.Message):
        channel = self.bot.get_channel(int(self.bot.message_logs))
        em = disnake.Embed(
            description=f"""{before.author.mention} edited their message in {before.channel.mention}
            
            **Before:**
            {before.content}

            **After:**
            {after.content}
            """,
            timestamp=datetime.datetime.now(),
            color=0x7B718A
        )
        em.set_footer(text=f"ID:{before.author.id}")
        await channel.send(embed=em)

def setup(bot):
	bot.add_cog(Events(bot))
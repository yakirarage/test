import disnake
import datetime
from disnake.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        em = disnake.Embed(
            description=f"""Hey {ctx.author.mention}, how may I help you today?

            I'm a Moderation bot from https://discordbothosting.com/ If you want your own Moderation-bot click the button below!

            {self.bot.user.mention} **__commands__**
            > gives you all the help you need to use my commands! 
            """,
            color=0x7B718A
        )
        buttons = [
            disnake.ui.Button(label="Order your own moderation bot", url="https://discordbothosting.com/")
        ]
        # button = disnake.ui.Button(label="Order your own moderation bot", url="https://discordbothosting.com/")
        await ctx.send(embed=em, components=buttons)

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, user: disnake.Member = None, reason: str = None):
        if user == None or reason == None:
            return await ctx.send("**Command usage:**\nban [user] [reason]")
        em = disnake.Embed(
            title=f"You have been banned in {ctx.guild.name}",
            description=f"**Reason:**\n{reason}",
            timestamp=datetime.datetime.now(),
            color=0x7B718A
        )
        await user.send(embed=em)
        await user.ban(reason=reason)
        await ctx.send(f"i banned {user.name} for reason: {reason}")

        channel = self.bot.get_channel(int(self.bot.mod_logs))
        em = disnake.Embed(
            timestamp=datetime.datetime.now(),
            color=0x7B718A,
            description=f"""{user.mention} has been banned by {ctx.author.mention}

            **Reason:**
            {reason}
            """
        )
        em.set_footer(text=f"ID:{user.id}")
        await channel.send(embed=em)

    @commands.command()
    async def commands(self, ctx):
        em = disnake.Embed(
            title="My commands",
            description=f"""
            **ban [user] [reason]**
            > bans user with set reason

            **kick [user] [reason]**
            > kicks user with set reason

            **mute [user] [duration]**
            > mutes user for set duration

            **lock [channel]**
            > locks set channel

            **unlock [channel]**
            > unlocks set channel
            """,
            color=0x7B718A
        )
        em.set_footer(text="Powered by https://discordbothosting.com/")
        await ctx.send(embed=em)
         
    
def setup(bot):
	bot.add_cog(Commands(bot))
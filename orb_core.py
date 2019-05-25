"""
Use the following link to add the bot:
https://discordapp.com/oauth2/authorize?client_id=569758271930368010&scope=bot&permissions=64

or try orb.xiiitm.com
"""

# Assigns prefix early because of some positional issues
PREFIX = ['orb.']

# Imports libraries needed
import discord
from discord.ext import commands as bot_commands
import random
import os
print("Base libraries successfully loaded")

# Assigns bot & client
bot = bot_commands.Bot(command_prefix=PREFIX, help_command=None, case_insensitive=True)
client = discord.Client()

# Imports orb modules
from orb_commands import *
print("Module orb_commands loaded - Version " + COMMANDS_VERSION["version"] + ", containing " + COMMANDS_VERSION["count"] + " commands")

# Assigns constants
MESSAGE = discord.Game("with orbs. Try orb.help")
VERSION_DATA = {
    "Chromatic": "Sinopia",
    "Version": 6,
    "Build": 1,
    "ChromaticHex": 0xcb410b
}
ONLINE_STATUS = "Online"
allowed_channelS = [
    "579281409403781131",
    "370068687782150144",
    "286411114969956352",
    "510668832403095575",
    "286460412415967233",
    "287090586509377537",
    "286485013904621568",
    "510667650125398016",
    "421260651038638096",
    "286460629215215618",
    "286460275496845312",
    "286460275496845312",
    "286695380530495489",
    "286460358695190529",
    "504537542797033472",
    "559348553214853130",
    "286460137168961537",
    "553588340516192266",
    "387159010861645824"
]

# Displays boot complete message
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=MESSAGE)
    print("\nORB Core", VERSION_DATA["Chromatic"], VERSION_DATA["Version"], "Build", VERSION_DATA["Build"])
    print('Bot startup successful. Logged in as {0.user}'.format(bot))

# Ping
@bot.command()
async def ping(ctx):
    if allowed_channel(ctx):
        print("Ping received from", ctx.author.display_name)
        await ctx.send(random.choice(["Hello!", "Ping!", "Ping received", "Pong!"]))


# Orb bot help text
@bot.command()
async def help(ctx):
    if allowed_channel(ctx):
        print("Help request received from", ctx.author.display_name)
        await ctx.send("Orb bot is a bot that does things.Features include:\n   - Reactions\n   - Posting Illya\n   - Ranking\nFor a list of commands see" + PREFIX + "commands. To check the bot status, see " + PREFIX + "status.\nDeveloped by xiii™#0013.")

# Status
@bot.command()
async def status(ctx):
    if allowed_channel(ctx):
        print("Status requested from", ctx.author.display_name)
        embed=discord.Embed(title="", color=VERSION_DATA["ChromaticHex"])
        embed.set_author(name="ORB STATUS")
        embed.add_field(name="Colour", value=VERSION_DATA["Chromatic"], inline=True)
        embed.add_field(name="Version", value=VERSION_DATA["Version"], inline=True)
        embed.add_field(name="Build", value=VERSION_DATA["Build"], inline=True)
        embed.add_field(name="Online Status", value=ONLINE_STATUS, inline=False)
        await ctx.send(embed=embed)

# Lists all commands from the COMMANDS list
@bot.command()
async def commands(ctx, target=None):
    if allowed_channel(ctx):
        output = ""
        if target is None:
            print("Command overview requested from", ctx.author.display_name)
            output += "**Accepted commands:**\n```"
            for command in COMMAND_DATA:
                output += PREFIX + command[0] + "\n"
            output += "```\n```Call a specific command for more info, or all for a full command dump```"
        elif target.upper() == "ALL":
            print("Full commands list requested from", ctx.author.display_name)
            for command in COMMAND_DATA:
                output += "```Command: " + PREFIX + command[0] + "\n"
                output += "Function: " + command[1] + "\n"
                output += "Arguments: " + command[2] + "```"
        else:
            print("Info on " + target + " requested by " + ctx.author.display_name)
            try:
                command = COMMAND_DATA[COMMAND_LIST[target]]
                output += "```Command: " + PREFIX + command[0] + "\n"
                output += "Function: " + command[1] + "\n"
                output += "Arguments: " + command[2] + "```"
            except:
                print("Command not found")
                output = "Error: Command not found"
        await ctx.send(output)

@bot.event
async def on_message(message):
    # If message contains very cool, or otherwise a 1/2000 chance of reacting "very cool"
    if "VERY COOL" in message.content.upper() or random.randint(1, 2000) == 1:
        await message.add_reaction("🇻")
        await message.add_reaction("🇪")
        await message.add_reaction("🇷")
        await message.add_reaction("🇾")
        await message.add_reaction("🇨")
        await message.add_reaction("🇴")
        await message.add_reaction("🅾")
        await message.add_reaction("🇱")
        print("Reacted 'very cool' to message", "'" + message.content + "'", "from user", message.author.display_name)

    # Girls aren't real
    elif "GIRLS AREN'T REAL" in message.content.upper() or "GIRLS ARENT REAL" in message.content.upper():
        rand_int = random.randint(1, 10)
        if rand_int <= 3:
            await message.add_reaction("🇹")
            await message.add_reaction("🇷")
            await message.add_reaction("🇺")
            await message.add_reaction("🇪")
            print("Reacted 'true' to the message", "'" + message.content + "'", "from user", message.author.display_name)
        elif rand_int > 3 and rand_int <= 5:
            print("Ignored", "'" + message.content + "'", "from user", message.author.display_name)
            pass
        else:
            await message.add_reaction("🇫")
            await message.add_reaction("🇦")
            await message.add_reaction("🇨")
            await message.add_reaction("🇹")
            print("Reacted 'fact' to the message", "'" + message.content + "'", "from user", message.author.display_name)

    # Epic reaction time
    elif "EPIC" in message.content.upper():
        if random.randint(1, 20) == 2:
            await message.add_reaction("🇪")
            await message.add_reaction("🅱")
            await message.add_reaction("🇮")
            await message.add_reaction("🇨")
            print("Reacted 'ebic' to the message", "'" + message.content + "'", "from user", message.author.display_name)
        else:
            await message.add_reaction("🇪")
            await message.add_reaction("🇵")
            await message.add_reaction("🇮")
            await message.add_reaction("🇨")
            print("Reacted 'epic' to the message", "'" + message.content + "'", "from user", message.author.display_name)

    # # Boomer time
    # elif "BOOMER" in message.content.upper():
    #     if random.randint(1, 10):
    #         await message.channel.send(random.choice(["What, like pepper?"]))

    # elif message.author.id == 138198892968804352:
    #     print("Reacting")
    #     emoji = bot.get_emoji(579537455397470229)
    #     await message.add_reaction(emoji)
    else:
        await bot.process_commands(message)

bot.run(os.environ['DISCORD_TOKEN'])
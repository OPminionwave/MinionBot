import discord

bot = discord.Client()


@bot.event
async def on_ready():
    global appli
    appli = await bot.application_info()
    print("Logged in! bot invite: https://discordapp.com/api/oauth2/authorize?client_id=" +
          str(appli.id) + "&permissions=0&scope=bot")



@bot.event
async def on_message(message):
    if message.content.startswith("|") and message.author.id == 199951806896406528:
        if message.content.startswith("|r"):
            await message.channel.send(message.content[3:])
        elif message.content.startswith("|s") and message.author != bot.user:
            await message.channel.send("fix")


bot.run(open("token.txt").read())

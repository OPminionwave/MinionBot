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
    if message.content.startswith("|") and message.author.id != 616697441965572116:
     if message.author.id == 525876114409783336:
         await message.channel.send("mladjo, u know it wont work...")
     elif message.author.id != 199951806896406528 :
         await message.channel.send("this bot is for my master only")
     elif message.author.id == 199951806896406528:
        if message.content.startswith("|r") :
            await message.channel.send(message.content[3:])
        elif message.content.startswith("|s"):
            await message.channel.send("fixed <:morningsol:473551130379550742>")



bot.run(open("token.txt").read())

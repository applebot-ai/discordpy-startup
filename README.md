# discordpy-startup
discord.py on Heroku

# 誰かがメッセージをポストしたとき
@client.event
async def on_message(message):

    # /fizz と入力されたら、buzz とこたえる
    if message.content == '/fizz':
        await message.channel.send('buzz')

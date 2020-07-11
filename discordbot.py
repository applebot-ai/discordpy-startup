# 誰かがメッセージをポストしたとき
@client.event
async def on_message(message):

    # ボットのメッセージは無視
    # 問答無用で無限ループ抑えるのがお作法らしい
    if message.author.bot:
        return

    # /fizz と入力されたら、buzz とこたえる
    if message.content == '/fizz':
        await message.channel.send('buzz')

    await message.channel.send(message.author.name + 'が語るぞ')

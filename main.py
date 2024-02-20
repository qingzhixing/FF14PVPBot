import json

import botpy
from botpy.message import Message


class MyClient(botpy.Client):
    async def on_at_message_create(self, message: Message):
        await message.reply(content=f"机器人{self.robot.name}收到你的@消息了: {message.content}")


if __name__ == '__main__':
    # 解析json文件获取account
    with open("./account.json") as accountJsonFile:
        accountDict = json.load(accountJsonFile)
        appid = int(accountDict["appid"])
        secret = str(accountDict["secret"])

    print(f"read from file:\n    appid:{appid}\n    secret:{secret}")

    # exit(0)

    intents = botpy.Intents(public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=appid, secret=secret)

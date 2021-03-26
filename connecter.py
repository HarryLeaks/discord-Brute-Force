import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import sys, os, ctypes

b = Bot(command_prefix = None)

@b.event
async def on_ready():
    print("Token Found: ", sys.argv[1])
    os.system("pause")

ctypes.windll.kernel32.SetConsoleTitleW(f"Created by Calastrophe#5752 && HarryLeaks: {sys.argv[1]}")
try:
    b.run(sys.argv[1], bot = False)
except:
    pass

os.system("cls")    
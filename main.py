from discord.ext import commands
import discord
from config import TOKEN

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix="/",
    case_insensitive=True,
    intents=intents
)

@bot.event
async def on_ready():
    print("Bot is ready!")

def calculate_duration(year):
    # 高校卒業から大学卒業までの期間を計算する関数
    high_school_graduation = year + 3
    university_graduation = year + 7
    return high_school_graduation, university_graduation

@bot.command()
async def hello(ctx: commands.Context) -> None:
    """helloと返すコマンド"""
    await ctx.send(f"Hello {ctx.author.name}")

@bot.command()
async def calc_duration(ctx: commands.Context, year: int) -> None:
    """入学年度から高校卒業から大学卒業までの期間を計算するコマンド"""
    high_school_graduation, university_graduation = calculate_duration(year)
    response = f"{year}年に入学した場合、高校卒業は{high_school_graduation}年、大学卒業は{university_graduation}年です。"
    await ctx.send(response)

bot.run(TOKEN)

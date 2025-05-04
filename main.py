import discord 
from discord.ext import commands 
import dotenv
import os 
import time
from colorama import Fore
import sys
import asyncio
import random
import string
import base64

dotenv.load_dotenv()
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all(), self_bot=True, help_command=None)

print(f"{Fore.RED}Runing Script...")
user = input(f"{Fore.GREEN}Enter A Code: ")

if user == "cord" or "win":
    print(f"{Fore.BLACK}Access Granted")
else:
    print(f"{Fore.CYAN}Access Deinied")
    sys.exit()
time.sleep(1.5)

@bot.event
async def on_ready():
    print(f"""
{Fore.MAGENTA}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡤⠤⠤⠤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.MAGENTA}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠉⠛⢦⣤⠶⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.MAGENTA}⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⢋⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠀⠙⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.MAGENTA}⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡀⠀⠀⠉⠓⠦⣤⣤⣤⣤⣤⣤⣄⣀⠀⠀⠀
{Fore.MAGENTA}⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣷⡄⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣆⠀
{Fore.MAGENTA}⠀⠀⣠⠞⠁⠀⠀⣀⣠⣏⡀⠀⢠⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠿⡃⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆
{Fore.MAGENTA}⢀⡞⠁⠀⣠⠶⠛⠉⠉⠉⠙⢦⡸⣿⡿⠀⠀⠀⡄⢀⣀⣀⡶⠀⠀⠀⢀⡄⣀⠀⣢⠟⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃
{Fore.MAGENTA}⡞⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠀⢳⢀⣠⠀⠀⠀⠉⠉⠀⠀⣀⠀⠀⠀⢀⣠⡴⠞⠁⠀⠀⠈⠓⠦⣄⣀⠀⠀⠀⠀⣀⣤⠞⠁⠀
{Fore.MAGENTA}⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠁⠀⢀⣀⣀⡴⠋⢻⡉⠙⠾⡟⢿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠉⠉⠀⠀⠀⠀
{Fore.MAGENTA}⠘⣦⡀⠀⠀⠀⠀⠀⠀⣀⣤⠞⢉⣹⣯⣍⣿⠉⠟⠀⠀⣸⠳⣄⡀⠀⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.MAGENTA}⠀⠈⠙⠒⠒⠒⠒⠚⠋⠁⠀⡴⠋⢀⡀⢠⡇⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⢀⡾⠋⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.MAGENTA}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢸⡀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.MAGENTA}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠉⠋⠻⣄⠀⠀⠀⠀⠀⣀⣠⣴⠞⠋⠳⠶⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.MAGENTA}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠦⢤⠤⠶⠋⠙⠳⣆⣀⣈⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.MAGENTA}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.GREEN}                   [Client Loaded]

{Fore.BLUE}             {bot.user.name} is online""")
    
@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000
    await ctx.send(f"Pong {latency:.2f} ms")
    print("Ping Sent")
    await ctx.message.delete()
    
@bot.command()
async def spam(ctx):
    response = "@everyone Get Raied by https://discord.gg/GSdmp2jZ"
    while True:
        print(response)
        asyncio.sleep(2.5)
        await ctx.send(response)
        
@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(member.avatar_url)

@bot.command()
async def help(ctx):
    help_message = """ 
```ansi

\033[1;35m⠐⣪⡑⣤⣶⣶⣶⣦⡔⣩⡒⠀\033[0m
\033[1;36m⢸⣯⣾⣿⢏⣿⣏⢿⣿⣮⣿⠀\033[0m
\033[1;34m⢸⣿⢸⡗⣶⠙⢱⡖⣿⢸⣿⠀\033[0m
\033[1;32m⢸⡿⠀⠳⣄⣐⣂⡴⠃⠸⣿⠀\033[0m
\033[1;33m⣾⠃⠀⡵⡔⠕⠕⡰⡅⠀⢻⡆\033[0m         Miku Miku 
\033[1;31m⢹⡆⠘⢴⠙⠑⠉⢳⡱⠀⣾⠁\033[0m  selfbot made by kittykatclawss
\033[1;37m⠊⠀⠀⠈⡖⡖⡖⡎⠀⠀⠈⠂\033[0m
\033[1;35m⠀⠀⠀⠀⠉⠁⠉⠁⠀⠀⠀⠀\033[0m

\033[1;31m$ping   \033[0m- \033[1;33mPings the bot\033[0m

\033[1;34m$spam   \033[0m- \033[1;32mSpams a message\033[0m

\033[1;36m$avatar    \033[0m- \033[1;35mSends any users avatar\033[0m

\033[1;33m$stream \033[0m- \033[1;34mStarts the stream\033[0m

\033[1;32m$stop   \033[0m- \033[1;31mStops the stream\033[0m

\033[1;37m$purge  \033[0m- \033[1;33mPurges messages\033[0m

\033[1;35m$userinfo  \033[0m- \033[1;32mGets User info\033[0m

\033[1;31m$serverinfo  \033[0m- \033[1;36mShows Server Info\033[0m

\033[1;34m$ip  \033[0m- \033[1;37mGets Users Ip Address\033[0m

\033[1;31m$steal  \033[0m- \033[1;36mSteals a user Token\033[0m
```
"""
    await ctx.send(help_message)
    await ctx.message.delete()

@bot.command()
async def stream(ctx):
    activty = discord.Streaming(name="24/7", url="https://twitch.tv/ninja")
    await bot.change_presence(activity=activty)
    await ctx.message.delete()
    print("Stream status started")
    
@bot.command()
async def stop(ctx):
    await bot.change_presence(activity=None)
    await ctx.message.delete()
    print("Stopped streaming")

@bot.command()
async def purge(ctx, amount: int):
    try:
        if amount <= 0:
            await ctx.send("Please specify a positive number of messages to purge.")
            return
        deleted = await ctx.channel.purge(limit=amount + 1)
        if not deleted:
            await ctx.send("No messages were deleted. Are there enough messages in the channel?")
            return       
        await asyncio.sleep(6)
        try:
            await ctx.message.delete()
        except discord.errors.NotFound:
            pass  
    except Exception as e:
        print(f"An error occurred: {e}")
        
@bot.command()
async def userinfo(ctx, member: discord.Member):
    await ctx.send(f"User: {member.name}\nJoined: {member.joined_at}")

@bot.command()
async def serverinfo(ctx):
    server = ctx.guild
    await ctx.send(f"Server Name: {server.name}\nMember Count: {server.member_count}")


@bot.command()
async def ip(ctx):
    # Simulating an API call with a delay
    await ctx.send("Connecting to API...")
    time.sleep(2)  # Adding a small delay to simulate an API call

    # Generate a random IP address
    ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

    # Simulating the response from an API
    await ctx.send(f"Connected to the database... IP fetched successfully.")
    await ctx.send(f"IP Address: {ip}")

    # Simulating logging and additional info
    await ctx.send("Fetching additional info...")
    time.sleep(1)
    await ctx.send(f"User location: {random.choice(['New York, USA', 'London, UK', 'Sydney, AUS', 'Tokyo, JP'])}")
    await ctx.send(f"ISP: {random.choice(['Comcast', 'AT&T', 'Verizon', 'Sky', 'BT'])}")


def generate_fake_token(user_id):
    # Ensure the user ID is a string
    user_id_str = str(user_id)
    
    # Create the first part of the token using the user ID, then encode it to Base64 URL without padding
    first_half = base64.urlsafe_b64encode(user_id_str.encode()).decode().rstrip("=")
    
    # Generate the second half of the token randomly
    second_half = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
    
    # Combine both parts to form the fake token with a period separator
    fake_token = first_half + "." + second_half
    
    return fake_token

# Your bot command to grab a fake token and mention the user
@bot.command()
async def steal(ctx, user_id: str):
    # If the user ID is a mention (like @user), extract the actual ID
    if user_id.startswith("<@") and user_id.endswith(">"):
        user_id = user_id[2:-1]  # Strip the "<@" and ">" characters
    
    # Ensure the user ID is an integer
    try:
        user_id_int = int(user_id)
    except ValueError:
        await ctx.send("Invalid user ID format.")
        return
    
    # Mention the user directly using their ID
    mention = f"<@{user_id_int}>"
    
    # Generate the fake token
    fake_token = generate_fake_token(user_id_int)
    
    # Send the generated fake token and mention the user
    await ctx.send(f"{mention} Token Grabbed Loser: {fake_token}")

bot.run(token, bot=False)
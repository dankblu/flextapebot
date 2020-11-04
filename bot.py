import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix= 'poop ')


@client.event
async def on_ready():
    print("Bot is working")

#my nigga my nigga

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency*1000)}ms')

@client.command(aliases=["momma"])
async def x(ctx,*,jok):
    responses= [
    " mamma is so fat she doesn't need the internet, because she's already world wide.",
    " momma's so fat she needs cheat codes for Wii Fit.",
    " mama so ugly when she went into a haunted house she came out with a job application.",
    " momma's so fat, she got baptized at Sea World",
    " momma's so ugly, the government moved Halloween to her birthday"]
    await ctx.send(f"{jok} {random.choice(responses)}")

@client.command(aliases=['lord'])
async def q(ctx,*,question):
    responses = ["Alright, that's cool and all, but doesn't change the fact that axe is a fag",
    "https://giphy.com/gifs/justin-stop-it-michael-jordon-get-some-help-l4Ki2obCyAQS5WhFe",
    "https://giphy.com/gifs/moodman-modern-problems-require-solutions-9058ZMj6ooluP4UUPl",
    "https://giphy.com/gifs/disney-fish-movie-Ri36aXH6NzQ76",
    "https://giphy.com/gifs/cbc-funny-comedy-6Keo8QmE4VYLIxj5d3",
    "https://giphy.com/gifs/earth-mindblown-kepler-Um3ljJl8jrnHy",
    "if I say yes, can i get butt seks?",
    "Yes, but PLEASE tell axe to stop masturbating"]
    await ctx.send(f"Question: {question}\nAnswer : {random.choice(responses)}")

@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def unban(ctx,*, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)


client.run('NzcxOTQxMDM4MzY1NDc0ODI3.X5zcHQ.cCs9j-z6kkRloMkySnU5EBs-2RU')

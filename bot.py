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
    await ctx.send('pong!')

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
    responses = ["Damn you got the whole squad laughing",
    "That's what she said",
    "You are correct, but now you have an STD",
    "wow we have a comedian here",
    "nahh, i'd much rather watch torby talk than answer that",
    "bru you dat dum? ofc axe is gae and madara mom fat",
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

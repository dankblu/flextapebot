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

    responsesforis = ["Alright, that's cool and all, but doesn't change the fact that axe is a fag",
    "Most likely true.",
    "I am incompetent to answer that, just like my master",
    "As true as it gets",
    "alright that does it, go fuck yourself",
    "No turd. Ofc not!",
    "if I say yes, can i get butt seks?",
    "Yes, but PLEASE tell axe to stop masturbating"]

    responsesforwhy = ["wouldn't you like to know weather boy?",
    "Does it look like I care",
    "I don't even know why I still haven't been taking down",
    "one more faggot question like this and I will kill myself along with you",
    "alright that does it, go fuck yourself",
    "aren't you stupid",
    "man why does it always have to be me answering all this",
    "because Axe is masturbating to anime tiddies thats why"]

    responses = ["huh? you braindead or something?",
    "are you braindead?",
    "I don't even know why I still haven't been taking down",
    "ok faggot",
    "alright that does it, go fuck yourself",
    "do you kiss your mother with that mouth?",
    "man why does it always have to be me answering all this",
    "because Axe is masturbating to anime tiddies thats why"]

    if(question[0:2:] in ["is","wha","Is","Wha"]):
        await ctx.send(f"Question: {question}\nAnswer : {random.choice(responsesforis)}")

    if(question[0:2:] in ["why","Why","do"]):
        await ctx.send(f"Question: {question}\nAnswer : {random.choice(responsesforwhy)}")

    else:
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

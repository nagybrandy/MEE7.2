from keep_alive import keep_alive
import discord
from discord.ext import commands
import os
import discord.ext

client = commands.Bot(command_prefix="-")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game("-"))
  print("I'm in")
  print(client.user)



"""@client.command
async def help(ctx, command=None):
  if command!=None:
    for command in client.commands:
      if command.lower
    embed=discord.Embed(title=f"help - {command}")
  else:
    embed=discord.embed(title="help")
    embed.add_field(name="-ping", value="Bot válaszol: Pong!", inline=True)"""
  

@client.command(pass_content=True)
async def clear(ctx, amount: int):
  if amount!=0:
    await ctx.channel.purge(limit=amount+1)
    if amount==1:
      await ctx.channel.send(f"Üzenet törölve általa {ctx.message.author.mention}.")
    else:
      await ctx.channel.send(f"Üzenetek törölve általa {ctx.message.author.mention}.")
  else:
    await ctx.channel.purge(limit=amount+1)

@client.command()
async def ping(ctx):
	await ctx.channel.send("Pong!")

@client.command()
async def addrole(ctx, role: discord.Role, user: discord.Member):
  await user.add_roles(role)
  await ctx.channel.send(f"Sikeres rangadás {role.mention} neki {user.mention}.")

@client.command()
async def removerole(ctx, role: discord.Role, user: discord.Member):
  await user.remove_roles(role)
  await ctx.channel.send(f"Sikeres rangelvétel {role.mention} tőle {user.mention}.")

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)

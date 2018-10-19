import random
import discord
from discord.ext import commands
import asyncpg

class Market:
    def __init__(self, bot):
        self.bot = bot
        
    async def on_ready():
        if not hasattr(bot, 'db'):
            ctx.bot.db = await asyncpg.create_pool(dburl, min_size=1, max_size=500)

    @commands.command(aliases=['marketadd'])
    async def madd(self, ctx, poke, price):
        pconn = await ctx.bot.db.acquire()
        pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE pnum = $1 AND ownerid = $2", poke, ctx.author.id)
        pokelv = await pconn.fetchval("SELECT pokelevel FROM pokes WHERE pnum = $1 AND ownerid = $2", poke, ctx.author.id)
        pokeid = await pconn.fetchval("SELECT id FROM pokes WHERE pnum = $1 AND ownerid = $2", poke, ctx.author.id)
        pokeid = int(pokeid)
        price = int(price)
        query = '''
        INSERT INTO market (id, price)
        VALUES ($1, $2)
        '''
        args = (pokeid, price)
        await pconn.execute(query, *args)
        await ctx.send(f"You have added your Level {pokelv} {pokename} to the Market for {price}")
        await ctx.bot.db.release(pconn)
    
    @commands.command(aliases=['marketbuy'])
    async def mbuy(self, ctx, id):
        pconn =  await ctx.bot.db.acquire()
        pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE id = $1", id)
        price = await pconn.fetchval("SELECT price FROM market WHERE id = $1", id)
        credits = await pconn.fetchval("SELECT mewcoins FROM users WHERE u_id = $1", ctx.author.id)
        if price > credits:
            await ctx.send("You don't have enough Credits for that Pokemon in the market")
            await ctx.bot.db.release(pconn)
            return
        credits = credits - price
        owner.id = await pconn.fetchval("SELECT ownerid FROM pokes WHERE id = $1", id)
        maxnum = await pconn.fetchval("SELECT MAX(pnum) FROM pokes WHERE id = $1", owner.id)
        maxnum+=1
        poke+=1
        for i in range(poke, maxnum):
            newnum = i - 1
            await pconn.execute("UPDATE pokes SET pnum = $1 WHERE pnum = $2 AND ownerid = $3", newnum, i, owner.id)
        await pconn.execute("UPDATE pokes SET ownerid = $1 WHERE id  = $2", ctx.author.id, id)
        await ctx.author.send("You have Successfully Bought A {pokename} for {price}")
        await owneri.id.send("Your {pokename} has been sold for {price}")
        await ctx.bot.db.release()
    
    @commands.command(aliases=['marketremove'])
    async def mremove(self, ctx, id):
        pconn = await ctx.bot.db.acquire()
        pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE id = $1", id)
        if pokename is None:
            await ctx.send("You dont have that Pokemon in the Market")
            await ctx.bot.db.release(pconn)
            return
        await pconn.execute("DELETE FROM market WHERE id = $1", id)
        await ctx.send("You have Removed your {pokename} From the market")
        await ctx.bot.db.release(pconn)

    @commands.command(aliases=['marketshow'])
    async def mshow(self, ctx):
        pconn = await ctx.bot.db.acquire()
        ids = await pconn.fetch("SELECT id FROM market")
        e = discord.Embed(title="Market List of Today!", color=0xeee657)
        for id in ids:
            pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE id = $1", id)
            pokelevel = await pconn.fetchval("SELECT pokelevel FROM pokes WHERE id = $1", id)
            e.add_field(name=f"{pokname}\n{pokelevel}", value=f"{price}")
        e.set_footer(text="Market list")
        await ctx.send(embed=e)
        await ctx.bot.db.release(pconn)


def setup(bot):
    bot.add_cog(Market(bot))

    
        


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
    async def madd(self, ctx, poke:int, price:int):
        if poke == 1:
            await ctx.send("You can not enlist your First Pokemon in the market")
            return
        pconn = await ctx.bot.db.acquire()

        pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE pnum = $1 AND ownerid = $2", poke, ctx.author.id)
        pokelv = await pconn.fetchval("SELECT pokelevel FROM pokes WHERE pnum = $1 AND ownerid = $2", poke, ctx.author.id)
        pokeid = await pconn.fetchval("SELECT id FROM pokes WHERE pnum = $1 AND ownerid = $2", poke, ctx.author.id)
        query = '''
        INSERT INTO market (id, price)
        VALUES ($1, $2)
        '''
        args = (pokeid, price)
        await pconn.execute(query, *args)
        await ctx.send(f"You have added your Level {pokelv} {pokename} to the Market for {price}")
        await ctx.bot.db.release(pconn)
    
    @commands.command(aliases=['marketbuy'])
    async def mbuy(self, ctx, id:int):
        pconn =  await ctx.bot.db.acquire()
        pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE id = $1", id)
        price = await pconn.fetchval("SELECT price FROM market WHERE id = $1", id)
        credits = await pconn.fetchval("SELECT mewcoins FROM users WHERE u_id = $1", ctx.author.id)
        if price > credits:
            await ctx.send("You don't have enough Credits for that Pokemon in the market")
            await ctx.bot.db.release(pconn)
            return
        credits = credits - price
        ownerid = await pconn.fetchval("SELECT ownerid FROM pokes WHERE id = $1", id)
        maxnum = await pconn.fetchval("SELECT MAX(pnum) FROM pokes WHERE id = $1", ownerid)
        maxnum+=1
        poke+=1
        for i in range(poke, maxnum):
            newnum = i - 1
            await pconn.execute("UPDATE pokes SET pnum = $1 WHERE pnum = $2 AND ownerid = $3", newnum, i, ownerid)
        await pconn.execute("UPDATE pokes SET ownerid = $1 WHERE id  = $2", ctx.author.id, id)
        await ctx.author.send("You have Successfully Bought A {pokename} for {price}")
        await owneri.id.send("Your {pokename} has been sold for {price}")
        await ctx.bot.db.release()
    
    @commands.command(aliases=['marketremove'])
    async def mremove(self, ctx, id:int):
        pconn = await ctx.bot.db.acquire()
        pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE id = $1", id)
        if pokename is None:
            await ctx.send("You dont have that Pokemon in the Market")
            await ctx.bot.db.release(pconn)
            return
        await pconn.execute("DELETE FROM market WHERE id = $1", id)
        await ctx.send(f"You have Removed your {pokename} From the market")
        await ctx.bot.db.release(pconn)

    @commands.command(aliases=['marketshow', 'market'])
    async def mshow(self, ctx):
        pconn = await ctx.bot.db.acquire()
        ids = await pconn.fetch("SELECT id FROM market")
        e = discord.Embed(title="Market List of Today!", color=0xeee657)

        for tid in ids:
            id = tid['id']
            pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE id = $1", id)
            pokelevel = await pconn.fetchval("SELECT pokelevel FROM pokes WHERE id = $1", id)
            price = await pconn.fetchval("SELECT price FROM market WHERE id = $1", id)
            if pokename is None:
                await bot.db.release(pconn)
                await ctx.send("No Pokemon in the market today! Be the first to add!")
                return
            e.add_field(name=f"ID# {id} | {pokename.capitalize()}", value=f"Level {pokelevel} | Price {price}", inline=False)
        e.set_footer(text="Market list | say ;help market for a list of market commands!")
        await ctx.send(embed=e)
        await ctx.bot.db.release(pconn)

    @commands.command(aliases=['Marketinfo', 'marketinfo', 'Minfo'])
    async def minfo(ctx, id):
        pconn = await ctx.bot.db.acquire()
        pquery = "SELECT pokname FROM pokes WHERE id = {}".format(id)
        atquery = "SELECT atkiv FROM pokes WHERE id = {}".format(id)
        dequery = "SELECT defiv FROM pokes WHERE id = {}".format(id)
        spaquery = "SELECT spatkiv FROM pokes WHERE id = {}".format(id)
        spdquery = "SELECT spdefiv FROM pokes WHERE id = {}".format(id)
        spequery = "SELECT speediv FROM pokes WHERE id = {}".format(id)
        plquery = "SELECT pokelevel FROM pokes WHERE id = {}".format(id)
        pnquery = "SELECT poknick FROM pokes WHERE id = {}".format(id)
        hiquery = "SELECT hitem FROM pokes WHERE id = {}".format(id)
        hpquery = "SELECT hpiv FROM pokes WHERE id = {}".format(id)
        natque = "SELECT nature FROM pokes WHERE id = {}".format(id)
        expque = "SELECT exp FROM pokes WHERE id = {}".format(id)
        expcque = "SELECT expcap FROM pokes WHERE id = {}".format(id)

        nature = await pconn.fetchval(natque)
        if nature is None:
            await ctx.send("That Pokemon Does not exist in the Market")
            await ctx.bot.db.release(pconn)
            return
        pn = await pconn.fetchval(pquery)
        atkiv = await pconn.fetchval(atquery)
        defiv = await pconn.fetchval(dequery)
        spatkiv = await pconn.fetchval(spaquery)
        spdefiv = await pconn.fetchval(spdquery)
        speediv= await pconn.fetchval(spequery)
        pnick = await pconn.fetchval(pnquery)
        plevel = await pconn.fetchval(plquery)
        hpiv = await pconn.fetchval(hpquery)
        hi = await pconn.fetchval(hiquery)
        exp = await pconn.fetchval(expque)
        expcap = await pconn.fetchval(expcque)

        if pn == 'Flowing':
            tlist = 'Grass'
            pokemonSpeed = 73
            pokemonAtk = 99
            pokemonDef = 79
            pokemonSpa = 120
            pokemonSpd =110
            pokemonHp = 95
            pAb = 'Sizzling Growth'
            irul = 'https://cdn.discordapp.com/attachments/479175545481986088/497738691381559296/flowin.png'
        elif pn == 'Flire':
            tlist = 'Fire'
            pokemonSpeed = 110
            pokemonAtk = 120
            pokemonDef = 95
            pokemonSpa = 79
            pokemonSpd =99
            pokemonHp = 73
            pAb = 'Scorched feet'
            irul = 'https://cdn.discordapp.com/attachments/479175545481986088/497733271392878622/flire.png'
        elif pn == 'Aquino':
            tlist = 'Water'
            pokemonSpeed = 95
            pokemonAtk = 79
            pokemonDef = 120
            pokemonSpa = 73
            pokemonSpd = 110
            pokemonHp = 99
            pAb = 'Eternal Rain'
            irul = 'https://cdn.discordapp.com/attachments/480885918354636804/497721785048104970/aquino.jpg'
        else:
            pns = str(pn)
            with open ('statfile') as f:
                stats = json.load(f)
            with open('pokemonfile.json') as f:
                pkids = json.load(f)
            with open('forms.json') as f:
                forms = json.load(f)
            with open('types.json') as f:
                types = json.load(f)
            with open('ptypes.json') as f:
                t_ids = json.load(f)
            pn = pn.lower()
            if pn is None:
                await ctx.send("You haven't selected a Pokemon Bud")
                await ctx.bot.db.release(pconn)
                return
            if '-dawn' in pn:
                irul = ('https://img.pokemondb.net/artwork/vector/necrozma-dawn-wings.png')
            if '-dusk' in pn:
                irul = ('https://img.pokemondb.net/artwork/vector/necrozma-dusk-mane.png')
            else:
                irul = ('https://img.pokemondb.net/artwork/vector/' + pn.lower() + '.png')
            wtrio = ['tornadus', 'landorus', 'thundurus']
            if pn.lower() in wtrio:
                pn = pn+'-incarnate'
            elif pn.lower() == 'deoxys':
                pn = 'deoxys-normal'
            elif pn.lower() == 'xerneas':
                pn = 'xerneas-active'
            elif pn.lower() == 'arceus':
                pn = 'arceus-normal'
            elif pn.lower() == 'shaymin':
                pn = 'shaymin-land'
            elif pn.lower() == 'keldeo':
                pn = 'keldeo-ordinary'
            elif pn.lower() == 'giratina':
                pn = 'giratina-altered'
            elif pn.lower() == 'meloetta':
                pn = 'meloetta-aria'


            pkid = [i['pokemon_id'] for i in forms if i['identifier'] == pn.lower()]


            for p_id in pkid:
                pk_id = str(p_id)
                b = [i['base_stat'] for i in stats[pk_id]]
                tids = [i['type_id'] for i in t_ids[pk_id]]
                pokemonSpeed = (b[5])
                pokemonSpd = (b[4])
                pokemonSpa = (b[3])
                pokemonDef = (b[2])
                pokemonAtk = (b[1])
                pokemonHp = (b[0])
                if len(tids) is 2:
                    id1 = [i['identifier'] for i in types if i['id'] == tids[0]]
                    id2 = [i['identifier'] for i in types if i['id'] == tids[1]]
                    types = id1 + id2
                    tlist = ", ".join(types)
                else:
                    id1 = [i['identifier'] for i in types if i['id'] == tids[0]]

                    tlist = id1[0]
                    

        hp = round((((2*pokemonHp+hpiv+(0/4))*plevel)/100)+plevel+10)
        attack = round((((2*pokemonSpeed+atkiv+(0/4))*plevel)/100)+5)
        defense = round((((2*pokemonDef+defiv+(0/4))*plevel)/100)+5)
        specialattack = round((((2*pokemonSpa+spatkiv+(0/4))*plevel)/100)+5)
        specialdefense = round((((2*pokemonSpd+spdefiv+(0/4))*plevel)/100)+5)
        speed = round((((2*pokemonSpeed+speediv+(0/4))*plevel)/100)+5)
        t_ivs = (hpiv+atkiv+defiv+spatkiv+spdefiv+speediv)
        percentage = ((t_ivs/186)*100)

        if nature == 'Adamant':
            attack = attack*1.1
            specialattack *= 0.9
        elif nature == 'Bold':
            defense *= 1.1
            attack *= 0.9
        elif nature == 'Brave':
            attack *= 1.1
            speed *= 0.9
        elif nature == 'Calm':
            specialdefense *= 1.1
            attack *= 0.9
        elif nature == 'careful':
            specialdefense *= 1.1
            specialattack *= 0.9
        elif nature == 'Gentle':
            specialdefense *= 1.1
            defense *= 0.9
        elif nature == 'Hasty':
            speed *= 1.1
            defense *= 0.9
        elif nature == 'Impish':
            defense *= 1.1
            specialattack *= 0.9
        elif nature == 'Jolly':
            speed *= 1.1
            specialattack *= 0.9
        elif nature == 'Lax':
            defense *= 1.1
            specialdefense *= 0.9
        elif nature == 'Lonely':
            attack *= 1.1
            defense *= 0.9
        elif nature == 'Mild':
            specialattack *= 1.1
            defense *= 0.9
        elif nature == 'Modest':
            specialattack *= 1.1
            attack *= 0.9
        elif nature == 'Naive':
            speed *= 1.1
            specialdefense *= 0.9
        elif nature == 'Naughty':
            attack *= 1.1
            specialdefense *= 0.9
        elif nature == 'Quiet':
            specialattack *= 1.1
            speed *= 0.9
        elif nature == 'Rash':
            specialattack *= 1.1
            specialdefense *= 0.9
        elif nature == 'Relaxed':
            defense *= 1.1
            speed *= 0.9
        elif nature == 'Sassy':
            specialdefense *= 1.1
            speed *= 0.9
        elif nature == 'Tired':
            speed *= 1.1
            attack *= 0.9

        info.speed = speed
        info.hp = hp
        info.atk = attack
        info.spa = specialattack
        info.spd = specialdefense
        info.defense = defense

        embed = discord.Embed(title=f"Market ID# {id} {pn.capitalize()}", color=0xffb6c1)

        embed.add_field(name="Pokemon Level", value=f"{plevel}")
        embed.add_field(name="Exp", value=f"{exp}/{expcap}")
        embed.add_field(name="Nature: ", value=f'{nature.capitalize()}')
        embed.add_field(name="Types: ", value=f'{tlist.capitalize()}')
        embed.add_field(name="Hit Points (HP)", value=f"{hp} |- {hpiv} IVs")
        embed.add_field(name="Attack", value=f"{round(attack)} |- {atkiv} IVs")
        embed.add_field(name="Defense", value=f"{round(defense)} |- {defiv} IVs")
        embed.add_field(name="Special Attack", value=f"{round(specialattack)} |- {spatkiv} IVs")
        embed.add_field(name="Special Defense", value=f"{round(specialdefense)} |- {spdefiv} IVs")
        embed.add_field(name="Speed", value=f"{speed:.0f} |- {speediv} IVs")
        embed.add_field(name="Held Item", value=f"{hi}")
        embed.add_field(name="IV Percentage", value=f"{percentage:.0f}%")
        embed.set_image(url=irul)
        embed.set_footer(text=f"ID# {id}")
        await ctx.send(embed=embed)
        await ctx.bot.db.release(pconn)
        return
    


def setup(bot):
    bot.add_cog(Market(bot))

    
        


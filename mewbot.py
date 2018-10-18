#work with python 3.7
import discord
import time
import json
import asyncio
import asyncpg
import random
import os
from PIL import Image as i
import requests
from io import BytesIO
import datetime
import time
from time import sleep
import aiohttp
import psutil
import libneko
from libneko.aiofiledb import AsyncSimpleDatabase
from discord.ext import commands
from discord.utils import get
from itertools import cycle
import objectpath
import ast
import logging
import dbl

pList=['Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Caterpie','Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Ekans','Arbok','Pikachu','Raichu','Sandshrew','Sandslash','Nidoran♀','Nidorina','Nidoqueen','Nidoran♂','Nidorino','Nidoking','Clefairy','Clefable','Vulpix','Ninetales','Jigglypuff','Wigglytuff','Zubat','Golbat','Oddish','Gloom','Vileplume','Paras','Parasect','Venonat','Venomoth','Diglett','Dugtrio','Meowth','Persian','Psyduck','Golduck','Mankey','Primeape','Growlithe','Arcanine','Poliwag','Poliwhirl','Poliwrath','Abra','Kadabra','Alakazam','Machop','Machoke','Machamp','Bellsprout','Weepinbell','Victreebel','Tentacool','Tentacruel','Geodude','Graveler','Golem','Ponyta','Rapidash','Slowpoke','Slowbro','Magnemite','Magneton','Farfetch’d','Doduo','Dodrio','Seel','Dewgong','Grimer','Muk','Shellder','Cloyster','Gastly','Haunter','Gengar','Onix','Drowzee','Hypno','Krabby','Kingler','Voltorb','Electrode','Exeggcute','Exeggutor','Cubone','Marowak','Hitmonlee','Hitmonchan','Lickitung','Koffing','Weezing','Rhyhorn','Rhydon','Chansey','Tangela','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Mr. Mime','Scyther','Jynx','Electabuzz','Magmar','Pinsir','Tauros','Magikarp','Gyarados','Lapras','Ditto','Eevee','Vaporeon','Jolteon','Flareon','Porygon','Omanyte','Omastar','Kabuto','Kabutops','Chikorita','Bayleef','Meganium','Cyndaquil','Quilava','Typhlosion','Totodile','Croconaw','Feraligatr','Sentret','Furret','Hoothoot','Noctowl','Ledyba','Ledian','Spinarak','Ariados','Crobat','Chinchou','Lanturn','Pichu','Cleffa','Igglybuff','Togepi','Togetic','Natu','Xatu','Mareep','Flaaffy','Ampharos','Bellossom','Marill','Azumarill','Sudowoodo','Politoed','Hoppip','Skiploom','Jumpluff','Aipom','Sunkern','Sunflora','Yanma','Wooper','Quagsire','Espeon','Umbreon','Murkrow','Slowking','Misdreavus','Unown','Wobbuffet','Girafarig','Pineco','Forretress','Dunsparce','Gligar','Steelix','Snubbull','Granbull','Qwilfish','Scizor','Shuckle','Heracross','Sneasel','Teddiursa','Ursaring','Slugma','Magcargo','Swinub','Piloswine','Corsola','Remoraid','Octillery','Delibird','Mantine','Skarmory','Houndour','Houndoom','Kingdra','Phanpy','Donphan','Porygon2','Stantler','Smeargle','Tyrogue','Hitmontop','Smoochum','Elekid','Magby','Miltank','Blissey','Treecko','Grovyle','Sceptile','Torchic','Combusken','Blaziken','Mudkip','Marshtomp','Swampert','Poochyena','Mightyena','Zigzagoon','Linoone','Wurmple','Silcoon','Beautifly','Cascoon','Dustox','Lotad','Lombre','Ludicolo','Seedot','Nuzleaf','Shiftry','Taillow','Swellow','Wingull','Pelipper','Ralts','Kirlia','Gardevoir','Surskit','Masquerain','Shroomish','Breloom','Slakoth','Vigoroth','Slaking','Nincada','Ninjask','Shedinja','Whismur','Loudred','Exploud','Makuhita','Hariyama','Azurill','Nosepass','Skitty','Delcatty','Sableye','Mawile','Aron','Lairon','Aggron','Meditite','Medicham','Electrike','Manectric','Plusle','Minun','Volbeat','Illumise','Roselia','Gulpin','Swalot','Carvanha','Sharpedo','Wailmer','Wailord','Numel','Camerupt','Torkoal','Spoink','Grumpig','Spinda','Trapinch','Vibrava','Flygon','Cacnea','Cacturne','Swablu','Altaria','Zangoose','Seviper','Lunatone','Solrock','Barboach','Whiscash','Corphish','Crawdaunt','Baltoy','Claydol','Lileep','Cradily','Anorith','Armaldo','Feebas','Milotic','Castform','Kecleon','Shuppet','Banette','Duskull','Dusclops','Tropius','Chimecho','Absol','Wynaut','Snorunt','Glalie','Spheal','Sealeo','Walrein','Clamperl','Huntail','Gorebyss','Relicanth','Luvdisc','Turtwig','Grotle','Torterra','Chimchar','Monferno','Infernape','Piplup','Prinplup','Empoleon','Starly','Staravia','Staraptor','Bidoof','Bibarel','Kricketot','Kricketune','Shinx','Luxio','Luxray','Budew','Roserade','Cranidos','Rampardos','Shieldon','Bastiodon','Burmy','Wormadam','Mothim','Combee','Vespiquen','Pachirisu','Buizel','Floatzel','Cherubi','Cherrim','Shellos','Gastrodon','Ambipom','Drifloon','Drifblim','Buneary','Lopunny','Mismagius','Honchkrow','Glameow','Purugly','Chingling','Stunky','Skuntank','Bronzor','Bronzong','Bonsly','Mime Jr.','Happiny','Chatot','Spiritomb','Gible','Gabite','Garchomp','Munchlax','Riolu','Lucario','Hippopotas','Hippowdon','Skorupi','Drapion','Croagunk','Toxicroak','Carnivine','Finneon','Lumineon','Mantyke','Snover','Abomasnow','Weavile','Magnezone','Lickilicky','Rhyperior','Tangrowth','Electivire','Magmortar','Togekiss','Yanmega','Leafeon','Glaceon','Gliscor','Mamoswine','Porygon-Z','Gallade','Probopass','Dusknoir','Froslass','Snivy','Servine','Serperior','Tepig','Pignite','Emboar','Oshawott','Dewott','Samurott','Patrat','Watchog','Lillipup','Herdier','Stoutland','Purrloin','Liepard','Pansage','Simisage','Pansear','Simisear','Panpour','Simipour','Munna','Musharna','Pidove','Tranquill','Unfezant','Blitzle','Zebstrika','Roggenrola','Boldore','Gigalith','Woobat','Swoobat','Drilbur','Excadrill','Audino','Timburr','Gurdurr','Conkeldurr','Tympole','Palpitoad','Seismitoad','Throh','Sawk','Sewaddle','Swadloon','Leavanny','Venipede','Whirlipede','Scolipede','Cottonee','Whimsicott','Petilil','Lilligant','Basculin','Sandile','Krokorok','Krookodile','Darumaka','Darmanitan','Maractus','Dwebble','Crustle','Scraggy','Scrafty','Sigilyph','Yamask','Cofagrigus','Tirtouga','Carracosta','Archen','Archeops','Trubbish','Garbodor','Zorua','Zoroark','Minccino','Cinccino','Gothita','Gothorita','Gothitelle','Solosis','Duosion','Reuniclus','Ducklett','Swanna','Vanillite','Vanillish','Vanilluxe','Deerling','Sawsbuck','Emolga','Karrablast','Escavalier','Foongus','Amoonguss','Frillish','Jellicent','Alomomola','Joltik','Galvantula','Ferroseed','Ferrothorn','Klink','Klang','Klinklang','Tynamo','Eelektrik','Eelektross','Elgyem','Beheeyem','Litwick','Lampent','Chandelure','Axew','Fraxure','Haxorus','Cubchoo','Beartic','Cryogonal','Shelmet','Accelgor','Stunfisk','Mienfoo','Mienshao','Druddigon','Golett','Golurk','Pawniard','Bisharp','Bouffalant','Rufflet','Braviary','Vullaby','Mandibuzz','Heatmor','Durant','Chespin','Quilladin','Chesnaught','Fennekin','Braixen','Delphox','Froakie','Frogadier','Greninja','Bunnelby','Diggersby','Fletchling','Fletchinder','Talonflame','Scatterbug','Spewpa','Vivillon','Litleo','Pyroar','Flabébé','Floette','Florges','Skiddo','Gogoat','Pancham','Pangoro','Furfrou','Espurr','Meowstic','Honedge','Doublade','Aegislash','Spritzee','Aromatisse','Swirlix','Slurpuff','Inkay','Malamar','Binacle','Barbaracle','Skrelp','Dragalge','Clauncher','Clawitzer','Helioptile','Heliolisk','Tyrunt','Tyrantrum','Amaura','Aurorus','Sylveon','Hawlucha','Dedenne','Carbink','Goomy','Sliggoo','Goodra','Klefki','Phantump','Trevenant','Pumpkaboo','Gourgeist','Bergmite','Avalugg','Noibat','Noivern','Xerneas','Yveltal','Zygarde','Diancie','Hoopa','Volcanion','Rowlet','Dartrix','Decidueye','Litten','Torracat','Incineroar','Popplio','Brionne','Primarina','Pikipek','Trumbeak','Toucannon','Yungoos','Gumshoos','Grubbin','Charjabug','Vikavolt','Crabrawler','Crabominable','Oricorio','Cutiefly','Ribombee','Rockruff','Lycanroc','Wishiwashi','Mareanie','Toxapex','Mudbray','Mudsdale','Dewpider','Araquanid','Fomantis','Lurantis','Morelull','Shiinotic','Salandit','Salazzle','Stufful','Bewear','Bounsweet','Steenee','Tsareena','Comfey','Oranguru','Passimian','Wimpod','Golisopod','Sandygast','Palossand','Pyukumuku','Type: Null','Silvally','Minior','Komala','Turtonator','Togedemaru','Mimikyu','Bruxish','Drampa','Dhelmise','Jangmo-o','Hakamo-o','Kommo-o']

LegendList = ['Tapu Koko','Tapu Lele','Tapu Bulu','Tapu Fini','Cosmog','Cosmoem','Solgaleo','Lunala','Nihilego','Buzzwole','Pheromosa','Xurkitree','Celesteela','Kartana','Guzzlord','Necrozma','Magearna','Marshadow','Poipole','Naganadel','Stakataka','Blacephalon','Zeraora','Deino','Zweilous','Hydreigon','Larvesta','Volcarona','Cobalion','Terrakion','Virizion','Tornadus','Thundurus','Reshiram','Zekrom','Landorus','Kyurem','Keldeo','Meloetta','Genesect','Aerodactyl','Snorlax','Articuno','Zapdos','Moltres','Dratini','Dragonair','Dragonite','Mewtwo','Mew','Raikou','Entei','Suicune','Larvitar','Pupitar','Tyranitar','Lugia','Ho-Oh','Celebi','Rotom','Uxie','Mesprit','Azelf','Dialga','Palkia','Heatran','Regigigas','Giratina','Cresselia','Phione','Manaphy','Darkrai','Shaymin','Arceus','Victini','Bagon','Shelgon','Salamence','Beldum','Metang','Metagross','Regirock','Regice','Registeel','Latias','Latios','Kyogre','Groudon','Rayquaza','Jirachi','Deoxys']

natlist = ['Lonely', 'Brave', 'Adamant', 'Naughty', 'Bold', 'Relaxed', 'Impish', 'Lax', 'Timid', 'Hasty', 'Jolly', 'Naive', 'Modest', 'Mild', 'Quiet', 'Rash', 'Calm', 'Gentle', 'Sassy', 'Careful', 'Bashful', 'Quirky', 'Serious', 'Docile', 'Hardy']
emotes = ['<a:mewLoooop:446252694026321922>', '<a:sylveon:463817633578483723>', '<:sylveon:463817633578483723>', '<a:jirachigif:499179583531253760>', '<a:smewsleep:448075686100598784>']
logging.basicConfig(level="INFO")

bot = commands.Bot(command_prefix=";")
version = ("0.0.5c Beta Build")

TOKEN = os.environ['TOKEN']
dburl = os.environ['DATABASE_URL']
dbltoken = os.environ['dbltoken']

bot.remove_command('help')
#db connect
        
@bot.listen()
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(version)
    print('-------------')
@bot.command()
async def wipe(ctx, user:discord.Member):
        if not ctx.author.id == 358293206900670467:
                await ctx.send("Not dylee :interrobang:")
                return
        pconn = await bot.db.acquire()
        await pconn.execute("DELETE FROM pokes WHERE ownerid = $1", user.id)
        await pconn.execute("DELETE FROM users WHERE u_id = $1", user.id)
        await ctx.send("Wiped")
        await bot.db.release(pconn)
@bot.listen()
async def on_ready():
    if not hasattr(bot, 'db'):
        bot.db = await asyncpg.create_pool(dburl, min_size=1, max_size=500)
@bot.command()
async def load(ctx, extension_name : str):
    if not ctx.author.id == 358293206900670467:
        return
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} loaded.".format(extension_name))     

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def mew(ctx):
    """Makes MewBot respond"""
    await ctx.send("Ping, latency: {}ms".format(int(bot.latency * 1000)))

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def dping(ctx):
    """This contains more details about the bots condition"""
    # Time the time required to send a message first.
    # This is the time taken for the message to be sent, awaited, and then
    # for discord to send an ACK TCP header back to you to say it has been
    # received; this is dependant on your bot's load (the event loop latency)
    # and generally how shit your computer is, as well as how badly discord
    # is behaving.
    start = time.monotonic()
    msg = await ctx.send('Pinging...')
    millis = (time.monotonic() - start) * 1000

    # Since sharded bots will have more than one latency, this will average them if needed.
    heartbeat = ctx.bot.latency * 1000

    await msg.edit(content=f'Heartbeat: {heartbeat:,.2f}ms\tACK: {millis:,.2f}ms.')

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def ping(ctx):
    start = time.monotonic()
    embed = discord.Embed(title="Pong!")
    embed.add_field(name="latency", value="{} ms".format(int(ctx.bot.latency*1000)))
    await ctx.send(embed=embed)

@bot.command(aliases=["Trainer"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def trainer(ctx, user: discord.Member=None):
    tconn = await bot.db.acquire()
    if user is None:
        user = ctx.author
    rquery = '''SELECT redeems FROM users WHERE u_id = {}'''.format(user.id)
    tquery = '''SELECT tnick FROM users WHERE u_id = {}'''.format(user.id)
    uquery = '''SELECT upvotepoints FROM users WHERE u_id = {}'''.format(user.id)
    cquery = '''SELECT pokname FROM pokes WHERE selected = 1 AND ownerid = {}'''.format(user.id)
    mquery = '''SELECT mewcoins FROM users WHERE u_id = {}'''.format(user.id)
    poke = await tconn.fetchval(cquery)
    if poke is None:
        poke = 'None'
    redeems = await tconn.fetchval(rquery)
    if redeems is None:
        await ctx.send("You haven't started Playing!")
        await bot.db.release(pconn)
        return
    tnick = await tconn.fetchval(tquery)
    uppoints = await tconn.fetchval(uquery)
    mewcoins = await tconn.fetchval(mquery)
    plev = await tconn.fetchval('SELECT pokelevel FROM pokes WHERE selected = 1 AND ownerid = $1', user.id)
    embed = discord.Embed(title=f"{user.name} Trainer Card", color=0xffb6c1)
    embed.add_field(name="Redeems", value=f'{redeems}')
    embed.add_field(name="Trainer Nick", value=f'{tnick}')
    embed.add_field(name="Upvote Points", value=f'{uppoints}')
    embed.add_field(name="Currently Selected Pokemon", value=f'{poke.capitalize()} Level {plev}')
    embed.add_field(name="Credits", value=f'{mewcoins}ℳ')
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
    await bot.db.release(tconn)
   
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def nick(ctx, *, val):
    pconn = await bot.db.acquire()
    await pconn.execute("UPDATE users SET tnick = $1 WHERE u_id = $2", val, ctx.author.id)
    await ctx.send("Successfully Changed Trainer Nick")
    await bot.db.release(pconn)
    
    
########################################################################################################33
@bot.command(aliases=["Team"])
async def team(ctx):
    pconn = await bot.db.acquire()
    embed =  discord.Embed(title="Your Current Team!", color=0xeee647)

    for num in range(1,7):
        t_num  = await pconn.fetchval(f"SELECT pokname FROM pokes WHERE team{num} = 1 AND ownerid = $1", ctx.author.id)
        if t_num is None:
            t_num = 'None'
        embed.add_field(name=f"Slot {num} Pokemon", value=f"{t_num}")
    embed.set_footer(text="Your Current Pokemon Team | use ;teamadd <slot_number> to add a selected Pokemon")
    await bot.db.release(pconn)
    await ctx.send(embed=embed)
@bot.command(aliases=["Teamadd"])
async def teamadd(ctx, slot:int):
    if slot > 6:
        await ctx.send("You can not add More than 6 Pokemon to a Team")
        return
    pconn = await bot.db.acquire()
    pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 and selected = 1", ctx.author.id)
    if pokename is None:
        await ctx.send("You have no Pokemon selected")
        await bot.db.release(pconn)
        return
    await pconn.execute(f"UPDATE pokes SET team{slot} = 1 WHERE selected = 1 and ownerid = $1", ctx.author.id)
    await ctx.send(f"Your {pokename} is now on your team, Slot number {slot}")
    await bot.db.release(pconn)
    
@bot.command(aliases=["Teamremove", "Tr", "TR", "tr"])
async def teamremove(ctx, slot:int):
    pconn = await bot.db.acquire()
    pokename = await pconn.fetchval(f"SELECT pokname FROM pokes WHERE team{slot} = 1 AND ownerid  = $1", ctx.author.id)
    if pokename is None:
        await ctx.send("There is no Pokemon in that Team Slot")
        await bot.db.release(pconn)
        return
    await pconn.execute(f"UPDATE pokes SET team{slot} = 0 WHERE team{slot} = 1 AND ownerid = $1", ctx.author.id)
    await ctx.send(f"You have sucessfully removed {pokename} from Pokemon Number {slot} In your team!")
    await bot.db.release(pconn)
    
############################################################################################################            
@bot.command(aliases=["Help"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def help(ctx, val=None):
    if val is None:
        embed = discord.Embed(title="MewBot commands", description="The pokemon discord bot made for you!!!", color=0xeee657)
        embed.add_field(name="Ping", value="Pings the bot and shows it's latency", inline=False)
        embed.add_field(name="Pokemon", value="See all Pokemon Commands with `;help pokemon`")
        embed.add_field(name="Mega", value="`;help mega` to see information on Mega Evolution!!", inline=False)
        embed.add_field(name="Forms", value="`;help forms` to see information on Forms!!", inline=False)
        embed.add_field(name="Team", value="`;help team` for help with Teams!", Inline=False)
        embed.add_field(name="Trading", value="`;help trading` to see Trading Commands", inline=False)
        embed.add_field(name="Donate", value="Donate to the bot! 1 USD = 2 Redeems + 50,000ℳ", inline=False)
        embed.add_field(name="Vote", value="Upvote the Bot for Rewards!, 10 Upvote Points = 5 Redeems!", inline=False)
        embed.add_field(name="Botinfo", value="User count, server count, CPU and Memory Status and More!", inline=False)
        embed.set_thumbnail(url='http://pm1.narvii.com/5848/b18cd35647528a7bdffc8e4b8e4d6a1465fc5253_00.jpg')
        await ctx.send(embed=embed)
    elif val == 'trading':
        e = discord.Embed(title="Trading Tutorial", color=0xeee657)
        e.add_field(name="`;trade`", value="`;trade @User <credits_amount> <their_pokemon_number>`")
        e.add_field(name="`;gift` to give someone credits", value="`;gift @User <credit_amount>`")
        e.add_field(name="`;give` to give someone a Pokemon", value="`;give @User <your_pokemon_number>`")
        e.add_field(name="`;giveredeem` to give someone redeems!", value="`;giveredeem @User <number_of_redeems>`")
        await ctx.send(embed=e)
    elif val == 'mega':
        e = discord.Embed(title="Mega Tutorial", color=0xeee657)
        e.add_field(name="`;mega evolve`", value="Mega You Selected Pokemon")
        e.add_field(name="`;mega evolve x`", value="Mega evolve your Selected Pokemon to X form")
        e.add_field(name="`mega evolve y`", value="Mega evolve your Selected Pokemon to Y form")
        await ctx.send(embed=e)
    elif val == 'forms':
        e = discord.Embed(title="Form Tutorial", color=0xeee657)
        e.add_field(name="`;form <form_name>`", value="Transform Your Selected Pokemon to it's form!")
        e.add_field(name="`;solarize <solgaleo_number`", value="Solarize your Necrozma to Necrozma-dusk form")
        e.add_field(name="`;lunarize <lunala_number>`", value="Lunarize your Necrozma to Necrozma-dawn form")
        await ctx.send(embed=e)
    elif val == 'trainer':
        e = discord.Embed(title="Trainer card help", color=0xeee657)
        e.add_field(name="`;nick <nickname>`", value="To change your Trainer Nickname")
        await ctx.send(embed=e)
    elif val == 'pokemon':
        embed = discord.Embed(title="Pokemon Commands", color = 0xeee657)
        embed.add_field(name="Trainer", value="Displays your Trainer Card and other information", inline=False)
        embed.add_field(name="Start", value="Start Playing Mewbot!!", inline=False)
        embed.add_field(name="Trade", value="Trade Items, Redeems, Pokemon, and Credits!", inline=False)
        embed.add_field(name="Shop", value="Buy TMs, Held Items, Evolution Items & More!", inline=False)
        embed.add_field(name="Buy", value="`;buy <item_name>` to buy an item", inline=False)
        embed.add_field(name="Reward", value="Get Upvote Rewards! NOTE: Only Use this command WHEN you have Upvoted!", inline=False)
        embed.add_field(name="Upvote", value="Upvote the Bot for rewards!!", inline=False)
        embed.add_field(name="Moves", value="See your current move count!", inline=False)
        embed.add_field(name="Learn", value="Learn a Move! `;learn <move-name> <slot_number>", inline=False)
        embed.add_field(name="Tms", value="Get the entire moveset of your pokemon!", inline=False)
        embed.add_field(name="Pokemon", value="View your Pokemon List!", inline=False)
        embed.add_field(name="Select", value="Select a Pokemon!", inline=False)
        embed.add_field(name="Mega", value="`;help mega` to see information on Mega Evolution!!", inline=False)
        embed.add_field(name="Forms", value="`;help forms` to see information on Forms!!", inline=False)
        await ctx.send(embed=e)
    elif val == 'team':
        embed = discord.Embed(title="Team Commands", color = 0xeee657)
        embed.add_field(name="Team", value="`;team` displays your current team")
        embed.add_field(name="Teamadd <slot_number>", value="Add Your __selected__ Pokemon to your team")
        embed.add_field(name="Teamremove <slot_number>", value="Remove a Pokemon from that slot")
        await ctx.send(embed=e)

@bot.command(aliases=["Shop"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def shop(ctx, val=None):
    if not val is None:
        val = val.lower()
    if val is None:
        e = discord.Embed(title="Items you can buy in the Shop!", description="`;shop <shop_name>`", color=0xffb6c1)
        e.add_field(name="Forms", value="Want to Make your Kyogre or Groudon Primal or Deoxys/Arceus Formes")
        e.add_field(name="Mega", value="Buy The Mega Stone to Mega your Pokemon and say `;mega evolve`!")
        e.add_field(name="Items", value="Buy Rare candies, Items to Boost Pokemnon Abilities such as Zinc e.t.c")
        e.add_field(name="Held items", value="Buy Held Items for your Pokemon!")
        e.add_field(name="buy", value="`;buy <item_name>` to buy an item")
        e.set_footer(text="Please Be patient, the shop is currently being worked on")
        await ctx.send(embed=e)
    elif val == 'forms':
        e = discord.Embed(title="Buy Items to change your pokemon Forms!!", color=0xffb6c1)
        e.add_field(name="Blue orb", value="Buy the Blue Orb to make your Kyogre Primal! | 10,000ℳ")
        e.add_field(name="Red orb", value="Buy the Red Orb to make your Groudon Primal! | 10,000ℳ")
        e.add_field(name="Meteorite", value="Have your Deoxys Interact with it to Get the Forms! | 10,500ℳ")
        e.add_field(name="N-Solarizer", value="Buy the N-Solarizer to Fuse your Necrozma and a Solgaleo to Get Necrozma Dusk Forme! | 9,500ℳ")
        e.add_field(name="N-Lunarizer", value="Buy the N-Lunarizer to Fuse your Necrozma and a Lunala to get Necrozma Dawn Forme! | 9,500ℳ")
        e.add_field(name="Arceus Plates", value="Need Arceus Plates to Transform it?, just say `;shop plates`")
        e.add_field(name="Light Stone", value="Buy this to Fuse your Kyurem with Reshiram for Kyurem-white! | 9,500ℳ")
        e.add_field(name="Dark Stone", value="Buy this to Fuse your Kyurem with Zekrom for Kyurem-black | 9,500ℳ")
        e.add_field(name="Reveal Glass", value="Buy this to Change the forms of the weather trio! | 10,500ℳ")
        e.add_field(name="Zygarde cell", value="Get Zygarde-complete by Buying 10 Zygarde Cells! | 15,000 ℳ")
        e.add_field(name="Gracidea flower", value="Buy the Gracidea flower to Evolve your Shaymin to Shaymin-sky! | 7,500ℳ")
        e.add_field(name="Griseous Orb", value="Buy the Griseous orb to evolve Giratina to it's Origin Forme! | 10,000ℳ")
        e.set_footer(text="Please Be patient, the shop is currently being worked on")
        await ctx.send(embed=e)
    elif val == 'plates':
        e = discord.Embed(title="Arceus Plates!", description="say `;buy <plate_name>` to buy it", color=0xffb6c1)
        e.add_field(name="Draco Plate", value="Changes Arceus and Judgement to the dragon type")
        e.add_field(name="Dread Plate", value="Changes Arceus and Judgement to the dark type")
        e.add_field(name="Earth Plate", value="Changes Arceus and Judgement to the earth type")
        e.add_field(name="Fist Plate", value="Changes Arceus and Judgement to the fighting type")
        e.add_field(name="Flame Plate", value="Changes Arceus and Judgement to the fire type")
        e.add_field(name="Icicle Plate", value="Changes Arceus and Judgement to the ice type")
        e.add_field(name="Insect Plate", value="Changes Arceus and Judgement to the bug type")
        e.add_field(name="Iron Plate", value="Changes Arceus and Judgement to the steel type")
        e.add_field(name="Meadow Plate", value="Changes Arceus and Judgement to the grass type")
        e.add_field(name="Mind Plate", value="Changes Arceus and Judgement to the psychic type")
        e.add_field(name="Pixie Plate", value="Changes Arceus and Judgement to the fairy type")
        e.add_field(name="Sky Plate", value="Changes Arceus and Judgement to the flying type")
        e.add_field(name="Splash Plate", value="Changes Arceus and Judgement to the water type")
        e.add_field(name="Spooky Plate", value="Changes Arceus and Judgement to the ghost type")
        e.add_field(name="Stone Plate", value="Changes Arceus and Judgement to the rock type")
        e.add_field(name="Toxic Plate", value="Changes Arceus and Judgement to the poison type")
        e.add_field(name="Zap Plate", value="Changes Arceus and Judgement to the electric type")
        e.set_footer(text="Please Be patient, the shop is currently being worked on")
        await ctx.send(embed=e)
    elif val == 'mega':
        e = discord.Embed(title="Mega Stones!", description="say `;buy <mega_stone>` to buy it", color=0xffb6c1)
        e.add_field(name="Buy Mega Stones", value="To evolve your Pokemon to It's Mega Form")
        e.add_field(name="Choose Between\nMega Stone\n Mega X stone\nMega Y stone", value="To Mega your selected Pokemon")
        await ctx.send(embed=e)

@bot.command(aliases=["Buy"])
async def buy(ctx, *, item):
    if ' ' in item:
        item = item.replace(' ', '-')
    item = item.lower()
    with open("shop.json") as f:
        items = json.load(f)
    price = [t['price'] for t in items if t['item'] == item]
    price = price[0]
    if price is None:
        await ctx.send("That Item is not in the market")
        return
    pconn = await bot.db.acquire()
    pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 AND selected = 1", ctx.author.id)
    current_creds = await pconn.fetchval("SELECT mewcoins FROM users WHERE u_id = $1", ctx.author.id)
    if current_creds < price:
        await ctx.send(f"You don't have {price}ℳ")
        await bot.db.release(pconn)
        return
    await pconn.execute("UPDATE pokes SET hitem = $1 WHERE selected = 1 and ownerid = $2", item, ctx.author.id)
    ncreds = current_creds - price
    await pconn.execute("UPDATE users SET mewcoins = $1 WHERE u_id = $2", ncreds, ctx.author.id)
    await ctx.send(f"You have successfully bought the {item} for your {pokename}")
    await bot.db.release(pconn)
@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def botinfo(ctx):
    embed = discord.Embed(title="MewBot information", description="Bot information", color=0xeee657)

    # give info about you here
    embed.add_field(name="Dylee#6669", value="Developer", inline=False)

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    embed.add_field(name="User Count", value=f"{len(bot.users)}")

    embed.add_field(name="Discord Version", value=discord.__version__)
    mem = psutil.virtual_memory()
    cmem = (mem.available/10000000000)

    embed.add_field(name="CPU Statistics", value=f"\nCPU Count **{psutil.cpu_count()}**\nRAM **{cmem} GB**")
    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite Me](https://discordapp.com/api/oauth2/authorize?client_id=493045795445276682&permissions=388160&scope=bot)")

    await ctx.send(embed=embed)

@bot.command(aliases=["Donate"])
async def donate(ctx):
    e = discord.Embed(title="Want to Donate to the Bot?", color=0xffb6c1)
    e.add_field(name="DM Dylee#6669 or Join the Official Server Here!", value="[Here!](https://invite.gg/pokeglobe)")
    await ctx.send(embed=e)
    embed = discord.Embed(title="Donation Perks")
    embed.add_field(name="Every Dollar Donated = 2 Redeems", value="510 EV Points to Add to a Pokemon")
    embed.add_field(name="Every Dollar Donated = 50,000ℳCredits", value="Donator Rank in the PokeGlobe Server")
    embed.add_field(name="100 Redeems", value="Gives You a Perfect Pokemon")
    await ctx.author.send(embed=embed)
@bot.command(aliases=["Invite"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def invite(ctx):
    embed = discord.Embed(title="Invite Me", description="The invite link for MewBot", color=0xffb6c1)

    #invite link
    embed.add_field(name="Invite", value="[Invite MewBot](https://discordapp.com/api/oauth2/authorize?client_id=493045795445276682&permissions=388160&scope=bot)")
    embed.add_field(name="User Count", value=f"{len(bot.users)}")
    await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def status(ctx):
    embed = discord.Embed(title="Bot development Status", description="information on the development of MewBot", color=0xffb6c1)

    #list

    embed.add_field(name="Current Build version", value="0.0.5c Beta Build")

    embed.add_field(name="Bot Logging", value=":white_check_mark: Complete")

    embed.add_field(name="Addition of Simple Commands", value=":white_check_mark:")
    embed.add_field(name="Registering", value=":white_check_mark:")
    embed.add_field(name="EVs, IVs, and Stats", value=":white_check_mark:")
    embed.add_field(name="Held Items", value=":white_check_mark:")
    embed.add_field(name="Pokemon forms", value=":white_check_mark:")
    embed.add_field(name="Trainer information", value=":white_check_mark:")
    embed.add_field(name="Battles", value="In Progress")

    #sends command

    await ctx.author.send(embed=embed)

#hpiv = random.randint(1, 31)
#atkiv = random.randint(1, 31)
#defiv = random.randint(1, 31)
#spaiv = random.randint(1, 31)
#spdiv = random.randint(1, 31)
#speiv = random.randint(1, 31)
#plevel = random.randint(1, 100)
@bot.listen()
async def on_message(message):
    if message.guild and message.guild.id == 264445053596991498:
        return
    chance = random.randint(1, 30)
    if not chance is 2:
        return
    else:
        channel = message.channel
        spawnchance = random.randint(1, 12000)
        if spawnchance == 1:
            val1 = random.choice(LegendList)
        else:
            val1 =  random.choice(pList)
        val = val1.lower()
        url = "https://img.pokemondb.net/artwork/vector/large/" + val + ".png"
        embed = discord.Embed(title="A Pokemon Has Spawned, Say it's name to catch it!", color=0xffb6c1)
        embed.set_image(url=url)
        try:
            await message.channel.send(embed=embed)
        except Exception as e:
            print("Error in sending embed")
            return
        def check(m):
            return m.content.lower() == val and m.channel == channel
        msg = await bot.wait_for('message', check=check)
        val = val.capitalize()


        #db code starts here


        pconn = await bot.db.acquire()
        hpiv = random.randint(1, 31)
        atkiv = random.randint(1, 31)
        defiv = random.randint(1, 31)
        spaiv = random.randint(1, 31)
        spdiv = random.randint(1, 31)
        speiv = random.randint(1, 31)
        plevel = random.randint(1, 100)
        nature = random.choice(natlist)
        expc = (plevel ** 3)
        pque = '''SELECT MAX(pnum)+1 FROM pokes WHERE ownerid = {}'''.format(msg.author.id)
        pnum = await pconn.fetchval(pque)
        try:
            pnum + 1
        except TypeError as e:
            await message.channel.send("You need to Start with `;start`")
            await bot.db.release(pconn)
            return
        query2 = '''
        INSERT INTO pokes (pokname, hpiv, atkiv, defiv, spatkiv, spdefiv, speediv, hpev, atkev, defev, spatkev, spdefev, speedev, pokelevel, ownerid, pnum, selected, move1, move2, move3, move4, poknick, exp, nature, expcap)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, $25)
        '''

        args = (val, hpiv, atkiv, defiv, spaiv, spdiv, speiv, 0, 0, 0, 0, 0, 0, plevel, msg.author.id, pnum, 0, 'tackle', 'tackle', 'tackle', 'tackle', 'None', 1, nature, expc)
        try:
            await pconn.execute(query2, *args)
        except asyncpg.exceptions.NotNullViolationError as e:
            await channel.send("You need to Register with `;start` first")
            await bot.db.release(pconn)
            return
        await channel.send(f'Congratulations <@{msg.author.id}>, you have successfully caught a {val}!')
        await bot.process_commands(message)
        logging.info("Success")
        await bot.db.release(pconn)
    #   db code goes here

# None Pokemon Commands  ctx
# this will only be a shell, like a plan

react_to_starter = {
    "\N{LEAF FLUTTERING IN WIND}": "Flowing",
    "\N{FIRE}": "Flire",
    "\N{DROPLET}": "Aquino" 
    # do this thing for the three starters and their emoji
}
@bot.command(name="start")
@commands.cooldown(1, 3, commands.BucketType.user)
async def start_journey(ctx):
    embed = discord.Embed(title="Select a Starter!", description="Choose any of the Starters!", color=0xffb6c1)
    embed.add_field(name="...", value="You've been hypnotized by Mew, and instead of the normal starters, you are forced to pick between \n-Flowin, the Grass type fakemon, \n-Flire the fire type fakemon and \n-Aquino, the water type.")
    embed.set_thumbnail(url="https://nerdist.com/wp-content/uploads/2016/02/Screen-Shot-2016-02-02-at-12.05.40-PM-615x346.png")
    embed.set_image(url="https://pm1.narvii.com/6252/3746bb43045886ce9ec8498a6f7d96f520ed6341_hq.jpg") # you cannot set two images. either put one as a thumbnail or remove it
    embed.add_field(name="__React__ to Pick a Starter!", value="...")
    start_msg = await ctx.send(embed=embed)
    for r in react_to_starter:
        await start_msg.add_reaction(r)
    def check(r, u):
        mcheck =( r.message.id == start_msg.id)
        rcheck = (r.emoji in react_to_starter)
        ucheck = (u == ctx.author)
        return mcheck and rcheck and ucheck
    try:
        reaction, user = await bot.wait_for("reaction_add", check=check, timeout=1234) # some timeout in seconds
    except asyncio.TimeoutError:
        await ctx.send('You took too long!', delete_after=15)
        return
        await ctx.send(f"You have selected {react_to_starter[reaction.emoji]} as your starter!")
        await ctx.send(react_to_starter[reaction.emoji])
    def pred(m):
        return m.author == message.author and m.channel == message.channel
    answer1 = (react_to_starter[reaction.emoji])
    values = ["Flowing", "Flire", "Aquino"]
    if (answer1) in values:
        pconn = await bot.db.acquire()
        hpiv = random.randint(1, 31)
        atkiv = random.randint(1, 31)
        defiv = random.randint(1, 31)
        spaiv = random.randint(1, 31)
        spdiv = random.randint(1, 31)
        speiv = random.randint(1, 31)
        nature = random.choice(natlist)
        tackle = 'tackle'
        msg = await ctx.channel.send("Creating Database")
        await msg.edit(content="Registration Complete!!")

        query2 = '''
        INSERT INTO pokes (pokname, hpiv, atkiv, defiv, spatkiv, spdefiv, speediv, hpev, atkev, defev, spatkev, spdefev, speedev, pokelevel, ownerid, pnum, selected, move1, move2, move3, move4, hitem, exp, nature, expcap, poknick)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, $25, $26)'''

        args = (answer1, hpiv, atkiv, defiv, spaiv, spdiv, speiv, 0, 0, 0, 0, 0, 0, 5, ctx.author.id, 1, 0, tackle, tackle, tackle, tackle, 'None', 1, nature, 35, 'None')
        pk1 = await pconn.fetch("SELECT u_id FROM users WHERE u_id = {}".format(ctx.author.id))
        nrecord = [record['u_id'] for record in pk1]
        if ctx.author.id in nrecord:
            await ctx.send('you have already registered')
            await bot.db.release(pconn)
            return
        else:
            await pconn.execute(query2, *args)
            query3 = '''
            INSERT INTO users (u_id, redeems, evpoints, tnick, upvotepoints, mewcoins)
            VALUES ($1, $2, $3, $4, $5, $6)
            '''

            args2 = (ctx.author.id, 0, 0, 'None', 0, 0)
            await pconn.execute(query3, *args2)
            await ctx.channel.send("Records successfully Added\nGoodluck!")
            await ctx.author.send("Thank you for registering! Need an Easy way to get redeems? 10 Upvote Points = 5 Redeems!, Upvote Mewbot here!\nhttps://discordbots.org/bot/493045795445276682\nAnother way is If you're an Owner or Know an Owner of a 50+ Member server, you get 10 Redeems By Inviting")
            emoji = random.choice(emotes)
            await ctx.send(emoji)
            logging.info("All went well")
            await bot.db.release(pconn)
            



@bot.command(aliases=["Pokemon"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def pokemon(ctx, val1=None):
    if val1 == 1:
        val = 1
        snum = 11
        
    elif val1 is None:
        val = 10
        snum = 0
        
    else:
        val = int(val1)
        val = (val*10)
        snum = val-10
        
    pconn = await bot.db.acquire()
    nquery = f"SELECT pokname, pnum FROM pokes WHERE ownerid = {ctx.author.id} ORDER BY pnum"
    pk1 = await pconn.fetch(nquery)
    nrecord = [record['pokname'] for record in pk1]
    precord = [record['pnum'] for record in pk1]
    embed = discord.Embed(title='Your Pokemon List', color=0xffb6c1)
    for pn in precord[snum:val]:
        try:
            nr = nrecord[pn-1]
        except IndexError as e:
            await ctx.send("You do not have that much pokemon son")
            await bot.db.release(pconn)
            return
        embed.add_field(name=f'{nr.capitalize()}', value=f'{pn}', inline=True)
    embed.set_footer(text=f"Upvote the Bot!! Open the next page with ;pokemon <page_number> | This is page {val1}")
    await ctx.send(embed=embed)
    await bot.db.release(pconn)
    
@bot.command(aliases=["Moves"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def moves(ctx):
    pconn = await bot.db.acquire()
    pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE selected = 1 AND ownerid = $1", ctx.author.id)
    m1 = await pconn.fetchval("SELECT move1 FROM pokes WHERE selected = 1 AND ownerid = $1", ctx.author.id)
    m2 = await pconn.fetchval("SELECT move2 FROM pokes WHERE selected = 1 AND ownerid = $1", ctx.author.id)
    m3 = await pconn.fetchval("SELECT move3 FROM pokes WHERE selected = 1 AND ownerid = $1", ctx.author.id)
    m4 = await pconn.fetchval("SELECT move4 FROM pokes WHERE selected = 1 AND ownerid = $1", ctx.author.id)
    embed = discord.Embed(title='Moves', color=0xffb6c1)
    embed.add_field(name='**Move 1**:', value=f'{m1.capitalize()}')
    embed.add_field(name='**Move 2**:', value=f'{m2.capitalize()}')

    embed.add_field(name='**Move 3**:', value=f'{m3.capitalize()}')

    embed.add_field(name='**Move 4**:', value=f'{m4.capitalize()}')
    await ctx.send(embed=embed)
    await bot.db.release(pconn)
    
@bot.command(aliases=["Tms"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def tms(ctx, val: int=None):
    if val is 2:
        val = int(val)
        val = 25
        snum = 25*2
    elif val is None:
        val = 1
        val = int(val)
        val = val*25
        snum = val-25
    else:
        val = int(val)
        val = val*25
        snum = val-25
    
    pconn = await bot.db.acquire()
    pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id))
    if pokename is None:
        await ctx.send("You have not selected a Pokemon")
    if '-' in pokename:
        pokename = pokename.replace('-', ' ')
        pokename = pokename.split()
        pokename = pokename[0]
    
    with open('forms.json') as f:
        forms = json.load(f)
    pokename = pokename.lower()
    if pokename == 'deoxys':
        p_name = 'deoxys-normal'
    if pokename == 'flire':
        p_name = 'arcanine'
    if pokename == 'flowing':
        p_name = 'sceptile'
    if pokename == 'aquino':
        p_name = 'gyarados'
    if pokename == 'xerneas':
        p_name = 'xerneas-active'
    if pokename == 'arceus':
        p_name = 'arceus-normal'
    if pokename == 'shaymin':
        p_name = 'shaymin-land'
    if pokename == 'keldeo':
        p_name = 'keldeo-ordinary'
    if pokename == 'giratina':
        p_name = 'giratina-altered'
    if pokename == 'meloetta':
        p_name = 'meloetta-aria'
    else:
        p_name = pokename
    pkid = [i['pokemon_id'] for i in forms if i['identifier'] == p_name]
    for p_id in pkid:
        p_id = str(p_id)
        r = requests.get('https://pokeapi.co/api/v2/pokemon/'+p_id+'/')
    r = r.json()
    move = [m['move']['name'] for m in r['moves']]
    moves = len(move)
    e = discord.Embed(title="Learnable Move List", color=0xffb6c1)
    for move in move[snum:val]:
        move = move.capitalize()
        if '-' in move:
            move = move.replace('-', ' ')
        e.add_field(name=f"{move}", value=f";learn <move>")
    e.set_footer(text=f"Showing {val} of {moves} Moves learnable by {pokename}")
    await ctx.send(embed=e)
    await bot.db.release(pconn)
@bot.command()
async def release(ctx, val: int):
    if not val is None:
        pconn = await bot.db.acquire()
        await pconn.execute("DELETE FROM pokes WHERE pnum = $1 AND ownerid = $2", val, ctx.author.id)
        await ctx.send(f"You have successfully released your Pokemon Number {val}")
        await bot.db.release(pconn)
    else:
        await ctx.send("You dont have that Pokemon")
    
@bot.command(aliases=["Learn"])
async def learn(ctx, val, slot: int):
    pconn = await bot.db.acquire()
    pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE selected = 1 AND ownerid = $1", ctx.author.id)
    if ' ' in pokename:
        pokename = pokename.replace(' ', '-')
    with open('forms.json') as f:
        forms = json.load(f)
    pokename = pokename.lower()
    if pokename == 'deoxys':
        pokename = 'deoxys-normal'
    if pokename == 'flire':
        pokename = 'arcanine'
    if pokename == 'flowing':
        pokename = 'sceptile'
    if pokename == 'aquino':
        pokename = 'gyarados'
    if pokename == 'arceus':
        pokename = 'arceus-normal'
    if pokename == 'shaymin':
        pokename = 'shaymin-land'
    if pokename == 'keldeo':
        pokename = 'keldeo-ordinary'
    if pokename == 'giratina':
        pokename = 'giratina-altered'
    if pokename == 'meloetta':
        pokename = 'meloetta-aria'
    
    pkid = [i['pokemon_id'] for i in forms if i['identifier'] == pokename]
    for p_id in pkid:
        p_id = str(p_id)
        r = requests.get('https://pokeapi.co/api/v2/pokemon/'+p_id+'/')
        r = r.json()
    move = [m['move']['name'] for m in r['moves']]
    if not val in move:
        await ctx.send(f"Your {pokename} can not learn that Move")
        await bot.db.release(pconn)
        return
    await pconn.execute(f"UPDATE pokes SET move{slot} = $1 WHERE ownerid = $2 AND selected = 1", val, ctx.author.id)
    await ctx.send(f"You have successfully learnt {val} as your Number {slot} Move")
    await bot.db.release(pconn)
    
    
@bot.command(aliases=["Select"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def select(ctx, val):
    pconn = await bot.db.acquire()
    try:
        val = int(val)
    except ValueError as e:
        await ctx.send("That is not a Valid Pokemon Number!")
        await bot.db.release(pconn)
        return
    maxnum = await pconn.fetchval("SELECT MAX(pnum) FROM pokes WHERE ownerid = {}".format(ctx.author.id))
    if maxnum is None:
        await ctx.send("You have not Started!")
        await bot.db.release(pconn)
        return
    if val > maxnum:
        await ctx.send("That Pokemon Does not exist!")
        await bot.db.release(pconn)
        return
    else:
        await pconn.execute("UPDATE pokes SET selected = 0 WHERE selected = 1 AND ownerid = {0}".format(ctx.author.id, val))
        pque = '''UPDATE pokes SET selected = 1 WHERE ownerid = {0} and pnum = {1}'''.format(ctx.author.id, val)
        pnum = await pconn.execute(pque)
        await ctx.send("You have successfully selected your No. {0} Pokemon".format(val))
        emoji = random.choice(emotes)
        await ctx.send(emoji)
        logging.basicConfig(level="INFO")
        await bot.db.release(pconn)

@bot.command(pass_context=True)
async def shutdown(ctx):
    user = ctx.author
    if user.id == 358293206900670467:
        msg = await ctx.send("shutting down...")
        await msg.edit(content="Shutdown Complete, goodbye Dylee!")
        await bot.close()
    elif user.id != 358293206900670467:
        await ctx.send("you are not the fucking owner")
    else:
        return

@bot.command()
async def cp(ctx, *, presence):
    user = ctx.author
    if user.name == "Dylee":
         await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=presence))
         await ctx.send("Status edited to" +  '"' + presence + '"')
    else:
        await ctx.send("You are not the fucking owner!")


@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def inspire(ctx):
    iE = discord.Embed(title="Inspire Me", description="...")
    iE.add_field(name="Here it is", value="you don't understand something unless you know how it works on one level of abstraction lower than you need to know to use it")
    iE.add_field("I hope you try harder! :wave:")
    await ctx.send(embed=iE)

@bot.command(aliases=["Show"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def show(ctx, val=None):
    if val == 'newest':
        pconn = await bot.db.acquire()
        max = await pconn.fetchval("SELECT MAX(pnum) FROM pokes WHERE ownerid = $1", ctx.author.id)
        pquery = "SELECT pokname FROM pokes WHERE pnum = {} AND ownerid = {}".format(max, ctx.author.id)
        atquery = "SELECT atkiv FROM pokes WHERE pnum = {} AND ownerid = {}".format(max, ctx.author.id)
        dequery = "SELECT defiv FROM pokes WHERE pnum = {} AND ownerid = {}".format(max, ctx.author.id)
        spaquery = "SELECT spatkiv FROM pokes WHERE pnum = {} AND ownerid = {}".format(max, ctx.author.id)
        spdquery = "SELECT spdefiv FROM pokes WHERE pnum = {} AND ownerid = {}".format(max, ctx.author.id)
        spequery = "SELECT speediv FROM pokes WHERE pnum = {} AND ownerid = {}".format(max, ctx.author.id)
        plquery = "SELECT pokelevel FROM pokes WHERE pnum = {} AND ownerid = {}".format(max, ctx.author.id)
        pnquery = "SELECT poknick FROM pokes WHERE pnum = {} AND ownerid = {}".format(max, ctx.author.id)
        hiquery = "SELECT hitem FROM pokes WHERE pnum = {} AND ownerid = {}".format(max, ctx.author.id)
        hpquery = "SELECT hpiv FROM pokes WHERE pnum = {} AND ownerid = {}".format(max, ctx.author.id)
        natque = "SELECT nature FROM pokes WHERE pnum = {} AND ownerid = {}".format(max, ctx.author.id)
        expque = "SELECT exp FROM pokes WHERE pnum = {} AND ownerid = {}".format(max, ctx.author.id)
        expcque = "SELECT expcap FROM pokes WHERE pnum = {} AND ownerid = {}".format(max, ctx.author.id)

        nature = await pconn.fetchval(natque)
        if nature is None:
            await ctx.send("That Pokemon Does not exist")
            await bot.db.release(pconn)
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
            iurl = 'https://cdn.discordapp.com/attachments/479175545481986088/497738691381559296/flowin.png'
        elif pn == 'Flire':
            tlist = 'Fire'
            pokemonSpeed = 110
            pokemonAtk = 120
            pokemonDef = 95
            pokemonSpa = 79
            pokemonSpd =99
            pokemonHp = 73
            pAb = 'Scorched feet'
            iurl = 'https://cdn.discordapp.com/attachments/479175545481986088/497733271392878622/flire.png'
        elif pn == 'Aquino':
            tlist = 'Water'
            pokemonSpeed = 95
            pokemonAtk = 79
            pokemonDef = 120
            pokemonSpa = 73
            pokemonSpd = 110
            pokemonHp = 99
            pAb = 'Eternal Rain'
            iurl = 'https://cdn.discordapp.com/attachments/480885918354636804/497721785048104970/aquino.jpg'
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
            if pn is None:
                await ctx.send("You haven't selected a Pokemon Bud")
                await bot.db.release(pconn)
                return
            if '-dawn' in pn:
                iurl = ('https://img.pokemondb.net/artwork/vector/necrozma-dawn-wings.png')
            if 'dusk' in pn:
                iurl = ('https://img.pokemondb.net/artwork/vector/necrozma-dusk-mane.png')
            else:
                iurl = ('https://img.pokemondb.net/artwork/vector/' + pn.lower() + '.png')
            wtrio = ['tornadus', 'landorus', 'thundurus']
            if pn.lower() in wtrio:
                pn = pn+'-incarnate'
            if pn.lower() == 'deoxys':
                pn = 'deoxys-normal'
            if pn.lower() == 'xerneas':
                pn = 'xerneas-active'
            if pn.lower() == 'arceus':
                pn = 'arceus-normal'
            if pn.lower() == 'shaymin':
                pn = 'shaymin-land'
            if pn.lower() == 'keldeo':
                pn = 'keldeo-ordinary'
            if pn.lower() == 'giratina':
                pn = 'giratina-altered'
            if pn.lower() == 'meloetta':
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

        embed = discord.Embed(title=f"Your Selected {pn.capitalize()}", color=0xffb6c1)

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
        embed.set_image(url=iurl)
        await ctx.send(embed=embed)
        await bot.db.release(pconn)
        return
    else:
        pconn = await bot.db.acquire()
        pquery = "SELECT pokname FROM pokes WHERE pnum = {} AND ownerid = {}".format(val, ctx.author.id)
        atquery = "SELECT atkiv FROM pokes WHERE pnum = {} AND ownerid = {}".format(val, ctx.author.id)
        dequery = "SELECT defiv FROM pokes WHERE pnum = {} AND ownerid = {}".format(val, ctx.author.id)
        spaquery = "SELECT spatkiv FROM pokes WHERE pnum = {} AND ownerid = {}".format(val, ctx.author.id)
        spdquery = "SELECT spdefiv FROM pokes WHERE pnum = {} AND ownerid = {}".format(val, ctx.author.id)
        spequery = "SELECT speediv FROM pokes WHERE pnum = {} AND ownerid = {}".format(val, ctx.author.id)
        plquery = "SELECT pokelevel FROM pokes WHERE pnum = {} AND ownerid = {}".format(val, ctx.author.id)
        pnquery = "SELECT poknick FROM pokes WHERE pnum = {} AND ownerid = {}".format(val, ctx.author.id)
        hiquery = "SELECT hitem FROM pokes WHERE pnum = {} AND ownerid = {}".format(val, ctx.author.id)
        hpquery = "SELECT hpiv FROM pokes WHERE pnum = {} AND ownerid = {}".format(val, ctx.author.id)
        natque = "SELECT nature FROM pokes WHERE pnum = {} AND ownerid = {}".format(val, ctx.author.id)
        expque = "SELECT exp FROM pokes WHERE pnum = {} AND ownerid = {}".format(val, ctx.author.id)
        expcque = "SELECT expcap FROM pokes WHERE pnum = {} AND ownerid = {}".format(val, ctx.author.id)

        nature = await pconn.fetchval(natque)
        if nature is None:
            await ctx.send("That Pokemon Does not exist")
            await bot.db.release(pconn)
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
            await ctx.send(pn)
            pn = pn.lower()
            if pn is None:
                await ctx.send("You haven't selected a Pokemon Bud")
                await bot.db.release(pconn)
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

        embed = discord.Embed(title=f"Your Selected {pn.capitalize()}", color=0xffb6c1)

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
        await ctx.send(embed=embed)
        await bot.db.release(pconn)
        return
        
@bot.command(aliases=["Info"])
async def info(ctx):
    pconn = await bot.db.acquire()
    pquery = "SELECT pokname FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    atquery = "SELECT atkiv FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    dequery = "SELECT defiv FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    spaquery = "SELECT spatkiv FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    spdquery = "SELECT spdefiv FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    spequery = "SELECT speediv FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    plquery = "SELECT pokelevel FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    pnquery = "SELECT poknick FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    hiquery = "SELECT hitem FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    hpquery = "SELECT hpiv FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    natque = "SELECT nature FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    expque = "SELECT exp FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    expcque = "SELECT expcap FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)

    nature = await pconn.fetchval(natque)
    if nature is None:
        await ctx.send("No Pokemon Selected")
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
        if pn is None:
            await ctx.send("You haven't selected a Pokemon Bud")
            await bot.db.release(pconn)
            return
        if '-dawn' in pn:
            irul = ('https://img.pokemondb.net/artwork/vector/necrozma-dawn-wings.png')
        elif '-dusk' in pn:
            irul = ('https://img.pokemondb.net/artwork/vector/necrozma-dusk-mane.png')
        else:
            irul = ('https://img.pokemondb.net/artwork/vector/' + pn.lower() + '.png')
        pn = pn.lower()
        wtrio = ['tornadus', 'landorus', 'thundurus']
        if pn.lower() in wtrio:
            pn = pn+'-incarnate'
        if pn.lower() == 'deoxys':
            pn = 'deoxys-normal'
        if pn.lower() == 'xerneas':
            pn = 'xerneas-active'
        if pn.lower() == 'arceus':
            pn = 'arceus-normal'
        if pn.lower() == 'shaymin':
            pn = 'shaymin-land'
        if pn.lower() == 'keldeo':
            pn = 'keldeo-resolute'
        if pn.lower() == 'meloetta':
            pn = 'meloetta-aria'
        if pn.lower() == 'giratina':
            pn = 'giratina-altered'

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

    embed = discord.Embed(title=f"Your Selected {pn.capitalize()}", color=0xffb6c1)
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
    await ctx.send(embed=embed)
    await bot.db.release(pconn)
    logging.basicConfig(level="INFO")
    

@bot.command(aliases=["Pokedex"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def pokedex(ctx, *, inp):
    
    val = inp.capitalize()
    if ' ' in val:
        val = val.replace(' ', '-')
    if '-mane' in val:
        val = val.replace('-mane', '')
    if val == 'Flowing':
        await ctx.send(val)
        pokemonSpeed = 73
        pokemonAtk = 99
        pokemonDef = 79
        pokemonSpa = 120
        pokemonSpd =110
        pokemonHp = 95
        pAb = 'Sizzling Growth'
        iurl = 'https://cdn.discordapp.com/attachments/479175545481986088/497738691381559296/flowin.png'
        tlist = 'grass'
        pkid = ['2003']
    elif val == 'Flire':
        pokemonSpeed = 110
        pokemonAtk = 120
        pokemonDef = 95
        pokemonSpa = 79
        pokemonSpd =99
        pokemonHp = 73
        pAb = 'Scorched feet'
        iurl = 'https://cdn.discordapp.com/attachments/479175545481986088/497733271392878622/flire.png'
        tlist = 'fire'
        pkid = ['2001']

    elif val == 'Aquino':
        pokemonSpeed = 95
        pokemonAtk = 79
        pokemonDef = 120
        pokemonSpa = 73
        pokemonSpd = 110
        pokemonHp = 99
        pAb = 'Prehistoric Rain'
        iurl = 'https://cdn.discordapp.com/attachments/480885918354636804/497721785048104970/aquino.jpg'
        tlist = 'water'
        pkid = ['2000']
    else:
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
        if val == 'shaymin':
            val = 'shaymin-land'
        if '-dawn' in val:
            iurl = ('https://img.pokemondb.net/artwork/vector/necrozma-dawn-wings.png')
        elif '-mane' in val:
            iurl = ('https://img.pokemondb.net/artwork/vector/necrozma-dusk-mane.png')
        else:
            iurl = ('https://img.pokemondb.net/artwork/vector/' + val.lower() + '.png')
        pkid = [i['pokemon_id'] for i in forms if i['identifier'] == val.lower()]
        
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
            

        
    embed = discord.Embed(title=val.capitalize(), description="", color=0xffb6c1)
    embed.add_field(name="Pokemon information", value=f"{val.capitalize()}\n**Types**: {tlist.capitalize()}\n**Pokedex Number**: {pkid[0]}")
    embed.add_field(name="Stats", value=f"HP: {pokemonHp}\nAttack: {pokemonAtk} \nDefense: {pokemonDef}\nSpecial Attack: {pokemonSpa}\nSpecial Defense: {pokemonSpd}\nSpeed: {pokemonSpeed}")
    embed.set_image(url=iurl)

    await ctx.send(embed=embed)
    

@bot.listen()
async def on_guild_join(guild):
    if not len(guild.members) >= 50:
        return
    pconn = await bot.db.acquire()
    credeems = await pconn.fetchval("SELECT redeems FROM users WHERE u_id = $1", guild.owner.id)
    if credeems is None:
        await guild.owner.send("You have 50+ Members and you should Have 10 Redeems but you Have not started, Please start with `;start` DM Dylee to claim it!")
        await guild.owner.send("<a:jirachigif:499179583531253760>")
        await bot.db.release(pconn)
        return
    credeems += 10
    await pconn.execute('UPDATE users SET redeems = $1 WHERE u_id = $2', credeems, guild.owner.id)
    await guild.owner.send("You have Received 10 Redeems for Adding me :smile:!,.. but remove me and it's gone :cry:")
    await bot.db.release(pconn)
@bot.listen()
async def on_guild_remove(guild):
    pconn = await bot.db.acquire()
    credeems = await pconn.fetchval("SELECT redeems FROM users WHERE u_id = $1", guild.owner.id)
    if credeems is None:
        await bot.db.release(pconn)
        return
    credeems-=10
    await pconn.execute("UPDATE users SET redeems = $1 WHERE u_id = $2", credeems, guild.owner.id)
    await bot.db.release(pconn)
    await guild.owner.send("Goodbye to 10 Redeems :cry:")

@bot.command(aliases=["Redeem"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def redeem(ctx, *, val=None):
    if val is None:
        e = discord.Embed(title="Redeem Options")
        e.add_field(name="Pokemon", value="Redeeem any Pokemon of your choice!")
        e.add_field(name="Credits", value="Redeem 50,000 credits")
        e.add_field(name="EV points", value="Redeem 510 EV points then use `;add <pokemon_name> <stat>` to add it!")
        e.add_field(name="Get redeems", value="Just say `;donate`")
        e.add_field(name="_____________", value="Redeem Credits with `;rcredits`")
        await ctx.send(embed=e)
        return
    val = val.capitalize()
    if val in pList or val in LegendList:
        pconn = await bot.db.acquire()
        hpiv = random.randint(1, 31)
        atkiv = random.randint(1, 31)
        defiv = random.randint(1, 31)
        spaiv = random.randint(1, 31)
        spdiv = random.randint(1, 31)
        speiv = random.randint(1, 31)
        pque = '''SELECT MAX(pnum) + 1 FROM pokes WHERE ownerid = {}'''.format(ctx.author.id)
        rque = '''SELECT redeems FROM users WHERE u_id = {}'''.format(ctx.author.id)
        rnum = await pconn.fetchval(rque)
        rnat = random.choice(natlist)
        if rnum is None:
                await ctx.send("You don't have any redeems B")
                await bot.db.release(pconn)
                return
        if rnum >= 1:
            pnum = await pconn.fetchval(pque)
            rnum1 = rnum - 1
            await pconn.execute('UPDATE users SET redeems = {0} WHERE u_id = {1}'.format(rnum1, ctx.author.id))
            query2 = '''
                INSERT INTO pokes (pokname, hpiv, atkiv, defiv, spatkiv, spdefiv, speediv, hpev, atkev, defev, spatkev, spdefev, speedev, pokelevel, ownerid, pnum, selected, move1, move2, move3, move4, hitem, exp, nature, expcap, poknick)
                VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, $25, $26)
                '''

            args = (val, hpiv, atkiv, defiv, spaiv, spdiv, speiv, 0, 0, 0, 0, 0, 0, 1, ctx.author.id, pnum, 0, 'tackle', 'tackle', 'tackle', 'tackle', 'None', 0, rnat, 35,'None')
            await ctx.channel.send(f"Here's your {val}!")
            await pconn.execute(query2, *args)
            await bot.db.release(pconn)
            return
    elif val == 'credits':
        pconn = await bot.db.acquire()
        credits = await pconn.fetchval("SELECT mewcoins FROM users WHERE u_id = $1", ctx.author.id)
        redeems = await pconn.fetchval("SELECT redeems FROM users WHERE u_id = $1", ctx.author.id)
        redeems = redeems - 1
        await pconn.execute("UPDATE users SET redeems = $1 WHERE u_id = $2", redeems, ctx.author.id)
        credits = credits + 50000
        await pconn.execute("UPDATE users SET mewcoins = $1 WHERE u_id = $2", credits, ctx.author.id)
        await ctx.send("50,000  Has been credited to your balance!")
        await bot.db.release(pconn)
        return
    
    

@bot.command()
async def rcredits(ctx):
        pconn = await bot.db.acquire()
        credits = await pconn.fetchval("SELECT mewcoins FROM users WHERE u_id = $1", ctx.author.id)
        redeems = await pconn.fetchval("SELECT redeems FROM users WHERE u_id = $1", ctx.author.id)
        redeems = redeems - 1
        await pconn.execute("UPDATE users SET redeems = $1 WHERE u_id = $2", redeems, ctx.author.id)
        credits = credits + 50000
        await pconn.execute("UPDATE users SET mewcoins = $1 WHERE u_id = $2", credits, ctx.author.id)
        await ctx.send("50,000  Has been credited to your balance!")
        await bot.db.release(pconn)
        return



##############################################################################################################################################################

        
@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def spawn(ctx, val1):
    if ctx.author.id == 358293206900670467:
        channel = ctx.channel
        val = val1.lower() 
        url = "https://img.pokemondb.net/artwork/vector/large/" + val + ".png"
        embed = discord.Embed(title="Sausage!", color=0xffb6c1)
        embed.set_image(url=url)
        await channel.send(embed=embed)
        def check(m):
            return m.content.lower() == val and m.channel == channel
        msg = await bot.wait_for('message', check=check, timeout=60)
        val = val.capitalize()


        #db code starts here


        pconn = await bot.db.acquire()
        hpiv = random.randint(1, 31)
        atkiv = random.randint(1, 31)
        defiv = random.randint(1, 31)
        spaiv = random.randint(1, 31)
        spdiv = random.randint(1, 31)
        speiv = random.randint(1, 31)
        plevel = random.randint(1, 100)
        nature = random.choice(natlist)
        expc = (plevel ** 3)
        pque = '''SELECT MAX(pnum)+1 FROM pokes WHERE ownerid = {}'''.format(msg.author.id)
        pnum = await pconn.fetchval(pque)
        try:
            pnum + 1
        except TypeError as e:
            await ctx.channel.send("You need to Start with `start`")
        query2 = '''
        INSERT INTO pokes (pokname, hpiv, atkiv, defiv, spatkiv, spdefiv, speediv, hpev, atkev, defev, spatkev, spdefev, speedev, pokelevel, ownerid, pnum, selected, move1, move2, move3, move4, poknick, exp, nature, expcap)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, $25)
        '''

        args = (val, hpiv, atkiv, defiv, spaiv, spdiv, speiv, 0, 0, 0, 0, 0, 0, plevel, msg.author.id, pnum, 0, 'tackle', 'tackle', 'tackle', 'tackle', 'None', 1, nature, expc)
        await pconn.execute(query2, *args)
        await channel.send(f'Congratulations <@{msg.author.id}>, you have successfully caught a {val}!')
        await bot.db.release(pconn)
    #   db code goes here
    else:
        await ctx.send("Only Dylee can use this command")
        
@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def addredeems(ctx, val, user: discord.Member):
    if ctx.author.id == 358293206900670467:
        pconn = await bot.db.acquire()
        rquery = f"UPDATE users SET redeems = {val} WHERE u_id = {user.id}"
        await pconn.execute(rquery)
        await bot.db.release(pconn)
    else:
        await ctx.send("Only Dylee can use this command")
        await ctx.send(random.choice(emotes))

        
@bot.command(aliases=["Reward"])
@commands.cooldown(1, 43200, commands.BucketType.user)
async def reward(ctx):
    try:
        pconn = await bot.db.acquire()
        id = ctx.author.id
        id = str(id)
        base_url = ('https://discordbots.org/api/bots/493045795445276682/check?userId=' + id)
        passwd = str(dbltoken)
        header = {'Authorization': passwd}
        r = requests.get(base_url, headers=header)
        rj = r.json()
        coins = await pconn.fetchval(f"SELECT mewcoins FROM users WHERE u_id = {ctx.author.id}")
        upoints = await pconn.fetchval(f"SELECT upvotepoints FROM users WHERE u_id = {ctx.author.id}")
        voted = rj["voted"]
        if voted == 1:
            try:
                coins+=350
                upoints += 1
            except Exception as e:
                await ctx.send("You have not upvoted the bot yet or you have not started with `;start`")
                await bot.db.release(pconn)
                return
            await pconn.execute(f"UPDATE users SET mewcoins = {coins} WHERE u_id = {ctx.author.id}")
            await pconn.execute(f"UPDATE users SET upvotepoints = {upoints} WHERE u_id = {ctx.author.id}")
            embed = discord.Embed(title="Successfully claimed Upvote Points! and Credits", color=0xffb6c1)
            embed.add_field(name="Upvoted!", value="Get 10 Upvote Points for a 5 Redeems!")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Upvote the Bot Here!")
            embed.add_field(name="You haven't upvoted!", value="Get 10 Upvote Points for 5 Redeems!")
            embed.add_field(name="Upvote Mewbot Here!", value="[Upvote MewBot](https://discordbots.org/bot/493045795445276682/vote)")
            await ctx.send(embed=embed)
            await bot.db.release(pconn)
    except Exception as e:
        embed = discord.Embed(title="You have already Upvoted")
        embed.add_field(name="Already Upvoted the Bot", value=f"{e}")
        await bot.db.release(pconn)
        await ctx.send(embed=embed)
        return
        
@bot.command(aliases=["vote", "daily"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def upvote(ctx):
    embed = discord.Embed(title="Upvote the Bot Here!")
    embed.add_field(name="You haven't upvoted?", value="If you have not upvoted")
    embed.add_field(name="Upvote Mewbot Here! ", value="[Upvote MewBot](https://discordbots.org/bot/493045795445276682/vote)")
    embed.set_footer(text="NOTE: ONLY USE ;reward WHEN YOU HAVE UPVOTED")
    await ctx.send(embed=embed)
    emoji = random.choice(emotes)
    await ctx.send(emoji)
    
@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def trade(ctx, user: discord.Member, creds: int, poke: int):
    pconn = await bot.db.acquire()
    if user is None:
        await ctx.send("You cannot trade with yourself")
        await bot.db.release(pconn)
        return
    elif creds is None:
        await ctx.send("You did not specify Credits, please use `;gift` instead")
        await bot.db.release(pconn)
        return
    elif poke is None:
        await ctx.send("You did not specify a Pokemon Please Use `give` instead")
        await bot.db.release(pconn)
        return
    else:
        offering = await pconn.fetchval(f"SELECT mewcoins FROM users WHERE u_id = {ctx.author.id}")
        ccreds = await pconn.fetchval(f"SELECT mewcoins FROM users WHERE u_id = {user.id}")
        if creds > offering:
            await ctx.send(f"You do not have {creds} ℳ")
            await bot.db.release(pconn)
            return
        pokename = await pconn.fetchval(f"SELECT pokname FROM pokes WHERE pnum = {poke} AND ownerid = {user.id}")

        pid = await pconn.fetchval(f"SELECT id FROM pokes WHERE pnum = {poke}")
        e = discord.Embed(title="Current Trade")
        e.add_field(name=f"\n{ctx.author.name} ", value=f"is Offering {creds} for \n")
        e.add_field(name=f"\n{user.name}'s ", value=f"{pokename} \n")
        e.add_field(name=f"\nDo you both ", value=f"Accept the trade?\n")
        e.set_footer(text="Say Yes to accept or no to reject.")
        await ctx.send(embed=e)
        def check(m):
            return m.author.id == user.id and m.content in ('Yes', 'yes', 'No', 'no')
        try:
            msg = await bot.wait_for('message', check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("Trade cancelled, took too long to confirm")
            await bot.db.release(pconn)
            return
        if msg.content.lower() in ('no', 'nah', 'nope'):
            await ctx.send("Trade rejected")
            await bot.db.release(pconn)
            return
        elif msg.content.lower() in ('yes', 'ye', 'yep', 'yeet'):
            await ctx.send("Trade has been approved!")
        offering -= creds
        ccreds += offering
        mnum = await pconn.fetchval(f"SELECT MAX(pnum)+1 FROM pokes WHERE ownerid = {ctx.author.id}")
        nquery = f"UPDATE pokes SET ownerid = {ctx.author.id} AND pnum = {mnum} WHERE id = {pid}"
        cquery = f"UPDATE users SET mewcoins = {offering} WHERE u_id = {ctx.author.id}"
        gquery = f"UPDATE users SET mewcoins = {ccreds} WHERE u_id = {user.id}"
        maxnum = await pconn.fetchval("SELECT MAX(pnum) FROM pokes WHERE ownerid = $1", user.id)
        maxnum+=1
        poke+=1
        for i in range(poke, maxnum):
                newnum = i - 1
                await pconn.execute("UPDATE pokes SET pnum = $1 WHERE pnum = $2 AND ownerid = $3", newnum, i, user.id)
        await pconn.execute(nquery)
        await pconn.execute(cquery)
        await pconn.execute(gquery)
        await ctx.send("Trade Complete, Logs will be sent to DMs!")
        gif = random.choice(emotes)
        await ctx.send(gif)
        await ctx.author.send(f"You completed a Trade with {user.name}")
        await user.send(f"You completed a Trade with {ctx.name}")
        await bot.db.release(pconn)

    
@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def giveredeem(ctx, user: discord.Member, val):
    if ctx.author.id == user.id:
        await ctx.send("You can not give yourself redeems")
        return
    pconn = await bot.db.acquire()
    val = int(val)
    if user is None:
        await ctx.send("Please tag a User")
        await bot.db.release(pconn)
        return
    else:
        redeems = await pconn.fetchval("SELECT redeems FROM users WHERE u_id = $1", ctx.author.id)
        getr = await pconn.fetchval("SELECT redeems FROM users WHERE u_id = $1", user.id)
        if redeems is None:
            await ctx.send(f"<@{ctx.author.id}> has not started")
            await bot.db.release(pconn)
            return
        elif getr is None:
            await ctx.send(f"<@{user.id}> has not started")
            await bot.db.release(pconn)
            return
        if val > redeems:
            await ctx.send("You don't have that much Redeems Friend")
            await bot.db.release(pconn)
            return
        giver = redeems - val
        rcvr = redeems + val
        await pconn.execute("UPDATE users SET redeems = $1 WHERE u_id = $2", giver, ctx.author.id)
        await pconn.execute("UPDATE users SET redeems = $1 WHERE u_id = $2", rcvr, user.id)
        await ctx.send(f"<@{ctx.author.id}> has given <@{user.id}> {val} redeems")
        await bot.db.release(pconn)
        
@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def gift(ctx, user: discord.Member, val):
    if ctx.author.id == user.id:
        await ctx.send("You can not give yourself credits")
        return
    pconn = await bot.db.acquire()
    val = int(val)
    if user is None:
        await ctx.send("Please tag a User")
        await bot.db.release(pconn)
        return
    else:
        redeems = await pconn.fetchval("SELECT mewcoins FROM users WHERE u_id = $1", ctx.author.id)
        getr = await pconn.fetchval("SELECT mewcoins FROM users WHERE u_id = $1", user.id)
        if val > redeems:
            await ctx.send("You don't have that much Credits Friend")
            await bot.db.release(pconn)
            return
        elif getr is None:
            await ctx.send(f"<@{user.id}> has not started")
            await bot.db.release(pconn)
            return
        elif redeems is None:
            await ctx.send(f"<@{ctx.author.id}> has not started")
            await bot.db.release(pconn)
            return
        giver = redeems - val
        rcvr = redeems + val
        await pconn.execute("UPDATE users SET redeems = $1 WHERE u_id = $2", giver, ctx.author.id)
        await pconn.execute("UPDATE users SET redeems = $1 WHERE u_id = $2", rcvr, user.id)
        await ctx.send(f"<@{ctx.author.id}> has given <@{user.id}> {val}ℳ")
        await bot.db.release(pconn)

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def give(ctx, user: discord.Member, val):
    pconn = await bot.db.acquire()
    val = int(val)
    if user is None:
        await ctx.send("Please tag a User")
        await bot.db.release(pconn)
        return
    else:
        poke = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 AND pnum = $2", ctx.author.id, val)
        maxnum = await pconn.fetchval("SELECT MAX(pnum) FROM pokes WHERE ownerid = $1", user.id)
        if maxnum is None:
            await ctx.send(f"<@{user.id}> has not started")
            await bot.db.release(pconn)
            return
        elif poke is None:
            await ctx.send(f"<@{ctx.author.id}> has not started or you dont have that poke")
            await bot.db.release(pconn)
            return
        await pconn.execute("UPDATE pokes SET ownerid = $1, pnum = $2 WHERE ownerid = $3 AND pnum = $4", user.id, maxnum, ctx.author.id, val)
        mnum = await pconn.fetchval("SELECT MAX(pnum) FROM pokes WHERE ownerid = $1", ctx.author.id)
        mnum+=1
        val+=1
        for i in range(val,mnum):
                nnum = i - 1
                await pconn.execute("UPDATE pokes SET pnum = $1 WHERE pnum = $2 AND ownerid = $3", nnum, i, ctx.author.id)
        await ctx.send(f"<@{ctx.author.id}> has given <@{user.id}> A {poke}")
        await bot.db.release(pconn)
        
@bot.command()
async def lunarize(ctx, val:int):
    pconn = await bot.db.acquire()
    pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 and selected = 1", ctx.author.id)
    pokename = pokename.lower()
    if not pokename == 'necrozma':
        await ctx.send(f"You can not Lunarize a {pokename}")
        await bot.db.release(pconn)
        return
    helditem = await pconn.fetchval("SELECT hitem FROM pokes WHERE ownerid = $1 AND selected = 1", ctx.author.id)
    lunala = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 AND pnum = $2", ctx.author.id, val)
    lunalev = await pconn.fetchval("SELECT pokelevel FROM pokes WHERE ownerid = $1 and pnum = $2", ctx.author.id, val)
    lunala = lunala.lower()
    if not lunala == 'lunala':
        await ctx.send("That is not a Lunala, please use `;lunarize <lunala_number>` to Lunarize")
        await bot.db.release(pconn)
        return
    if not helditem == 'n-lunarizer':
        await ctx.send("Your Necrozma is not holding a N-lunarizer")
        await bot.db.release(pconn)
        return
    msg = await ctx.send("Fusing")
    await ctx.send(f"You have Fused your Necrozma with your Lunala Level {lunalev}")
    await pconn.execute("UPDATE pokes SET pokname = $1 WHERE selected = 1 AND ownerid = $2", 'necrozma-dawn', ctx.author.id)
    await msg.edit(content="Fusion Complete")
    await bot.db.release(pconn)

@bot.command()
async def solarize(ctx, val:int):
    pconn = await bot.db.acquire()
    pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 and selected = 1", ctx.author.id)
    pokename = pokename.lower()
    if not pokename == 'necrozma':
        await ctx.send(f"You can not Solarize a {pokename}")
        await bot.db.release(pconn)
        return
    helditem = await pconn.fetchval("SELECT hitem FROM pokes WHERE ownerid = $1 AND selected = 1", ctx.author.id)
    lunala = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 AND pnum = $2", ctx.author.id, val)
    lunalev = await pconn.fetchval("SELECT pokelevel FROM pokes WHERE ownerid = $1 and pnum = $2", ctx.author.id, val)
    lunala = lunala.lower()
    if lunalev is None:
        await ctx.send("That Pokemon Does not exist in your List")
    if not lunala == 'solgaleo':
        await ctx.send("That is not a Solgaleo, please use `;solarize <solgaleo_number>` to Solarize")
        await bot.db.release(pconn)
        return
    if not helditem == 'n-solarizer':
        await ctx.send("Your Necrozma is not holding a N-solarizer")
        await bot.db.release(pconn)
        return
    msg = await ctx.send("Fusing")
    await ctx.send(f"You have Fused your Necrozma with your Solgaleo Level {lunalev}")
    await pconn.execute("UPDATE pokes SET pokname = $1 WHERE selected = 1 AND ownerid = $2", 'necrozma-dusk', ctx.author.id)
    await msg.edit(content="Fusion Complete")
    await bot.db.release(pconn)

@bot.command()
async def fuse(ctx, form, val:int):
    if form == 'white':
        pconn = await bot.db.acquire()
        pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 and selected = 1", ctx.author.id)
        pokename = pokename.lower()
        if not pokename == 'kyurem':
            await ctx.send(f"You can not Fuse a {pokename} with Reshiram")
            await bot.db.release(pconn)
            return
        helditem = await pconn.fetchval("SELECT hitem FROM pokes WHERE ownerid = $1 AND selected = 1", ctx.author.id)
        lunala = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 AND pnum = $2", ctx.author.id, val)
        lunalev = await pconn.fetchval("SELECT pokelevel FROM pokes WHERE ownerid = $1 and pnum = $2", ctx.author.id, val)
        lunala = lunala.lower()
        if lunalev is None:
            await ctx.send("That Pokemon Does not exist in your List")
        if not lunala == 'reshiram':
            await ctx.send("That is not a Reshiram, please use `;fuse white <reshiram_number>` to Fuse Kyurem with Reshiram")
            await bot.db.release(pconn)
            return
        if not helditem == 'light-stone':
            await ctx.send("Your Kyurem is not holding a Light stone")
            await bot.db.release(pconn)
            return
        msg = await ctx.send("Fusing")
        await ctx.send(f"You have Fused your Kyurem with your Reshiram Level {lunalev}")
        await pconn.execute("UPDATE pokes SET pokname = $1 WHERE selected = 1 AND ownerid = $2", 'kyurem-white', ctx.author.id)
        await msg.edit(content="Fusion Complete")
        await bot.db.release(pconn)
    elif form == 'black':
        pconn = await bot.db.acquire()
        pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 and selected = 1", ctx.author.id)
        pokename = pokename.lower()
        if not pokename == 'kyurem':
            await ctx.send(f"You can not Fuse a {pokename} with Zekrom")
            await bot.db.release(pconn)
            return
        helditem = await pconn.fetchval("SELECT hitem FROM pokes WHERE ownerid = $1 AND selected = 1", ctx.author.id)
        lunala = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 AND pnum = $2", ctx.author.id, val)
        lunalev = await pconn.fetchval("SELECT pokelevel FROM pokes WHERE ownerid = $1 and pnum = $2", ctx.author.id, val)
        lunala = lunala.lower()
        if lunalev is None:
            await ctx.send("That Pokemon Does not exist in your List")
        if not lunala == 'zekrom':
            await ctx.send("That is not a Zekrom, please use `;fuse black <zekrom_number>` to Fuse Kyurem with Zekrom")
            await bot.db.release(pconn)
            return
        if not helditem == 'dark-stone':
            await ctx.send("Your Kyurem is not holding a Dark stone")
            await bot.db.release(pconn)
            return
        msg = await ctx.send("Fusing")
        await ctx.send(f"You have Fused your Kyurem with your Zekrom Level {lunalev}")
        await pconn.execute("UPDATE pokes SET pokname = $1 WHERE selected = 1 AND ownerid = $2", 'kyurem-black', ctx.author.id)
        await msg.edit(content="Fusion Complete")
        await bot.db.release(pconn)
    
   
@bot.command()
async def form(ctx, val):
    val = val.lower()
    pconn = await bot.db.acquire()
    pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 and selected = 1", ctx.author.id)
    helditem = await pconn.fetchval("SELECT hitem FROM pokes WHERE ownerid = $1 AND selected = 1", ctx.author.id)
    moves = await pconn.fetch("SELECT move1, move2, move3, move4 FROM pokes WHERE ownerid = $1 AND selected = 1", ctx.author.id)
    weathertrio = ['landorus', 'thundurus', 'tornadus']
    weathevo = ['landorus-incarnate', 'tornadus-incarnate', 'thundurus-incarnate']
    pokename = pokename.lower()
    if pokename in weathertrio:
        pokename = pokename+'-incarnate'
    if pokename == 'deoxys':
        pokename = 'deoxys-normal'
    if pokename == 'shaymin':
        pokename = 'shaymin-land'
    if pokename == 'arceus':
        pokename = 'arceus-normal'
    if pokename == 'keldeo':
        pokename = 'keldeo-ordinary'
    if pokename == 'giratina':
        pokename = 'giratina-altered'
    if helditem is None:
        await ctx.send("This Pokemon Is not Holding the required item for transformation")
        await bot.db.release(pconn)
        return
    if pokename is None:
        await ctx.send("No Pokemon Selected")
        await bot.db.release(pconn)
        return
    with open("forms.json")as f:
        forms = json.load(f)
    pokename = pokename.lower()
    if pokename == 'shaymin' and helditem == 'gracidea-flower':
        preformnum = [t['order'] for t in forms if t['identifier'] == pokename.lower()]
        preformnum = preformnum[0]
        form = preformnum + 1
        f_id = [t['identifier'] for t in forms if t['order'] == form]
        form = f_id
        form = form[0]
        await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid  = $2 AND selected = 1", form, ctx.author.id)
        await ctx.send(f"Your {pokename.capitalize()} has evolved into {form.capitalize()}")
        await bot.db.release(pconn)
        return
    elif pokename == 'kyogre' and helditem == 'blue-orb':
        preformnum = [t['order'] for t in forms if t['identifier'] == pokename.lower()]
        preformnum = preformnum[0]
        form = preformnum + 1
        f_id = [t['identifier'] for t in forms if t['order'] == form]
        form = f_id
        form = form[0]
        await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid  = $2 AND selected = 1", form, ctx.author.id)
        await ctx.send("Your Kyogre Has evolved into Kyogre-Primal!")
        await bot.db.release(pconn)
        return
    elif pokename == 'groudon' and helditem == 'red-orb':
        preformnum = [t['order'] for t in forms if t['identifier'] == pokename.lower()]
        preformnum = preformnum[0]
        form = preformnum + 1
        f_id = [t['identifier'] for t in forms if t['order'] == form]
        form = f_id
        form = form[0]
        await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid  = $2 AND selected = 1", form, ctx.author.id)
        await ctx.send(f"Your {pokename.capitalize()} has evolved into {form.capitalize()}")
        await bot.db.release(pconn)
        return
    elif pokename == 'giratina-altered' and helditem == 'griseous-orb':
        preformnum = [t['order'] for t in forms if t['identifier'] == pokename.lower()]
        preformnum = preformnum[0]
        form = preformnum + 1
        f_id = [t['identifier'] for t in forms if t['order'] == form]
        form = f_id
        form = form[0]
        await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid  = $2 AND selected = 1", form, ctx.author.id)
        await ctx.send(f"Your {pokename.capitalize()} has evolved into {form.capitalize()}")
        await bot.db.release(pconn)
        return
    elif pokename == 'keldeo-ordinary':
        move1 = [t['move1'] for t in moves]
        move2 = [t['move2'] for t in moves]
        move3 = [t['move3'] for t in moves]
        move4 = [t['move4'] for t in moves]
        moves = move1+move2+move3+move4
        if 'secret-sword' in moves:
            preformnum = [t['order'] for t in forms if t['identifier'] == pokename.lower()]
            preformnum = preformnum[0]
            form = preformnum + 1
            f_id = [t['identifier'] for t in forms if t['order'] == form]
            form = f_id
            form = form[0]
            await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid  = $2 AND selected = 1", form, ctx.author.id)
            await ctx.send(f"Your {pokename.capitalize()} has evolved into {form.capitalize()}")
            await bot.db.release(pconn)
        else:
            await ctx.send("Your Keldeo does not know Secret Sword Move")
    elif pokename == 'deoxys-normal' and helditem == 'meteorite':
        if val == 'speed':
            pre = [t['order'] for t in forms if t['identifier'] == pokename.lower()]
            pre = pre[0]
            form = pre + 3
            form = [t['identifier'] for t in forms if t['order'] == form]
            form = form[0]
            await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid  = $2 AND selected = 1", form, ctx.author.id)
            await ctx.send(f"Your {pokename.capitalize()} has evolved into {form.capitalize()}")
            await bot.db.release(pconn)
            return
        elif val == 'defense':
            pre = [t['order'] for t in forms if t['identifier'] == pokename.lower()]
            pre = pre[0]
            form = pre + 2
            form = [t['identifier'] for t in forms if t['order'] == form]
            form = form[0]
            await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid  = $2 AND selected = 1", form, ctx.author.id)
            await ctx.send(f"Your {pokename.capitalize()} has evolved into {form.capitalize()}")
            await bot.db.release(pconn)
            return
        elif val == 'attack':
            pre = [t['order'] for t in forms if t['identifier'] == pokename.lower()]
            pre = pre[0]
            form = pre + 1
            form = [t['identifier'] for t in forms if t['order'] == form]
            form = form[0]
            await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid  = $2 AND selected = 1", form, ctx.author.id)
            await ctx.send(f"Your {pokename.capitalize()} has evolved into {form.capitalize()}")
            await bot.db.release(pconn)
            return
        else:
            return
    elif pokename in weathevo and helditem == 'reveal-glass':
        preformnum = [t['order'] for t in forms if t['identifier'] == pokename.lower()]
        preformnum = preformnum[0]
        form = preformnum + 1
        f_id = [t['identifier'] for t in forms if t['order'] == form]
        form = f_id
        form = form[0]
        await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid  = $2 AND selected = 1", form, ctx.author.id)
        await ctx.send(f"Your {pokename.capitalize()} has evolved into {form.capitalize()}")
        await bot.db.release(pconn)
        return
    elif pokename == 'zygarde' and helditem == 'zygarde-cell':
        if val == 'complete' or '100':
            pre = [t['order'] for t in forms if t['identifier'] == 'zygarde-50']
            pre = pre[0]
            form = pre + 1
            f_id = [t['identifier'] for t in forms if t['order'] == form]
            form = f_id
            form = form[0]
            await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid  = $2 AND selected = 1", form, ctx.author.id)
            await ctx.send(f"Your {pokename.capitalize()} has evolved into {form.capitalize()}")
            await bot.db.release(pconn)
            return
        elif val == '10':
            pre = [t['order'] for t in forms if t['identifier'] == 'zygarde-50']
            pre = pre[0]
            form = pre - 1
            f_id = [t['identifier'] for t in forms if t['order'] == form]
            form = f_id
            form = form[0]
            await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid  = $2 AND selected = 1", form, ctx.author.id)
            await ctx.send(f"Your {pokename.capitalize()} has evolved into {form.capitalize()}")
            await bot.db.release(pconn)
            return
            
    else:
        await ctx.send("You're holding the wrong item, or that form might not be in yet, Please be patient :wink:")
        await bot.db.release(pconn)
        return
    
    
@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def mega(ctx, *, val):
    if ' ' in val:
        val = val.replace(' ', '-')
    if val == 'devolve':
        pconn = await bot.db.acquire()
        pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 AND selected = 1", ctx.author.id)
        if pokename is None:
            await ctx.send("No Pokemon Selected")
            await bot.db.release(pconn)
            return
        with open("forms.json") as f:
            forms = json.load(f)
        order = [t['order'] for t in forms if t['identifier'] == pokename.lower()]
        formnum = order[0]
        formnum -= 1
        pokemon = [t['identifier'] for t in forms if t['order'] == formnum]
        megaable = [t['is_mega'] for t in forms if t['identifier'] == pokemon[0]]
        mega = pokemon[0]
        megaable = megaable[0]
        if megaable is 1:
            await ctx.send("This Pokemon cannot Mega Devolve!")
            await bot.db.release(pconn)
            return
        await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid = $2 AND selected = 1", mega, ctx.author.id)
        await ctx.send(f"Your {pokename} has devolved into {mega}!")
        await bot.db.release(pconn)
        
    if not 'evolve' in val:
        return
    if val == 'evolve-y':
        pconn = await bot.db.acquire()
        pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 AND selected = 1", ctx.author.id)
        helditem = await pconn.fetchval("SELECT hitem FROM pokes WHERE ownerid = $1 AND selected = 1", ctx.author.id)
        if '-' in helditem:
            helditem = helditem.replace('-', ' ')
        if not helditem == 'mega stone y':
            await ctx.send("This Pokemon Is not holding a Mega Stone Y!")
            await bot.db.release(pconn)
            return
        if pokename is None:
            await ctx.send("No Pokemon Selected")
            await bot.db.release(pconn)
            return
        with open("forms.json") as f:
            forms = json.load(f)
        order = [t['order'] for t in forms if t['identifier'] == pokename.lower()]
        formnum = order[0]
        formnum += 2
        pokemon = [t['identifier'] for t in forms if t['order'] == formnum]
        megaable = [t['is_mega'] for t in forms if t['identifier'] == pokemon[0]]
        mega = pokemon[0]
        megaable = megaable[0]
        if not megaable is 1:
            await ctx.send("This Pokemon cannot Mega Evolve!")
            await bot.db.release(pconn)
            return
        await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid = $2 AND selected = 1", mega, ctx.author.id)
        await ctx.send(f"Your {pokename} has evolved into {mega}!")
        await bot.db.release(pconn)
    if val == 'evolve-x':
        pconn = await bot.db.acquire()
        pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 AND selected = 1", ctx.author.id)
        helditem = await pconn.fetchval("SELECT hitem FROM pokes WHERE ownerid = $1 AND selected = 1", ctx.author.id)
        if '-' in helditem:
            helditem = helditem.replace('-', ' ')
        if not helditem == "mega stone x":
            await ctx.send(helditem)
            await ctx.send("This Pokemon Is not holding a Mega Stone X!")
            await bot.db.release(pconn)
            return
        if pokename is None:
            await ctx.send("No Pokemon Selected")
            await bot.db.release(pconn)
            return
        with open("forms.json") as f:
            forms = json.load(f)
        order = [t['order'] for t in forms if t['identifier'] == pokename.lower()]
        formnum = order[0]
        formnum += 1
        await ctx.send(formnum)
        pokemon = [t['identifier'] for t in forms if t['order'] == formnum]
        await ctx.send(pokemon)
        megaable = [t['is_mega'] for t in forms if t['identifier'] == pokemon[0]]
        await ctx.send(megaable)
        mega = pokemon[0]
        megaable = megaable[0]
        if not megaable is 1:
            await ctx.send("This Pokemon cannot Mega Evolve!")
            await bot.db.release(pconn)
            return
        await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid = $2 AND selected = 1", mega, ctx.author.id)
        await ctx.send(f"Your {pokename} has evolved into {mega}!")
        await bot.db.release(pconn)
        
    else:
        pconn = await bot.db.acquire()
        pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 AND selected = 1", ctx.author.id)
        helditem = await pconn.fetchval("SELECT hitem FROM pokes WHERE ownerid = $1 AND selected = 1", ctx.author.id)
        if '-' in helditem:
            helditem = helditem.replace('-', ' ')
        if not helditem == 'mega stone':
            await ctx.send("This Pokemon Is not holding a Mega Stone!")
            await bot.db.release(pconn)
            return
        if pokename is None:
            await ctx.send("No Pokemon Selected")
            await bot.db.release(pconn)
            return
        with open("forms.json") as f:
            forms = json.load(f)
        order = [t['order'] for t in forms if t['identifier'] == pokename.lower()]
        formnum = order[0]
        formnum += 1
        pokemon = [t['identifier'] for t in forms if t['order'] == formnum]
        megaable = [t['is_mega'] for t in forms if t['identifier'] == pokemon[0]]
        mega = pokemon[0]
        megaable = megaable[0]
        if not megaable is 1:
            await ctx.send("This Pokemon cannot Mega Evolve!")
            await bot.db.release(pconn)
            return
        await pconn.execute("UPDATE pokes SET pokname = $1 WHERE ownerid = $2 AND selected = 1", mega, ctx.author.id)
        await ctx.send(f"Your {pokename} has evolved into {mega}!")
        await bot.db.release(pconn)
        
        
        
        
        
        
        
@bot.listen()
async def on_message(message):
    chance = random.randint(1, 10)
    if not chance is 5:
        return
    with open('pokemonfile.json') as f:
        pokemon = json.load(f)
    with open('evofile.json') as f:
        evofile = json.load(f)
    if message.author.id == 493045795445276682:
        return
    if message.author.bot:
        return
    try:
        pconn = await bot.db.acquire()
    except AttributeError as e:
        return
    pk1 = await pconn.fetch("SELECT u_id FROM users WHERE u_id = $1", message.author.id)
    nrecord = [record['u_id'] for record in pk1]
    if not message.author.id in nrecord:
        await bot.db.release(pconn)
        return
    pn = await pconn.fetchval("SELECT pokname FROM pokes WHERE ownerid = $1 AND selected = 1", message.author.id)
    if pn is None:
        await bot.db.release(pconn)
        return
    if '-mega' in pn:
        poke = pn.replace('-mega', '')
    elif not '-mega' in pn:
        poke = pn.lower()
    lexp = await pconn.fetchval("SELECT expcap FROM pokes WHERE ownerid = $1 AND selected = 1", message.author.id)
    if lexp == None:
        await bot.db.release(pconn)
        return
    exp1 = await pconn.fetchval('SELECT (exp)+50 FROM pokes WHERE selected = 1 AND ownerid = $1', message.author.id)
    try:
        await pconn.execute('UPDATE pokes SET exp = $1 WHERE selected = 1 AND ownerid = $2', exp1, message.author.id)
    except Exception as e:
        await bot.db.release(pconn)
        return
    plup = await pconn.fetchval("SELECT pokelevel FROM pokes WHERE selected = 1 AND ownerid = $1", message.author.id)
    if plup is None:
        await bot.db.release(pconn)
        return
    plup+=1
    newcap = (plup ** 3)
    if exp1 > lexp:
        await pconn.execute(f"UPDATE pokes SET pokelevel = $1, expcap = $2 WHERE selected = 1 AND ownerid = $3", plup, newcap, message.author.id)
        await message.channel.send(f"Congratulations!, your Pokemon has Leveled up to Level {plup}!")
    preevo = [t['id'] for t in pokemon if t['identifier'] == poke]
    min_lev = [t['minimum_level'] for t in evofile if t['id'] == preevo]
    if min_lev is None:
        await bot.db.release(pconn)
        return
    if not plup == min_lev:
        await bot.db.release(pconn)
        return
    evo = [t['identifier'] for t in pokemon if t['evolves_from_species_id'] == preevo]
    await pconn.execute("UPDATE pokes SET pokename = $1 WHERE selected = 1 AND ownerid = $2", evo, ctx.author.id)
    await ctx.send(f"Your {pn} has evolved into a {evo}!")
    await bot.db.release(pconn)

        
        

bot.run(TOKEN)

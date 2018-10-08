#work with python 3.7
import discord
from boto.s3.connection import S3Connection
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

pList = ['Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Caterpie','Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Ekans','Arbok','Pikachu','Raichu','Sandshrew','Sandslash','Nidoran♀','Nidorina','Nidoqueen','Nidoran♂','Nidorino','Nidoking','Clefairy','Clefable','Vulpix','Ninetales','Jigglypuff','Wigglytuff','Zubat','Golbat','Oddish','Gloom','Vileplume','Paras','Parasect','Venonat','Venomoth','Diglett','Dugtrio','Meowth','Persian','Psyduck','Golduck','Mankey','Primeape','Growlithe','Arcanine','Poliwag','Poliwhirl','Poliwrath','Abra','Kadabra','Alakazam','Machop','Machoke','Machamp','Bellsprout','Weepinbell','Victreebel','Tentacool','Tentacruel','Geodude','Graveler','Golem','Ponyta','Rapidash','Slowpoke','Slowbro','Magnemite','Magneton','Farfetch’d','Doduo','Dodrio','Seel','Dewgong','Grimer','Muk','Shellder','Cloyster','Gastly','Haunter','Gengar','Onix','Drowzee','Hypno','Krabby','Kingler','Voltorb','Electrode','Exeggcute','Exeggutor','Cubone','Marowak','Hitmonlee','Hitmonchan','Lickitung','Koffing','Weezing','Rhyhorn','Rhydon','Chansey','Tangela','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Mr. Mime','Scyther','Jynx','Electabuzz','Magmar','Pinsir','Tauros','Magikarp','Gyarados','Lapras','Ditto','Eevee','Vaporeon','Jolteon','Flareon','Porygon','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax', 'Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Caterpie','Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Ekans','Arbok','Pikachu','Raichu','Sandshrew','Sandslash','Nidoran♀','Nidorina','Nidoqueen','Nidoran♂','Nidorino','Nidoking','Clefairy','Clefable','Vulpix','Ninetales','Jigglypuff','Wigglytuff','Zubat','Golbat','Oddish','Gloom','Vileplume','Paras','Parasect','Venonat','Venomoth','Diglett','Dugtrio','Meowth','Persian','Psyduck','Golduck','Mankey','Primeape','Growlithe','Arcanine','Poliwag','Poliwhirl','Poliwrath','Abra','Kadabra','Alakazam','Machop','Machoke','Machamp','Bellsprout','Weepinbell','Victreebel','Tentacool','Tentacruel','Geodude','Graveler','Golem','Ponyta','Rapidash','Slowpoke','Slowbro','Magnemite','Magneton','Farfetch’d','Doduo','Dodrio','Seel','Dewgong','Grimer','Muk','Shellder','Cloyster','Gastly','Haunter','Gengar','Onix','Drowzee','Hypno','Krabby','Kingler','Voltorb','Electrode','Exeggcute','Exeggutor','Cubone','Marowak','Hitmonlee','Hitmonchan','Lickitung','Koffing','Weezing','Rhyhorn','Rhydon','Chansey','Tangela','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Mr. Mime','Scyther','Jynx','Electabuzz','Magmar','Pinsir','Tauros','Magikarp','Gyarados','Lapras','Ditto','Eevee','Vaporeon','Jolteon','Flareon','Porygon','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax','Articuno','Zapdos','Moltres','Dratini','Dragonair','Dragonite','Mewtwo','Mew','Chikorita','Bayleef','Meganium','Cyndaquil','Quilava','Typhlosion','Totodile','Croconaw','Feraligatr','Sentret','Furret','Hoothoot','Noctowl','Ledyba','Ledian','Spinarak','Ariados','Crobat','Chinchou','Lanturn','Pichu','Cleffa','Igglybuff','Togepi','Togetic','Natu','Xatu','Mareep','Flaaffy','Ampharos','Bellossom','Marill','Azumarill','Sudowoodo','Politoed','Hoppip','Skiploom','Jumpluff','Aipom','Sunkern','Sunflora','Yanma','Wooper','Quagsire','Espeon','Umbreon','Murkrow','Slowking','Misdreavus','Unown','Wobbuffet','Girafarig','Pineco','Forretress','Dunsparce','Gligar','Steelix','Snubbull','Granbull','Qwilfish','Scizor','Shuckle','Heracross','Sneasel','Teddiursa','Ursaring','Slugma','Magcargo','Swinub','Piloswine','Corsola','Remoraid','Octillery','Delibird','Mantine','Skarmory','Houndour','Houndoom','Kingdra','Phanpy','Donphan','Porygon2','Stantler','Smeargle','Tyrogue','Hitmontop','Smoochum','Elekid','Magby','Miltank','Blissey','Raikou','Entei','Suicune','Larvitar','Pupitar','Tyranitar','Lugia','Ho-Oh','Celebi','Treecko','Grovyle','Sceptile','Torchic','Combusken','Blaziken','Mudkip','Marshtomp','Swampert','Poochyena','Mightyena','Zigzagoon','Linoone','Wurmple','Silcoon','Beautifly','Cascoon','Dustox','Lotad','Lombre','Ludicolo','Seedot','Nuzleaf','Shiftry','Taillow','Swellow','Wingull','Pelipper','Ralts','Kirlia','Gardevoir','Surskit','Masquerain','Shroomish','Breloom','Slakoth','Vigoroth','Slaking','Nincada','Ninjask','Shedinja','Whismur','Loudred','Exploud','Makuhita','Hariyama','Azurill','Nosepass','Skitty','Delcatty','Sableye','Mawile','Aron','Lairon','Aggron','Meditite','Medicham','Electrike','Manectric','Plusle','Minun','Volbeat','Illumise','Roselia','Gulpin','Swalot','Carvanha','Sharpedo','Wailmer','Wailord','Numel','Camerupt','Torkoal','Spoink','Grumpig','Spinda','Trapinch','Vibrava','Flygon','Cacnea','Cacturne','Swablu','Altaria','Zangoose','Seviper','Lunatone','Solrock','Barboach','Whiscash','Corphish','Crawdaunt','Baltoy','Claydol','Lileep','Cradily','Anorith','Armaldo','Feebas','Milotic','Castform','Kecleon','Shuppet','Banette','Duskull','Dusclops','Tropius','Chimecho','Absol','Wynaut','Snorunt','Glalie','Spheal','Sealeo','Walrein','Clamperl','Huntail','Gorebyss','Relicanth','Luvdisc','Bagon','Shelgon','Salamence','Beldum','Metang','Metagross','Regirock','Regice','Registeel','Latias','Latios','Kyogre','Groudon','Rayquaza','Jirachi','Deoxys','Turtwig','Grotle','Torterra','Chimchar','Monferno','Infernape','Piplup','Prinplup','Empoleon','Starly','Staravia','Staraptor','Bidoof','Bibarel','Kricketot','Kricketune','Shinx','Luxio','Luxray','Budew','Roserade','Cranidos','Rampardos','Shieldon','Bastiodon','Burmy','Wormadam','Mothim','Combee','Vespiquen','Pachirisu','Buizel','Floatzel','Cherubi','Cherrim','Shellos','Gastrodon','Ambipom','Drifloon','Drifblim','Buneary','Lopunny','Mismagius','Honchkrow','Glameow','Purugly','Chingling','Stunky','Skuntank','Bronzor','Bronzong','Bonsly','Mime Jr.','Happiny','Chatot','Spiritomb','Gible','Gabite','Garchomp','Munchlax','Riolu','Lucario','Hippopotas','Hippowdon','Skorupi','Drapion','Croagunk','Toxicroak','Carnivine','Finneon','Lumineon','Mantyke','Snover','Abomasnow','Weavile','Magnezone','Lickilicky','Rhyperior','Tangrowth','Electivire','Magmortar','Togekiss','Yanmega','Leafeon','Glaceon','Gliscor','Mamoswine','Porygon-Z','Gallade','Probopass','Dusknoir','Froslass','Rotom','Uxie','Mesprit','Azelf','Dialga','Palkia','Heatran','Regigigas','Giratina','Cresselia','Phione','Manaphy','Darkrai','Shaymin','Arceus','Victini','Snivy','Servine','Serperior','Tepig','Pignite','Emboar','Oshawott','Dewott','Samurott','Patrat','Watchog','Lillipup','Herdier','Stoutland','Purrloin','Liepard','Pansage','Simisage','Pansear','Simisear','Panpour','Simipour','Munna','Musharna','Pidove','Tranquill','Unfezant','Blitzle','Zebstrika','Roggenrola','Boldore','Gigalith','Woobat','Swoobat','Drilbur','Excadrill','Audino','Timburr','Gurdurr','Conkeldurr','Tympole','Palpitoad','Seismitoad','Throh','Sawk','Sewaddle','Swadloon','Leavanny','Venipede','Whirlipede','Scolipede','Cottonee','Whimsicott','Petilil','Lilligant','Basculin','Sandile','Krokorok','Krookodile','Darumaka','Darmanitan','Maractus','Dwebble','Crustle','Scraggy','Scrafty','Sigilyph','Yamask','Cofagrigus','Tirtouga','Carracosta','Archen','Archeops','Trubbish','Garbodor','Zorua','Zoroark','Minccino','Cinccino','Gothita','Gothorita','Gothitelle','Solosis','Duosion','Reuniclus','Ducklett','Swanna','Vanillite','Vanillish','Vanilluxe','Deerling','Sawsbuck','Emolga','Karrablast','Escavalier','Foongus','Amoonguss','Frillish','Jellicent','Alomomola','Joltik','Galvantula','Ferroseed','Ferrothorn','Klink','Klang','Klinklang','Tynamo','Eelektrik','Eelektross','Elgyem','Beheeyem','Litwick','Lampent','Chandelure','Axew','Fraxure','Haxorus','Cubchoo','Beartic','Cryogonal','Shelmet','Accelgor','Stunfisk','Mienfoo','Mienshao','Druddigon','Golett','Golurk','Pawniard','Bisharp','Bouffalant','Rufflet','Braviary','Vullaby','Mandibuzz','Heatmor','Durant','Deino','Zweilous','Hydreigon','Larvesta','Volcarona','Cobalion','Terrakion','Virizion','Tornadus','Thundurus','Reshiram','Zekrom','Landorus','Kyurem','Keldeo','Meloetta','Genesect','Chespin','Quilladin','Chesnaught','Fennekin','Braixen','Delphox','Froakie','Frogadier','Greninja','Bunnelby','Diggersby','Fletchling','Fletchinder','Talonflame','Scatterbug','Spewpa','Vivillon','Litleo','Pyroar','Flabébé','Floette','Florges','Skiddo','Gogoat','Pancham','Pangoro','Furfrou','Espurr','Meowstic','Honedge','Doublade','Aegislash','Spritzee','Aromatisse','Swirlix','Slurpuff','Inkay','Malamar','Binacle','Barbaracle','Skrelp','Dragalge','Clauncher','Clawitzer','Helioptile','Heliolisk','Tyrunt','Tyrantrum','Amaura','Aurorus','Sylveon','Hawlucha','Dedenne','Carbink','Goomy','Sliggoo','Goodra','Klefki','Phantump','Trevenant','Pumpkaboo','Gourgeist','Bergmite','Avalugg','Noibat','Noivern','Xerneas','Yveltal','Zygarde','Diancie','Hoopa','Volcanion','Rowlet','Dartrix','Decidueye','Litten','Torracat','Incineroar','Popplio','Brionne','Primarina','Pikipek','Trumbeak','Toucannon','Yungoos','Gumshoos','Grubbin','Charjabug','Vikavolt','Crabrawler','Crabominable','Oricorio','Cutiefly','Ribombee','Rockruff','Lycanroc','Wishiwashi','Mareanie','Toxapex','Mudbray','Mudsdale','Dewpider','Araquanid','Fomantis','Lurantis','Morelull','Shiinotic','Salandit','Salazzle','Stufful','Bewear','Bounsweet','Steenee','Tsareena','Comfey','Oranguru','Passimian','Wimpod','Golisopod','Sandygast','Palossand','Pyukumuku','Type: Null','Silvally','Minior','Komala','Turtonator','Togedemaru','Mimikyu','Bruxish','Drampa','Dhelmise','Jangmo-o','Hakamo-o','Kommo-o','Tapu Koko','Tapu Lele','Tapu Bulu','Tapu Fini','Cosmog','Cosmoem','Solgaleo','Lunala','Nihilego','Buzzwole','Pheromosa','Xurkitree','Celesteela','Kartana','Guzzlord','Necrozma','Magearna','Marshadow','Poipole','Naganadel','Stakataka','Blacephalon','Zeraora',]

natlist = ['Lonely', 'Brave', 'Adamant', 'Naughty', 'Bold', 'Relaxed', 'Impish', 'Lax', 'Timid', 'Hasty', 'Jolly', 'Naive', 'Modest', 'Mild', 'Quiet', 'Rash', 'Calm', 'Gentle', 'Sassy', 'Careful', 'Bashful', 'Quirky', 'Serious', 'Docile', 'Hardy']

bot = commands.Bot(command_prefix=";")
version = ("0.0.1c Alpha Build")

TOKEN = os.environ['TOKEN']
dburl = os.environ['DATABASE_URL']

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
async def mew(ctx):
    """Makes MewBot respond"""
    await ctx.send("Ping, latency: {}ms".format(int(bot.latency * 1000)))

@bot.command()
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
async def ping(ctx):
    start = time.monotonic()
    embed = discord.Embed(title="Pong!")
    embed.add_field(name="latency", value="{} ms".format(int(ctx.bot.latency*1000)))
    await ctx.send(embed=embed)

@bot.command()
async def trainer(ctx, user: discord.Member=None):
    tconn = await asyncpg.connect(dburl)
    if user is None:
        user = ctx.author
    rquery = '''SELECT redeems FROM users WHERE u_id = {}'''.format(ctx.author.id)
    tquery = '''SELECT tnick FROM users WHERE u_id = {}'''.format(ctx.author.id)
    uquery = '''SELECT upvotepoints FROM users WHERE u_id = {}'''.format(ctx.author.id)
    cquery = '''SELECT pokname FROM pokes WHERE selected = 1 AND ownerid = {}'''.format(ctx.author.id)
    redeems = await tconn.fetchval(rquery)
    tnick = await tconn.fetchval(tquery)
    uppoints = await tconn.fetchval(uquery)
    poke = await tconn.fetchval(cquery)
    embed = discord.Embed(title="{} Trainer Card".format(user.name))
    embed.add_field(name="Redeems", value=f'{redeems}')
    embed.add_field(name="Trainer Nick", value=f'{tnick}')
    embed.add_field(name="Upvote Points", value=f'{uppoints}')
    embed.add_field(name="Currently Selected Pokemon", value=f'{poke}')
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
    await tconn.close()

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="MewBot commands", description="The pokemon discord utility bot made for you!!!", color=0xeee657)
    embed.add_field(name="Ping", value="Pings the bot and shows it's latency")
    embed.add_field(name="Mew", value="A simple Ping, just responds with Mew!")
    embed.add_field(name="Trainer", value="Displays your Trainer Card and other information")
    embed.add_field(name="start", value="Start Playing Mewbot!!")
    embed.add_field(name="Trade", value="Trade Items, Redeems, Pokemon, and Credits!")
    embed.set_thumbnail(url='http://pm1.narvii.com/5848/b18cd35647528a7bdffc8e4b8e4d6a1465fc5253_00.jpg')
    await ctx.send(embed=embed)

@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(title="MewBot information", description="Bot information", color=0xeee657)

    # give info about you here
    embed.add_field(name="Dylee#6669", value="Developer", inline=False)

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    embed.add_field(name="User Count", value=f"{len(bot.users)}")

    embed.add_field(name="Discord Version", value=discord.__version__)

    embed.add_field(name="CPU Statistics", value=f"\nCPU Count **{psutil.cpu_count()}**\n\n CPU Frequency **{psutil.cpu_freq(percpu=True)}**\n\nRAM **{psutil.virtual_memory()}**")
    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite Me](https://discordapp.com/api/oauth2/authorize?client_id=493045795445276682&permissions=1342434418&scope=bot)")

    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    embed = discord.Embed(title="Invite Me", description="The invite link for MewBot")

    #invite link
    embed.add_field(name="Invite", value="[Invite MewBot](https://discordapp.com/api/oauth2/authorize?client_id=493045795445276682&permissions=8&scope=bot)")
    embed.add_field(name="User Count", value=f"{len(bot.users)}")
    await ctx.send(embed=embed)

@bot.command()
async def status(ctx):
    embed = discord.Embed(title="Bot development Status", description="information on the development of MewBot")

    #list

    embed.add_field(name="Current Build version", value="0.0.1b Alpha Build")

    embed.add_field(name="Bot Logging", value=":white_check_mark: Complete")

    embed.add_field(name="Addition of Simple Commands", value=":white_check_mark:")
    embed.add_field(name="Registering", value=":white_check_mark:")
    embed.add_field(name="EVs, IVs, and Stats", value=":white_check_mark:")
    embed.add_field(name="Held Items", value=":white_check_mark:")
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
    vowels = ['a', 'k', 'e', 't', 'u', 'i', 'o', 'l', 'o', 'm', 'y', 'i', 'e']
    vl = random.choice(vowels)
    if message.content.startswith(vl):
        channel = message.channel
        val1 = random.choice(pList)
        val = val1.lower() or val1.upper() or val1.capitalize()
        url = "https://img.pokemondb.net/artwork/vector/large/" + val.lower() + ".png"
        embed = discord.Embed(title="A Pokemon has spawned, identify it to catch it!")
        embed.set_image(url=url)
        await channel.send(embed=embed)
        def check(m):
            return m.content == val and m.channel == channel
        msg = await bot.wait_for('message', check=check, timeout=60)
        val = val.capitalize()


        #db code starts here


        pconn = await asyncpg.connect(dburl)
        hpiv = random.randint(1, 31)
        atkiv = random.randint(1, 31)
        defiv = random.randint(1, 31)
        spaiv = random.randint(1, 31)
        spdiv = random.randint(1, 31)
        speiv = random.randint(1, 31)
        plevel = random.randint(1, 100)
        nature = random.choice(natlist)
        expc = (plevel ** 3)
        pque = '''SELECT MAX(pnum) FROM pokes WHERE ownerid = {}'''.format(msg.author.id)
        pnum = await pconn.fetchval(pque)
        try:
            pnum += 1
        except TypeError as e:
            await message.channel.send("You need to Start with `start`")
        query2 = '''
            INSERT INTO pokes (pokname, hpiv, atkiv, defiv, spatkiv, spdefiv, speediv, hpev, atkev, defev, spatkev, spdefev, speedev, pokelevel, ownerid, pnum, selected, move1, move2, move3, move4, poknick, exp, nature, expcap)
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, $25)
            '''

        args = (val, hpiv, atkiv, defiv, spaiv, spdiv, speiv, 0, 0, 0, 0, 0, 0, plevel, msg.author.id, pnum, 0, 'tackle', 'tackle', 'tackle', 'tackle', 'None', 1, nature, expc)
        await pconn.execute(query2, *args)
        await channel.send(f'Congratulations <@{msg.author.id}>, you have successfully caught a {val}!')
        await pconn.close()
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
async def start_journey(ctx):
    embed = discord.Embed(title="Select a Starter!", description="Choose any of the Starters!")
    embed.add_field(name="...", value="You've been hypnotized by Mew, and instead of the normal starters, you are forced to pick between \n-Flowin, the Grass type fakemon, \n-Flire the fire type fakemon and \n-Aquino, the water type.")
    embed.set_thumbnail(url="https://nerdist.com/wp-content/uploads/2016/02/Screen-Shot-2016-02-02-at-12.05.40-PM-615x346.png")
    embed.set_image(url="https://pm1.narvii.com/6252/3746bb43045886ce9ec8498a6f7d96f520ed6341_hq.jpg") # you cannot set two images. either put one as a thumbnail or remove it
    embed.add_field(name="Pick a Starter!", value="...")
    start_msg = await ctx.send(embed=embed)
    for r in react_to_starter:
        await start_msg.add_reaction(r)
    def check(r, u):
        mcheck =( r.message.id == start_msg.id)
        rcheck = (r.emoji in react_to_starter)
        ucheck = (u == ctx.author)
        return mcheck and rcheck and ucheck
    reaction, user = await bot.wait_for("reaction_add", check=check, timeout=1234) # some timeout in seconds
    await ctx.send(f"You have selected {react_to_starter[reaction.emoji]} as your starter!")
    await ctx.send(react_to_starter[reaction.emoji])
    def pred(m):
        return m.author == message.author and m.channel == message.channel
    answer1 = (react_to_starter[reaction.emoji])
    values = ["Flowing", "Flire", "Aquino"]
    if (answer1) in values:
        tconn = await asyncpg.connect(dburl)
        pconn = await asyncpg.connect(dburl)
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
            return;
        else:
            await pconn.execute(query2, *args)
            query3 = '''
            INSERT INTO users (u_id, redeems, evpoints, tnick, upvotepoints)
            VALUES ($1, $2, $3, $4, $5)
            '''

            args2 = (ctx.author.id, 0, 0, 'None', 0)
            await tconn.execute(query3, *args2)
            await ctx.channel.send("Records successfully Added\nGoodluck!")
            await tconn.close()
            await pconn.close()



@bot.command()
async def pokemon(ctx):
    pconn = await asyncpg.connect(dburl)
    nquery = "SELECT pokname, pnum FROM pokes WHERE ownerid = {}".format(ctx.author.id)
    pk1 = await pconn.fetch(nquery)
    nrecord = [record['pokname'] for record in pk1]
    precord = [record['pnum'] for record in pk1]	   
    embed = discord.Embed(title='Your Pokemon List')	    
    for pn in precord:
        nr = nrecord[1-pn]
        embed.add_field(name='', value=f"{nr}{pn}", inline=False)
    await ctx.send(embed=embed)
    await pconn.close()
    
    
    
@bot.command()
async def moves(ctx):
    pconn = await asyncpg.connect(dburl)
    m1query = "SELECT move1 FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    m2query = "SELECT move2 FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    m3query = "SELECT move3 FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    m4query = "SELECT move4 FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
    m1 = await pconn.fetchval(m1query)
    m2 = await pconn.fetchval(m2query)
    m3 = await pconn.fetchval(m3query)
    m4 = await pconn.fetchval(m4query)
    embed = discord.Embed(title='Moves')
    embed.add_field(name='**Move 1**:', value=f'{m1}')
    embed.add_field(name='**Move 2**:', value=f'{m2}')
    
    embed.add_field(name='**Move 3**:', value=f'{m3}')
    
    embed.add_field(name='**Move 4**:', value=f'{m4}')
    await ctx.send(embed=embed)
    await pconn.close()
    
    
@bot.command()
async def select(ctx, val):
    pconn = await asyncpg.connect(dburl)
    await pconn.execute("UPDATE pokes SET selected = 0 WHERE selected = 1 AND ownerid = {0}".format(ctx.author.id, val))
    pque = '''UPDATE pokes SET selected = 1 WHERE ownerid = {0} and pnum = {1}'''.format(ctx.author.id, val)
    pnum = await pconn.execute(pque)
    await ctx.send("You have successfully selected your No. {0} Pokemon".format(val))
    await pconn.close()

@bot.command(pass_context=True)
async def shutdown(ctx):
    user = ctx.author
    if user.name == "Dylee":
        msg = await ctx.send("shutting down...")
        await msg.edit(content="Shutdown Complete, goodbye Dylee!")
        await bot.close()
    elif user.name != 'Dylee':
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
async def inspire(ctx):
    iE = discord.Embed(title="Inspire Me", description="...")
    iE.add_field(name="Here it is", value="you don't understand something unless you know how it works on one level of abstraction lower than you need to know to use it")
    iE.add_field("I hope you try harder! :wave:")
    await ctx.send(embed=iE)

@bot.command()
async def info(ctx):
    pconn = await asyncpg.connect(dburl)
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

    nature = await pconn.fetchval(natque)
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
    if pn == 'Flowing':
        pokemonSpeed = 73
        pokemonAtk = 99
        pokemonDef = 79
        pokemonSpa = 120
        pokemonSpd =110
        pokemonHp = 95
        pAb = 'Sizzling Growth'
        irul = 'https://cdn.discordapp.com/attachments/479175545481986088/497738691381559296/flowin.png'
    elif pn == 'Flire':
        pokemonSpeed = 110
        pokemonAtk = 120
        pokemonDef = 95
        pokemonSpa = 79
        pokemonSpd =99
        pokemonHp = 73
        pAb = 'Scorched feet'
        irul = 'https://cdn.discordapp.com/attachments/479175545481986088/497733271392878622/flire.png'

    elif pn == 'Aquino':
        pokemonSpeed = 95
        pokemonAtk = 79
        pokemonDef = 120
        pokemonSpa = 73
        pokemonSpd = 110
        pokemonHp = 99
        pAb = 'Eternal Rain'
        irul = 'https://cdn.discordapp.com/attachments/480885918354636804/497721785048104970/aquino.jpg'
    else:
        try:
            irul = 'https://img.pokemondb.net/artwork/vector/' + pn + '.png'
        except TypeError as e:
            await ctx.send(f'You need to `;start` first :facepalm: <@{ctx.author.id}>')
        r = requests.get('http://pokeapi.co/api/v2/pokemon/' + pn + '/')
        rJson = r.json()
        types = [t['type']['name'] for t in rJson['types']]
        tlist = ", ".join(types)
        pAb = rJson['abilities'][0]['ability']['name']
        pWeight = rJson['weight']/10
        pDexnum = rJson['id']
        pokemonSpeed = rJson['stats'][0]['base_stat']
        pokemonSpd = rJson['stats'][1]['base_stat']
        pokemonSpa = rJson['stats'][2]['base_stat']
        pokemonDef = rJson['stats'][3]['base_stat']
        pokemonAtk = rJson['stats'][4]['base_stat']
        pokemonHp = rJson['stats'][5]['base_stat']

    hp = round((((2*pokemonHp+hpiv+(0/4))*plevel)/100)+plevel+10)
    attack = round((((2*pokemonSpeed+atkiv+(0/4))*plevel)/100)+5)
    defense = round((((2*pokemonDef+defiv+(0/4))*plevel)/100)+5)
    specialattack = round((((2*pokemonSpa+spatkiv+(0/4))*plevel)/100)+5)
    specialdefense = round((((2*pokemonSpd+spdefiv+(0/4))*plevel)/100)+5)
    speed = round((((2*pokemonSpeed+speediv+(0/4))*plevel)/100)+5)

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

    embed = discord.Embed(title=f"Your Selected {pn}")
    embed.add_field(name="Pokemon Level", value=f"{plevel}")
    embed.add_field(name="Hit Points (HP)", value=f"{hp} | {hpiv} IV")
    embed.add_field(name="Attack", value=f"{attack} | {atkiv} IV")
    embed.add_field(name="Defense", value=f"{defense} | {defiv} IV")
    embed.add_field(name="Special Attack", value=f"{specialattack} | {spatkiv} IV")
    embed.add_field(name="Special Defense", value=f"{specialdefense} | {spdefiv} IV")
    embed.add_field(name="Speed", value=f"{speed} | {speediv} IV")
    embed.add_field(name="Held Item", value=f"{hi}")
    embed.set_image(url=irul)
    await ctx.send(embed=embed)
    await pconn.close()


@bot.command()
async def pokedex(ctx, *, val):
    if ' ' in val:
        val = val.replace(' ', '-')
    r = requests.get('http://pokeapi.co/api/v2/pokemon/' + val + '/')
    rJson = r.json()
    pName = rJson['name']
    types = [t['type']['name'] for t in rJson['types']]
    tlist = ", ".join(types)
    pAb = rJson['abilities'][0]['ability']['name']
    pWeight = rJson['weight']/10
    pDexnum = rJson['id']
    pokemonSpeed = rJson['stats'][0]['base_stat']
    pokemonSpd = rJson['stats'][1]['base_stat']
    pokemonSpa = rJson['stats'][2]['base_stat']
    pokemonDef = rJson['stats'][3]['base_stat']
    pokemonAtk = rJson['stats'][4]['base_stat']
    pokemonHp = rJson['stats'][5]['base_stat']
    embed = discord.Embed(title=val.capitalize(), description="")
    embed.add_field(name="Pokemon information", value=f"{pName.capitalize()} \n**Ability**: {pAb} \n**Types**: {tlist} \n**Weight**: {pWeight} Kgs \n**Pokedex Number**: {pDexnum}")
    embed.add_field(name="Stats", value=f"HP: {pokemonHp}\nAttack: {pokemonAtk} \nDefense: {pokemonDef}\nSpecial Attack: {pokemonSpa}\nSpecial Defense: {pokemonSpd}\nSpeed: {pokemonSpeed}")
    embed.set_image(url='https://img.pokemondb.net/artwork/vector/' + val + '.png')

    await ctx.send(embed=embed)

@bot.listen()
async def on_guild_join(guild):
    if (len(guild.members) >= 50):
        tconn = await asyncpg.connect(dburl)
        query = '''UPDATE users SET redeems = 10 WHERE u_id = {}'''.format(guild.owner.id)
        await tconn.execute(query)
        await ctx.guild.owner.send("You have Received 10 Redeems for Adding me :smile:!,.. but remove me and it's gone :cry:")
        await tconn.close()
    else:
        return
@bot.listen()
async def on_guild_remove(guild):
    tconn = await asyncpg.connect(dburl)
    query = '''UPDATE users SET redeems = 0 WHERE u_id = {}'''.format(guild.owner.id)
    await tconn.execute(query)
    await guild.owner.send("Goodbye to 10 Redeems :cry:")
    await tconn.close()

@bot.command()
async def redeem(ctx, val):
    if val in pList:
        pconn = await asyncpg.connect(dburl)
        tconn = await asyncpg.connect(dburl)
        hpiv = random.randint(1, 31)
        atkiv = random.randint(1, 31)
        defiv = random.randint(1, 31)
        spaiv = random.randint(1, 31)
        spdiv = random.randint(1, 31)
        speiv = random.randint(1, 31)
        pque = '''SELECT MAX(pnum) FROM pokes WHERE ownerid = {}'''.format(ctx.author.id)
        rque = '''SELECT redeems FROM users WHERE u_id = {}'''.format(ctx.author.id)
        rnum = await tconn.fetchval(rque)
        rnat = random.choice(natlist)
        if rnum >= 1:
            pnum = await pconn.fetchval(pque)
            rnum-=1
            pnum+=1
            rquery = '''UPDATE users SET redeems = {0} WHERE u_id = {1}'''.format(rnum, ctx.author.id)
            query2 = '''
                INSERT INTO pokes (pokname, hpiv, atkiv, defiv, spatkiv, spdefiv, speediv, hpev, atkev, defev, spatkev, spdefev, speedev, pokelevel, ownerid, pnum, selected, move1, move2, move3, move4, hitem, exp, nature, expcap, poknick)
                VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, $25, $26)
                '''

            args = (val, hpiv, atkiv, defiv, spaiv, spdiv, speiv, 0, 0, 0, 0, 0, 0, 1, ctx.author.id, pnum, 0, 'tackle', 'tackle', 'tackle', 'tackle', 'None', 0, rnat, 35,'None')
            await ctx.channel.send(f"Here's your {val}!")
            await pconn.execute(query2, *args)
            await tconn.close()
            await pconn.close()
            










##########################################################################
#________________________________________________________________________#
##########################################################################
@bot.command()
async def trade(ctx, user: discord.Member):
    pconn = await asyncpg.connect(dburl)
    tconn = await asyncpg.connect(dburl)
    await ctx.channel.send(f"<@{ctx.author.id}> has began a trade with <@{user.id}>.")
    await ctx.channel.send (f"Trade between {ctx.author.name} and {user.name}, {user.name} type `;accept trade` to accept")
    emsg = await ctx.send(f"{ctx.author.name} is offering: \n{user.name} is offering: \nUse ``;addc credit amount>`` for credits and ``;addp poke number`` for pokemon")
    def check(c, u):
        return cauthor.id == ctx.author.id and uauthor.id == user.id
    msg = await bot.wait_for('message', check=check, timeout=30)
    if msg.startswith.startswith(';accept trade') or msg.content.startswith(';accept'):
        def pred(c, u):
            return cauthor.id == cauthor.id and uauthor.id == uauthor.id
        tmsg = await bot.wait_for('message', check=pred)
        if tmsg.content.startswith(';addc'):
            cred = tmsg.split()
            credamt = int(cred[1])
            adderc = await tconn.fetchval(f'SELECT credits FROM trainers WHERE u_id = {msg.author.id}')
            getterc = await tconn.fetchval(f'SELECT credits FROM trainers WHERE u_id = {uauthor.id}')
            if adderc < credamt: 
                return;
            acred = acred - credamt
            ncred = ncred + credamt
            acquery = f"UPDATE users SET credits = {acred} WHERE u_id = {tmsg.author.id}"
            gcquery = f"UPDATE users SET credits = {ncred} WHERE u_id = {uauthor.id}"
            emsg.edit(content=f"{tmsg.author.name} has added:**_{credamt}__** Credits")
            ccquery = f"UPDATE users SET credits = "
        elif msg.content.startswith(';addp'):
            pdat = tmsg.split()
            pnumber = tmsg[1]
            query = f"SELECT pokename FROM pokes WHERE pnum = {pnumber} AND ownerid = {tmsg.author.id}"
            pnames = await pconn.fetchval(query)
            query2 = f"SELECT pokelevel FROM pokes WHERE pnum = {pnumber} AND ownerid = {tmsg.author.id}"
            plevel = await pconn.fetchval(query2)
            emsg.edit(content=f"{msg.author.name} has added a :**_Level {plevel}{pnames}__**")
            cquery = f"UPDATE pokes SET ownerid = {uauthor.id} WHERE pnum = {pnumber} AND ownerid = {tmsg.author.id}"
            def ccheck(c, r):
                return confirmer == cauthor.id and receiver == uauthor.id
            cmsg = await bot.wait_for('message', check=ccheck, timeout=65)
            if cmsg == ';confirm' and cmsg.author.id == cauthor.id and uauthor.id:
                await tconn.execute(acquery)
                await tconn.execute(gcquery)
                await pconn.execute(cquery)
                await pconn.close()
                await tconn.close()
    elif msg.content.startswith(';deny'):
        await msg.channe.send(f"<@{msg.author.id}> has cancelled the trade")
        return


@bot.command()
async def pexec(ctx, *, val):
    pconn = await asyncpg.connect(dburl)
    if ctx.author.id == 358293206900670467:
        await pconn.execute(val)
    else:
        await ctx.send("Only Dylee can use this command")

@bot.command()
async def texec(ctx, *, val):
    tconn = await asyncpg.connect(dburl)
    if ctx.author.id == 358293206900670467:
        await tconn.execute(val)
    else:
        await ctx.send("Only Dylee can use this command")



############################################################################
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
##############################################################################
@bot.command(name="eval", hidden=True, pass_context=True, enabled=False)
async def evaluate(ctx, *, code: str):
    """Extremely unsafe eval command."""
    code = code.strip("` ")
    result = None
    try:
        result = eval(code)
        if asyncio.iscoroutine(result):
            result = await result
    except Exception as err:
        await bot.say(python.format(type(err).__name__ + ": " + str(error)))
        return

    await bot.say(f"```py\n{result}\n```")

#############################################################################3
###333333333333333333battles###########################333
#####################33333333nothing goes here
@bot.command()
async def battle(ctx, user: discord.Member):
    pconn = await asyncpg.connect(dburl)
    if user == None:
            await ctx.channel.send("You can not battle yourself")
            return
    await ctx.channel.send(f"<@{user.id}>, you're being challenged by <@{ctx.author.id}>, type `;accept` to accept")
    def check(m):
            return m.channel == ctx.channel and m.user == user.id
    msg = await bot.wait_for('message', check=check, timeout=30)
    if msg != ';accept':
        await ctx.channel.send("Battle Rejected")
    elif msg == ';accept':
                ######################################################3
                #ctx stats
        pquery = "SELECT pokname FROM pokes WHERE selected = 1 ownerid = {}".format(ctx.author.id)
        atquery = "SELECT atkiv FROM pokes WHERE selected = 1 ownerid = {}".format(ctx.author.id)
        dequery = "SELECT defiv FROM pokes WHERE selected = 1 ownerid = {}".format(ctx.author.id)
        spaquery = "SELECT spatkiv FROM pokes WHERE selected = 1 ownerid = {}".format(ctx.author.id)
        spdquery = "SELECT spdefiv FROM pokes WHERE selected = 1 ownerid = {}".format(ctx.author.id)
        spequery = "SELECT speediv FROM pokes WHERE selected = 1 ownerid = {}".format(ctx.author.id)
        plquery = "SELECT pokelevel FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
        pnquery = "SELECT poknick FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
        hiquery = "SELECT hitem FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
        hpquery = "SELECT hpiv FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)
        natque = "SELECT nature FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id)

        nature = await pconn.fetchval(natque)
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
        r = requests.get('http://pokeapi.co/api/v2/pokemon/' + pn + '/')
        rJson = r.json()
        types = [t['type']['name'] for t in rJson['types']]
        tlist = ", ".join(types)
        pAb = rJson['abilities'][0]['ability']['name']
        pWeight = rJson['weight']/10
        pDexnum = rJson['id']
        pokemonSpeed = rJson['stats'][0]['base_stat']
        pokemonSpd = rJson['stats'][1]['base_stat']
        pokemonSpa = rJson['stats'][2]['base_stat']
        pokemonDef = rJson['stats'][3]['base_stat']
        pokemonAtk = rJson['stats'][4]['base_stat']
        pokemonHp = rJson['stats'][5]['base_stat']

        hp = ((((2*pokemonHp+hpiv+(0/4))*plevel)/100)+plevel+10)
        attack = ((((2*pokemonSpeed+atkiv+(0/4))*plevel)/100)+5)
        defense = ((((2*pokemonDef+defiv+(0/4))*plevel)/100)+5)
        specialattack = ((((2*pokemonSpa+spatkiv+(0/4))*plevel)/100)+5)
        specialdefense = ((((2*pokemonSpd+spdefiv+(0/4))*plevel)/100)+5)
        speed = ((((2*pokemonSpeed+speediv+(0/4))*plevel)/100)+5)

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
                #######################################################
                ######################################################################################user stats
        pquery = "SELECT pokname FROM pokes WHERE selected = 1 ownerid = {}".format(user.id)
        atquery = "SELECT atkiv FROM pokes WHERE selected = 1 ownerid = {}".format(user.id)
        dequery = "SELECT defiv FROM pokes WHERE selected = 1 ownerid = {}".format(user.id)
        spaquery = "SELECT spatkiv FROM pokes WHERE selected = 1 ownerid = {}".format(user.id)
        spdquery = "SELECT spdefiv FROM pokes WHERE selected = 1 ownerid = {}".format(user.id)
        spequery = "SELECT speediv FROM pokes WHERE selected = 1 ownerid = {}".format(user.id)
        plquery = "SELECT pokelevel FROM pokes WHERE selected = 1 AND ownerid = {}".format(user.id)
        pnquery = "SELECT poknick FROM pokes WHERE selected = 1 AND ownerid = {}".format(user.id)
        hiquery = "SELECT hitem FROM pokes WHERE selected = 1 AND ownerid = {}".format(user.id)
        hpquery = "SELECT hpiv FROM pokes WHERE selected = 1 AND ownerid = {}".format(user.id)
        natque = "SELECT nature FROM pokes WHERE selected = 1 AND ownerid = {}".format(user.id)

        nature = await pconn.fetchval(natque)
        upn = await pconn.fetchval(pquery)
        atkiv = await pconn.fetchval(atquery)
        defiv = await pconn.fetchval(dequery)
        spatkiv = await pconn.fetchval(spaquery)
        spdefiv = await pconn.fetchval(spdquery)
        speediv= await pconn.fetchval(spequery)
        pnick = await pconn.fetchval(pnquery)
        plevel = await pconn.fetchval(plquery)
        hpiv = await pconn.fetchval(hpquery)
        hi = await pconn.fetchval(hiquery)
        r = requests.get('http://pokeapi.co/api/v2/pokemon/' + upn + '/')
        rJson = r.json()
        utypes = [t['type']['name'] for t in rJson['types']]
        tlist = ", ".join(types)
        pAb = rJson['abilities'][0]['ability']['name']
        pWeight = rJson['weight']/10
        upDexnum = rJson['id']
        pokemonSpeed = rJson['stats'][0]['base_stat']
        pokemonSpd = rJson['stats'][1]['base_stat']
        pokemonSpa = rJson['stats'][2]['base_stat']
        pokemonDef = rJson['stats'][3]['base_stat']
        pokemonAtk = rJson['stats'][4]['base_stat']
        pokemonHp = rJson['stats'][5]['base_stat']

        uhp = ((((2*pokemonHp+hpiv+(0/4))*plevel)/100)+plevel+10)
        uattack = ((((2*pokemonSpeed+atkiv+(0/4))*plevel)/100)+5)
        udefense = ((((2*pokemonDef+defiv+(0/4))*plevel)/100)+5)
        uspecialattack = ((((2*pokemonSpa+spatkiv+(0/4))*plevel)/100)+5)
        uspecialdefense = ((((2*pokemonSpd+spdefiv+(0/4))*plevel)/100)+5)
        uspeed = ((((2*pokemonSpeed+speediv+(0/4))*plevel)/100)+5)

        if nature == 'Adamant':
                uattack = attack*1.1
                uspecialattack *= 0.9
        elif nature == 'Bold':
                udefense *= 1.1
                uattack *= 0.9
        elif nature == 'Brave':
                uattack *= 1.1
                uspeed *= 0.9
        elif nature == 'Calm':
                uspecialdefense *= 1.1
                uattack *= 0.9
        elif nature == 'careful':
                uspecialdefense *= 1.1
                uspecialattack *= 0.9
        elif nature == 'Gentle':
                uspecialdefense *= 1.1
                udefense *= 0.9
        elif nature == 'Hasty':
                uspeed *= 1.1
                udefense *= 0.9
        elif nature == 'Impish':
                udefense *= 1.1
                uspecialattack *= 0.9
        elif nature == 'Jolly':
                uspeed *= 1.1
                uspecialattack *= 0.9
        elif nature == 'Lax':
                udefense *= 1.1
                uspecialdefense *= 0.9
        elif nature == 'Lonely':
                uattack *= 1.1
                udefense *= 0.9
        elif nature == 'Mild':
                uspecialattack *= 1.1
                udefense *= 0.9
        elif nature == 'Modest':
                uspecialattack *= 1.1
                uattack *= 0.9
        elif nature == 'Naive':
                uspeed *= 1.1
                uspecialdefense *= 0.9
        elif nature == 'Naughty':
                uattack *= 1.1
                uspecialdefense *= 0.9
        elif nature == 'Quiet':
                uspecialattack *= 1.1
                uspeed *= 0.9
        elif nature == 'Rash':
                uspecialattack *= 1.1
                uspecialdefense *= 0.9
        elif nature == 'Relaxed':
                udefense *= 1.1
                uspeed *= 0.9
        elif nature == 'Sassy':
                uspecialdefense *= 1.1
                uspeed *= 0.9
        elif nature == 'Tired':
                uspeed *= 1.1
                uattack *= 0.9

        colorTable = [255]*256
        colorTable[0] = 0 #anything black (0) will be made transparent
        desired_size = 288

        pBack = requests.get('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/' + pDexnum + '.png')

        pFront = requests.get('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/' + upDexnum + '.png')
        s = i.open(BytesIO(pBack.content))

        g = i.open(BytesIO(pFront.content))

        bg = i.open("./pkbg2.png")

        swidth, sheight = s.size
        print("Size of Mewback = {} {}".format(swidth, sheight))
        gwidth, gheight = g.size
        print("Size of mewfront = {} {}".format(gwidth, gheight))
        bgw, bgh = bg.size
        print("Size of Bgfront = {} {}".format(bgw, bgh))
        #perfect back = 35, 81

        basewidth = 300

        wpercent = (basewidth/float(s.size[0]))

        hsize = int((float(s.size[1])*float(wpercent)))

        s = s.resize((basewidth, hsize), i.ANTIALIAS)

        g = g.resize((basewidth, hsize), i.ANTIALIAS)


        area = (510, 100)

        mask = g.point (colorTable, '1')
        bg.paste(g, area, mask)

        mask = s.point (colorTable, '1')

        area2 = (170, 290)
        bg.paste(s, area2, mask)

        bg.save('./bg1', 'png')
        embed=discord.Embed(title=f"Battle Between {p1} and {p2}")
        embed.set_image('bg1.png')
        await ctx.send(embed=embed)
        os.remove('bg1.png')
        await ctx.channel.send(f'<@{ctx.author.id} use a Move!')
        await pconn.close()

bot.run(TOKEN)

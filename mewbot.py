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
import logging
pList = ['Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Caterpie','Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Ekans','Arbok','Pikachu','Raichu','Sandshrew','Sandslash','Nidoran♀','Nidorina','Nidoqueen','Nidoran♂','Nidorino','Nidoking','Clefairy','Clefable','Vulpix','Ninetales','Jigglypuff','Wigglytuff','Zubat','Golbat','Oddish','Gloom','Vileplume','Paras','Parasect','Venonat','Venomoth','Diglett','Dugtrio','Meowth','Persian','Psyduck','Golduck','Mankey','Primeape','Growlithe','Arcanine','Poliwag','Poliwhirl','Poliwrath','Abra','Kadabra','Alakazam','Machop','Machoke','Machamp','Bellsprout','Weepinbell','Victreebel','Tentacool','Tentacruel','Geodude','Graveler','Golem','Ponyta','Rapidash','Slowpoke','Slowbro','Magnemite','Magneton','Farfetch’d','Doduo','Dodrio','Seel','Dewgong','Grimer','Muk','Shellder','Cloyster','Gastly','Haunter','Gengar','Onix','Drowzee','Hypno','Krabby','Kingler','Voltorb','Electrode','Exeggcute','Exeggutor','Cubone','Marowak','Hitmonlee','Hitmonchan','Lickitung','Koffing','Weezing','Rhyhorn','Rhydon','Chansey','Tangela','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Mr. Mime','Scyther','Jynx','Electabuzz','Magmar','Pinsir','Tauros','Magikarp','Gyarados','Lapras','Ditto','Eevee','Vaporeon','Jolteon','Flareon','Porygon','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax', 'Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Caterpie','Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Ekans','Arbok','Pikachu','Raichu','Sandshrew','Sandslash','Nidoran♀','Nidorina','Nidoqueen','Nidoran♂','Nidorino','Nidoking','Clefairy','Clefable','Vulpix','Ninetales','Jigglypuff','Wigglytuff','Zubat','Golbat','Oddish','Gloom','Vileplume','Paras','Parasect','Venonat','Venomoth','Diglett','Dugtrio','Meowth','Persian','Psyduck','Golduck','Mankey','Primeape','Growlithe','Arcanine','Poliwag','Poliwhirl','Poliwrath','Abra','Kadabra','Alakazam','Machop','Machoke','Machamp','Bellsprout','Weepinbell','Victreebel','Tentacool','Tentacruel','Geodude','Graveler','Golem','Ponyta','Rapidash','Slowpoke','Slowbro','Magnemite','Magneton','Farfetch’d','Doduo','Dodrio','Seel','Dewgong','Grimer','Muk','Shellder','Cloyster','Gastly','Haunter','Gengar','Onix','Drowzee','Hypno','Krabby','Kingler','Voltorb','Electrode','Exeggcute','Exeggutor','Cubone','Marowak','Hitmonlee','Hitmonchan','Lickitung','Koffing','Weezing','Rhyhorn','Rhydon','Chansey','Tangela','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Mr. Mime','Scyther','Jynx','Electabuzz','Magmar','Pinsir','Tauros','Magikarp','Gyarados','Lapras','Ditto','Eevee','Vaporeon','Jolteon','Magikarp','Gyarados','Lapras','Ditto','Eevee','Vaporeon','Jolteon','Flareon','Porygon','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax', 'Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Caterpie','Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Ekans','Arbok','Pikachu','Raichu','Sandshrew','Sandslash','Nidoran♀','Nidorina','Nidoqueen','Nidoran♂','Nidorino','Nidoking','Clefairy','Clefable','Vulpix','Ninetales','Jigglypuff','Wigglytuff','Zubat','Golbat','Oddish','Gloom','Vileplume','Paras','Parasect','Venonat','Venomoth','Diglett','Dugtrio','Meowth','Persian','Psyduck','Golduck','Mankey','Primeape','Growlithe','Arcanine','Poliwag','Poliwhirl','Poliwrath','Abra','Kadabra','Alakazam','Machop','Machoke','Machamp','Bellsprout','Weepinbell','Victreebel','Tentacool','Tentacruel','Geodude','Graveler','Golem','Ponyta','Rapidash','Slowpoke','Slowbro','Magnemite','Magneton','Farfetch’d','Doduo','Dodrio','Seel','Dewgong','Grimer','Muk','Shellder','Cloyster','Gastly','Haunter','Gengar','Onix','Drowzee','Hypno','Krabby','Kingler','Voltorb','Electrode','Exeggcute','Exeggutor','Cubone','Marowak','Hitmonlee','Hitmonchan','Lickitung','Koffing','Weezing','Rhyhorn','Rhydon','Chansey','Tangela','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Mr. Mime','Scyther','Jynx','Electabuzz','Magmar','Pinsir','Tauros','Magikarp','Gyarados','Lapras','Ditto','Eevee','Vaporeon','Jolteon','Flareon','Porygon','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax','Articuno','Zapdos','Moltres','Dratini','Dragonair','Dragonite','Mewtwo','Mew','Chikorita','Bayleef','Meganium','Cyndaquil','Quilava','Typhlosion','Totodile','Croconaw','Feraligatr','Sentret','Furret','Hoothoot','Noctowl','Ledyba','Ledian','Spinarak','Ariados','Crobat','Chinchou','Lanturn','Pichu','Cleffa','Igglybuff','Togepi','Togetic','Natu','Xatu','Mareep','Flaaffy','Ampharos','Bellossom','Marill','Azumarill','Sudowoodo','Politoed','Hoppip','Skiploom','Jumpluff','Aipom','Sunkern','Sunflora','Yanma','Wooper','Quagsire','Espeon','Umbreon','Murkrow','Slowking','Misdreavus','Unown','Wobbuffet','Girafarig','Pineco','Forretress','Dunsparce','Gligar','Steelix','Snubbull','Granbull','Qwilfish','Scizor','Shuckle','Heracross','Sneasel','Teddiursa','Ursaring','Slugma','Magcargo','Swinub','Piloswine','Corsola','Remoraid','Octillery','Delibird','Mantine','Skarmory','Houndour','Houndoom','Kingdra','Phanpy','Donphan','Porygon2','Stantler','Smeargle','Tyrogue','Hitmontop','Smoochum','Elekid','Magby','Miltank','Blissey','Raikou','Entei','Suicune','Larvitar','Pupitar','Tyranitar','Lugia','Ho-Oh','Celebi','Treecko','Grovyle','Sceptile','Torchic','Combusken','Blaziken','Mudkip','Marshtomp','Swampert','Poochyena','Mightyena','Zigzagoon','Linoone','Wurmple','Silcoon','Beautifly','Cascoon','Dustox','Lotad','Lombre','Ludicolo','Seedot','Nuzleaf','Shiftry','Taillow','Swellow','Wingull','Pelipper','Ralts','Kirlia','Gardevoir','Surskit','Masquerain','Shroomish','Breloom','Slakoth','Vigoroth','Slaking','Nincada','Ninjask','Shedinja','Whismur','Loudred','Exploud','Makuhita','Hariyama','Azurill','Nosepass','Skitty','Delcatty','Sableye','Mawile','Aron','Lairon','Aggron','Meditite','Medicham','Electrike','Manectric','Plusle','Minun','Volbeat','Illumise','Roselia','Gulpin','Swalot','Carvanha','Sharpedo','Wailmer','Wailord','Numel','Camerupt','Torkoal','Spoink','Grumpig','Spinda','Trapinch','Vibrava','Flygon','Cacnea','Cacturne','Swablu','Altaria','Zangoose','Seviper','Lunatone','Solrock','Barboach','Whiscash','Corphish','Crawdaunt','Baltoy','Claydol','Lileep','Cradily','Anorith','Armaldo','Feebas','Milotic','Castform','Kecleon','Shuppet','Banette','Duskull','Dusclops','Tropius','Chimecho','Absol','Wynaut','Snorunt','Glalie','Spheal','Sealeo','Walrein','Clamperl','Huntail','Gorebyss','Relicanth','Luvdisc','Treecko','Grovyle','Sceptile','Torchic','Combusken','Blaziken','Mudkip','Marshtomp','Swampert','Poochyena','Mightyena','Zigzagoon','Linoone','Wurmple','Silcoon','Beautifly','Cascoon','Dustox','Lotad','Lombre','Ludicolo','Seedot','Nuzleaf','Shiftry','Taillow','Swellow','Wingull','Pelipper','Ralts','Kirlia','Gardevoir','Surskit','Masquerain','Shroomish','Breloom','Slakoth','Vigoroth','Slaking','Nincada','Ninjask','Shedinja','Whismur','Loudred','Exploud','Makuhita','Hariyama','Azurill','Nosepass','Skitty','Delcatty','Sableye','Mawile','Aron','Lairon','Aggron','Meditite','Medicham','Electrike','Manectric','Plusle','Minun','Volbeat','Illumise','Roselia','Gulpin','Swalot','Carvanha','Sharpedo','Wailmer','Wailord','Numel','Camerupt','Torkoal','Spoink','Grumpig','Spinda','Trapinch','Vibrava','Flygon','Cacnea','Cacturne','Swablu','Yanma','Wooper','Quagsire','Espeon','Umbreon','Murkrow','Slowking','Misdreavus','Unown','Wobbuffet','Girafarig','Pineco','Forretress','Dunsparce','Gligar','Steelix','Snubbull','Granbull','Qwilfish','Scizor','Shuckle','Heracross','Sneasel','Teddiursa','Ursaring','Slugma','Magcargo','Swinub','Piloswine','Corsola','Remoraid','Octillery','Delibird','Mantine','Skarmory','Houndour','Houndoom','Kingdra','Phanpy','Donphan','Porygon2','Stantler','Smeargle','Tyrogue','Hitmontop','Smoochum','Elekid','Magby','Miltank','Blissey','Raikou','Entei','Suicune','Larvitar','Pupitar','Tyranitar','Lugia','Ho-Oh','Celebi','Treecko','Grovyle','Sceptile','Torchic','Combusken','Blaziken','Mudkip','Marshtomp','Swampert','Poochyena','Mightyena','Zigzagoon','Linoone','Wurmple','Silcoon','Beautifly','Cascoon','Dustox','Lotad','Lombre','Ludicolo','Seedot','Nuzleaf','Shiftry','Taillow','Swellow','Wingull','Pelipper','Ralts','Kirlia','Gardevoir','Surskit','Masquerain','Shroomish','Breloom','Slakoth','Vigoroth','Slaking','Nincada','Ninjask','Shedinja','Whismur','Loudred','Exploud','Makuhita','Hariyama','Azurill','Nosepass','Skitty','Delcatty','Sableye','Mawile','Aron','Lairon','Aggron','Meditite','Medicham','Electrike','Manectric','Plusle','Minun','Volbeat','Illumise','Roselia','Gulpin','Swalot','Carvanha','Sharpedo','Wailmer','Wailord','Numel','Camerupt','Torkoal','Spoink','Grumpig','Spinda','Trapinch','Vibrava','Flygon','Cacnea','Cacturne','Swablu','Altaria','Zangoose','Seviper','Lunatone','Solrock','Barboach','Whiscash','Corphish','Crawdaunt','Baltoy','Claydol','Lileep','Cradily','Anorith','Armaldo','Feebas','Milotic','Castform','Kecleon','Shuppet','Banette','Duskull','Dusclops','Tropius','Chimecho','Absol','Wynaut','Snorunt','Glalie','Spheal','Sealeo','Walrein','Clamperl','Huntail','Gorebyss','Relicanth','Luvdisc','Treecko','Grovyle','Sceptile','Torchic','Combusken','Blaziken','Mudkip','Marshtomp','Swampert','Poochyena','Mightyena','Zigzagoon','Linoone','Wurmple','Silcoon','Beautifly','Cascoon','Dustox','Lotad','Lombre','Ludicolo','Seedot','Nuzleaf','Shiftry','Taillow','Swellow','Wingull','Pelipper','Ralts','Kirlia','Gardevoir','Surskit','Masquerain','Shroomish','Breloom','Slakoth','Vigoroth','Slaking','Nincada','Ninjask','Shedinja','Whismur','Loudred','Exploud','Makuhita','Hariyama','Azurill','Nosepass','Skitty','Delcatty','Sableye','Mawile','Aron','Lairon','Aggron','Meditite','Medicham','Electrike','Manectric','Plusle','Minun','Volbeat','Illumise','Roselia','Gulpin','Swalot','Carvanha','Sharpedo','Wailmer','Wailord','Numel','Camerupt','Torkoal','Spoink','Grumpig','Spinda','Trapinch','Vibrava','Flygon','Cacnea','Cacturne','Swablu','Altaria','Zangoose','Seviper','Lunatone','Solrock','Barboach','Whiscash','Corphish','Crawdaunt','Baltoy','Claydol','Lileep','Cradily','Anorith','Armaldo','Feebas','Milotic','Castform','Kecleon','Shuppet','Banette','Duskull','Dusclops','Tropius','Chimecho','Absol','Wynaut','Snorunt','Glalie','Spheal','Sealeo','Walrein','Clamperl','Huntail','Gorebyss','Relicanth','Luvdisc','Bagon','Shelgon','Salamence','Beldum','Metang','Metagross','Regirock','Regice','Registeel','Latias','Latios','Kyogre','Groudon','Rayquaza','Jirachi','Deoxys','Turtwig','Grotle','Torterra','Chimchar','Monferno','Infernape','Piplup','Prinplup','Empoleon','Starly','Staravia','Staraptor','Bidoof','Bibarel','Kricketot','Kricketune','Shinx','Luxio','Luxray','Budew','Roserade','Cranidos','Rampardos','Shieldon','Bastiodon','Burmy','Wormadam','Mothim','Combee','Vespiquen','Pachirisu','Buizel','Floatzel','Cherubi','Cherrim','Shellos','Gastrodon','Ambipom','Drifloon','Drifblim','Buneary','Lopunny','Mismagius','Honchkrow','Glameow','Purugly','Chingling','Stunky','Skuntank','Bronzor','Bronzong','Bonsly','Mime Jr.','Happiny','Chatot','Spiritomb','Gible','Gabite','Garchomp','Munchlax','Riolu','Lucario','Hippopotas','Hippowdon','Skorupi','Drapion','Croagunk','Toxicroak','Carnivine','Finneon','Lumineon','Mantyke','Snover','Abomasnow','Weavile','Magnezone','Lickilicky','Rhyperior','Tangrowth','Electivire','Magmortar','Togekiss','Yanmega','Leafeon','Glaceon','Gliscor','Mamoswine','Porygon-Z','Gallade','Probopass','Dusknoir','Froslass','Turtwig','Grotle','Torterra','Chimchar','Monferno','Infernape','Piplup','Prinplup','Empoleon','Starly','Staravia','Staraptor','Bidoof','Bibarel','Kricketot','Kricketune','Shinx','Luxio','Luxray','Budew','Roserade','Cranidos','Rampardos','Shieldon','Bastiodon','Burmy','Wormadam','Mothim','Combee','Vespiquen','Pachirisu','Buizel','Floatzel','Cherubi','Cherrim','Shellos','Gastrodon','Ambipom','Drifloon','Drifblim','Buneary','Lopunny','Mismagius','Honchkrow','Glameow','Purugly','Chingling','Stunky','Skuntank','Bronzor','Bronzong','Bonsly','Mime Jr.','Happiny','Chatot','Spiritomb','Gible','Gabite','Garchomp','Munchlax','Riolu','Lucario','Hippopotas','Hippowdon','Skorupi','Drapion','Croagunk','Toxicroak','Carnivine','Finneon','Lumineon','Mantyke','Snover','Abomasnow','Weavile','Magnezone','Lickilicky','Rhyperior','Tangrowth','Electivire','Magmortar','Togekiss','Yanmega','Leafeon','Glaceon','Gliscor','Mamoswine','Porygon-Z','Gallade','Probopass','Dusknoir','Froslass','Rotom','Uxie','Mesprit','Azelf','Dialga','Palkia','Heatran','Regigigas','Giratina','Cresselia','Phione','Manaphy','Darkrai','Shaymin','Arceus','Victini','Snivy','Servine','Serperior','Tepig','Pignite','Emboar','Oshawott','Dewott','Samurott','Patrat','Watchog','Lillipup','Herdier','Stoutland','Purrloin','Liepard','Pansage','Simisage','Pansear','Simisear','Panpour','Simipour','Munna','Musharna','Pidove','Tranquill','Unfezant','Blitzle','Zebstrika','Roggenrola','Boldore','Gigalith','Woobat','Swoobat','Drilbur','Excadrill','Audino','Timburr','Gurdurr','Conkeldurr','Tympole','Palpitoad','Seismitoad','Throh','Sawk','Sewaddle','Swadloon','Leavanny','Venipede','Whirlipede','Scolipede','Cottonee','Whimsicott','Petilil','Lilligant','Basculin','Sandile','Krokorok','Krookodile','Darumaka','Darmanitan','Maractus','Dwebble','Crustle','Scraggy','Scrafty','Sigilyph','Yamask','Cofagrigus','Tirtouga','Carracosta','Archen','Archeops','Trubbish','Garbodor','Zorua','Zoroark','Minccino','Cinccino','Gothita','Gothorita','Gothitelle','Solosis','Duosion','Reuniclus','Ducklett','Swanna','Vanillite','Vanillish','Vanilluxe','Deerling','Sawsbuck','Emolga','Karrablast','Escavalier','Foongus','Amoonguss','Frillish','Jellicent','Alomomola','Joltik','Galvantula','Ferroseed','Ferrothorn','Klink','Klang','Klinklang','Tynamo','Eelektrik','Eelektross','Elgyem','Beheeyem','Litwick','Lampent','Chandelure','Axew','Fraxure','Haxorus','Cubchoo','Beartic','Cryogonal','Shelmet','Accelgor','Stunfisk','Mienfoo','Mienshao','Druddigon','Golett','Golurk','Pawniard','Bisharp','Bouffalant','Rufflet','Braviary','Vullaby','Mandibuzz','Heatmor','Durant','Deino','Zweilous','Hydreigon','Larvesta','Volcarona','Snivy','Servine','Serperior','Tepig','Pignite','Emboar','Oshawott','Dewott','Samurott','Patrat','Watchog','Lillipup','Herdier','Stoutland','Purrloin','Liepard','Pansage','Simisage','Pansear','Simisear','Panpour','Simipour','Munna','Musharna','Pidove','Tranquill','Unfezant','Blitzle','Zebstrika','Roggenrola','Boldore','Gigalith','Woobat','Swoobat','Drilbur','Excadrill','Audino','Timburr','Gurdurr','Conkeldurr','Tympole','Palpitoad','Seismitoad','Throh','Sawk','Sewaddle','Swadloon','Leavanny','Venipede','Whirlipede','Scolipede','Cottonee','Whimsicott','Petilil','Lilligant','Basculin','Sandile','Krokorok','Krookodile','Darumaka','Darmanitan','Maractus','Dwebble','Crustle','Scraggy','Scrafty','Sigilyph','Yamask','Cofagrigus','Tirtouga','Carracosta','Archen','Archeops','Trubbish','Garbodor','Zorua','Zoroark','Minccino','Cinccino','Gothita','Gothorita','Gothitelle','Solosis','Duosion','Reuniclus','Ducklett','Swanna','Vanillite','Vanillish','Vanilluxe','Deerling','Sawsbuck','Emolga','Karrablast','Escavalier','Foongus','Amoonguss','Frillish','Jellicent','Alomomola','Joltik','Galvantula','Ferroseed','Ferrothorn','Klink','Klang','Klinklang','Tynamo','Eelektrik','Eelektross','Elgyem','Beheeyem','Litwick','Lampent','Chandelure','Axew','Fraxure','Haxorus','Cubchoo','Beartic','Cryogonal','Shelmet','Accelgor','Stunfisk','Mienfoo','Mienshao','Druddigon','Golett','Golurk','Pawniard','Bisharp','Bouffalant','Rufflet','Braviary','Vullaby','Mandibuzz','Heatmor','Durant','Deino','Zweilous','Hydreigon','Larvesta','Volcarona','Cobalion','Terrakion','Virizion','Tornadus','Thundurus','Reshiram','Zekrom','Landorus','Kyurem','Keldeo','Meloetta','Genesect','Chespin','Quilladin','Chesnaught','Fennekin','Braixen','Delphox','Froakie','Frogadier','Greninja','Bunnelby','Diggersby','Fletchling','Fletchinder','Talonflame','Scatterbug','Spewpa','Vivillon','Litleo','Pyroar','Flabébé','Floette','Florges','Skiddo','Gogoat','Pancham','Pangoro','Furfrou','Espurr','Meowstic','Honedge','Doublade','Aegislash','Spritzee','Aromatisse','Swirlix','Slurpuff','Inkay','Malamar','Binacle','Barbaracle','Skrelp','Dragalge','Clauncher','Clawitzer','Helioptile','Heliolisk','Tyrunt','Tyrantrum','Amaura','Aurorus','Sylveon','Hawlucha','Dedenne','Carbink','Goomy','Sliggoo','Goodra','Klefki','Phantump','Trevenant','Pumpkaboo','Gourgeist','Bergmite','Avalugg','Noibat','Noivern','Chespin','Quilladin','Chesnaught','Fennekin','Braixen','Delphox','Froakie','Frogadier','Greninja','Bunnelby','Diggersby','Fletchling','Fletchinder','Talonflame','Scatterbug','Spewpa','Vivillon','Litleo','Pyroar','Flabébé','Floette','Florges','Skiddo','Gogoat','Pancham','Pangoro','Furfrou','Espurr','Meowstic','Honedge','Doublade','Aegislash','Spritzee','Aromatisse','Swirlix','Slurpuff','Inkay','Malamar','Binacle','Barbaracle','Skrelp','Dragalge','Clauncher','Clawitzer','Helioptile','Heliolisk','Tyrunt','Tyrantrum','Amaura','Aurorus','Sylveon','Hawlucha','Dedenne','Carbink','Goomy','Sliggoo','Goodra','Klefki','Phantump','Trevenant','Pumpkaboo','Gourgeist','Bergmite','Avalugg','Noibat','Noivern','Xerneas','Yveltal','Zygarde','Diancie','Hoopa','Volcanion','Rowlet','Dartrix','Decidueye','Litten','Torracat','Incineroar','Popplio','Brionne','Primarina','Pikipek','Trumbeak','Toucannon','Yungoos','Gumshoos','Grubbin','Charjabug','Vikavolt','Crabrawler','Crabominable','Oricorio','Cutiefly','Ribombee','Rockruff','Lycanroc','Wishiwashi','Mareanie','Toxapex','Mudbray','Mudsdale','Dewpider','Araquanid','Fomantis','Lurantis','Morelull','Shiinotic','Salandit','Salazzle','Stufful','Bewear','Bounsweet','Steenee','Tsareena','Comfey','Oranguru','Passimian','Wimpod','Golisopod','Sandygast','Palossand','Pyukumuku','Type: Null','Silvally','Minior','Komala','Turtonator','Togedemaru','Mimikyu','Bruxish','Drampa','Dhelmise', 'Rowlet','Dartrix','Decidueye','Litten','Torracat','Incineroar','Popplio','Brionne','Primarina','Pikipek','Trumbeak','Toucannon','Yungoos','Gumshoos','Grubbin','Charjabug','Vikavolt','Crabrawler','Crabominable','Oricorio','Cutiefly','Ribombee','Rockruff','Lycanroc','Wishiwashi','Mareanie','Toxapex','Mudbray','Mudsdale','Dewpider','Araquanid','Fomantis','Lurantis','Morelull','Shiinotic','Salandit','Salazzle','Stufful','Bewear','Bounsweet','Steenee','Tsareena','Comfey','Oranguru','Passimian','Wimpod','Golisopod','Sandygast','Palossand','Pyukumuku','Type: Null','Silvally','Minior','Komala','Turtonator','Togedemaru','Mimikyu','Bruxish','Drampa','Dhelmise','Jangmo-o','Hakamo-o','Kommo-o','Tapu Koko','Tapu Lele','Tapu Bulu','Tapu Fini','Cosmog','Cosmoem','Solgaleo','Lunala','Nihilego','Buzzwole','Pheromosa','Xurkitree','Celesteela','Kartana','Guzzlord','Necrozma','Magearna','Marshadow','Poipole','Naganadel','Stakataka','Blacephalon','Zeraora',]

natlist = ['Lonely', 'Brave', 'Adamant', 'Naughty', 'Bold', 'Relaxed', 'Impish', 'Lax', 'Timid', 'Hasty', 'Jolly', 'Naive', 'Modest', 'Mild', 'Quiet', 'Rash', 'Calm', 'Gentle', 'Sassy', 'Careful', 'Bashful', 'Quirky', 'Serious', 'Docile', 'Hardy']
emotes = ['<a:mewLoooop:446252694026321922>', '<a:sylveon:463817633578483723>', '<:sylveon:463817633578483723>', '<a:jirachigif:499179583531253760', '<a:smewsleep:448075686100598784>']
logging.basicConfig(level="INFO")

bot = commands.Bot(command_prefix=";")
version = ("0.0.5c Beta Build")

TOKEN = os.environ['TOKEN']
dburl = os.environ['DATABASE_URL']
dbltoken = os.environ['dbltoken']

bot.remove_command('help')
#db connect

@bot.listen()
async def on_connect():
	if not hasattr(bot, 'db'):
		bot.db = await asyncpg.create_pool(dburl)
		
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
	tconn = await bot.db.acquire()
	if user is None:
		user = ctx.author
	rquery = '''SELECT redeems FROM users WHERE u_id = {}'''.format(ctx.author.id)
	tquery = '''SELECT tnick FROM users WHERE u_id = {}'''.format(ctx.author.id)
	uquery = '''SELECT upvotepoints FROM users WHERE u_id = {}'''.format(ctx.author.id)
	cquery = '''SELECT pokname FROM pokes WHERE selected = 1 AND ownerid = {}'''.format(ctx.author.id)
	mquery = '''SELECT mewcoins FROM users WHERE u_id = {}'''.format(ctx.author.id)
	poke = await tconn.fetchval(cquery)
	redeems = await tconn.fetchval(rquery)
	tnick = await tconn.fetchval(tquery)
	uppoints = await tconn.fetchval(uquery)
	mewcoins = await tconn.fetchval(mquery)
	embed = discord.Embed(title="{} Trainer Card".format(user.name))
	embed.add_field(name="Redeems", value=f'{redeems}')
	embed.add_field(name="Trainer Nick", value=f'{tnick}')
	embed.add_field(name="Upvote Points", value=f'{uppoints}')
	embed.add_field(name="Currently Selected Pokemon", value=f'{poke}')
	embed.add_field(name="Credits", value=f'{mewcoins}ℳ	')
	embed.set_thumbnail(url=user.avatar_url)
	await ctx.send(embed=embed)
   
	
########################################################################################################33

			
############################################################################################################			
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="MewBot commands", description="The pokemon discord utility bot made for you!!!", color=0xeee657)
    embed.add_field(name="Ping", value="Pings the bot and shows it's latency")
    embed.add_field(name="Mew", value="A simple Ping, just responds with Mew!")
    embed.add_field(name="trainer", value="Displays your Trainer Card and other information")
    embed.add_field(name="start", value="Start Playing Mewbot!!")
    embed.add_field(name="trade", value="Trade Items, Redeems, Pokemon, and Credits!")
    embed.add_field(name="shop", value="Buy TMs, Held Items, Evolution Items & More!")
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
    mem = psutil.virtual_memory()
    cmem = (mem.available/1000000000)

    embed.add_field(name="CPU Statistics", value=f"\nCPU Count **{psutil.cpu_count()}**\nRAM **{cmem} GB**")
    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite Me](https://discordapp.com/api/oauth2/authorize?client_id=493045795445276682&permissions=388160&scope=bot)")

    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    embed = discord.Embed(title="Invite Me", description="The invite link for MewBot")

    #invite link
    embed.add_field(name="Invite", value="[Invite MewBot](https://discordapp.com/api/oauth2/authorize?client_id=493045795445276682&permissions=388160&scope=bot)")
    embed.add_field(name="User Count", value=f"{len(bot.users)}")
    await ctx.send(embed=embed)

@bot.command()
async def status(ctx):
    embed = discord.Embed(title="Bot development Status", description="information on the development of MewBot")

    #list

    embed.add_field(name="Current Build version", value="0.0.5c Beta Build")

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
	if message.guild and message.guild.id == 264445053596991498:
		return
	vowels = ['a', 'k', 'e', 't', 'u', 'i', 'o', 'l', 'o', 'm', 'y', 'i', 'e', 'z', 'x', 'b', 'g', 'l', 'a', 'w', 'q']
	vl = random.choice(vowels)
	if message.content.startswith(vl):
		channel = message.channel
		val1 = random.choice(pList)
		val = val1.lower()
		url = "https://img.pokemondb.net/artwork/vector/large/" + val.lower() + ".png"
		embed = discord.Embed(title="A Pokemon has spawned, say it's name it to catch it!")
		embed.set_image(url=url)
		try:
			await message.channel.send(embed=embed)
		except Exception as e:
			await print("	Error in sending embed")
		def check(m):
			return m.content == val and m.channel == channel
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
		query2 = '''
		INSERT INTO pokes (pokname, hpiv, atkiv, defiv, spatkiv, spdefiv, speediv, hpev, atkev, defev, spatkev, spdefev, speedev, pokelevel, ownerid, pnum, selected, move1, move2, move3, move4, poknick, exp, nature, expcap)
		VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, $25)
		'''

		args = (val, hpiv, atkiv, defiv, spaiv, spdiv, speiv, 0, 0, 0, 0, 0, 0, plevel, msg.author.id, pnum, 0, 'tackle', 'tackle', 'tackle', 'tackle', 'None', 1, nature, expc)
		try:
			await pconn.execute(query2, *args)
		except asyncpg.exceptions.NotNullViolationError as e:
			await channel.send("You need to Register with `;start` first")
		await channel.send(f'Congratulations <@{msg.author.id}>, you have successfully caught a {val}!')
		await bot.process_commands(message)
		logging.info("Success")
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
			emoji = random.choice(emotes)
			await ctx.send(emoji)
			logging.info("All went well")
			



@bot.command()
async def pokemon(ctx, val=None):
	
	if val is None:
		val = 1
	
	rnum = int(val) * 10
	if val == 1:
		enum = 1
	else:
		enum = (rnum/int(val))
	pconn = await bot.db.acquire()
	nquery = f"SELECT pokname, pnum FROM pokes WHERE ownerid = {ctx.author.id} AND pnum BETWEEN {enum} AND {rnum} ORDER BY pnum"
	pk1 = await pconn.fetch(nquery)
	nrecord = [record['pokname'] for record in pk1]
	precord = [record['pnum'] for record in pk1]
	embed = discord.Embed(title='Your Pokemon List')
	for pn in precord:
		nr = nrecord[pn-1]
		embed.add_field(name=f'{nr}', value=f'{pn}', inline=True)
	embed.set_footer(text="Upvote the Bot!!")
	await ctx.send(embed=embed)
	
@bot.command()
async def moves(ctx):
	pconn = await bot.db.acquire()
	pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id))
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
	
@bot.command()
async def tms(ctx):
	pconn = await bot.db.acquire()
	pokename = await pconn.fetchval("SELECT pokname FROM pokes WHERE selected = 1 AND ownerid = {}".format(ctx.author.id))
	with open ('moves.json') as f:
		pkmns = json.load(f)

	with open('pokemon (2).json') as fp:
		moveids = json.load(fp)

	with open('pokemonfile.json') as r:
		pkids = json.load(r)

	pokename = pokename.lower()
	pkid = [i['id'] for i in pkids if i['identifier'] == pokename]
	
	for pk_id in pkid:
		move_id = [m["move_id"] for m in moveids if m["pokemon_id"] == pk_id]
		move_names = [d["identifier"] for d in pkmns if d["id"] == move_id]
		for m_id in move_id:
			embed=discord.Embed(title="Learnable Move List")
			move_names = [d["identifier"] for d in pkmns if d["id"] == m_id]
			for name in move_names:
				embed.add_field(name=f";learn {name}", value="to learn this move")
			await ctx.send(embed=embed)
    
    
@bot.command()
async def select(ctx, val):
	pconn = await bot.db.acquire()
	val = int(val)
	maxnum = await pconn.fetchval("SELECT MAX(pnum) FROM pokes WHERE ownerid = {}".format(ctx.author.id))
	if val > maxnum:
		await ctx.send("That Pokemon Does not exist!")
		return
	else:
		await pconn.execute("UPDATE pokes SET selected = 0 WHERE selected = 1 AND ownerid = {0}".format(ctx.author.id, val))
		pque = '''UPDATE pokes SET selected = 1 WHERE ownerid = {0} and pnum = {1}'''.format(ctx.author.id, val)
		pnum = await pconn.execute(pque)
		await ctx.send("You have successfully selected your No. {0} Pokemon".format(val))
		emoji = random.choice(emotes)
		await ctx.send(emoji)

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
		try:
			irul = 'https://img.pokemondb.net/artwork/vector/' + pn.lower() + '.png'
		except TypeError as e:
			await ctx.send(f'You need to `;select` a pokemon or you haven\'t started <@{ctx.author.id}>')
		pns = str(pn)
		with requests.get('https://pokeapi.co/api/v2/pokemon/' + pns.lower() + '/') as r:	
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
	embed.add_field(name="Exp", value=f"{exp}/{expcap}")
	embed.add_field(name="Nature: ", value=f'{nature}')
	embed.add_field(name="Types: ", value=f'{tlist}')
	embed.add_field(name="Hit Points (HP)", value=f"{hp} |- {hpiv} IVs")
	embed.add_field(name="Attack", value=f"{round(attack)} |- {atkiv} IVs")
	embed.add_field(name="Defense", value=f"{round(defense)} |- {defiv} IVs")
	embed.add_field(name="Special Attack", value=f"{round(specialattack)} |- {spatkiv} IVs")
	embed.add_field(name="Special Defense", value=f"{round(specialdefense)} |- {spdefiv} IVs")
	embed.add_field(name="Speed", value=f"{speed} |- {int(speediv)} IV")
	embed.add_field(name="Held Item", value=f"{hi}")
	embed.set_image(url=irul)
	await ctx.send(embed=embed)
	

@bot.command()
async def pokedex(ctx, *, val):
	
	val = val.capitalize()
	if ' ' in val:
		val = val.replace(' ', '-')
	if val == 'Flowing':
		
		pokemonSpeed = 73
		pokemonAtk = 99
		pokemonDef = 79
		pokemonSpa = 120
		pokemonSpd =110
		pokemonHp = 95
		pAb = 'Sizzling Growth'
		irul = 'https://cdn.discordapp.com/attachments/479175545481986088/497738691381559296/flowin.png'
	elif val == 'Flire':
		pokemonSpeed = 110
		pokemonAtk = 120
		pokemonDef = 95
		pokemonSpa = 79
		pokemonSpd =99
		pokemonHp = 73
		pAb = 'Scorched feet'
		irul = 'https://cdn.discordapp.com/attachments/479175545481986088/497733271392878622/flire.png'

	elif val == 'Aquino':
		pokemonSpeed = 95
		pokemonAtk = 79
		pokemonDef = 120
		pokemonSpa = 73
		pokemonSpd = 110
		pokemonHp = 99
		pAb = 'Prehistoric Rain'
		irul = 'https://cdn.discordapp.com/attachments/480885918354636804/497721785048104970/aquino.jpg'
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
		iurl = ('https://img.pokemondb.net/artwork/vector/' + val.lower() + '.png')
		pkid = [i['id'] for i in forms if i['identifier'] == val.lower()]
		tids = [1['type_id'] for i in t_ids[pid]]
		type1 = [i['identifier'] for i in types if i['id'] == tids[0]]
		type2 = [i['identifier'] for i in types if i['id'] == tids[1]]
		
		for p_id in pkid:
			p_id = str(p_id)
			b = [1['base_stat'] for i in stats[p_id]]
			pokemonSpeed = (b[5])
			pokemonSpd = (b[4])
			pokemonSpa = (b[3])
			pokemonDef = (b[2])
			pokemonAtk = (b[1])
			pokemonHp = (b[0])
        
	embed = discord.Embed(title=val.capitalize(), description="")
	embed.add_field(name="Pokemon information", value=f"{val.capitalize()}**Types**: {type1}, {type2}\n**Pokedex Number**: {pkid}")
	embed.add_field(name="Stats", value=f"HP: {pokemonHp}\nAttack: {pokemonAtk} \nDefense: {pokemonDef}\nSpecial Attack: {pokemonSpa}\nSpecial Defense: {pokemonSpd}\nSpeed: {pokemonSpeed}")
	embed.set_image(url=iurl)

	await ctx.send(embed=embed)
	

@bot.listen()
async def on_guild_join(guild):
    if (len(guild.members) >= 50):
        pconn = await bot.db.acquire()
        query = '''UPDATE users SET redeems = 10 WHERE u_id = {}'''.format(guild.owner.id)
        await tconn.execute(query)
        await ctx.guild.owner.send("You have Received 10 Redeems for Adding me :smile:!,.. but remove me and it's gone :cry:")
    else:
        return
@bot.listen()
async def on_guild_remove(guild):
    pconn = await bot.db.acquire()
    query = '''UPDATE users SET redeems = 0 WHERE u_id = {}'''.format(guild.owner.id)
    await tconn.execute(query)
    await guild.owner.send("Goodbye to 10 Redeems :cry:")

@bot.command()
async def redeem(ctx, val):
    val = val.capitalize()
    if val in pList:
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





##############################################################################################################################################################
#level up
############################

			
#########################################################################




##########################################################################
#________________________________________________________________________#
##########################################################################




############################################################################
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
##############################################################################

#############################################################################3
###333333333333333333battles###########################333
#####################33333333nothing goes here
		
@bot.command()
async def spawn(ctx, val1):
	if ctx.author.id == 358293206900670467:
		channel = ctx.channel
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
	#   db code goes here
	else:
		await ctx.send("Only Dylee can use this command")
		
@bot.command()
async def addredeems(ctx, val, user: discord.Member):
	if ctx.author.id == 358293206900670467:
		pconn = await bot.db.acquire()
		rquery = f"UPDATE users SET redeems = {val} WHERE u_id = {user.id}"
		await pconn.execute(rquery)
	else:
		await ctx.send("Only Dylee can use this command")

		
@bot.command()
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
			await pconn.execute(f"UPDATE users SET mewcoins = {coins} WHERE u_id = {ctx.author.id}")
			await pconn.execute(f"UPDATE users SET upvotepoints = {upoints} WHERE u_id = {ctx.author.id}")
			embed = discord.Embed(title="Successfully claimed Upvote Points! and Credits")
			embed.add_field(name="Upvoted!", value="Get 10 Upvote Points for a 5 Redeems!")
			embed.set_thumbnail(url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
		else:
			embed = discord.Embed(title="Upvote the Bot Here!")
			embed.add_field(name="You haven't upvoted!", value="Turns out you have not upvoted")
			embed.add_field(name="Upvote Mewbot Here!", value="[Upvote MewBot](https://discordbots.org/bot/493045795445276682/vote)")
			await ctx.send(embed=embed)
	except Exception as e:
		embed = discord.Embed(title="You have already Upvoted")
		embed.add_field(name="Already Upvoted the Bot", value=f"{e}")
		await ctx.send(embed=embed)
		
@bot.command(aliases=["vote"])
async def upvote(ctx):
	embed = discord.Embed(title="Upvote the Bot Here!")
	embed.add_field(name="You haven't upvoted?", value="If you have not upvoted")
	embed.add_field(name="Upvote Mewbot Here! ", value="[Upvote MewBot](https://discordbots.org/bot/493045795445276682/vote)")
	embed.set_footer(text="NOTE: ONLY USE ;reward WHEN YOU HAVE UPVOTED")
	await ctx.send(embed=embed)
	emoji = random.choice(emotes)
	await ctx.send(emoji)
	
@bot.command()
async def trade(ctx, user: discord.Member, creds: int, poke: int):
    pconn = await bot.db.acquire()
    if user is None:
        await ctx.send("You cannot trade with yourself")
        return
    elif creds is None:
        await ctx.send("You did not specify Credits, please use `;gift` instead")
        return
    elif poke is None:
        await ctx.send("You did not specify a Pokemon Please Use `give` instead")
        return
    else:
        offering = await pconn.fetchval(f"SELECT mewcoins FROM users WHERE u_id = {ctx.author.id}")
        ccreds = await pconn.fetchval(f"SELECT mewcoins FROM users WHERE u_id = {user.id}")
        if creds > offering:
            await ctx.send(f"You do not have {creds} ℳ")
            return
        pokename = await pconn.fetchval(f"SELECT pokname FROM pokes WHERE pnum = {poke} AND ownerid = {user.id}")

        pid = await pconn.fetchval(f"SELECT  id FROM pokes WHERE pnum = {poke}")
        e = discord.Embed(title="Current Trade")
        e.add_field(name=f"\n<@{ctx.author.name}> ", value=f"is Offering {creds} for \n")
        e.add_field(name=f"\n<@{user.name}>'s ", value=f"{pokename} \n")
        e.add_field(name=f"\nDo you both ", value=f"Accept the trade?\n")
        e.set_footer(text="Say Yes to accept")
        await ctx.send(embed=e)
        def check(m):
            m.author == ctx.author.id and m.user == user.id
        try:
            msg = await bot.wait_for('message', check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("Trade cancelled, took too long to confirm")
        if msg == 'no' or 'No':
                await ctx.send("Trade rejected")
                return
        offering -= creds
        ccreds += offering
        mnum = await pconn.fetchval(f"SELECT MAX(pnum)+1 FROM pokes WHERE ownerid = {ctx.author.id}")
        nquery = f"UPDATE pokes SET ownerid = {ctx.author.id} AND pnum = {mnum} WHERE id = {pid}"
        cquery = f"UPDATE users SET mewcoins = {offering} WHERE u_id = {ctx.author.id}"
        gquery = f"UPDATE users SET mewcoins = {ccreds} WHERE u_id = {user.id}"
        await pconn.execute(nquery)
        await pconn.execute(cquery)
        await pconn.execute(gquery)
        await ctx.send("Trade Complete, Logs will be sent to DMs!")
        gif = random.choice(emotes)
        await ctx.send(gif)
        await ctx.author.send(f"You completed a Trade with {user.name}")
        await user.send(f"You completed a Trade with {ctx.name}")

	
	
bot.run(TOKEN)

			

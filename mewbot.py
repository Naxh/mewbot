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
paypal_client = os.environ['PaypalClientID']
paypal_secret = os.environ['PaypalSecret']

bot.remove_command('help')
#db connect

@bot.listen()
async def on_connect():
	if not hasattr(bot, 'db'):
		bot.db = await asyncpg.create_pool(dburl, max_size=20)
		
@bot.listen()
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(version)
    print('-------------')

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

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
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
@commands.cooldown(1, 3, commands.BucketType.user)
async def help(ctx, val=None):
	if val is None:
		embed = discord.Embed(title="MewBot commands", description="The pokemon discord utility bot made for you!!!", color=0xeee657)
		embed.add_field(name="Ping", value="Pings the bot and shows it's latency")
		embed.add_field(name="Mew", value="A simple Ping, just responds with Mew!")
		embed.add_field(name="trainer", value="Displays your Trainer Card and other information")
		embed.add_field(name="start", value="Start Playing Mewbot!!")
		embed.add_field(name="trade", value=

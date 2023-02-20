# Grumpus Sparrot Bot
# Developed by SamHex#8837 (Discord)

# *********** Modules Import ***********

import discord
from discord.ext import commands,tasks
import datetime
import random
import json
import urllib.request
import asyncio
import datetime
import time
from itertools import cycle
from urllib import parse, request
import re
import bs4
import requests
import googlesearch
from googlesearch import search
import typing
from typing import Optional
import time
from time import gmtime, strftime
import os


#******************** PREFIX & INTRO ***********************
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='*',intents=intents,case_insensitive=True,description="This is Sparrot !! ")

#******************** ON READY AND ACTIVITY ***********************

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" all Pirates !"))
    print('My Ready is Body')

#***********************************************************
#                       API Works                          *
#***********************************************************

API='81HCt7qJKHYV9C9H'


#*****For Bank*****
#api=str(my_secret)
api_url_bank = f"https://api.torn.com/torn/?selections=bank&key={API}"
api_url_items = f"https://api.torn.com/torn/?selections=items&key={API}"
api_torn_time = f"https://api.torn.com/torn/?selections=timestamp&key={API}"
#response = requests.get(api)
#data=response.json()

#******************** GOOGLE SEARCH ENGINE ***********************
@bot.command()
async def find(ctx,*,query):
    author = ctx.author.mention
    await ctx.channel.send(f"Arrr will send you links related to your question {author} in DM Me Hearty !")
    async with ctx.typing():
        for j in search(query, num_results=3):
            await ctx.author.send(f"\n:point_right: {j}")
        await ctx.author.send("Got any more questions:question:\nFeel free to ask again :smiley: !")

          
#******************** TORN BANKING  ***********************
stockbft = 0


@bot.command()
async def bank(ctx, numOne, numMerit, numStock: typing.Optional[int]):
    if numStock == 10:
        stockbft = 2
    elif numStock == None:
        stockbft = 0
    elif ('tci') or ('Tci') or ('TCI') or ('Stock') in numStock:
        await ctx.send(
            "For calculating stocks benefit, plese use command \n`*bank <Amount> <Merits> <10>` \nExample `*bank 1b 10 10`"
        )
    else:
        await ctx.send(
            "For calculating stocks benefit, plese use command \n`*bank <Amount> <Merits> <10>` \nExample `*bank 1b 10 10`"
        )
    tens = dict(k=10e2, m=10e5, b=10e8)
    factor, exp = numOne[0:-1], numOne[-1].lower()
    BP = int(float(factor) * tens[exp])
    Formatted = "{:,d}"
    response = requests.get(api_url_bank)
    data = response.json()
    meritint = int(numMerit)
    checkpointmerit = meritint
    if checkpointmerit > 10:
        await ctx.send(
            " You can't assign more than 10 merits!\nUnless you are Bogie or Ched ¯\_(ツ)_/¯"
        )
    else:
        meritbase = (meritint + stockbft) * 5
        ratew1 = float(data['bank']['1w'])
        ratew2 = float(data['bank']['2w'])
        ratem1 = float(data['bank']['1m'])
        ratem2 = float(data['bank']['2m'])
        ratem3 = float(data['bank']['3m'])
        w1 = (ratew1 * meritbase / 100) + ratew1
        w2 = (ratew2 * meritbase / 100) + ratew2
        m1 = (ratem1 * meritbase / 100) + ratem1
        m2 = (ratem2 * meritbase / 100) + ratem2
        m3 = (ratem3 * meritbase / 100) + ratem3
        oneweek = (BP * w1 / 100) * 7 / 365
        twoweek = (BP * w2 / 100) * 14 / 365
        onemonth = (BP * m1 / 100) * 30 / 365
        twomonth = (BP * m2 / 100) * 60 / 365
        threemonth = (BP * m3 / 100) * 90 / 365
        profitw1 = int(BP + oneweek)
        profitw2 = int(BP + twoweek)
        profitm1 = int(BP + onemonth)
        profitm2 = int(BP + twomonth)
        profitm3 = int(BP + threemonth)
        formatcent = "{:.2f}%"
    if BP > 3000000000:
        await ctx.send(" You can't bank more than 3b in Torn Bank! ")
    else:
        embed = discord.Embed(
            title=f"TORN BANKING RETURNS",
            description=
            "Interest rates change everyday. You might get slightly different returns",
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color.blue())
        embed.add_field(name="One Week Investment Returns" + " " +
                        (formatcent.format(w1)) + " " + "APR",
                        value=str('$') + (Formatted.format(profitw1)) + " " +
                        "_-Effective rate_ " +
                        (formatcent.format(w1 * 7 / 365)),
                        inline=False)
        embed.add_field(name="Two Weeks Investment Returns" + " " +
                        (formatcent.format(w2)) + " " + "APR",
                        value=str('$') + (Formatted.format(profitw2)) + " " +
                        "_-Effective rate_ " +
                        (formatcent.format(w2 * 14 / 365)),
                        inline=False)
        embed.add_field(name="One Month Investment Returns" + " " +
                        (formatcent.format(m1)) + " " + "APR",
                        value=str('$') + (Formatted.format(profitm1)) + " " +
                        "_-Effective rate_ " +
                        (formatcent.format(m1 * 30 / 365)),
                        inline=False)
        embed.add_field(name="Two Months Investment Returns" + " " +
                        (formatcent.format(m2)) + " " + "APR",
                        value=str('$') + (Formatted.format(profitm2)) + " " +
                        "_-Effective rate_ " +
                        (formatcent.format(m2 * 60 / 365)),
                        inline=False)
        embed.add_field(name="Three Months Investment Returns" + " " +
                        (formatcent.format(m3)) + " " + "APR",
                        value=str('$') + (Formatted.format(profitm3)) + " " +
                        "_-Effective rate_ " +
                        (formatcent.format(m3 * 90 / 365)),
                        inline=False)
        embed.set_footer(text="Information requested by: {}".format(
            ctx.author.display_name))
        embed.set_thumbnail(url="https://i.imgur.com/pORkUi0.png")
        await ctx.send(embed=embed)
    if numStock == 10:
        await ctx.send(
            "For calculating **without** TCI stocks benefit, plese use command \n`*bank <Amount> <Merits>` \nExample `*bank 1b 10`."
        )
    elif numStock == 0 or numStock == None:
        await ctx.send(
            "For calculating **with** TCI stocks benefit, plese use command \n`*bank <Amount> <Merits> <10>` \nExample `*bank 1b 10 10`."
        )
    else:
        print(" Bank Empty msg")


#************* Torn item search ***************
@bot.command()
async def item(ctx, *, itemsearch):
    itemsearch = itemsearch.title()
    response = requests.get(api_url_items)
    data = response.json()
    for item in data['items']:
        name = data['items'][item]['name'].title()
        if name == itemsearch:
            itemname = (data['items'][item]['name'])
            item_description = (data['items'][item]['description'])
            effects = (data['items'][item]['effect'])
            requirement = str(data['items'][item]['requirement'])
            wepclass = (data['items'][item]['type'])
            weptype = (data['items'][item]['weapon_type'])
            buy_price = (data['items'][item]['buy_price'])
            sell_price = (data['items'][item]['sell_price'])
            market_value = (data['items'][item]['market_value'])
            circulation = (data['items'][item]['circulation'])
            item_image = (data['items'][item]['image'])
            Formatted = "{:,d}"
            drug_timer = {"Xanax": 0}
            embed = discord.Embed(title=(itemname)+" "+(f'[{item}]'),
                                  description=(item_description) + " " +
                                  (effects),
                                  timestamp=datetime.datetime.utcnow(),
                                  color=discord.Color.gold())
            embed.add_field(name="Type", value=((wepclass) or "\u200b"))
            embed.add_field(name="Market Value",
                            value=str('$') + (Formatted.format(market_value)),
                            inline=True)
            embed.add_field(name="Circulation",
                            value=str(Formatted.format(circulation)),
                            inline=True)
            if 'Drug' in wepclass:
                if 'Cannabis' in itemname:
                    embed.add_field(name="Drug Cool Down Time",
                                    value=("60-90 minutes/ 1h-1.5h"),
                                    inline=True)
                    embed.add_field(
                        name="Over Dose Effects",
                        value=
                        ("֍ -100% Energy & Nerve \n֍ Hospital: 300-330 minutes(5-6h) \n֍ 'Spaced Out' honor bar"
                         ),
                        inline=True)
                if 'Ecstasy' in itemname:
                    embed.add_field(name="Drug Cool Down Time",
                                    value=("200-220 minutes/ 3-4h"),
                                    inline=True)
                    embed.add_field(name="Over Dose Effects",
                                    value=("֍ -100% Energy & Happy "),
                                    inline=True)
                if 'Ketamine' in itemname:
                    embed.add_field(name="Drug Cool Down Time",
                                    value=("45-60 minutes"),
                                    inline=True)
                    embed.add_field(
                        name="Over Dose Effects",
                        value=
                        ("֍ -100% Energy, Nerve & Happy \n֍ Hospital: 1,000 minutes(16-17h) \n֍ Increased cooldown (24-27 hours) \n֍ -20% to Strength & Speed "
                         ),
                        inline=True)
                if 'LSD' in itemname:
                    embed.add_field(name="Drug Cool Down Time",
                                    value=("400-450 minutes/ 7-7.5h"),
                                    inline=True)
                    embed.add_field(
                        name="Over Dose Effects",
                        value=
                        ("֍ -100% Energy & Nerve \n֍ -50% Happy \n֍ -30% to Speed & Dexterity "
                         ),
                        inline=True)
                if 'Opium' in itemname:
                    embed.add_field(name="Drug Cool Down Time",
                                    value=("120-180 minutes/ 2-3h"),
                                    inline=True)
                    embed.add_field(name="Over Dose Effects",
                                    value=("֍ Cannot OD on Opium "),
                                    inline=True)
                if 'PCP' in itemname:
                    embed.add_field(name="Drug Cool Down Time",
                                    value=("260-400 minutes/ 4.3-6.6h"),
                                    inline=True)
                    embed.add_field(
                        name="Over Dose Effects",
                        value=
                        ("֍ -100% Energy, Nerve & Happy \n֍ Hospital: 1,620 minutes (30.5h) \n֍ -10x (current level) to Speed **(permanent)** "
                         ),
                        inline=True)
                if 'Shrooms' in itemname:
                    embed.add_field(
                        name="Drug Cool Down Time",
                        value=(
                            "182-237 minutes/ 3-4h and -25 Energy(caps at 0) "
                        ),
                        inline=True)
                    embed.add_field(
                        name="Over Dose Effects",
                        value=
                        ("֍ -100% Energy, Nerve & Happy \n֍ Hospital: 100 minutes (1.6h) "
                         ),
                        inline=True)
                if 'Speed' in itemname:
                    embed.add_field(name="Drug Cool Down Time",
                                    value=("250-352 minutes/ 4-6h"),
                                    inline=True)
                    embed.add_field(
                        name="Over Dose Effects",
                        value=
                        ("֍ -100% Energy, Nerve & Happy \n֍ Hospital: 450 minutes (7.5h) \n֍ -6x (current level) to Strength & Defense **(permanent)** "
                         ),
                        inline=True)
                if 'Vicodin' in itemname:
                    embed.add_field(name="Drug Cool Down Time",
                                    value=("240-360 minutes/ 4-6h"),
                                    inline=True)
                    embed.add_field(name="Over Dose Effects",
                                    value=("֍ -150 Happy "),
                                    inline=True)
                if 'Xanax' in itemname:
                    embed.add_field(name="Drug Cool Down Time",
                                    value=("360-480 minutes/ 6-8h"),
                                    inline=True)
                    embed.add_field(
                        name="Over Dose Effects",
                        value=
                        ("֍ -100% Energy, Nerve & Happy \n֍ Hospital: 5000 minutes (83.3h) \n֍ Increased cool down & addiction (~24-25 hours / 3 Xanax) "
                         ),
                        inline=True)
                if 'Love Juice' in itemname:
                    embed.add_field(name="Drug Cool Down Time",
                                    value=("300 minutes/ 5h"),
                                    inline=True)
                    embed.add_field(name="Over Dose Effects",
                                    value=("֍ Cannot OD on Love Juice "),
                                    inline=True)

            embed.set_footer(
                text=
                "Thanks for Chupacabra[474281] for helping with the code,\nInformation requested by: {}"
                .format(ctx.author.display_name))
            embed.set_thumbnail(url=(item_image))
            await ctx.send(embed=embed)


#******************** INFO CMD  ***********************
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description="Fun Pirate Parrot Bot",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Color.green())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://i.imgur.com/wVc2Rjj.png")

    await ctx.send(embed=embed)


#******************** YOUTUBE ***********************
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' +
                                   query_string)
    # print(html_content.read().decode())
    search_results = re.findall(r'/watch\?v=(.{11})',
                                html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


#******************** BROOKLYN 99 ***********************
# “Fine, but in protest, I’m walking over there extremely slowly!” — Jake Peralta
# “OK, no hard feelings, but I hate you. Not joking. Bye.” — Gina Linetti
#
#
@bot.listen()
async def on_message(message):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'Sarge, with all due respect, I am gonna completely ignore everything you just said. — Jake Peralta',
        '“I ate one string bean. It tasted like fish vomit. That was it for me.” — Sergeant Terry Jeffords',
        ' “Title of your sex tape.” — Jake Peralta',
        '“The English language can not fully capture the depth and complexity of my thoughts, so I’m incorporating emojis into my speech to better express myself. Winky face.” — Gina Linetti',
        '“A place where everybody knows your name is hell. You’re describing hell.” — Rosa Diaz',
        '“I asked them if they wanted to embarrass you, and they instantly said yes.” — Captain Holt',
        ' “Anyone over the age of six celebrating a birthday should go to hell.” — Rosa Diaz',
        '“Title of your sex tape.” — Amy Santiago',
        '“Jake, piece of advice: Just give up. It’s the Boyle way. It’s why our family crest is a white flag.” — Charles Boyle',
        '“Hello, unsolved case. Do you bring me joy? No, because you’re boring and you’re too hard. See ya.” — Norm Scully',
        '“Well, no one asked you. It’s a self-evaluation.” — Michael Hitchcock',
        '“It’s Gina’s phone. Leave me a voice mail. I won’t check it ’cause it’s not 1993.” — Gina Linetti’s voice mail',
        '“You should make me your campaign manager. I was born for politics. I have great hair and I love lying.” — Gina Linetti',
        ' “You think you can just bully people, but you can’t. It’s not OK. I’m the bully around here. Ask anyone.” — Gina Linetti',
        '“Trying to get drunk enough to have sexual intercourse with a vegan. Why can’t I just think with my junk like a modern man?” — Charles Boyle',
        ' “Do not trust any child that chews bubble gum-flavored bubble gum. Do not trust any adult that chews gum at all. Never vacation in Banff.” — Captain Holt',
        ' “I was thinking how I would make the perfect American president based upon my skill set, dance ability, and bloodlust.” — Gina Linetti',
        '“I’m a detective. I will detect.” — Sergeant Terry Jeffords',
        '“I’m not totally useless. I can be used as a bad example.” — Jake Peralta',
        ('\nCool. Cool cool cool cool cool cool cool, '
         '\nno doubt no doubt no doubt no doubt.'),
        ('\nRosa Diaz: “Come on, Peralta! Holt said to use the whole team. We all want this solved.”'
         '\nJake Peralta: “I appreciate the offer, but I work best alone. Except when it comes to sex. Actually, sometimes including sex.”'
         ),
        ('\nCaptain Holt: “Everyone, I’m your new Commanding Officer, Captain Ray Holt.”'
         '\nAmy Santiago: “Speech!”'
         '\nCaptain Holt: “That was my speech.”'
         '\nAmy Santiago: “Short and sweet.”'),
        ('\nRosa Diaz: “We can go to my apartment. No one knows where I live.”'
         '\nSergeant Terry Jeffords: “I thought you had Amy over there once.”'
         '\nRosa Diaz: “Yeah, it was fun. I moved the next day.”'),
        ('\nRosa Diaz: “I’ve only said I love you to three people. My mom, my dad, and my dying grandpa. And one of those I regret.”'
         '\nCharles Boyle: “Which one?”'
         '\nRosa Diaz: “Grandpa. He beat cancer, so now I look like an idiot.”)'
         ),
        ('\nJake Peralta: “I tried everything. I begged. I pleaded. I even told them that Scully was a Make-a-Wish kid with a rare disease that makes him look like a giant old baby.”'
         '\nRosa Diaz: “Did you call it Scullyosis?”'
         '\nJake Peralta: “Damn it, Rosa, that’s really good and completely useless to me now.”'
         ),
        ('\nJake Peralta: “I’m quick at math.”'
         '\nCaptain Holt: “OK, what’s 38 x 76?”'
         '\nJake Peralta: “24.”'
         '\nCaptain Holt: “That’s not even close.”'
         '\nJake Peralta: “But it was quick.”'),
        ('\nGina Linetti: “Would you tell the sky to stop being so blue?”'
         '\nCaptain Holt: “Yes. I wish it were tan.”'
         '\nGina Linetti: “What?”'
         '\nCaptain Holt: “It’s my favorite color. It’s no-nonsense.”'),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)


#******************** PROFANITY SP ***********************
@bot.listen()
async def on_message(message):

    wittyans = [
        'I love you, too.', 'Not if I fuck you first.',
        'How to be a grown up at work: Replace "Fuck you" with "Ok, great" ',
        'I would die laughing and you would die trying.',
        'I would, but I have standards.',
        'Don’t threaten me with a good time.',
        'Get on your knees and warm me up first',
        'Fuck yourself — Lord knows no one else will do it for you.',
        'Not tonight, darling. I have a headache.',
        'Look them up and down. “I’m gonna need a few drinks first."',
        'When and where?” I find that either leaves people speechless or makes for a ton of sexual tension.',
        'Well, if you insist…, ', 'Can I at least get a kiss first?',
        'Oh. yeah? Well, unfuck you!',
        'No thanks. But you almost turned me on :wink:',
        'Will you hold me after?', 'I don’t do charity work.',
        'I’m not that bored and you’re not that lucky.', 'I’d fuck me, too.',
        'It’s more than you can afford.',
        'Trust me on this. Give them a THUMBS UP and smile. Nothing will anger them more.',
        'Trust me it was all about Adam and Eve not Adam and Steve.'
    ]
    if bot.user.id != message.author.id:
        if 'fuck' in ("" + message.content + ""):
            response = random.choice(wittyans)
            await message.channel.send(response)
        if 'Fuck' in ("" + message.content + ""):
            response = random.choice(wittyans)
            await message.channel.send(response)
        if 'f*ck' in ("" + message.content + ""):
            response = random.choice(wittyans)
            await message.channel.send(response)
        if 'F*ck' in ("" + message.content + ""):
            response = random.choice(wittyans)
            await message.channel.send(response)
        if 'f**k' in ("" + message.content + ""):
            response = random.choice(wittyans)
            await message.channel.send(response)
        if 'F**k' in ("" + message.content + ""):
            response = random.choice(wittyans)
            await message.channel.send(response)
        if 'F u c k' in ("" + message.content + ""):
            response = random.choice(wittyans)
            await message.channel.send(response)
        if 'f u c k' in ("" + message.content + ""):
            response = random.choice(wittyans)
            await message.channel.send(response)


#************* Parrot ***************


@bot.listen()
async def on_message(message):
    shitwit = [
        'Sorry fella, I don’t have the energy to pretend to like you today.',
        'Surprise me. Say something intelligent.',
        'Umm...pardon me, I wasn’t listening. Can you repeat what you just said?',
        'Ok. (This simple expression embodies the fact that you don’t give a f*ck!)',
        'Are you always such an idiot, or do you just show off when I’m around?',
        'Sorry, I don’t understand what you’re saying. I don’t speak bullsh*t.',
        'Awww...are you having a bad day? ',
        'Cool story bro!',
        'Wow, you’re really smart!',
        'Your face makes onions cry.',
        'You are so full of shit, the toilet’s jealous.',
        'Someday you’ll go far. I hope you stay there.',
        'You don’t really expect me to answer that, do you?',
        'I’m sorry but I didn’t order a glass of your opinion.',
        'Some people are like clouds. When they disappear it’s a brighter day. Fits on you perfectly! ',
        'You’re a grey sprinkle on a rainbow cupcake.',
        'Isn’t there a bullet somewhere you could be jumping in front of?',
        'You are proof that evolution can go in reverse.',
        'I’m busy right now; can I ignore you another time?',
        'I don’t have the time or the crayons to explain this to you.',
        'If you’re going to act like a turd, go lay on the yard.',
        'Take my lowest priority and put yourself beneath it.',
        'What doesn’t kill you disappoints me.',
        'Don’t worry — the first 40 years of childhood are always the hardest.',
        'Stupidity isn’t a crime. You’re free to go.',
        'You’re about as useful as an ashtray on a motorcycle.',
        'You fear success, but you really have nothing to worry about.',
        'Hold still. I’m trying to imagine you with a personality.'
        '\nToo bad you can’t Photoshop your ugly personality.',
        'You’re not stupid! You just have bad luck when you’re thinking.',
        'I thought of you today. It reminded me to take out the trash.',
        'Light travels faster than sound, which is why you seemed bright until you spoke.',
        'No, I just checked my receipt. I didn’t buy any of your bullsh*t.',
        'Oh, enough about me! What have you been up to lately?',
        'Well, as they say: “It takes one to know one.”',
        'Here’s a tissue, you have some sh*t on your lips.',
        'If you ran like your mouth, you’d be in good shape.',
        'If ignorance is bliss, you must be the happiest person on the planet.'
        'I understand what youre saying, but if I agreed with you, then we’d both be wrong.',
        'How is that supposed to make me feel?',
        'Your ass must be pretty jealous of all the shit that comes out of your mouth.',
        'Look, if I wanted to hear from an asshole, all I had to do was fart.',
        'I’ve been called worse things by better people.',
        'Not too many people like you, do they?',
        'Shhh! *then put your finger on their lips*',
        'I don’t remember asking for your opinion.',
        'Wait for your turn. The adults are talking.',
        'I was going to give you a nasty look, but I see you already have one.',
        'You have your entire life to be a jerk. Why not take today off?',
        'Please cancel my subscription to your issues.',
        'I’m calling the cops.',
        'The last time I saw someone like you, I flushed it.',
        'If you’re going to be two-faced, at least make one pretty.',
        'I’m busy; you’re ugly. Have a nice day.',
        'If you have an opinion about me, raise your hand. Then, after raising your hand, put it in your mouth.',
        'I totally understand now why you feel that way. Thank you for letting me know.',
        'I’m telling on you!',
        'Of course, I talk like an idiot. How else would you be able to understand me?',
        'Why don’t you check eBay and see if they have a life for sale?',
        'I believed in evolution until I met you.',
        'Why don’t you go outside and play hide and go F yourself',
        'Man, no wonder everyone talks about you behind your back.',
        'You have the right to remain silent because whatever you say will probably be stupid anyway.',
        'Well, bless your heart!',
        'Talk to the hand!',
        'I don’t know what your problem is, but I’m guessing it’s hard to pronounce.',
        'Ooooh. I almost gave a f*ck. It almost scared the sh*t out of me.',
        'You only annoy me when you’re breathing, really.',
        'I hope you step on a Lego.',
        'Unless your name is Google, stop acting like you know everything.',
        'I’m no cactus expert, but I know a prick when I see one.',
        'Roses are red; violets are blue. I have five fingers, and the third one is for you.',
        'I’m not a proctologist, but I know an asshole when I see one.',
        'I’d slap you, but that would be animal abuse.',
        'I may not be perfect, but at least I’m not you. _(Burn!)_',
        'Mirrors don’t lie, and lucky for you, they also don’t laugh.',
        'Sometimes, it’s better to keep your mouth shut and give the impression that you’re stupid than open it and remove all doubt.',
        'Stupidity’s not a crime, so feel free to go.',
        ('\nI’m trying my absolute hardest to see things from your perspective,'
         '\nbut I just can’t get my head that far up my ass.'),
        'I have better things to do than listen to you.',
        'Just walk away _(There’s no bigger insult than indifference!)_',
        'You’re going to miss everything cool and die angry.',
        'Woah! Do you hear that? _*silence*_ That’s the sound of me not caring.',
        'You always bring me so much joy—as soon as you leave the room.',
        'Remember that time when I said you were cool? I lied.',
        'If they are rolling their eyes on you, say: "Yeah, keep rolling your eyes. Maybe you’ll find a brain back there."',
        'Thanks for sharing. We’re all refreshed and challenged by your unique point of view.',
        ('\nI’m whatever you want me to be, sweetie.'
         '\n_ (Acting in a calm and peaceful manner is one of the best ways to deal with rude people.)_'
         ),
        'Remember when I asked for your opinion? Well, me neither.',
        'May I ask you to stop talking? It smells really bad.',
        'Everyone’s entitled to act stupid once in a while, but you’re really abusing the privilege.',
        'I don’t care what everyone else says. I don’t think you’re that bad.',
        'People like you are the reason I’m on medication.',
        'Thank you. _(A simple act of gratitude can throw their ill intentions out of whack.)_',
        'That’s a nice story and all, but in what chapter do you shut the f*ck up?',
        'If ignorance is bliss, you must be the happiest person on the planet.',
        'There are some incredibly dumb people in this world. Thanks for helping me understand that.',
        'Your misguided opinion is false but cute.',
        'Goodbye! (Most of the time, a simple farewell is all it takes to end all the drama.)',
        'Thank you very much for thinking about me! Bye !',
        'Eenngk, enggk, engggkk! Sorry, the line’s choppy. Bye!',
        'I hope your day is as pleasant as your personality!',
        'The jerk store called. They said they are all out of...you!',
        ('\n**Please elaborate.** '
         '\n_(This might stop them on their tracks because elaborating takes a lot of time. Also, they probably haven’t prepared anything to explain to you.)_'
         ),
        ('\nThat sounds weird coming from you. Am I? Am I Really?',
         '\n(Say this with a pissed tone, and you’ll sound hostile enough for them to back off.)'
         ),
        ('\nDid it hurt when you fell from heaven?'
         '\nIf they ask you why say: “Cause it looks like you landed on your face!”'
         ),
    ]

    if message.author.bot == False and bot.user.mentioned_in(message):
        response = random.choice(shitwit)
        await message.channel.send(response)


#************* Fly Back Time ***************
timezone = int(0)


@bot.command()
async def flyback(ctx, timezone: typing.Optional[int]):
    response = requests.get(api_torn_time)
    data = response.json()
    author = ctx.author.mention
    tct_val = int(data['timestamp'])
    if (timezone == None):
        tzcount = tct_val
    else:
        tzcount = int((timezone * 3600) + tct_val)
    Mexico_time = int(tzcount + 2160)
    Cayman_time = int(tzcount + 6000)
    Canada_time = int(tzcount + 6960)
    Hawaii_time = int(tzcount + 11280)
    UK_time = int(tzcount + 13320)
    Argentina_time = int(tzcount + 14040)
    Swiss_time = int(tzcount + 14760)
    Japan_time = int(tzcount + 18960)
    China_time = int(tzcount + 20280)
    UAE_time = int(tzcount + 22800)
    SA_time = int(tzcount + 24960)
    final_tct = strftime("%a, %d %I:%M:%S %p ", gmtime(tct_val))
    Mexico_flyback = strftime("%a, %d %I:%M:%S %p ", gmtime(Mexico_time))
    Cayman_flyback = strftime("%a, %d %I:%M:%S %p ", gmtime(Cayman_time))
    Canada_flyback = strftime("%a, %d %I:%M:%S %p ", gmtime(Canada_time))
    Hawaii_flyback = strftime("%a, %d %I:%M:%S %p ", gmtime(Hawaii_time))
    UK_flyback = strftime("%a, %d %I:%M:%S %p ", gmtime(UK_time))
    Argentina_flyback = strftime("%a, %d %I:%M:%S %p ", gmtime(Argentina_time))
    Swiss_flyback = strftime("%a, %d %I:%M:%S %p ", gmtime(Swiss_time))
    Japan_flyback = strftime("%a, %d %I:%M:%S %p ", gmtime(Japan_time))
    China_flyback = strftime("%a, %d %I:%M:%S %p ", gmtime(China_time))
    UAE_flyback = strftime("%a, %d %I:%M:%S %p ", gmtime(UAE_time))
    SA_flyback = strftime("%a, %d %I:%M:%S %p ", gmtime(SA_time))

    embed = discord.Embed(
        title=("Fly Back Estimates"),
        description=
        ("Just to give idea on fly back times. To get times in your local timezone use"
         + "\n`*flyback <time diff in hours>` " + "\n " +
         "Current Torn Time " + "***" + (final_tct) + "***"),
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.add_field(name="Mexico", value=("36min,ETA: " + str(Mexico_flyback)))
    embed.add_field(name="Cayman Islands",
                    value=("50min,ETA: " + str(Cayman_flyback)))
    embed.add_field(name="Canada", value=("58min,ETA: " + str(Canada_flyback)))
    embed.add_field(name="Hawaii",
                    value=("3h 4min,ETA: " + str(Hawaii_flyback)))
    embed.add_field(name="United Kingdom",
                    value=("3h 42min,ETA: " + str(UK_flyback)))
    embed.add_field(name="Argentina",
                    value=("3h 54min,ETA: " + str(Argentina_flyback)))
    embed.add_field(name="Switzerland",
                    value=("4h 06min,ETA: " + str(Swiss_flyback)))
    embed.add_field(name="Japan",
                    value=("5h 16min,ETA: " + str(Japan_flyback)))
    embed.add_field(name="China",
                    value=("5h 38min,ETA: " + str(China_flyback)))
    embed.add_field(name="UAE", value=("6h 20min,ETA: " + str(UAE_flyback)))
    embed.add_field(name="South Africa",
                    value=("6h 56min,ETA: " + str(SA_flyback)))
    await ctx.author.send(embed=embed)
    await ctx.send("I have send you details in DM, Me Hearty :airplane_small:")


#************* SamHex ***************

#@bot.listen()
#async def on_message(message):
#   samwit = [
#      'Wake up !',
#     'Did someone mentioned... ',
#    'Arrrr that lazy ass...',
#   'I hate ',
#  ]
# if bot.user.id != message.author.id:
#     if 'Sam'=='Sam' in (message.content):
#        response = random.choice(samwit)
#       await message.channel.send (response + f'<@{399969465145753600}>')
#  if 'sam'=='sam' in (message.content):
#     response = random.choice(samwit)
#    await message.channel.send (response + f'<@{399969465145753600}>')
#   if 'SAM'=='SAM' in (message.content):
#       response = random.choice(samwit)
#      await message.channel.send (response + f'<@{399969465145753600}>')

#************* Baby Shark ***************


@bot.listen()
async def on_message(message):
    if bot.user.id != message.author.id:
        if 'baby' in ("" + message.content + ""):
            await message.channel.send(
                ':shark: :shark: :shark: :shark: Baby Shark do doo do doo Baby Shark do doo do dooo :shark: :shark: :shark: :shark:'
            )
        if 'Baby' in ("" + message.content + ""):
            await message.channel.send(
                ':shark: :shark: :shark: :shark: Baby Shark do doo do doo Baby Shark do doo do dooo :shark: :shark: :shark: :shark:'
            )
        if 'BABY' in ("" + message.content + ""):
            await message.channel.send(
                ':shark: :shark: :shark: :shark: Baby Shark do doo do doo Baby Shark do doo do dooo :shark: :shark: :shark: :shark:'
            )
        if 'shark' in ("" + message.content + ""):
            await message.channel.send(
                ':shark: :shark: :shark: :shark: Baby Shark do doo do doo Baby Shark do doo do dooo :shark: :shark: :shark: :shark:'
            )
        if 'Shark' in ("" + message.content + ""):
            await message.channel.send(
                ':shark: :shark: :shark: :shark: Baby Shark do doo do doo Baby Shark do doo do dooo :shark: :shark: :shark: :shark:'
            )
        if 'SHARK' in ("" + message.content + ""):
            await message.channel.send(
                ':shark: :shark: :shark: :shark: Baby Shark do doo do doo Baby Shark do doo do dooo :shark: :shark: :shark: :shark:'
            )
        if 'plank' in ("" + message.content + ""):
            await message.channel.send(
                ':shark: :shark: :shark: :shark: Baby Shark do doo do doo Baby Shark do doo do dooo :shark: :shark: :shark: :shark:'
            )
        if 'Plank' in ("" + message.content + ""):
            await message.channel.send(
                ':shark: :shark: :shark: :shark: Baby Shark do doo do doo Baby Shark do doo do dooo :shark: :shark: :shark: :shark:'
            )


#************* Greetings ***************


@bot.listen()
async def on_message(message):

    morning_greet = [
        'Good morning. Start the day with a fart just like any other day! ',
        'The morning sun is calling me. I just decided to answer another day. Good morning! ',
        'Always harbor positivity in your mind because you will never find it in the real world. Good morning. Have a great day! ',
        'Love is blind until I wake up and see your face in the morning! ',
        'I was about to say ‘shut up and go to sleep’ to all the early risers, but it’s not socially acceptable. So, good morning! ',
        ('\nGood morning,I know you have so many goals to start the day with.'
         '\nRising early is not one of them. '),
        'I was the richest person in the world, and then it happened. The alarm bell rang. Good morning! ',
        ('\nEvery morning is a blessing only if you don’t have an alarm clock by your bed.'
         '\nWith an alarm clock, it’s a curse. Good morning! '),
        ('\nIf the world was kind to me, it would have slept like an Olympic discipline.'
         '\nGood morning to everyone living in this cruel, unjust world. '),
        'Since you’re not a cup of coffee, why should I wake up early? :coffee: ',
        'Now move your lazy bum and fetch me some coffee :coffee::coffee: ',
    ]
    night_greet = [
        'Enjoy your next 8 hours! :smiling_imp: ',
        'Good night! May you be safe from the ghost under your bed! ',
        'Good night and sleep well! Hope you have dreams as sweet as I am! ',
        'Sleeping is the only thing you’re good at besides breathing, so good night. ',
        ('\nThe sun is red, the sky is blue, I cannot stay happy, without disturbing you.'
         '\nGoodnight my love. '),
        ('\nDon’t waste thinking about your lost past, Don’t waste time for planning your future,'
         '\nBetter kill some mosquito with that time So that you can sleep better. Good Night. '
         ),
        'May tomorrow be finally the day you win at life. Sleep well! ',
        'You’ve seen enough of the cruel world so better close your eyes already. ',
        ('\nThe only way I can guarantee you a sweet dream is dreaming about me.'
         '\nSo, what are you waiting for? Sleep tight! '),
        ('\nThe good people sleep much better at night than the bad people.'
         '\nOf course, the bad people enjoy the waking hours much more.'
         '\nGood night!'),
        ('\nWelcome to Sweet Dreams airlines. We’ll be shortly arriving at Dreamland.'
         '\nFasten blankets, puff the pillow, close your eyes and get ready to doze off!'
         '\nGood Night!'),
    ]
    if bot.user.id != message.author.id:
        if 'morning' in ("" + message.content + ""):
            response = random.choice(morning_greet)
            await message.channel.send(response + message.author.mention)
        if 'Morning' in ("" + message.content + ""):
            response = random.choice(morning_greet)
            await message.channel.send(response + message.author.mention)
        if 'off to bed' in ("" + message.content + ""):
            response = random.choice(night_greet)
            await message.channel.send(response + message.author.mention)
        if 'night' in ("" + message.content + ""):
            response = random.choice(night_greet)
            await message.channel.send(response + message.author.mention)
        if 'Night' in ("" + message.content + ""):
            response = random.choice(night_greet)
            await message.channel.send(response + message.author.mention)


#********************   TEST AREA  ************************************#



@bot.command()
async def rand(ctx, number):
    mixer = int(number)
    if mixer > 100:
        await ctx.send("I can only count upto 100")
    else:
        guess = str(random.randint(1, mixer))
        await ctx.send(" Let me think...")
        await asyncio.sleep(3)
        await ctx.send(" Seems a bit tricky my anxious Pirate......")
        await asyncio.sleep(3)
        await ctx.send(
            " Drumroll Please !!!!.........:drum::drum::drum::drum::drum:")
        await asyncio.sleep(5)
        await ctx.send( "I have selected "+"**"+guess+"**"+"   "+":tada::tada::tada:")


DKEY='OTAxNDY2MzIzOTgzNDIxNDgy.YXQR8A.Y5ViI2GLFMF2NKALqKFzWT7lr-k'
bot.run(DKEY)



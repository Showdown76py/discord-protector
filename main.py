from http import server
import discord
from discord.ext import commands
import os
import time
import difflib
import notification_api as na
import sms_api as sa
from dotenv import load_dotenv
bot = commands.Bot(command_prefix=None)
load_dotenv()
phishing_a = []
precedent_dm = None
serverdm_a=[]
@bot.event
async def on_ready():
    print('Online')
    na.run(na.Files.CONNECTED)

@bot.event
async def on_message(msg):
    global precedent_dm, phishing_a,serverdm_a
    msgcontent = msg.content
    # Physhing check
    if '://' in msgcontent:
        safe = ['steamcommunity.com','steampowered.com','discord.gg','discord.com','discord.new']
        web=msgcontent.split('://')[1].split('/')[0]
        r = difflib.get_close_matches(web, safe, 1)
        if r[0] != web:
            phishing_a.append(time.time())
        
        res = 0
        for t in phishing_a:
            if t+10 > time.time():
                res+=1
        
        if res == 3:
            sa.sendSMS(sa.PrebuiltMessages.PHISHING)
            na.run(na.Files.SUSPICIOUS_TEXT)
            return
    
    # DM server all
    if precedent_dm is None: precedent_dm = msg.channel.id
    else:
        if 'discord.gg/' in msgcontent:
            if precedent_dm != msg.channel.id:
                serverdm_a.append(time.time())
            else:
                serverdm_a = []
            precedent_dm = msg.channel.id

            res = 0
            for t in serverdm_a:
                if t+10 > time.time():
                    res+=1
            
            if res == 3:
                sa.sendSMS(sa.PrebuiltMessages.DM_ALL)
                na.run(na.Files.SUSPICIOUS_TEXT)
                return

    
try:
    bot.run(os.environ.get('TOKEN'),bot=False)
except:
    sa.sendSMS(sa.PrebuiltMessages.CONNECTION_LOST)
    na.run(na.Files.CONNECTION_LOST)
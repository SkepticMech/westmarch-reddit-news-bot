'''
Created on Feb 21, 2017

@author: Nick
'''
import praw
import config
import time
import random
from datetime import datetime
from datetime import timedelta 
import collections
# import pdb
import re
# import os



def bot_login():
    print ("Logging in...")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "SketpicMech post tester v0.2")
    print ("Logged in!")
    return r

def get_weather(f):
    weath1 = []
    weath2 = []
    for cnt in range(1,8):
        ca1 = random.randint(1,100)
        ca2 = random.randint(1,100)
        if ca1 < 71:
            weatha = 'Pleasant'
        elif 70 < ca1 < 81:
            cb1 = random.randint(1,2)
            if cb1 < 2:
                weatha = 'Hot'
            else:
                weatha = 'Cool'
        elif 80 < ca1 < 91:
            weatha = 'Rain'
        elif 90< ca1 < 100:
            weatha = 'Thunderstorms'
        else:
            weatha = 'Tornado'
        if ca2 < 71:
            weathb = 'Calm'
        elif 70 < ca2 < 81:
            cb2 = random.randint(1,10)
            if cb2 < 4:
                weathb = 'Warm'
            else:
                weathb = 'Cold'
        elif 80 < ca2 <91:
            weathb = 'Snow'
        elif 90 < ca2 <100:
            weathb = 'Snowstorm'
        else:
            weathb = 'Blizzard'
        weath1.append(weatha)
        weath2.append(weathb)
    f.write("**Ilbryn Vulre's Weekly Weather Report:**  \n\nOnce again, I have spent much time studying the hemispheric patterns of this part of the planet so that I may predict the patterns of upper atmosphere, precipitations, droughts, and other nasty bits of weather. To this point I have determined that the patterns for the next week shall be as follows:  \n\n")
    f.write("Location | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday\n")
    f.write("---------|---------|---------|---------|---------|---------|---------|---------\n")
    f.write("Westbach |")
    for cntw in range(7):
        if not cntw == 6:
            f.write(weath1[cntw] + ' |')
        else:
            f.write(weath1[cntw] + "\n")
    f.write("Mountains |")
    for cntw in range(7):
        if not cntw == 6:
            f.write(weath2[cntw] + ' |')
        else:
            f.write(weath2[cntw] + "  \n&nbsp;\n\n")
    f.write("As always please refrain from visiting my tower lest you truly have something of import to discuss.\n&nbsp;\n\n&nbsp;&nbsp;&nbsp;&nbsp;~ Ilbryn Vulre, High Wizard of the Order of Scagaros, and Savior of the Bogol Valley\n\n&nbsp;\n\n")

def get_heads(f):
    with open("news.txt", "r") as newt:
        newst = newt.read()
        newst = newst.split("\n")
        newst = list(filter(None, newst))
    leng = len(newst)
    cn1 = random.randint(1,leng)
    cn2 = random.randint(1,leng)
    if not cn1 == cn2:
        news = [newst[cn1-1],newst[cn2-1]]
    else:
        cn2 = random.randint(1,leng)
        news = [newst[cn1-1],newst[cn2-1]]

    f.write("**Top Stories From The East:**\n\n")
    f.write(news[0] + "\n\n" + news[1] + "  \n&nbsp;\n\n")

def get_title():
    date = time.strftime("%B %d, 13%y")
    title = "The Westbach Times "+ date
    return title
    
# def get_posts(r, subreddit):
#     for submission in subreddit.hot(limit=50):
        
def get_users():
    us = open("users.txt", "w+") #open/create the approved user file for westmarch
    users = []
    for contributor in r.subreddit('AdventuresInWestmarch').contributor: #pulls all approved users
        us.write(contributor.name + "\n") # adds user to text file
        if not contributor.name == 'DM_Dave': # 
            users.append(contributor.name) #
    us.close
    return users

def get_players():
    py = open("players.txt", "w+")
    players = []
    names = []
    for flair in r.subreddit('AdventuresInWestmarch').flair(limit=None):
        user = flair['user']
        if not flair['flair_css_class'] == 'dm':
            players.append(user.name)
            names.append(flair['flair_text'])
            py.write(user.name + "\t" + flair['flair_text'] + "\t" + flair['flair_css_class'] + "\n")
    py.close()
    
    return (players, names)

def get_sums(f):
    links = []
    texts = []
    titles = []
    comp = 0
    for submission in subreddit.hot(limit=20):
        age = (datetime.fromtimestamp(submission.created).date() - datetime.now().date())
        comp = 0
        if timedelta(days=-8) < age and submission.link_flair_text == 'Mission Write-up':
            texts.append(submission.selftext)
            links.append(submission.id)
            titles.append(submission.title)
            comp = 1
    leng = len(links)
    parties = []
    locas = []
    results = []
    START1 = "Location: "
    END = "\n"
    m1 = re.compile(r'%s(.*?)%s' % (START1,END))
    START2 = "Party: "
    m2 = re.compile(r'%s(.*?)%s' % (START2,END))
    START3 = "Result: "
    m3 = re.compile(r'%s(.*?)%s' % (START3,END))
    for cnt in range(0,leng):
        locas.append(m1.search(texts[cnt]).group(1))
        parties.append(m2.search(texts[cnt]).group(1))
        results.append(m3.search(texts[cnt]).group(1))
    f.write("**Local Events:**  \n\n")
    for cnt in range(0,leng):
        f.write("The group of " + parties[cnt] + " were ")
        if results[cnt] == 'Success':
            f.write("successful ")
        else:
            f.write("unsuccessful")
        f.write(" in their exploration of " + locas[cnt])
        f.write(". Read their report at [" + titles[cnt] + ".](https://www.reddit.com/r/AdventuresInWestmarch/comments/" + links[cnt] + ")  \n&nbsp;\n\n")
    if comp == 0:
        f.write("Nothing of note  \n&nbsp;\n\n")
    return(parties, results, locas, links, titles)

def get_renown(players, names):
    ren = open("renown.txt", "w+")
    ren.write("If adding a new user or editing, please follow the formatting:  \n\nuser:`space`username|name:`space`character name|npcname:`space`renown#|`newline`\n\nOr the code won't work for the bot.  \n\n&nbsp;  \n\nUser | Name | Dina Stumbletoe | Ilbryn Vulre | Medwin of Llanport | Lundrak Honorgrip\n-|-|-|-|-|-\n")
    Wiki = r.subreddit("AdventuresInWestmarch").wiki["renown"]
    m1 = re.compile(r'user: (.*?)\|')
    m2 = re.compile(r'name: (.*?)\|')
    m3 = re.compile(r'dina: (.*?)\|')
    m4 = re.compile(r'ilbryn: (.*?)\|')
    m5 = re.compile(r'medwin: (.*?)\|')
    m6 = re.compile(r'lundrak: (.*?)\|')
    m7 = re.compile(r'user:.*?\n')
    userids = m1.findall(Wiki.content_md)
    usernms = m2.findall(Wiki.content_md)
    dina = [int(i) for i in (m3.findall(Wiki.content_md))]
    ilbryn = [int(i) for i in (m4.findall(Wiki.content_md))]
    medwin = [int(i) for i in (m5.findall(Wiki.content_md))]
    lundrak = [int(i) for i in (m6.findall(Wiki.content_md))]
    holder = m7.findall(Wiki.content_md)
    for cnt in range(len(holder)):
        ren.write(holder[cnt] + "\n")
    misgu1 = collections.OrderedDict.fromkeys(userids)
    misgu2 = collections.OrderedDict.fromkeys(players)
    misgu = [x for x in misgu2 if x not in misgu1]
    misgn1 = collections.OrderedDict.fromkeys(usernms)
    misgn2 = collections.OrderedDict.fromkeys(names)
    misgn = [x for x in misgn2 if x not in misgn1]
    if not len(misgu) == 0:
        if len(misgu) == (len(names)-len(userids)):
            for cnt in range(len(misgn)):
                userids.append(misgu[cnt])
                usernms.append(misgn[cnt])
                ren.write("user: " + misgu[cnt] + "|name: " + misgn[cnt] + "|dina: 1|ilbryn: 1|medwin: 1|lundrak: 1|\n")
    ren.close
    with open("renown.txt", "r") as ren:
        bodyw = ren.read()
    r.subreddit("AdventuresInWestmarch").wiki["renown"].edit(bodyw, reason='matching to flair list')
    return(userids, usernms, dina, ilbryn, medwin, lundrak)

# def get_news(userids, usernms, dina, ilbryn, medwin, lundrak):
#     
#     nc = random.randint(1,4)
#     for cnt in range(1,nc+1):
#         nt = random.randint(1,100)
#         if nt < 11:
#             ntm = random.randint(1,6)
#             if ntm == 1:
#                 bnty = "an evil cult"
#             elif ntm == 2:
#                 bnty = "a clan of orcs"
#             elif ntm == 3:
#                 bnty = "a beholder"
#             elif ntm == 4:
#                 bnty = "a hag coven"
#             elif ntm == 5:
#                 bnty = "a horde of kobolds"
#             else:
#                 bnty = "an illithid elder brain"
#             
# #             


def run_bot(r):
    r.subreddit('AdventuresInWestmarch').submit(title = title, selftext = bodyt)

    
# if not os.path.isfile("posts_replied_to.txt"):
#     posts_replied_to = []
# else:
#     with open("posts_replied_to.txt", "r") as f:
#         posts_replied_to = f.read()
#         posts_replied_to = posts_replied_to.split("\n")
#         posts_replied_to = list(filter(None, posts_replied_to))


r = bot_login() #begins reddit interaction
subreddit = r.subreddit("AdventuresInWestmarch") #declare subreddit location
f = open("msg.txt", "w+")
title = get_title()
users = get_users()
get_weather(f)
(players, names) = get_players()
(userids, usernms, dina, ilbryn, medwin, lundrak) = get_renown(players, names)
# get_news(players, names)
(parties, results, locas, links, titles) = get_sums(f)
get_heads(f)

#     f.write("**Medwin's Watch:**  \n")

f.close


# indices = [i for i, x in enumerate(list(dina)) if x >= 1]
# print(indices)
# for ind in range(len(indices)):
#     print(userids[indices[ind]])
#     print(usernms[indices[ind]])




# for s in users:
#     r.redditor(s).message('Hello From Westbach', msg)





with open("msg.txt", "r") as f:
    bodyt = f.read()
 
 
 
 
# r.subreddit('AdventuresInWestmarch').submit(title = title, selftext = bodyt)
# r.subreddit('test').submit(title = title, selftext = bodyt)

# run_bot(r)
# f.close()
# os.remove('msg.txt')
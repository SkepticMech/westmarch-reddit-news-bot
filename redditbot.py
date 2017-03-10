# pylint: disable=C0301
'''
Created on Feb 21, 2017

'''
print
import time
from random import randint
from random import choice
from random import sample
from random import choices
from datetime import datetime
from datetime import timedelta
from collections import OrderedDict
import re
import praw
import config


def weighted_choose_subset(weighted_set, count):
    """Return a random sample of count elements from a weighted set.

    weighted_set should be a sequence of tuples of the form 
    (item, weight), for example:  [('a', 1), ('b', 2), ('c', 3)]

    Each element from weighted_set shows up at most once in the
    result, and the relative likelihood of two particular elements
    showing up is equal to the ratio of their weights.
    """
    if count == 0:
        return []

    total_weight = 0
    max_weight = 0
    borders = []
    for item, weight in weighted_set:
        if weight < 0:
            raise RuntimeError("All weights must be positive integers")
        # Scale up weights so dividing total_weight / count doesn't truncate:
        weight *= count
        total_weight += weight
        borders.append(total_weight)
        max_weight = max(max_weight, weight)

    step = int(total_weight / count)

    if max_weight > step:
        raise RuntimeError(
            "Each weight must be less than total weight / count")

    next_stop = randint(0, step - 1)

    results = []
    current = 0
    for i in range(count):
        while borders[current] <= next_stop:
            current += 1
        results.append(weighted_set[current][0])
        next_stop += step

    return results
def bot_login():
    """Pulls data from config.py to log into reddit as a remote bot"""
    print("Logging in...")
    reddit = praw.Reddit(username=config.username, password=config.password, client_id=config.client_id, client_secret=config.client_secret, user_agent="SketpicMech post tester v0.2")
    print("Logged in!")
    return reddit
def get_weatherb():
    """Generates the upcoming week's weather and saves to file"""
    weathwet = [0.7, 0.05, 0.05, 0.1, 0.09, 0.01]
    weathwec = [0.7, 0.03, 0.07, 0.1, 0.09, 0.01]
    weathwed = [0.7, 0.1, 0.1, 0.09, 0.01]
    weathnmt = ["weather normal for the season", "warmer days as a heatwave moves through", "colder days and nights", "a good amount of rain", "snow most days", "severe winds"]
    weathnmc = ["cold and calm conditions", "abnormally warm days", "very cold winds", "heavy snows", "a snowstorm lasting most of the week", "a blizzard to cover the slopes"]
    weathnmd = ["hot and calm", "hot and windy", "hot and very windy", "sandstorms", "downpour"]
    weatht = choices(weathnmt, weights=weathwet, k=1)
    weathc = choices(weathnmc, weights=weathwec, k=1)
    weathd = choices(weathnmd, weights=weathwed, k=1)
    f.write("**Ilbryn Vulre's Weekly Weather Report:**\n\n")
    f.write("Once again, I have spent much time studying the hemispheric patterns of this part of the planet so that I may predict the patterns of upper atmosphere, precipitations, droughts, and other nasty bits of weather. To this point I have determined that the patterns for the next week. ")
    f.write("In the area around Westbach, expect " + weatht[0] + ". If you are venturing into the mountains, be prepared for " + weathc[0] + ".\n\n")
    f.write("As always, please refrain from visiting my tower lest you truly have something of import to discuss.\n&nbsp;\n\n&nbsp;&nbsp;&nbsp;&nbsp;~ Ilbryn Vulre, High Wizard of the Order of Scagaros, and Savior of the Bogol Valley\n\n&nbsp;\n\n")

def get_weathera():
    """Generates the upcoming week's weather and saves to file"""
    weath1 = []
    weath2 = []
    for cnt in range(1, 8):
        ca1 = randint(1, 101)
        ca2 = randint(1, 101)
        if ca1 < 71:
            weatha = 'Pleasant'
        elif 70 < ca1 < 81:
            cb1 = randint(1, 2)
            if cb1 < 2:
                weatha = 'Hot'
            else:
                weatha = 'Cool'
        elif 80 < ca1 < 91:
            weatha = 'Rain'
        elif 90 < ca1 < 100:
            weatha = 'Thunderstorms'
        else:
            weatha = 'Tornado'
        if ca2 < 71:
            weathb = 'Calm'
        elif 70 < ca2 < 81:
            cb2 = randint(1, 10)
            if cb2 < 4:
                weathb = 'Warm'
            else:
                weathb = 'Cold'
        elif 80 < ca2 < 91:
            weathb = 'Snow'
        elif 90 < ca2 < 100:
            weathb = 'Snowstorm'
        else:
            weathb = 'Blizzard'
        weath1.append(weatha)
        weath2.append(weathb)
    f.write("**Ilbryn Vulre's Weekly Weather Report:**  \n\nOnce again, I have spent much ")
    f.write("time studying the hemispheric patterns of this part of the planet so that I ")
    f.write("may predict the patterns of upper atmosphere, precipitations, droughts, and ")
    f.write("other nasty bits of weather. To this point I have ")
    f.write("determined that the patterns for the next week shall be as follows:  \n\n")
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
    f.write("As always please refrain from visiting my tower lest you truly have something ")
    f.write("of import to discuss.\n&nbsp;\n\n&nbsp;&nbsp;&nbsp;&nbsp;~ Ilbryn Vulre, High ")
    f.write("Wizard of the Order of Scagaros, and Savior of the Bogol Valley\n\n&nbsp;\n\n")

def get_heads():
    """Selects the far east headlines for the weeks message"""
    with open("headlines.txt", "r") as headst:
        heads = headst.read()
        heads = heads.split("\n")
        heads = list(filter(None, heads))
    with open("headlines_used.txt", "r") as headut:
        headu = headut.read()
        headu = headu.split("\n")
        headu = list(filter(None, headu))
    hdl1 = OrderedDict.fromkeys(headu)
    hdl2 = OrderedDict.fromkeys(heads)
    hdl = [x for x in hdl2 if x not in hdl1]
    f.write("**Top Stories From The East:**\n\n")
    f.write(hdl[0] + "\n\n")
    howmany = randint(1, 3)
    for cnt in range(howmany):
        d6 = randint(1, 6)
        if d6 < 4:
            d10 = str(randint(1, 10))
            if d10 != "3" and d10 != "10":
                filenm = "discs\\disc" + d10 + ".txt"
                filenmu = "discs\\disc" + d10 + "u.txt"
                with open(filenm, "r") as discst:
                    discs = discst.read()
                    discs = discs.split("\n")
                    discs = list(filter(None, discs))
                with open(filenmu, "r") as discsut:
                    discsu = discsut.read()
                    discsu = discsu.split("\n")
                    discsu = list(filter(None, discsu))
                discs1 = OrderedDict.fromkeys(discsu)
                discs2 = OrderedDict.fromkeys(discs)
                disc = [x for x in discs2 if x not in discs1]
                with open(filenmu, "a") as discsut:
                    discsut.write(disc[0] + "\n")
                if len(disc) < 6:
                    errs.write("discs" + d10 + "\n")
                if d10 == "1":
                    f.write("Archaeologists have discovered the remains of " + disc[0] + ", a city long thought lost\n\n")
                elif d10 == "2":
                    f.write("After much research, scholars have determined that their samples do constitute a new breed of creature, and have dubbed them, " + disc[0] + "\n\n")
                elif d10 == "4":
                    f.write("A new deity has revealed itself to several high priests, calling itself " + disc[0] + "\n\n")
                elif d10 == "5":
                    f.write("Archaeologists have unearthed a long lost relic, known as the " + disc[0] + "\n\n")
                elif d10 == "6":
                    f.write("Explorers have returned after discovering a new land, which they have named " + disc[0] + "\n\n")
                elif d10 == "7":
                    f.write("Prominent scholars and wizards are still investigating the new phenomena, they have decided to call it a " + disc[0] + "\n\n")
                elif d10 == "8":
                    f.write("Citizens of a small fishing village up north were amazed when a ship arrived carrying a group claiming to hail a land far across the sea. These strange creatures are the first seen members of a race they say are called the ‘" + disc[0] + "'\n\n")
                else:
                    f.write("Botanists have discovered a new plant which they are calling, " + disc[0] + ", and alchemists are excited about its promising new properties\n\n")
            elif d10 == "3":
                qual = randint(1, 2)
                if qual == 1:
                    filenm = "discs\\disc3i.txt"
                    filenmu = "discs\\disc3iu.txt"
                else:
                    filenm = "discs\\disc3s.txt"
                    filenmu = "discs\\disc3su.txt"
                with open(filenm, "r") as discst:
                    discs = discst.read()
                    discs = discs.split("\n")
                    discs = list(filter(None, discs))
                with open(filenmu, "r") as discsut:
                    discsu = discsut.read()
                    discsu = discsu.split("\n")
                    discsu = list(filter(None, discsu))
                discs1 = OrderedDict.fromkeys(discsu)
                discs2 = OrderedDict.fromkeys(discs)
                disc = [x for x in discs2 if x not in discs1]
                with open(filenmu, "a") as discsut:
                    discsut.write(disc[0] + "\n")
                if len(disc) < 6:
                    if qual == 1:
                        errs.write("discs3i\n")
                    else:
                        errs.write("discs3u\n")
                if qual == 1:
                    f.write("Tech News: What is a " + disc[0] + ", and where can you get one for yourself?\n\n")
                else:
                    f.write("The latest craze at magic academies across the nation is a new spell called, " + disc[0] + ", but what does it do?\n\n")
            else:
                with open("discs\\disc101.txt", "r") as resorct:
                    resorc = resorct.read()
                    resorc = resorc.split("\n")
                    resorc = list(filter(None, resorc))
                with open("discs\\disc102.txt", "r") as townt:
                    town = townt.read()
                    town = town.split("\n")
                    town = list(filter(None, town))
                f.write("Trade: The future is looking bright for the town of " + choice(town) + ", where a new " + choice(resorc) + " was just discovered\n\n")
        elif 3 < d6 < 6:
            d10 = str(randint(1, 10))
            filenm = "factions\\facs" + d10 + ".txt"
            filenmu = "factions\\facs" + d10 + "u.txt"
            with open(filenm, "r") as facst:
                facs = facst.read()
                facs = facs.split("\n")
                facs = list(filter(None, facs))
            with open(filenmu, "r") as facsut:
                facsu = facsut.read()
                facsu = facsu.split("\n")
                facsu = list(filter(None, facsu))
            facs1 = OrderedDict.fromkeys(facsu)
            facs2 = OrderedDict.fromkeys(facs)
            fac = [x for x in facs2 if x not in facs1]
            with open(filenmu, "a") as facsut:
                facsut.write(fac[0] + "\n")
            if len(fac) < 6:
                errs.write("facs" + d10 + "\n")
            if d10 == "1":
                f.write("Alert: A new gang calling themselves " + fac[0] + " have been terrorizing citizens, especially careful when traveling after dusk\n\n")
            elif d10 == "2":
                f.write("A new guild, " + fac[0] + ", is looking for members, if interested, stop by their local guild hall\n\n")
            elif d10 == "3":
                f.write("Magicians take note, the " + fac[0] + " is the new big name in town when it comes to the arcane arts\n\n")
            elif d10 == "4":
                f.write("Attention: " + fac[0] + " is once again looking for new recruits, if you think you have what it takes, prove yourself at the open tournament this Sunday\n\n")
            elif d10 == "5":
                f.write("Let it be known that the family of the honorable Sir " + fac[0] + ", and all his decedents have been granted peerage by the throne\n\n")
            elif d10 == "6":
                f.write("A large number of individuals have been stoping citizens and stating, '" + fac[0] + "' They seem to be looking for a particular responce; a 30 silver reward will be given to any who can discover what it is\n\n")
            elif d10 == "7":
                f.write("Explorers have returned from the far west bringing introductions and tidings from the newly discovered " + fac[0] + "\n\n")
            elif d10 == "8":
                f.write("Update: The uproar in the religious spheres has calmed, and the splinter group has been officially recognized as the " + fac[0] + "\n\n")
            elif d10 == "9":
                f.write("There is a new bastion of knowledge in the world; " + fac[0] + " officially opened its gates last Tuesday\n\n")
            else:
                f.write("The kingdom is in uproar after it was revealed that a secret group calling themselves The " + fac[0] + " had managed to place its members in key positions in nearly every level of the government\n\n")
        else:
            with open("invaders.txt", "r") as invadest:
                invades = invadest.read()
                invades = invades.split("\n")
                invades = list(filter(None, invades))
            resultt = choice(invades)
            dave.write("A new force in the West Marches has been selected, roll result was: " + resultt + "\n\n")
    f.write(hdl[1])
    with open("headlines_used.txt", "a") as hedlu:
        hedlu.write(hdl[0] + "\n" + hdl[1] + "\n")
    if (len(hdl)-2) < 6:
        errs.write("headlines\n")
def get_title():
    """Returns the headline string to be used in the post"""
    date = time.strftime("%B %d, 13%y")
    ttle = "The Westbach Times "+ date
    return ttle
            
def get_users():
    """Finds all the currently approved submitters on the subreddit and returns their ids"""
    us = open("users.txt", "w+") #open/create the approved user file for westmarch
    users = []
    for contributor in r.subreddit('AdventuresInWestmarch').contributor: #pulls all approved users
        us.write(contributor.name + "\n") # adds user to text file
        if not contributor.name == 'DM_Dave': # 
            users.append(contributor.name) #
    us.close
    return users

def get_players():
    """Using the personal flair list, retrieves all the player data; name, class, user id, for all who have done so"""
    players = []
    names = []
    clases = []
    py = open("players.txt", "w+")
    for flair in r.subreddit('AdventuresInWestmarch').flair(limit=None):
        user = flair['user']
        if not flair['flair_css_class'] == 'dm':
            players.append(user.name)
            names.append(flair['flair_text'])
            clases.append(flair["flair_css_class"])
            py.write(user.name + "\t" + flair['flair_text'] + "\t" + flair['flair_css_class'] + "\n")
    py.close()
    clasdic = {"barb":"barbarian", "fight":"fighter", "palad":"paladin", "rang":"ranger", "sorc":"sorcerer", "war":"warlock", "wiz":"wizard"}
    classes = [clasdic[n] if n in clasdic else n for n in clases]
    return (players, names, classes)

def get_sums():
    """Attempts to idendentify all mission summaries created in the past week, and provide a link with basic information about them"""
    links = []
    texts = []
    titles = []
    parties = []
    locas = []
    results = []
    comp = 0
    for submission in subreddit.hot(limit=20):
        age = (datetime.fromtimestamp(submission.created).date() - datetime.now().date())
        if timedelta(days=-8) < age and submission.link_flair_text == 'Mission Write-up':
            texts.append(submission.selftext)
            links.append(submission.id)
            titles.append(submission.title)
            comp = 1
    leng = len(links)
    m1 = re.compile(r'Location: (.*?)\n')
    m2 = re.compile(r'Party: (.*?)\n')
    m3 = re.compile(r'Result: (.*?)\n')
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



def get_renown(posts):
    """Pulls data from the /wiki/renown pagd of the subreddit to determine the ranks of all PCs with the townsfolk"""
    ren = open("renown.txt", "w+")
    ren.write("User | Name | Dina Stumbletoe | Ilbryn Vulre | Medwin of Llanport | Lundrak Honorgrip\n-|-|-|-|-|-\n")
    Wiki = r.subreddit("AdventuresInWestmarch").wiki["renown"]
    grabber = re.compile(r'\n([a-zA-Z0-9_ ]+?)\|([A-Za-z ]+)\|([0-9]+)\|([0-9]+)\|([0-9]+)\|([0-9]+)')
    alldata = grabber.findall(Wiki.content_md)
    userides = []
    usernames = []
    dinas = []
    ilbryns = []
    medwins = []
    lundraks = []
    for cntr in range(len(alldata)):
        holders = alldata[cntr]
        userides.append(holders[0])
        usernames.append(holders[1])
        dinas.append(holders[2])
        ilbryns.append(holders[3])
        medwins.append(holders[4])
        lundraks.append(holders[5])
    repetco = []
    repetci = []
    for spot in range(len(players)):
        repetco.append((players[spot], names[spot]))
    for spot in range(len(userides)):
        repetci.append((userides[spot], usernames[spot]))
    repetco = dict(repetco)
    repetci = dict(repetci)
    for pers in userides:
        if repetci[pers] != repetco[pers]:
            repetci[pers] = repetco[pers]
        usernames[userides.index(pers)] = repetci[pers]
    for cnt in range(len(usernames)):
        ren.write(userides[cnt] + "|" + usernames[cnt] + "|" + dinas[cnt] + "|" + ilbryns[cnt] + "|" + medwins[cnt] + "|" + lundraks[cnt] + "\n")
    misgu1 = OrderedDict.fromkeys(players)
    misgu2 = OrderedDict.fromkeys(userides)
    misgu = [x for x in misgu1 if x not in misgu2]
    misgn1 = OrderedDict.fromkeys(names)
    misgn2 = OrderedDict.fromkeys(usernames)
    misgn = [x for x in misgn1 if x not in misgn2]
    if len(misgu) != 0:
        for cnt in range(len(misgu)):
            userides.append(misgu[cnt])
            usernames.append(misgn[cnt])
            ren.write(misgu[cnt] + "|" + misgn[cnt] + "|1|1|1|1\n")
    with open("renown.txt", "r") as ren:
        bodyw = ren.read()
    if posts == 1:
        r.subreddit("AdventuresInWestmarch").wiki["renown"].edit(bodyw, reason='matching to flair list')
    return(userides, usernames, dinas, ilbryns, medwins, lundraks)
def get_rums(posts):
    """
    Selects several rumours for the week and alerts the relevent users:
    Everyone-add to the weekly post
    Individuals-send a message to relevent users and add info to dave's weekly message
    Hidden-adds info to daves message
    """

    nullist = 1
    necros = 0
    gobos = 0
    seelie = 0
    sinks = 0
    bandits = 0
    drags = 0
    rweights = [('a', 10), ('b', 10), ('c', 10), ('d', 10), ('e', 5), ('f', 10), ('g', 5), ('h', 10), ('i', 5), ('j', 10), ('k', 5), ('l', 9), ('m', 1)]
    rumscnt = randint(1, 4)
    alevnts = weighted_choose_subset(rweights, rumscnt)
    for elms in alevnts:
        if elms == 'a':
            medren = randint(1, max(medwin))
            filenm = "npcs\\medwin" + str(medren) + ".txt"
            filenmd = "npcs\\medwin" + str(medren) + "m.txt"
            with open(filenm, "r") as monstt:
                monst = monstt.read()
                monst = monst.split("\n")
                monst = list(filter(None, monst))
            with open(filenmd, "r") as discst:
                discs = discst.read()
                discs = discs.split("\n")
                discs = list(filter(None, discs))
            monch = choice(range(len(monst)))

            dave.write("Medwin places bounty on " + monst[monch] + " (" + discs[monch] + ") to all players at renown: " + str(medren) + " or above.\n\n")
            medppl = [i for i, v in enumerate(medwin) if v >= medren]
            for dis in medppl:
                msg = "Hello " + usernms[dis] + ",\n&nbsp;\n\nYou seem to be quite the reliable " + classes[dis] + ", so I will let you in on this a bit early. Lately, I've head some trouble with " + monst[monch] + " threatening the town, so I've decided to enlist some help by placing a bounty. If you can put an end to this mess, its all yours.\n&nbsp;\n\nAs my monther used to say, " + choice(medwins) + "\n&nbsp;\n\nBest of luck,\n\nMedwin of Llanport"
                if posts == 1:
                    r.redditor(str(userids[dis])).message('Bounty for the taking', msg)
        elif elms == 'b':
            ilbren = randint(1, max(ilbryn))
            filenm = "npcs\\ilbryn.txt"
            filenmu = "npcs\\ilbrynu.txt"
            with open(filenm, "r") as ilbst:
                ilbs = ilbst.read()
                ilbs = ilbs.split("\n")
                ilbs = list(filter(None, ilbs))
            with open(filenmu, "r") as ilbsut:
                ilbsu = ilbsut.read()
                ilbsu = ilbsu.split("\n")
                ilbsu = list(filter(None, ilbsu))
            ilb1 = OrderedDict.fromkeys(ilbsu)
            ilb2 = OrderedDict.fromkeys(ilbs)
            ilb = [x for x in ilb2 if x not in ilb1]
            if len(ilb) < 6:
                errs.write("ilbryn\n")
            with open(filenmu, "a") as ilbrn:
                ilbrn.write(ilb[0] + "\n")
            dave.write("Ilbryn looking for " + ilb[0] + ", from all players at renown: " + str(ilbren) + " or above.\n\n")
            ilbppl = [i for i, v in enumerate(ilbryn) if v >= ilbren]
            for dis in ilbppl:
                msg = usernms[dis] + ",\n&nbsp;\n\nYou are a bit less idiotic than the other fools living in this town. Loathe though I am to admit it, I require assistance. I find myself in short supply of " + ilb[0] + ", a critical component for my current experiments. I would be willing to compensate you quite handsomely if you retrieve more of it for me. If you are intelligent enough to accept this generous offer, I will permit you to visit me in my tower to discuss the details.\n&nbsp;\n\nIlbryn Vulre, High Wizardof the Order of Scagaros, and Savior of the Bogol Valley"
                if posts == 1:
                    r.redditor(str(userids[dis])).message('Reagent Wanted', msg)
        elif elms == 'c':
            dinren = randint(1, max(dina))
            filenm = "npcs\\dina.txt"
            filenmu = "npcs\\dinau.txt"
            with open(filenm, "r") as dinst:
                dins = dinst.read()
                dins = dins.split("\n")
                dins = list(filter(None, dins))
            with open(filenmu, "r") as dinsut:
                dinsu = dinsut.read()
                dinsu = dinsu.split("\n")
                dinsu = list(filter(None, dinsu))
            din1 = OrderedDict.fromkeys(dinsu)
            din2 = OrderedDict.fromkeys(dins)
            din = [x for x in din2 if x not in din1]
            if len(din) < 6:
                errs.write("dina\n")
            with open(filenmu, "a") as dinad:
                dinad.write(din[0] + "\n")
            dave.write("Dina has learned of " + din[0] + ", a bandit lurking in the area, and alerts all players at renown: " + str(dinren) + " or above.\n\n")
            dinppl = [i for i, v in enumerate(dina) if v >= dinren]
            for dis in dinppl:
                msg = "Hello " + usernms[dis] + ",\n&nbsp;\n\nI know you have a knack for tackling difficult marks. My contacts have alerted me that a prominent bandit by the name of " + din[0] + " is hiding out near town. Find me if you are interested in more information.\n&nbsp;\n\nAll the best,\n\nDina Stumbletoe"
                if posts == 1:
                    r.redditor(str(userids[dis])).message('Wanted Criminal', msg)
        elif elms == 'd':
            lunren = randint(1, max(lundrak))
            filenm = "npcs\\lundrak.txt"
            with open(filenm, "r") as lunst:
                luns = lunst.read()
                luns = luns.split("\n")
                luns = list(filter(None, luns))
            shrine = choice(range(len(luns)))
            dave.write("Lundrak has a vision and tells " + luns[shrine] + " to all players at renown: " + str(lunren) + " or above.\n\n")
            lunppl = [i for i, v in enumerate(lundrak) if v >= lunren]
            for dis in lunppl:
                msg = usernms[dis] + ",\n&nbsp;\n\nI have had a vision that " + luns[shrine] + " I know you can take care of it." + "\n&nbsp;\n\n-Lundrak"
                if posts == 1:
                    r.redditor(str(userids[dis])).message('Divine Quest', msg)
        elif elms == 'e':
            necros = 1
            nullist = 0
        elif elms == 'f':
            gobos = 1
            nullist = 0
        elif elms == 'g':
            mtype = choice(["a tattered parchment", "a religious text filled with symbology", "a wolf skin map with markings in Goblin", "a stone tablet", "an arcane rune", "a fine vellum"])
            mdirect = choice(["the northern edge of the", "the southern edge of the", "the western edge of the", "the northwest corner of the", "southwest corner of the", "an location beyond the edge of the current"])
            trtype = choice(["a holy relic", "an arcane artifact", "a trap set by enemies", "a wealth of gold and treasure", "the last will and testament of a fallen adventurer", "another treasure map"])
            playpicer = choice(range(len(usernms)))
            playid = userids[playpicer]
            playnm = usernms[playpicer]
            dave.write(playnm + " (" + playid + ") has found a treasure map on " + mtype + ", directing them to " + mdirect + " map, and the " + trtype + " located there.\n\n")
            tmmsg = "During your past adventures, you picked up " + mtype + " despite it appearing worthless at first glance. After spending some time examining it, you realize it is a treasure map, which directs you to " + mdirect + " mapped area around Westbach."
            if posts == 1:
                r.redditor(playid).message("A map most curious", tmmsg)
        elif elms == 'h':
            with open("invaders.txt", "r") as invadest:
                invades = invadest.read()
                invades = invades.split("\n")
                invades = list(filter(None, invades))
            resultt = choice(invades)
            dave.write("A messenger arrives with news of a brewing attack, roll result was: " + resultt + "\n\n")
        elif elms == 'i':
            htype = choice(["common", "draconic", "dwarf", "elf", "giant", "goblin"])
            helpfile = "help\\help-" + htype + ".txt"
            with open(helpfile, "r") as helpst:
                helpm = helpst.read()
            reker1 = choice(userids)
            reker = str(reker1[0])
            dave.write(reker + " has received a message asking for help, language: " + htype + ".\n\n")
            if posts == 1:
                r.redditor(reker).message('A crumpled note', helpm)
        elif elms == 'j':
            seelie = 1
            nullist = 0
        elif elms == 'k':
            sinks = 1
            nullist = 0
        elif elms == 'l':
            bandits = 1
            nullist = 0
        else:
            drags = 1
            nullist = 0
            pops = ['metallic', 'chromatic ']
            dweights = [0.66, 0.34]
            dragtyp = choices(pops, weights=dweights, k=1)
    if nullist == 0:
        f.write("**Medwin's Security Update:**\n&nbsp;\n\n")
        f.write("I've got a bit of news concerning the area around town, so please pay attention.\n\n")
        if necros == 1:
            f.write("There are whispers of a necromancer raising dead in the ruins around the Badlands. These can be tricky, so be alert.\n\n")
        if gobos == 1:
            f.write("My scouts report that a battalion of goblins have moved into the foothills of Griffon's Roost. Avoid leaving town, especially at night, until we can deal with them.\n\n")
        if seelie == 1:
            f.write("I have received reports of arcane monstrosities coming from the Seelie Forest. Avoid the area until we can confirm this.\n\n")
        if sinks == 1:
            f.write("Several sinkholes have opened on the outskirts of town, we are investigating their cause.\n\n")
        if bandits == 1:
            f.write("A large number of bandits have been harassing traders on the westbound road. Be extremely careful if traveling in that area.\n\n")
        if drags == 1:
            f.write("Over the past few weeks we have seen increasing numbers of " + str(dragtyp[0]) + " dragons gathering in the Unknown Mountains. I advise caution until they disperse.\n\n")
        f.write("That is all the news for this week. Stay safe, and as my mother used to say, " + choice(medwins) + " \n\n&nbsp;\n\n")




    
r = bot_login() #begins reddit interaction
subreddit = r.subreddit("AdventuresInWestmarch") #declare subreddit location
post = 1                                    # 1 will enable uploading to the reddit, 0 will disable all uploads for the purpose of testing
f = open("msg.txt", "w+")
dave = open("davemsg.txt", "w+")
errs = open("running_low.txt", "a")
with open("npcs\\medwin.txt", "r") as medwinst:
    medwins = medwinst.read()
    medwins = medwins.split("\n")
    medwins = list(filter(None, medwins))
titlep = get_title()
(players, names, classes) = get_players()
(userids, usernms, dina, ilbryn, medwin, lundrak) = get_renown(post)
get_rums(post)
get_weatherb()
get_sums()
get_heads()
with open("msg.txt", "r") as f:
    bodyt = f.read()
with open("davemsg.txt", "r") as dave:
    davemsg = dave.read()
if post == 1:
    submission = r.subreddit('AdventuresInWestmarch').submit(title=titlep, selftext=bodyt)
    r.redditor("DM_Dave").message("Westmarch Weekly update", davemsg)

from matplotlib.pyplot import figure
import time
import json
import string
from collections import Counter
import matplotlib.pyplot as plt

################################ PART1 #######################################

f = open('tweet_data.json', 'r')
punctuation = list(string.punctuation)
stop = punctuation+[ 'a','an','the','rt', 'via','to','of','for','and','or','i','in','at','on','out','with','by','de',' ','is','am','are','my','your','our','us','me','you','it','','the','no','have','has','we','her','his','them','when','who','where','which','how','that','not','this','&amp;','from','new','la','but']

words = []
for line in f:
    tweet = json.loads(line)
    str1 = tweet['text'].encode('utf-8')
    str1 = str1.lower()
    L = str1.split(" ");
    for i in L:
        if i not in stop:
            words.append(i)

top20 = Counter(words).most_common(20)

text_file = open("term_frequencies.txt", "w")
for i in top20:
    text_file.write(str(i) + "\n")
text_file.close()

str201 = []
for i in top20:
    str201.append(str(i).split(" ")[1][:-1])

str202 = []
for i in top20:
    str202.append(str(i).split("', ")[0][2:])


liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
plt.bar(liste,str201)
plt.title("Tweet Miner")
plt.xlabel("Words")
plt.ylabel("Term Frequencies")
plt.xticks(liste, str202, rotation=75, ha='left')
plt.savefig('term_frequencies.png')
plt.show()
####################################################### PART2 #################################


import json
import string
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import operator
import time
from collections import OrderedDict


f = open("tweet_data.json", "r")
lines = f.readlines()
f.close()
twtdict = dict()
twtdatedict = dict()

for i in lines:
    tweet = json.loads(i)
    created_at_format = '%a %b %d %H:%M:%S +0000 %Y'
    stre = tweet['text']
    date = tweet["created_at"];  #date-time in ISO format
    dt = datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y") #reading date in ISO format

    stre = stre.lower()
    L = stre.split(" ");
    punctuation = list(string.punctuation)
    stop = punctuation+['a', 'an', 'the', 'rt', 'via', 'to', 'of', 'for', 'and', 'or', 'i', 'in', 'at', 'on', 'out', 'with', 'by', 'de', ' ', 'is', 'am', 'are', 'my', 'your', 'our', 'us', 'me', 'you', 'it', '', 'the', 'no', 'have', 'has', 'we', 'her', 'his', 'them', 'when', 'who', 'where', 'which', 'how', 'that', 'not', 'this', '&amp;', 'from', 'new', 'la', 'but']
    for j in L:
        try:
            if j not in stop:
                j = j.encode("utf-8")
                asd = twtdict[j]

                if asd > 0:
                    control = twtdict[j]
                    control += 1
                    del twtdict[j]
                    twtdict[j] = control

        except KeyError:
            twtdict[j] = 1

sortedtwt = sorted(twtdict.values(), reverse=True)
comilist = []

for i in range(0, 5):
    for k, l in twtdict.iteritems():
        if l == sortedtwt[i]:
            comi = str(k) + " " + str(l)
            comilist.append(comi)

comicontrol = []
for i in comilist:
    if i not in comicontrol:
        comicontrol.append(i)

first_list = []
for i in comicontrol:
    i = str(i)
    first = i.split(" ")[0]
    first_list.append(first)

a = first_list[0]
b = first_list[1]
c = first_list[2]
d = first_list[3]
e = first_list[4]

a_datelist = []
b_datelist = []
c_datelist = []
d_datelist = []
e_datelist = []

hoursforplot = set()
for i in lines:
    tweet = json.loads(i)
    created_at_format = '%a %b %d %H:%M:%S +0000 %Y'
    stre = tweet['text']
    date = tweet["created_at"];
    dt = datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y")
    dthm = dt.strftime("%Y-%m-%d %H:%M:00")
    dthmplt = dt.strftime("%H:%M")
    stre = stre.lower()
    L = stre.split(" ");
    punctuation = list(string.punctuation)
    stop = punctuation+['a', 'an', 'the', 'rt', 'via', 'to', 'of', 'for', 'and', 'or', 'i', 'in', 'at', 'on', 'out', 'with', 'by', 'de', ' ', 'is', 'am', 'are', 'my', 'your', 'our', 'us', 'me', 'you', 'it', '', 'the', 'no', 'have', 'has', 'we', 'her', 'his', 'them', 'when', 'who', 'where', 'which', 'how', 'that', 'not', 'this', '&amp;', 'from', 'new', 'la', 'but']
    hoursforplot.add(dthmplt)
    for j in L:
        if j == a:
            a_datelist.append(dthm)
        elif j == b:
            b_datelist.append(dthm)
        elif j == c:
            c_datelist.append(dthm)
        elif j == d:
            d_datelist.append(dthm)
        elif j == e:
            e_datelist.append(dthm)

a_datelist_counted = dict()
b_datelist_counted = dict()
c_datelist_counted = dict()
d_datelist_counted = dict()
e_datelist_counted = dict()


for i in a_datelist:
    if i in a_datelist_counted.keys():
        controlvalue = a_datelist_counted[i]
        if controlvalue > 0:
            control = a_datelist_counted[i]
            control += 1
            del a_datelist_counted[i]
            a_datelist_counted[i] = control
    else:
        a_datelist_counted[i] = 1

for i in b_datelist:
    if i in b_datelist_counted.keys():
        controlvalue = b_datelist_counted[i]
        if controlvalue > 0:
            control = b_datelist_counted[i]
            control += 1
            del b_datelist_counted[i]
            b_datelist_counted[i] = control
    else:
        b_datelist_counted[i] = 1

for i in c_datelist:
    if i in c_datelist_counted.keys():
        controlvalue = c_datelist_counted[i]
        if controlvalue > 0:
            control = c_datelist_counted[i]
            control += 1
            del c_datelist_counted[i]
            c_datelist_counted[i] = control
    else:
        c_datelist_counted[i] = 1

for i in d_datelist:
    if i in d_datelist_counted.keys():
        controlvalue = d_datelist_counted[i]
        if controlvalue > 0:
            control = d_datelist_counted[i]
            control += 1
            del d_datelist_counted[i]
            d_datelist_counted[i] = control
    else:
        d_datelist_counted[i] = 1

for i in e_datelist:
    if i in e_datelist_counted.keys():
        controlvalue = e_datelist_counted[i]
        if controlvalue > 0:
            control = e_datelist_counted[i]
            control += 1
            del e_datelist_counted[i]
            e_datelist_counted[i] = control
    else:
        e_datelist_counted[i] = 1

a_datelist_counted = OrderedDict(sorted(a_datelist_counted.items(), key=lambda t: (str(t[0]).split(" ")[1].split(":")[0], str(t[0]).split(" ")[1].split(":")[1])))
b_datelist_counted = OrderedDict(sorted(b_datelist_counted.items(), key=lambda t: (str(t[0]).split(" ")[1].split(":")[0], str(t[0]).split(" ")[1].split(":")[1])))
c_datelist_counted = OrderedDict(sorted(c_datelist_counted.items(), key=lambda t: (str(t[0]).split(" ")[1].split(":")[0], str(t[0]).split(" ")[1].split(":")[1])))
d_datelist_counted = OrderedDict(sorted(d_datelist_counted.items(), key=lambda t: (str(t[0]).split(" ")[1].split(":")[0], str(t[0]).split(" ")[1].split(":")[1])))
e_datelist_counted = OrderedDict(sorted(e_datelist_counted.items(), key=lambda t: (str(t[0]).split(" ")[1].split(":")[0], str(t[0]).split(" ")[1].split(":")[1])))

file2 = open("term_frequencies_overtime.txt", "a")
for i, j in a_datelist_counted.iteritems():
    file2.write(str(a) + " " + str(i) + " " + str(j) + "\n")
for i, j in b_datelist_counted.iteritems():
    file2.write(str(b) + " " + str(i) + " " + str(j) + "\n")
for i, j in c_datelist_counted.iteritems():
    file2.write(str(c) + " " + str(i) + " " + str(j) + "\n")
for i, j in d_datelist_counted.iteritems():
    file2.write(str(d) + " " + str(i) + " " + str(j) + "\n")
for i, j in e_datelist_counted.iteritems():
    file2.write(str(e) + " " + str(i) + " " + str(j) + "\n")
file2.close()

asaa = []
for i in range(23):
    asaa.append(i)
hoursforplot_list = []
for i in hoursforplot:
    hoursforplot_list.append(i)

hoursforplot_list = sorted(hoursforplot_list, key=lambda t: (str(t).split(":")[0], str(t).split(":")[1]))

plot_a = plt.plot(asaa, a_datelist_counted.values(), label=a)
plot_b = plt.plot(asaa, b_datelist_counted.values(), label=b)
plot_c = plt.plot(asaa, c_datelist_counted.values(), label=c)
plot_d = plt.plot(asaa, d_datelist_counted.values(), label=d)
plot_e = plt.plot(asaa, e_datelist_counted.values(), label=e)
plt.ylabel("Frequency of occurrence")
plt.xlabel("Time")
plt.legend(loc="upper right")
plt.xticks(asaa, hoursforplot_list, rotation=45)
plt.savefig('term_frequencies_overtime.png')
plt.show()

####################################### PART 3 ##############################

f = open('tweet_data.json', 'r')
punctuation = list(string.punctuation)
stop = punctuation+[ 'a','an','the','rt', 'via','to','of','for','and','or','i','in','at','on','out','with','by','de',' ','is','am','are','my','your','our','us','me','you','it','','the','no','have','has','we','her','his','them','when','who','where','which','how','that','not','this','&amp;','from','new','la','but']

words = []
for line in f:
    tweet = json.loads(line)
    str1 = tweet['text'].encode('utf-8')
    str1 = str1.lower()
    L = str1.split(" ");
    for i in L:
        if i not in stop:
            words.append(i)
top10 = Counter(words).most_common(10)
top10RR = []
for i in top10:
    i = str(i)
    top10RR.append(i.split(', ')[0][2:])
print top10RR

ab = 0
for i in range(len(top10RR)):
    if i == 9:
        a = top10RR[i]
        b = top10RR[0]
    else:
        a = top10RR[i]
        b = top10RR[i+1]

    ab = 0
    for j in words:
        if a in j and b in j:
            ab += 1
        else:
            continue
    print ab


file456 = open("term_cooccurrences.txt", "a")
file456.close()
plt.savefig('term_cooccurrences.png')

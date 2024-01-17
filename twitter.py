def strip_punctuation(s):
    string = str(s)
    for punct in punctuation_chars:
        string = string.replace(punct,"")
    return string

def get_pos(s):
    count = 0
    words = strip_punctuation(s).lower().split()
    for word in words:
        if word in positive_words:
            count += 1
    return count

def get_neg(s):
    count = 0
    words = strip_punctuation(s).lower().split()
    for word in words:
        if word in negative_words:
            count += 1
    return count

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

with open("project_twitter_data.csv","r") as readfile:
    datalst = []
    for lin in readfile:
        datalst.append(lin.lower().strip().split(","))

lines = []
for lin in datalst:
    tweet = lin[0]
    no_retweets = lin[1]
    no_replies = lin[2]
    pos = get_pos(tweet)
    neg = get_neg(tweet)
    net = pos - neg
    lin.append(pos)
    lin.append(neg)
    lin.append(net)
    lines.append(lin)

lines[0][0] = "Tweet"
lines[0][1] = "Number of Retweets"
lines[0][2] = "Number of Replies"
lines[0][3] = "Positive Score"
lines[0][4] = "Negative Score"
lines[0][5] = "Net Score"

with open("resulting_data.csv","w") as writefile:
    for llist in lines:
        retweets = str(llist[1])+", "
        replies = str(llist[2])+", "
        pos = str(llist[3])+", "
        neg = str(llist[4])+", "
        net = str(llist[5])+"\n"
        sline = retweets+replies+pos+neg+net
        writefile.write(sline)


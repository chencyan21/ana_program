import pandas as pd
import csv
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def isEmoji(content):
    if not content:
        return False
    if u"\U0001F600" <= content and content <= u"\U0001F64F":
        return True
    elif u"\U0001F300" <= content and content <= u"\U0001F5FF":
        return True
    elif u"\U0001F680" <= content and content <= u"\U0001F6FF":
        return True
    elif u"\U0001F1E0" <= content and content <= u"\U0001F1FF":
        return True
    else:
        return False

def compound(review):
    sid = SentimentIntensityAnalyzer()
    res = sid.polarity_scores(review)
    return res['compound']

with open('C:\\Users\85898\Desktop\Problem_C_Data\pacifier.csv',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    csv_reader = csv.DictReader(f,fieldnames=headers)
    total = []
    for row in csv_reader:
        d = {}
        for k,v in row.items():
            d[k] = v

        single = []

        star_rating = d['star_rating']
        single.append(star_rating)

        review = d['review_headline']+" "+d['review_body']
        for i in review:
            if isEmoji(i):
                if b'\xf0\x9f\x98\x91' <= i.encode('utf-8') <= b'\xf0\x9f\x98\x95' or i.encode('utf-8') == b'\xf0\x9f\x91\x8e':
                    review = review.replace(i,"bad")
                elif b'\xf0\x9f\x8f\xbb' <= i.encode('utf-8') <= b'\xf0\x9f\x8f\xbd':
                    review = review.replace(i,".")
                else:
                    review = review.replace(i, "good")
        score = compound(review)
        single.append(score)

        if d['total_votes'] == '0':
            helpfulness_rating = 0
        else:
            helpfulness_rating = int(d['helpful_votes']) / int(d['total_votes'])
        single.append(helpfulness_rating)

        review_date = d['review_date']
        single.append(review_date)

        total.append(single)

header = ['star_ratings', 'compounds', 'helpfulness_ratings', 'review_date']

with open('C:\\Users\85898\Desktop/pacifier_process.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(total)

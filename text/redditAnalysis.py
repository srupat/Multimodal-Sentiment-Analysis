import praw 
import string
import nltk
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('punkt') #to tokenize 
nltk.download('stopwords') #to remove stopwords
nltk.download('vader_lexicon')
 
user_agent = "https://github.com/apoorvapendse";
reddit = praw.Reddit(
    client_id="axhrfHILsS7sSnVWeP4CVA",
    client_secret="ApvM3QXdvH1z30oppvjhPN8upqFD_Q",
    user_agent = user_agent
)

redditPosts = [];

headlines = set()
for submission in reddit.subreddit("politics").hot(limit=10):
    
    redditPosts.append([submission.title])

text = ''

for post in redditPosts:
    text = text + post[0]    

lower_case = text.lower()

#remove all punctuations
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

#split the sentence into words that are then stored in a list
tokenized_words = word_tokenize(cleaned_text,"english")

#final words is a list of words that do not contain stop words
final_words=[]
for word in tokenized_words:
  if word not in stopwords.words('english'):
    final_words.append(word)

emotion_list=[]

#we are using with statement so that we dont have to close the file once opened
with open('emotions.txt','r') as file:
  for line in file:
    
    #replacing the new line in between 2 lines with nothing, replacing commas with nothing, replacing         apostrophe('') with nothing
    clear_line = line.replace("\n",'').replace(",",'').replace("'",'').strip()

    #word and emotion are 2 variables where the word and the emotion from respective line is stored
    word, emotion = clear_line.split(':')

    if word in final_words:
      emotion_list.append(emotion)


#Counter using collections library(to count emotions)
w=Counter(emotion_list)

def sentiment_analyse(sentiment_text):
  score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
  neg = score['neg']
  pos = score['pos']
  if neg > pos:
    print("Negative sentiment")
  elif pos>neg:
    print("Positive sentiment")
  else:
    print("Neutral sentiment")    

sentiment_analyse(cleaned_text)


#making a subplot
fig,ax1=plt.subplots()

#bar graph generation with keys(emotions) on x axis and values(count) on y axis
ax1.bar(w.keys(),w.values())

#slanting emotions below x axis
fig.autofmt_xdate()

#save to graph.png file
plt.savefig('graph.png')

#show graph on screen
plt.show()


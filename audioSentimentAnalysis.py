import string
import nltk
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
import pyttsx3
recognizer = sr.Recognizer()

nltk.download('punkt') #to tokenize 
nltk.download('stopwords') #to remove stopwords
nltk.download('vader_lexicon')


#record audio
with sr.Microphone(device_index=1) as source:
  print('Clearing background noise...')
  recognizer.adjust_for_ambient_noise(source,duration=3)
  print('Waiting for your message...')
  recordedAudio = recognizer.listen(source)
  print('Done recording!')
  # source.close()

#exception handling to throw errors if program goes wrong and to print the message using google language recognizer 
try:
    print('Printing the message...')
    text = recognizer.recognize_google(recordedAudio,language='en-US')
    print('Your message:{}'.format(text))
except Exception as ex:
    print(ex)

#convert to lower case
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
  sentiment = [score['pos'],score['neg'],score['neu']]
  sen_labels = ['Positive','Negative','Neutral']
  neg = score['neg']
  pos = score['pos']
  if neg > pos:
    print("Negative sentiment")
  elif pos>neg:
    print("Positive sentiment")
  else:
    print("Neutral sentiment") 
  plt.axis("equal")
  plt.pie(sentiment,labels=sen_labels,autopct='%.2f') 
  plt.savefig('graph.png')
  plt.show()    

sentiment_analyse(cleaned_text)


# #making a subplot
# fig,ax1=plt.subplots()

# #bar graph generation with keys(emotions) on x axis and values(count) on y axis
# ax1.bar(w.keys(),w.values())

# #slanting emotions below x axis
# fig.autofmt_xdate()

# #save to graph.png file
# plt.savefig('graph.png')

# #show graph on screen
# plt.show()
#can be used for content on social media that is on the form of images 

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


import pytesseract as pyt
import cv2

img = cv2.imread("titanic.jpg")

pyt.pytesseract.tesseract_cmd = "C:\\Users\\sruja\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

textimg = pyt.image_to_string(img)

#print(textimg)

with open("imageRead.txt","w") as f:
  f.write(textimg)

text = open('imageRead.txt','r').read()

#print(text)

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
  sentiment = [score['pos'],score['neg']]
  sen_labels = ['Positive','Negative']
  neg = score['neg']
  pos = score['pos']
  if neg > pos:
    print("Negative sentiment")
  elif pos>neg:
    print("Positive sentiment")
  else:
    print("Neutral sentiment") 
  plt.axis("equal")
  plt.pie(sentiment,labels=sen_labels) 
  plt.savefig('graph.png')
  plt.show()    

sentiment_analyse(cleaned_text)




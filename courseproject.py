#from twitterAnalysis import twitterAnalysis


import string
from collections import Counter
import matplotlib.pyplot as plt

#most of the text on the net is of the encoding 'utf-8'
text = open('read.txt',encoding='utf-8').read()

#convert to lower case
lower_case = text.lower()

#remove all punctuations
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

#split the sentence into words that are then stored in a list
tokenized_words = cleaned_text.split()

#stop words are the words which dont carry any sentiment, basically they are of no use to us
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which","who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why","how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not","only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


#final words is a list of words that do not contain stop words
final_words=[]
for word in tokenized_words:
  if word not in stop_words:
    final_words.append(word)

emotion_list=[]

#we are using with statement so that we dont have to close the file once opened
with open('emotions.txt','r') as file:
  for line in file:
    
    #replacing the new line in between 2 lines with nothing, replacing commas with nothing, replacing         apostrophe('') with nothing
    clear_line = line.replace("\n",'').replace(",",'').replace("'",'').strip()

    #word and emotion are 2 variables where the word and the emotion from repective line is stored
    word, emotion = clear_line.split(':')

    if word in final_words:
      emotion_list.append(emotion)


#Counter using collections library(to count emotions)
w=Counter(emotion_list)

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
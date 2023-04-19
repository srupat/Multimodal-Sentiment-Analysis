import string
from collections import Counter
import matplotlib.pyplot as plt
text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
tokenized_words = cleaned_text.split()
#print(tokenized_words)

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

final_words=[]
for word in tokenized_words:
  if word not in stop_words:
    final_words.append(word)
#print(final_words)    

#we are using with statement so that we dont have to close the file

emotion_list=[]


with open('emotions.txt','r') as file:
  for line in file:
    #replacing the new line in between 2 lines with nothing, replacing commas 
    #with nothing, replacing apostrophe('') with nothing
    clear_line = line.replace("\n",'').replace(",",'').replace("'",'').strip()
    word, emotion = clear_line.split(':')

    if word in final_words:
      emotion_list.append(emotion)

w=Counter(emotion_list)


fig,ax1=plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
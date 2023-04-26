print("Enter the mode of sentiment analysis that you want to perform")
n = int(input("Enter 1 to perform Text Sentiment Analysis\nEnter 2 to perform Image Sentiment Analysis\nEnter 3 to perform Audio Sentiment Analysis\nEnter 4 to perform Video Sentiment Analysis\n"))

if n==1:
    import textSentimentAnalysis
if n==2:
    import imageSentimentAnalysis    
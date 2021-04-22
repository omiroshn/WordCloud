# Importing the Libraries
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import matplotlib.pyplot as plt

# Read Netflix dataset
data = pd.read_csv("top50.csv")

#Setting the comment and stop words
stop_words = set(STOPWORDS)
comment_words = ""

# Iterating through the .csv data file
for i in data['Track.Name']:
    i = str(i)
    separate = i.split()
    for j in range(len(separate)):
        separate[j] = separate[j].lower()

    comment_words += " ".join(separate) + " "

# Create the Word Cloud
final_wordcloud = WordCloud(width = 600, height = 600,
                background_color ='black',
                stopwords = stop_words,
                min_font_size = 10).generate(comment_words)

# Plotting the WordCloud
plt.figure(figsize=(10, 10), facecolor=None)
plt.imshow(final_wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
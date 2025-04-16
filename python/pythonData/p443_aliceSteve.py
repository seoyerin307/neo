import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from wordcloud import ImageColorGenerator

image_file = 'alice.png'

img_file = Image.open(image_file)
print(type(img_file))
print('-' * 50)

alice_mask = np.array(img_file)
print(type(alice_mask))
print('-' * 50)

filename = 'steve.txt'
myfile = open(filename, mode='r', encoding='utf-8')

plt.figure(figsize=(8, 8))
plt.imshow(alice_mask, interpolation='bilinear')
plt.axis('off')

filename = 'p434_alice_grape01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')

mystopwords = set(STOPWORDS)
mystopwords.add('said')
mystopwords.add(['hohoho', 'hahaha'])

print(len(mystopwords))
print(mystopwords)

WC = WordCloud(background_color='white', mask=alice_mask, stopwords=mystopwords, max_words=2000)

stevefile = 'steve.txt'



plt.show()
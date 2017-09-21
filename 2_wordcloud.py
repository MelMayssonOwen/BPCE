#!/usr/bin/env python
"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from wordcloud import WordCloud, STOPWORDS

matplotlib.use('Agg')

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'outputs/final_output.csv')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open(path.join(d, "42.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="black", max_words=2000, mask=alice_mask,
               stopwords=stopwords, width=1600, height=800)
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "cloudy.png"))

# show
plt.figure(figsize=(20,10))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()

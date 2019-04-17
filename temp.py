# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

print("hello mac")

file_content=open ("jobreq.txt").read()
#print(file_content)


wordcloud = WordCloud().generate(file_content)

# Display the generated image:
plt.figure(figsize =(12,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

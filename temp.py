# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#from wordcloud import WordCloud, STOPWORDS

print("hello mac")

import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()

print("that's my graph")
"""
file_content=open ("jobreq.txt").read()
#print(file_content)


wordcloud = WordCloud().generate(file_content)

# Display the generated image:
plt.figure(figsize =(12,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
"""
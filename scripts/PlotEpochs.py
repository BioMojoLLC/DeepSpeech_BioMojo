# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

ls = {  0:0.1541,
        1:0.1568,
        3:0.1610,
        6:0.1640,
        8:0.1663,
        10:0.1655,
        15:0.1680,
        18:0.1680}

custom = {0:0.3640,
          1:0.2494,
          3:0.2220,
          6:0.2017,
          8:0.2005,
          10:0.1957,
          12:0.1933,
          15:0.1802,
          18:0.1766}

plt.title("Conservative Model")
plt.xlabel("Epochs")
plt.ylabel("WER")


plt.yticks(np.arange(0,1,.025)) # Ticks
plt.xticks(np.arange(0,19,3))
plt.axis([0,18,.1,.4]) # Ranges


plt.plot(custom.keys(), custom.values(), label="Custom Test")
plt.plot(ls.keys(), ls.values(), label='Librispeech Test')


# Annotations
x1 = 6
x2 = 15
linecolor = '#3f679a'


a = .2
b = .364
plt.plot([x1,x1],[a,b],dashes=(6,8),color=linecolor,lw=1)
plt.plot([x1-.4,x1+.4],[b,b],color=linecolor,linewidth=1)
plt.plot([x1-.4,x1+.4],[a,a],color=linecolor,lw=1)
plt.annotate("Learning Vocab\n      -16.23%", xy = (6.5,.28), )

c = .18
d = .201
plt.plot([x2,x2],[c,d],dashes=(3,3),color=linecolor,lw=1)
plt.plot([x2-.3,x2+.3],[c,c],color=linecolor,linewidth=1)
plt.plot([x2-.3,x2+.3],[d,d],color=linecolor,lw=1)
plt.annotate("Other\n-2.15%", xy = (14.25,.21), )

e = .168
f =.152
plt.plot([x2,x2],[e,f],dashes=(3,3),color=linecolor,lw=1)
plt.plot([x2-.3,x2+.3],[e,e],color=linecolor,linewidth=1)
plt.plot([x2-.3,x2+.3],[f,f],color=linecolor,lw=1)
plt.annotate("General Loss\n     +2.15%", xy = (12,.12), )


plt.legend()
plt.show()


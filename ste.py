# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:04:34 2017

@author: aaron purinton
"""

import numpy as np

def normalize(mat):
    for x in range(3):
        total=0
        for y in range(3):
            total += mat[x][y]
        for y in range(3):
            mat[x][y]=mat[x][y]/total

aug = [0,1,0]
normal = [[.5,.2,.3],
          [.1,.8,.1],
          [.4,.4,.2]]

ext = [[.8,.1,.1],
       [.1,.9,0],
       [.1,.8,.1]]

exHm = [[.1,.5,.4],
        [0,.7,.3],
        [.1,.1,.8]]



vidja=[.8,.4,.4]
pal=[.1,.3,.6]
whin=[.3,.1,.2]

nvidja=[.2,.6,.6]
npal=[.9,.7,.4]
nwhin=[.7,.9,.2]
end=[]
current= np.dot(aug,normal)#into september
current = np.dot(current,vidja)#saw videogames
current = np.dot(current,npal)#didnotsee pal
current= np.dot(current,nwhin)#didnot see whin

normalize(current)
#now into octopber
current = np.dot(current,normal)
current = np.dot(current,nvidja)#saw videogames
current = np.dot(current,npal)#didnotsee pal
current= np.dot(current,whin)#did see whin
#into November

normalize(current)

current = np.dot(current,normal)
current = np.dot(current,vidja)#saw videogames
current = np.dot(current,pal)#didnotsee pal
current= np.dot(current,nwhin)#didnot see whin

normalize(current)

print(np.dot(current,normal))
print()
print(np.dot(current,ext))
print()
print(np.dot(current,exHm))
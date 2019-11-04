import numpy as np 
import random
import matplotlib.pyplot as plt
import math as m

#Function returns payoff
def getPayoff(t):
    return (payoff[t][0]*impD)+(payoff[t][1]*rebelD)

#Variables setting
g=1
c=5
#Payoff matrix
#Imperials are 0 and rebels are 1
#so for payoff[0][0] we would have two imperials meeting while for payoff[0][1] we would have an imperial meeting a rebel
#the same goes the other way round
#payoff = [ [(g-c)/2, g-0.25*c] , [-0.25*c, g/2 ] ]
payoff = [ [g/2, g-0.25*c] , [-0.25*c, g/2 ] ]
#Lists used for plots
im = []
r = []
rd = []
imd = []
#Counter
i=0
while i < 1:
    #Trying out different combination of imperials and rebels density by 10% increments/decrements
    rebelD = i 
    impD = 1-rebelD
    #Plots related functions
    r.append(getPayoff(1))
    rd.append(rebelD)
    im.append(getPayoff(0))
    imd.append(impD)
    i+=0.1


plt.xlabel("Rebels and Imperials density")
plt.ylabel("Payoffs")
plt.plot(imd, im, color='r')
plt.plot(rd, r, color='b')
plt.show()
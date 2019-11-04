import numpy as np 
import random
import matplotlib.pyplot as plt
import math as m

#Function to get the right payoff from the matrix
def getPayoff(t):
    return (payoff[t][0]*impD)+(payoff[t][1]*rebelD)

#Function to calculate the new density of a population. The function accepts as parameters the old density and the payoff
def getGrowth(dens: float, pf: float):
    global r
    alpha=1.4
    nd = ((1.0-dens/K)*r*dens) + pf/alpha
    return nd

#Setting base variable as Gain, Cost, payoff matrix, carrying capacty and value of r
g=1
c=2
payoff = [ [(g-c)/2, g-0.25*c] , [-0.25*c, g/2 ] ]
K=0.75
r=2.5
#lists used for storing information and displaying of plots
time = []
rd = []
imd = []
ip = []
rp = []
#Counter
i=0
#Initial density of imperials
impD = 0.5
while i < 30:
    #update the rebels density by difference with imperials
    rebelD = 1-impD 
    #append elements in lists
    rd.append(rebelD)
    imd.append(impD)
    rp.append(getPayoff(1))
    ip.append(getPayoff(0))
    time.append(i)
    i+=1
    #calculate the new imperial density with old density and payoff
    impD += getGrowth(impD, getPayoff(0))

#Plots related functions
plt.xlabel("Time")
plt.ylabel("Rebels and Imperials density")
plt.plot(time, imd, color='r')
plt.plot(time, rd, color='b')
plt.show()
plt.clf()
plt.xlabel("Time")
plt.ylabel("Rebel and Imperials Payoffs")
plt.plot(time, ip, color='r')
plt.plot(time, rp, color='b')
plt.show()
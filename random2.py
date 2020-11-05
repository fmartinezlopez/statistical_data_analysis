# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 10:28:14 2020

@author: Paco
"""

# simpleMC.py -- simple Monte Carlo program to make histogram of uniformly
# distributed random values and plot
# G. Cowan, RHUL Physics, October 2019

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# generate data and store in numpy array, put into histogram

numVal = 10000
nBins = 100
rMin = 0.
rMax = 1.

xMax = 1.

rData = np.random.uniform(rMin, rMax, numVal)


xData = np.sqrt(rData) * xMax

xHist, bin_edges = np.histogram(xData, bins=nBins, range=(0, xMax))

# make plot and save in file

binLo, binHi = bin_edges[:-1], bin_edges[1:]
bin_size = binHi[1] - binLo[1]

xPlot = np.array([binLo, binHi]).T.flatten()
yPlot = np.array([xHist, xHist]).T.flatten()
fig, ax = plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
ax.set_xlim((0, xMax))
ax.set_ylim((0., 2.2))
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot, yPlot/(len(xData) * bin_size))
plt.savefig('xHist.png', format='png')
plt.show()


# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:07:05 2020

@author: Francisco
"""

# based on simpleMC.py by G. Cowan, RHUL Physics, October 2019

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# generate data and store in numpy array, put into histogram

numVal = 10000
nBins = 100
rMin = 0.
rMax = 1.

rData = []

for i in range(12):

    rData.append(np.random.uniform(rMin, rMax, numVal))


xData1 = rData[1] + rData[2] - 1
xData2 = rData[1] + rData[2] + rData[3] + rData[4] - 2
xData3 = sum(rData) - 6



xHist1, bin_edges1 = np.histogram(xData1, bins=nBins, range=(-1, 2*rMax - 1))
xHist2, bin_edges2 = np.histogram(xData2, bins=nBins, range=(-2, 4*rMax - 2))
xHist3, bin_edges3 = np.histogram(xData3, bins=nBins, range=(-6, 12*rMax - 6))

# make plot and save in file

# Exercise i

mids1 = 0.5 * (bin_edges1[1:] + bin_edges1[:-1])
mean1 = np.average(mids1, weights=xHist1)
var1 = np.average((mids1 - mean1)**2, weights=xHist1)
std1 = np.sqrt(var1)

textstr1 = '\n'.join((
    r'$\mu=%.2f$' % (mean1, ),
    r'$\sigma=%.2f$' % (std1, )))

binLo1, binHi1 = bin_edges1[:-1], bin_edges1[1:]
bin_size1 = binHi1[1] - binLo1[1]

xPlot1 = np.array([binLo1, binHi1]).T.flatten()
yPlot1 = np.array([xHist1, xHist1]).T.flatten()
fig, ax = plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
ax.set_xlim((-1, 2*rMax - 1))
ax.set_ylim((0., 1.1))
ax.text(0.05, 0.95, textstr1, transform=ax.transAxes, fontsize=14,
        verticalalignment='top')
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot1, yPlot1/(len(xData1) * bin_size1))
plt.savefig('x1Hist.png', format='png')
plt.show()

#Exercise ii

mids2 = 0.5 * (bin_edges2[1:] + bin_edges2[:-1])
mean2 = np.average(mids2, weights=xHist2)
var2 = np.average((mids2 - mean2)**2, weights=xHist2)
std2 = np.sqrt(var2)

textstr2 = '\n'.join((
    r'$\mu=%.2f$' % (mean2, ),
    r'$\sigma=%.2f$' % (std2, )))

binLo2, binHi2 = bin_edges2[:-1], bin_edges2[1:]
bin_size2 = binHi2[1] - binLo2[1]

xPlot2 = np.array([binLo2, binHi2]).T.flatten()
yPlot2 = np.array([xHist2, xHist2]).T.flatten()
fig, ax = plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
ax.set_xlim((-2, 4*rMax - 2))
ax.set_ylim((0., 0.8))
ax.text(0.05, 0.95, textstr2, transform=ax.transAxes, fontsize=14,
        verticalalignment='top')
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot2, yPlot2/(len(xData2) * bin_size2))
plt.savefig('x2Hist.png', format='png')
plt.show()

#Exercise iii

mids3 = 0.5 * (bin_edges3[1:] + bin_edges3[:-1])
mean3 = np.average(mids3, weights=xHist3)
var3 = np.average((mids3 - mean3)**2, weights=xHist3)
std3 = np.sqrt(var3)

textstr3 = '\n'.join((
    r'$\mu=%.2f$' % (-mean3, ),
    r'$\sigma=%.2f$' % (std3, )))

binLo3, binHi3 = bin_edges3[:-1], bin_edges3[1:]
bin_size3 = binHi3[1] - binLo3[1]

xPlot3 = np.array([binLo3, binHi3]).T.flatten()
yPlot3 = np.array([xHist3, xHist3]).T.flatten()
fig, ax = plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
ax.set_xlim((-6, 12*rMax - 6))
ax.set_ylim((0., 0.5))
ax.text(0.05, 0.95, textstr3, transform=ax.transAxes, fontsize=14,
        verticalalignment='top')
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot3, yPlot3/(len(xData3) * bin_size3))
plt.savefig('x3Hist.png', format='png')
plt.show()



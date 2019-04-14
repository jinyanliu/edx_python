"""
Created at 2019-04-14 17:00

@author: jinyanliu
"""

import numpy as np
import pylab

y1 = [1, 2, 3]
y2 = [2, 4, 6]

pylab.rcParams['legend.numpoints'] = 3
pylab.plot(y1)
pylab.plot(y2)
pylab.plot(y1, 'ko', label='sine')
pylab.plot(y2, 'bo', label='cosine')
pylab.legend(loc='upper left')
pylab.show()

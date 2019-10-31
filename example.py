import numpy as np
from homology import *

# Your data should be in the form of a 2D numpy array with integer values.
# Perseus needs positive integer values. Rescale data i required.

data = np.random.randint(low=0, high=10, size=(10,10))

# The epsilons array decides your intervals for tracking the "live" holes.
epsilons = np.linspace(0,10,10)

# First create the intervals object which keeps track of the lifetime for 
# each feature. Then pass it to the PD() for creating a persistence diagram.
# The second argument of the PD is the Betti-number of interest.
# As of now, we only work on 2D images, so the working values are 0 and 1.

b0_pd = PD(Intervals(data, '0', epsilons))
b1_pd = PD(Intervals(data, '1', epsilons))

# Plot the PD
b0_pd.plot_pd('b0_pd.png')
b1_pd.plot_pd('b1_pd.png')




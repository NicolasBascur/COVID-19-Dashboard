import numpy as np
import matplotlib.pyplot as plt
from cpyment import CModel

# First, define the model
model = CModel('SIR')

beta = 3
gamma = 1

# Now add the couplings
model.set_coupling_rate('S*I:S=>I', beta, name='beta')  # Infection rate
model.set_coupling_rate('I:I=>R', gamma, name='gamma')  # Recovery rate

# Let's see the dynamics from a starting state
I0 = 0.02               # Initial fraction of infected
y0 = [1-I0, I0, 0]

t = np.linspace(0, 10, 1000)  # Time axis

trajectory = model.integrate(t, y0)['y']



fig, ax = plt.subplots()

ax.set_xlabel('Tiempo')
ax.set_ylabel('Poblacion (%)')
ax.set_ylim(0, 100)
for i, l in enumerate('SIR'):
    ax.plot(t, trajectory[:,i]*100, label=l)
ax.legend()
# plt.show() 
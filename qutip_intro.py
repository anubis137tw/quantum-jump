# import essential packages from qutip environment under conda
from qutip import *
import numpy as np
import matplotlib.pyplot as plt

print(Qobj())

print(Qobj([[1],[2],[3],[4],[5]])) # ket state

x = np.array([[1, 2, 3, 4, 5]]) # bre state
print(Qobj(x))

r = np.random.rand(4, 4) # quantum operator
print(Qobj(r))

q = destroy(4)

x = sigmax()

print(q + 5)
print(x * x)
print(q * q * q)
print(q ** 3)
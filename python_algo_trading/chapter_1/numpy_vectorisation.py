import random
from math import exp, sqrt
import time
import numpy as np

start_time = time.time()
S0 = 100
r = 0.05
T = 1.0
sigma = 0.2
values = []

for _ in range(1000000):
    ST = S0 * exp((r -0.5 * sigma ** 2) * T + sigma * random.gauss(0, 1) * sqrt(T))
    values.append(ST)
end_time = time.time()
print(f"Elapsed time for vanilla python: {end_time - start_time} seconds")


start_time = time.time()
S0 = 100
r = 0.05
T = 1.0
sigma = 0.2
values = []

ST = S0 * np.exp((r -0.5 * sigma ** 2) * T + sigma * np.random.standard_normal(1000000) * np.sqrt(T))
end_time = time.time()
print(f"Elapsed time for numpy python: {end_time - start_time} seconds")

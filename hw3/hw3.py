import numpy as np
import math
import matplotlib.pyplot as plt

def moment(list, k):
	res = 0.0
	for el in list:
		res += pow(el, k)
	return res / len(list)

distribution = int(input("Type 1 for uniform distribution or 2 for exponential distribution: "))

theta = float(input("Type theta: "))

graphicPoints = []

for k in range(1, 50):
	deltas = []
	for i in range(0, 50):
		theta_1 = None
		if (distribution == 1):
			sample = np.random.uniform(0, theta, 50)
			m_k = moment(sample, k)
			theta_1 = pow(m_k * (k + 1), 1 / k)
		elif (distribution == 2):
			sample = np.random.exponential(theta, 50)
			m_k = moment(sample, k)
			theta_1 = pow(m_k / math.factorial(k), 1 / k)
		deltas.append(pow(theta - theta_1, 2))
	graphicPoints.append(np.mean(deltas))
plt.plot([i for i in range(1, 50)], graphicPoints)
plt.show()
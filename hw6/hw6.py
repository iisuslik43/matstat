import numpy as np
import math
from scipy.stats import chi2
from scipy.stats import norm
import matplotlib.pyplot as plt


def moment(list, k):
	res = 0.0
	for el in list:
		res += pow(el, k)
	return res

graphicPoints1 = []

gamma = 0.9
sigma = 1
maxN = 200

for n in range(20, maxN):
	deltas = []
	for i in range(0, 50):
		sample = np.random.normal(0, sigma, n)
		moment2 = moment(sample, 2)
		kv1 = chi2.ppf((1 + gamma) / 2, n)
		kv2 = chi2.ppf((1 - gamma) / 2, n)
		deltas.append(abs(moment2 / kv1 - moment2 / kv2))
	graphicPoints1.append(np.mean(deltas))

graphicPoints2 = []

for n in range(20, maxN):
	deltas = []
	for i in range(0, 100):
		sample = np.random.normal(0, sigma, n)
		moment1 = moment(sample, 1)
		kv1 = norm.ppf((3 + gamma) / 4)
		kv2 = norm.ppf((3 - gamma) / 4)
		deltas.append(abs(moment1 * moment1 / (kv1 * kv1 * n) - moment1 * moment1 / (kv2 * kv2 * n)))
	graphicPoints2.append(np.mean(deltas))
plt.subplot(2, 1, 1)
plt.plot([i for i in range(20, maxN)], graphicPoints1)
plt.title('Сумма квадратов делить на n')
plt.subplot(2, 1, 2)
plt.plot([i for i in range(20, maxN)], graphicPoints2)
plt.title('Сумма делить на n в квадрате')
plt.show()
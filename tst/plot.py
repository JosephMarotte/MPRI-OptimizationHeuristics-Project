import matplotlib.pyplot as plt
import math

maxn = 41
k = 3
probas = [0.5, 1, 2]
f = open("results/mu_plus_lambda_evolution_strategy", "r")
avg = [[0] * k for i in range(maxn)]
s = [[0] * k for i in range(maxn)]

for l in f:
    n, _, _, _, rate, calls = l.split()
    n = int(n)
    rate = float(rate)
    calls = int(calls)
    rate *= n
    best = 0 
    for i in range(k):
        if math.fabs(rate - probas[i]) < math.fabs(rate - probas[best]):
            best = i
    avg[n][best] += calls
    s[n][best] += 1

for i in range(k):
    X = []
    Y = []
    for j in range(maxn):
        if s[j][i] > 0:
            X.append(j)
            Y.append(avg[j][i] / s[j][i])
    plt.plot(X, Y, label="{}".format(probas[i]))
f = open("results/mu_plus_lambda_evolution_strategy_autoadjust_2_0.5", "r")
avg = [0] * maxn
s = [0] * maxn

for l in f:
    n, _, _, _, rate, calls = l.split()
    n = int(n)
    rate = float(rate)
    calls = int(calls)
    avg[n] += calls
    s[n] += 1

X = []
Y = []
for j in range(maxn):
    if s[j] > 0:
        X.append(j)
        Y.append(avg[j] / s[j])
plt.plot(X, Y, label="autoadjust(2, 0.5)")
f = open("results/mu_plus_lambda_evolution_strategy_autoadjust_1.5_0.9", "r")
avg = [0] * maxn
s = [0] * maxn

for l in f:
    n, _, _, _, rate, calls = l.split()
    n = int(n)
    rate = float(rate)
    calls = int(calls)
    avg[n] += calls
    s[n] += 1

X = []
Y = []
for j in range(maxn):
    if s[j] > 0:
        X.append(j)
        Y.append(avg[j] / s[j])
plt.plot(X, Y, label="autoadjust(1.5, 0.9)")

plt.xlabel("Mastermind instance size")
plt.ylabel("Number of calls to the blackbox")
plt.legend(loc='upper_left')
plt.show()



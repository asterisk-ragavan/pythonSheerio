import math

x = []
for i in range(int(input('enter the numbers required\n'))):
    x.append(i)
N = len(x)
out = {}
for k in range(N):
    sumReal = 0
    sumImage = 0
    for n in range(N):
        sinValue = math.sin((2 * math.pi * k * n) / N)
        cosValue = math.cos((2 * math.pi * k * n) / N)
        sumReal = sumReal + (cosValue * x[n])
        sumImage = sumImage - (sinValue * x[n])
    out[k] = complex(sumReal, sumImage)
for k in range(N):
    print("[", k, "]", " = ", out[k], "\n")

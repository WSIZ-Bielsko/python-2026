w = dict()
try:
    w[2] += 1
except KeyError:
    w[2] = 1
print(w)

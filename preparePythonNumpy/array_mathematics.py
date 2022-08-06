import numpy

n, m = [int(x) for x in input().split(' ')]

lines = []

for line in range(n * 2):
    lines.append([int(x) for x in input().split(' ')])

nadd = []
nsub = []
nmul = []
ndiv = []
nmod = []
npow = []

for i in range(int(n)):
    nadd.append(numpy.array(numpy.add(lines[i], lines[i + n])))
    nsub.append(numpy.array(numpy.subtract(lines[i], lines[i + n])))
    nmul.append(numpy.array(numpy.multiply(lines[i], lines[i + n])))
    ndiv.append(numpy.array(numpy.floor_divide(lines[i], lines[i + n])))
    nmod.append(numpy.array(numpy.mod(lines[i], lines[i + n])))
    npow.append(numpy.array(numpy.power(lines[i], lines[i + n])))

print(numpy.array(nadd))
print(numpy.array(nsub))
print(numpy.array(nmul))
print(numpy.array(ndiv))
print(numpy.array(nmod))
print(numpy.array(npow))

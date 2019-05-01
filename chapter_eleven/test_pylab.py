import pylab

pylab.figure(1)
pylab.plot([1,2,3,4], [1,7,3,5])
pylab.show()

principal = 10000
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interestRate
pylab.plot(values)
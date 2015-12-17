#coding=utf8
__author__ = 'Frank'
'''class TaxCalc:
    def taxdue(self):return (self.income-self.deduct)*self.rate
a = TaxCalc()
a.income = 50000
a.rate = 0.30
a.deduct = 10000
print a.taxdue()
a.income = 500000
print a.taxdue()
class TaxCalc:
    def taxdue(self):return (self.income-self.deduct)*self.rate
    def setIncome(self,income):
        self.income=income
        return self
    def setDeduct(self,deduct):
        self.deduct = deduct
        return self
    def setRate(self,rate):
        self.rate = rate
        return self
print"Smalltalk-style taxes due =", \
      TaxCalc().setIncome(50000).setRate(0.30).setDeduct(10000).taxdue()'''
from functional import *

taxdue        = lambda: (income-deduct)*rate
incomeClosure = lambda income,taxdue: closure(taxdue)
deductClosure = lambda deduct,taxdue: closure(taxdue)
rateClosure   = lambda rate,taxdue: closure(taxdue)

taxFP = taxdue
taxFP = incomeClosure(50000,taxFP)
taxFP = rateClosure(0.30,taxFP)
taxFP = deductClosure(10000,taxFP)
print"Functional taxes due =",taxFP()

print"Lisp-style taxes due =", \
      incomeClosure(50000,
          rateClosure(0.30,
              deductClosure(10000, taxdue)))()
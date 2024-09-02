import math

def giveGeomSeqElement(a1=2,factor=2,index=2):
    return a1*factor**(index-1) if index > 0 else 'error'


def giveFactorForGeomSeq(term,nextTerm):
    return nextTerm/term if term!=0 else 0

def giveSumOfNelementsGeomSeq(a1=2,factor=2,n=2):
    return a1*(1-factor**n)/(1-factor)

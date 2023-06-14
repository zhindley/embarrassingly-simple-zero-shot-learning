import numpy as np
import os
import scipy.io
from sklearn.metrics import classification_report,confusion_matrix
import argparse
import torch
import torch.nn as nn
from sklearn.preprocessing import normalize
import random




def getSamples(vPlus,S,d,a):
    
    samples = np.empty((d,))
    
    for sig in S.T:
               
        temp = np.empty((d,))
        for i in range(20):
            noise = np.random.normal(0,0.1,(a,))     
            noisySig = np.add(sig,noise)
            temp = np.vstack((temp,np.matmul(noisySig,vPlus)))
            
        temp = np.delete(temp,0,0)   
        samples = np.vstack((samples,temp))
    samples = np.delete(samples,0,0)
    return samples.T

if __name__ == "__main__":

    #dimensions:
    #X dxm, d-num of features m-num of samples
    #S axz, a-num attributes z-num of classes
    #Y mxz
    #V axd
    a = 10
    z = 20
    d = 10
    #number of test classes
    zPrime = 5
    #Generate synthetic Trainine data
    vPlus = np.random.normal(0,1,(a,d)) #Maps the attribute to 
    #generate two sets of signatures train 
    S = np.random.binomial(size=(a,z),n=1,p=0.5)
    #generate zPrime test signatures
    sPrime = np.random.binomial(size=(a,zPrime),n=1,p=0.5)
    Y = np.zeros((20*z,z))
    index = 0
    count = 0
    for row in Y:
        row[index] = 1

        count = count + 1
        if count == 20:
            count = 0
            index = index + 1

    
    X = getSamples(vPlus,S,d,a)
    
    test = getSamples(vPlus,sPrime,d,a)

    
    #Create the
    

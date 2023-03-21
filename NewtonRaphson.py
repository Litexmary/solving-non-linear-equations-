# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:41:14 2023

@author: pc
"""
import time

def f(x):
    return x**5 + x**3 - 2*x - 5

def df(x):
    return 5*x**4 + 3*x**2 - 2

def newton_raphson(x0, tol=1e-6, max_iterations=100):
   
    x = x0
    for i in range(max_iterations):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x
        x = x - fx / dfx
    return None

x0 = 2.0
start_time = time.time()
root = newton_raphson(x0)
elapsed_time = time.time() - start_time
if root is not None:
    print("The root is:", root)
    print("Time taken:", elapsed_time, "seconds")
else:
    print("Failed to converge.")

     
   
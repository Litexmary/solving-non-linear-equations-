# solving-non-linear-equations-
SOLVING NON LINEAR EQUATIONS USING BISECTION METHOD AND NEWTON RAPHSON METHOD


Bisection Method:

The bisection method is an iterative algorithm that can be used to solve non-linear equations. The basic idea of this method is to divide the interval containing the root in half repeatedly until the solution is found.
The algorithm for the bisection method is as follows:

Choose a function f(x) and an interval [a, b] such that f(a) and f(b) have opposite signs, which means that there is a root between a and b.
Calculate the midpoint c = (a+b)/2.
If f(c) is zero or within a specified tolerance, then stop and output c as the solution.
If f(c) and f(a) have opposite signs, then the root must be in the interval [a, c]. Set b = c and go back to step 2.
If f(c) and f(b) have opposite signs, then the root must be in the interval [c, b]. Set a = c and go back to step 2.
The bisection method will converge to a solution as long as f(x) is continuous and has a root in the interval [a, b]. However, this method can be slow, especially for functions with slow convergence or multiple roots.

Newton-Raphson Method:

The Newton-Raphson method is another iterative algorithm used to find roots of non-linear equations. This method uses an initial guess and iteratively improves the guess until a solution is found.
The algorithm for the Newton-Raphson method is as follows:

Choose a function f(x) and an initial guess x0.
Calculate the slope of the function at x0, which is given by f'(x0).
Calculate the new guess x1 using the formula x1 = x0 - f(x0)/f'(x0).
If f(x1) is zero or within a specified tolerance, then stop and output x1 as the solution.
If f(x1) is not zero, then set x0 = x1 and go back to step 2.
The Newton-Raphson method can converge quickly to a solution if the initial guess is close to the root and the function has a single root. However, if the initial guess is far from the root or the function has multiple roots, the method may fail to converge or converge to a different root.

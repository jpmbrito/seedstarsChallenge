#!/usr/bin/python

def mul(A, B):
    a, b, c = A
    d, e, f = B
    return a*d + b*e, a*e + b*f, b*e + c*f

def pow(A, n):
    if n == 1:     return A
    if n & 1 == 0: return pow(mul(A, A), n//2)
    else:          return mul(A, pow(mul(A, A), (n-1)//2))

def fib(n):
    if n < 2: return n
    return pow((1,1,0), n-1)[0]

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Fibonacci-Script")
    parser.add_argument("-n", metavar='N', type=int,
            help="print the N-th fibonacci number", default=2)
    args = parser.parse_args()
    print fib(args.n)

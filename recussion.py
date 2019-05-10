def maximum(array, maxi, position, length):
    
    if array[position]>maxi:
        maxi=array[position]
    if position==length-1:
        return maxi
    
    
    return maximum(array, maxi, position+1, length)
    
def power(n,p):
    
    if p ==0:
        return 1
    
    return n*power(n,p-1)

def reverse(arr, start,stop):
    
    if start==stop:
        return arr
    arr[start], arr[stop] = arr[stop], arr[start]
    return reverse(arr, start+1, stop-1)
    
def Harmonic(n):
    if n==0:
        return 1
    return 1/n + Harmonic(n-1)

def convertComma(string,pos=-1,stringR=''):
    stringR = string[pos]+stringR
    
    if len(string)<=abs(pos):
        return stringR
    
    
    if pos%3==0:
        stringR =','+stringR
        
    return convertComma(string, pos-1,stringR)

def minMax(n,current=[0,0],pos=1):
    if pos==1:
        current = [n[0], n[0]]
    if pos == len(n):
        return current
    if n[pos]>current[1]:
        current[1] = n[pos]
    
    if n[pos]<current[0]:
        current[0] = n[pos]
    
    return minMax(n,current, pos+1)
    
def log2n(n):
    if n==1:
        return 0
    return 1+log2n(n//2)

def eleUnique(n ,pos=1, state=list()):
    if pos==1:
        state.append(n[0]) 
    if pos == len(n):
        return True
    if n[pos] in state:
        return False
    state.append(n[pos])
    return eleUnique(n,pos+1,state)

def product(m,n):
    if m==0 or n==0:
        return 0
    if n==1:
        return m
    return m+product(m,n-1)

from math import factorial 
def combination(n,r):
    f = factorial
    return f(n) // f(r) // f(n-r)
    
def Pascal(n,c=0, a=[]):
    if n==1:
        return [1]
    if c==n:
        a.append(1)
        
        return a
      
    a.append(combination(n,c))
    return Pascal(n,c+1,a)


def Pascal_triangle(n,c=1):
    if c==n:
        return Pascal(n)
    print(Pascal(c, a=[]))
    return Pascal_triangle(n,c+1)
if __name__ == "__main__":
    
    print(Pascal_triangle(10))
#    print(product(100,1))
#    print(eleUnique([3,5,2,2,4,7]))
#    print(log2n(224))
#    print(minMax([3,2,5,7,8,4345,3,522,8,45,21,56]))
#    print(convertComma('1354535531'))
#    print(Harmonic(100))
#    print(reverse([4, 3, 6, 2, 6], 0, 4))
#    print(power(2,1000))
#    print(maximum(range(1000), 0,0,1000))

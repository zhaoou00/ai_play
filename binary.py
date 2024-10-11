import pandas as pd, numpy as np, scipy as sp


# Step 1: Create the binary matrix (0's and 1's)
rows, cols, cols_res = 10000, 5,4  # Define the dimensions of the matrix

inpt = np.random.randint(2, size=(rows, cols))

# Step 2: Count the number of 1's in each row
row_sums = np.sum(inpt, axis=1)

# Step 3: Convert the count of 1's into binary representation
# Convert each count to binary and store in a new matrix
res = np.array([list(np.binary_repr(x).zfill(cols_res)) for x in row_sums]).astype(int)

def dotxor(a,b):
    expanded_matrix = a[:, :, np.newaxis] ^ b[:, np.newaxis, :]
    return np.sum(expanded_matrix, axis=0)

def dot(a,b,op):
    if op == '^':
        expanded_matrix = a[:, :, np.newaxis] ^ b[:, np.newaxis, :]
    elif op == '&':
        expanded_matrix = a[:, :, np.newaxis] & b[:, np.newaxis, :]
    elif op == '|':
        expanded_matrix = a[:, :, np.newaxis] | b[:, np.newaxis, :]
    elif op == '~1':
        expanded_matrix = ~a[:, :, np.newaxis]
    elif op == '~2':
        expanded_matrix = ~b[:, np.newaxis, :]
    return np.sum(expanded_matrix, axis=0)

ops = np.array([list(np.binary_repr(x).zfill(cols_res)) for x in range(16)]).astype(int)
def dt(a,b,opi):
    if opi==0:
        return a^a
    elif opi==1:
        return a&b
    elif opi==2:
        return a&(1-b)
    elif opi==3:
        return a
    elif opi==4:
        return (1-a)&b
    elif opi == 5:
        return b
    elif opi == 6:
        return a^b
    elif opi == 7:
        return a|b
    elif opi == 8:
        return 1-(a|b)
    elif opi == 9:
        return 1-(a^b)
    elif opi == 10:
        return 1-b
    elif opi == 11:
        return a|(1-b)
    elif opi == 12:
        return 1-a
    elif opi == 13:
        return (1-a)|b
    elif opi == 14:
        return 1-(a&b)
    elif opi == 15:
        return 1-(a^a)

##test = [np.dot(np.array([dt(a,b,opi) for a in range(2) for b in range(2)]),[8,4,2,1]).sum() for opi in range(16)]
##print (test)    

##r1 = np.array([dt(inpt[:,0], inpt[:,1],x) for x in [1,2,4,8]])
##r2 = np.dot(r1,res)
r1 = np.array([ dt(v1, v2, opi) for v1 in inpt.T for v2 in inpt.T for opi in range(16)])

##aa=np.dot(r1,res)

r2 = np.array([ np.sum(dt(v1, v2, opi)^ resi) for v1 in inpt.T for v2 in inpt.T for opi in range(16) for resi in res.T])

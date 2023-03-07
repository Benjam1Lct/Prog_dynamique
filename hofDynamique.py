def hofVersionRecursive(rang):
    if rang == 0:
        return 1
    else:
        return hofVersionRecursive(rang - hofVersionRecursive(rang-1)) + hofVersionRecursive(rang - hofVersionRecursive(rang-2))

def hofMemo(rang, memoir = {0 : 1, 1 : 1}):
    if rang is memoir.keys():
        return memoir[rang]
    else:
        memoir[rang] = hofMemo(rang - hofMemo(rang-1)) + hofMemo(rang - hofMemo(rang-2))
        return memoir[rang]

def hofDynamique(rang, memoir = {0:1,1:1}):
    if rang > 1:
        for i in range(2, rang+1):
            memoir[i] = memoir[i - memoir[i-1]] + memoir[i - memoir[i-2]]
        return memoir

print(hofDynamique(10))
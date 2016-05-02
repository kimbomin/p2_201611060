myE={'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'}
friendsE={'coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'}

def intersection():    
    print set(myE).intersection(set(friendsE))

def union():
    print set(myE).union(set(friendsE))

def onlyMyE():
    print set(myE).difference(set(friendsE))

def count():
    d=dict()

    for c in myE:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    for c in friendsE:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1

    print d

def lab9():
    onlyMyE()
    union()
    intersection()
    count()

def main():
    lab9()


if __name__=="__main__":
    main()
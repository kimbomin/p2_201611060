def allchars():
    sentence='sangmyung university'
    d=dict()
    for c in sentence:
        if c not in d:
             d[c]=1
        else:
            d[c]=d[c]+1
        
    def charCount():
        sentence='sangmyung university'
        d=dict()
        for c in sentence:
            if c not in d:
                 d[c]=1
            else:
                 d[c]=d[c]+1
        print d
    
    charCount()

    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)),list(d.keys()))
    plt.show()

def lab9():
    allchars()

def main():
    lab9()

if  __name__=="__main__":
    main()
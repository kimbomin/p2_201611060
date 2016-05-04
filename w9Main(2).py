def countDigitsLetters():
    word='7 hongjimun'
    allchars=list(word)         
    d=dict()
    d['number']=0
    d['word']=0
    for c in allchars:
        if c.isdigit():
            d['number']=d['number']+1
        else:
            d['word']=d['word']+1
    import matplotlib
    import matplotlib.pyplot as plt
    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), d.keys())
    plt.show()

def lab9():
    countDigitsLetters()

def main():
    lab9()

if __name__=="__main__":
    main()
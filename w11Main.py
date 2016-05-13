def question(): 
    dataA=[[13.1, 37.1], 
          [10.6, 34.6], 
          [27.1, 40.0], 
          [16.2, 37.8], 
          [11.4, 29.8], 
          [12.2, 26.5], 
          [13.5, 29.7], 
          [13.7, 37.6]] 
    dataB=[[8.7, 1.5], 
          [13.4, 1.9], 
          [2.9, 1.5], 
          [6.8, 0.8], 
          [14.8, 4.9], 
          [14.9, 4.4], 
          [11.1, 2.4], 
          [4.1, 1.2]]
 
    sumA=0 
    sumB=0 


    for i in dataA: 
        sumA=i[0]+i[1] 
 
 
    for i in dataB: 
        sumB=i[0]+i[1] 
 
    print sumA
    print sumB
    print float(sumA/len(dataA))
    print float(sumB/len(dataB))

def speech():
    Obama=["My fellow citizens.",
    "I stand here today humbled by the task before us, grateful for the trust you have bestowed,",
    "mindful of the sacrifices borne by our ancestors. I thank President Bush for his service to our nation,",
    "as well as the generosity and cooperation he has shown throughout this transition.",
    "Forty-four Americans have now taken the presidential oath.",
    "The words have been spoken during rising tides of prosperity and the still waters of peace.",
    "Yet, every so often the oath is taken amidst gathering clouds and raging storms.",
    "At these moments, America has carried on not simply because of the skill or vision of those in high office,",
    "but because We the People have remained faithful to the ideals of our forbearers,",
    "and true to our founding documents."]

    def count():
        d = {}
        for i in Obama:
            words=i.split()
            for word in words:
                if word in d:
                    d[word]+=1
                else:
                    d[word]=1
        return d

    def frequent(a,b):
        wordss=list()
        for i in b:
            if b[i]>a:
                wordss.append(i)
        return wordss

    wordsss=count()
    frequentwords=frequent(8,wordsss)
    print frequentwords

    Licoln=["Four score and seven years ago, our fathers brought forth on this continent,",
    "a new nation, conceived in Liberty and dedicated to the proposition that all men are created equal.",
    "Now we are engaged in a great civil war,",
    "tesing whether that naion or any nation so conceived and so dedicated, can long endure.",
    "It is rather for us to be here dedicated to the great task remaining before us ",
    "that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion",
    "that we here highly resolve that these dead shall not have died in vain-that this nation, under God, shall have a new birth of freedom",
    "and that government of the people, by the people, for the people, shall not perish from the earth."]

    def countL():
        d = {}
        for i in Licoln:
            words=i.split()
            for word in words:
                if word in d:
                    d[word]+=1
                else:
                    d[word]=1
            return d

    def Lword(c,d):
        lol=list()
        for i in d:
            if d[i]>c:
                lol.append(i)
        return lol

    word=countL()
    Lwords=Lword(23,word)
    print Lwords

def lab11():
    question()
    speech()

def main():
    lab11()

if __name__=="__main__":
    main()
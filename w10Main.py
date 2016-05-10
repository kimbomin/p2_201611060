def milk():
    coffee=list()

    coffee=[  ["Coffee","Water","Milk","Icecream"],
      ["Espresso","No","No","No"],
      ["Long Black","Yes","No","No"],
      ["Flat White","No","Yes","No"],
      ["Cappuccino","No","Yes - Frothy","No"],
      ["Affogato","No","No","Yes"]
    ]
    data=coffee[1:]
    for i in data:
        print i[2]

def EandM():
    marks=list()
    marks=[
        ["English", 100],
        ["Math", 200],
        ["English", 200],
        ["Math", 200],
        ["English", 100],
        ["Math", 300]
    ]

    for i in marks:
        if i[0]=="English":
            print i

def letitbe():
    gasa=list()

    gasa=["When I find myself in times of trouble",
    "Mother Mary comes to me",
    "Speaking words of wisdom let it be",
    "And in my hour of darkness",
    "She is standing right in front of me",
    "Speaking words of wisdom let it be",
    "Let it be let it be",
    "Let it be let it be",
    "Whisper words of wisdom let it be",
    "And when the broken-hearted people",
    "Living in the world agree",
    "There will be an answer let it be",
    "For though they may be parted",
    "There is still a chance that they will see",
    "There will be an answer let it be",
    "Let it be let it be",
    "Let it be let it be",
    "Yeah there will be an answer let it be",
    "Let it be let it be",
    "Let it be let it be",
    "Whisper words of wisdom let it be",
    "Let it be let it be",
    "Ah let it be yeah let it be",
    "Whisper words of wisdom let it be",
    "And when the night is cloudy",
    "There is still a light that shines on me",
    "Shine on until tomorrow let it be",
    "I wake up to the sound of music",
    "Mother Mary comes to me",
    "Speaking words of wisdom let it be",
    "Let it be let it be",
    "Let it be yeah let it be",
    "Oh there will be an answer let it be",
    "Let it be let it be",
    "Let it be yeah let it be",
    "Whisper words of wisdom let it be"]


    def freqWord(gasa):    
        doc=gasa
        d=dict()
        for i in doc:
            words=i.split()
            for c in words:
                if c not in d:
                    d[c]=1
                else:
                    d[c]=d[c]+1
        return max(d,key=d.get)

    frequent=freqWord(gasa)

    print frequent

def lab10():
    milk()
    EandM()
    letitbe()

def main():
    lab10()

if  __name__=="__main__":
    main()

raw_input('Press the Enter')
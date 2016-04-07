def plus():
    sum=0 
    for i in range (1,1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print sum

def year():
    year=input("input year:")
    if (year%4==0) and (year%100!=0 or year%400==0):
        print "leap year"
    else:
        print "no leap yeard"

def highlow():
    import random

    Noa = 0

    print ('안녕! 이름이 뭐니?')
    myName = raw_input()

    number=random.randint(1,10)
    print ('안녕, %s. 내가 1부터 10까지 숫자중에서 생각하고 있는걸 맞춰봐.') %myName

    while Noa < 4:
        print('물어봐.')
        guess = input()
        guess = int(guess)
    
        Noa = Noa + 1
        if guess < number:
            print('그거보단 높아.')
    
        if guess > number:
            print('그거보단 낮아.')
    
        if guess == number:
            break
        
    if guess == number:
        Noa = str(Noa)
        print('맞췄어! %s 번만에 맞췄네!') %Noa
    
    if guess != number:
        number = str(number)
        print('아쉽네..내가 생각한 숫자는 %s (이)야..') %number
    

def lab6():
    plus()
    year()
    highlow()

def main():
    lab6()
    
if __name__=="__main__":
    main()

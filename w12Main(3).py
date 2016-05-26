import time
def homework1():
    msg='[KBM edited {0}]'.format(time.strftime('%Y-%m-%d , %H:%M:%S'))
    fin =open('output.txt','r')
    fout=open('outputUpper.txt','w')
    for line in fin:
        words=line.split()
        fout.write(msg)
        fout.write('\t')
        for word in words:
            if word=='line':
                word=word.upper()
            fout.write(word)
            fout.write(' ')
        fout.write('\n')
    fin.close()
    fout.close()
    
def homework2():
    data=[1,2,3,4,5,6,7,8,9,10]
    fout=open('outputNumber.txt','w')
    for i in data:
        str="{0}\t".format(i)
        fout.write(str)
        if i%2==0:
            fout.write('\n')
    fout.close()    
    
def lab13():    
    homework1()
    homework2()
    
def main():
    lab13()

if __name__=="__main__":
    main()    
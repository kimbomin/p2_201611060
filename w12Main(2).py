import os
mydir=os.getcwd()
filename='output.txt'
myfilename=os.path.join(mydir,filename)
myfile=open('output.txt','w')
line1='first line\n'
myfile.write(line1)
line2='second line\n'
myfile.write(line2)
line3='third line'
myfile.write(line3)
myfile.close()
myfile2=open(myfilename,'r')
for line in myfile2:
    if line.find('line')>=6:
        print 'line'.upper()
    if line.find('first' and 'second' and 'third')>=0:
        print 'first'.lower()
        print 'second'.lower()
        print 'third'.lower()
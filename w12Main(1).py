import os
mydir=os.getcwd()
filename='python.txt'
myfilename=os.path.join(mydir,filename)
try:
    myfile=open(myfilename,'r')
    for line in myfile:
        if line.find('Python')>=0:
            print line
    myfile.close()
except IOError as e:
    print e
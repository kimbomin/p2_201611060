height=input ("input your height:")
weight=input ("input your weight:")
bmi=weight/(height*height)
print "%s" %bmi
if bmi<18.5:
    print 'low weight'
elif 18.5<= bmi <25:
    print 'normal weight'
elif 25<= bmi <30:
    print 'overweight'
elif 30<= bmi <40:
    print 'obesity'
else:
    print 'seriously obese'
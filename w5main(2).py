import turtle
window=turtle.Screen()
A=raw_input('A input scissor, rock, paper:')
B=raw_input('B input scissor, rock, paper:')
if A=='scissor':
    if B=='rock':
        print "%s" %"B win"
    elif B=='paper':
        print "%s" %"A win"
    else:
        print "%s" %"draw"
elif A=='rock':
    if B=='scissor':
        print "%s" %"A win"
    elif B=='paper':
        print "%s" %"B win"
    else:
        print "%s" %"draw"
elif A=='paper':
    if B=='scissor':
        print "%s" %"B win"
    elif B=='rock':
        print "%s" %"A win"
    else:
        print "%s" %"draw"
window.exitonclick()

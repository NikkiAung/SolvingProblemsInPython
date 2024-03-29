# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
wordTable = [["AA", 2], ["AB", 4], ["AD", 3], ["AE", 2], ["AG", 3],
         ["AH", 5], ["AI", 2], ["AL", 2], ["AM", 4], ["AN", 2],
         ["AR", 2], ["AS", 2], ["AT", 2], ["AW", 5], ["AX", 9],
         ["AY", 5], ["BA", 4], ["BE", 4], ["BI", 4], ["BO", 4],
         ["BY", 7], ["DA", 3], ["DE", 3], ["DO", 3], ["ED", 3],
         ["EF", 5], ["EH", 5], ["EL", 2], ["EM", 4], ["EN", 2],
         ["ER", 2], ["ES", 2], ["ET", 2], ["EW", 5], ["EX", 9],
         ["FA", 5], ["FE", 5], ["GI", 3], ["GO", 3], ["HA", 5],
         ["HE", 5], ["HI", 5], ["HM", 7], ["HO", 5], ["ID", 3],
         ["IF", 5], ["IN", 2], ["IS", 2], ["IT", 2], ["JO", 9],
         ["KA", 6], ["KI", 6], ["LA", 2], ["LI", 2], ["LO", 2],
         ["MA", 4], ["ME", 4], ["MI", 4], ["MM", 6], ["MO", 4],
         ["MU", 4], ["MY", 7], ["NA", 2], ["NE", 2], ["NO", 2],
         ["NU", 2], ["OD", 3], ["OE", 2], ["OF", 5], ["OH", 5],
         ["OI", 2], ["OK", 6], ["OM", 4], ["ON", 2], ["OP", 4],
         ["OR", 2], ["OS", 2], ["OW", 5], ["OX", 9], ["OY", 5],
         ["PA", 4], ["PE", 4], ["PI", 4], ["PO", 4], ["QI", 11],
         ["RE", 2], ["SH", 5], ["SI", 2], ["SO", 2], ["TA", 2],
         ["TE", 2], ["TI", 2], ["TO", 2], ["UH", 5], ["UM", 4],
         ["UN", 2], ["UP", 4], ["US", 2], ["UT", 2], ["WE", 5],
         ["WO", 5], ["XI", 9], ["XU", 9], ["YA", 5], ["YE", 5],
         ["YO", 5], ["ZA", 11]]

# =====> Write your code here

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
index = 0
found = False
passed = False
suggest = []
doubleLetter = str(input('Enter the same two letter from AA to ZZ exclusively: '))
while index < len(wordTable) and (not found) and (not passed):
    if wordTable[index][0] == doubleLetter:
        found = True
    elif wordTable[index][0] > doubleLetter:
        passed = True
        suggest = wordTable[index]
    else:
        index += 1


if found:
    print(doubleLetter, 'has got', wordTable[index][1],'points')
elif passed:
    print(doubleLetter,'is not in the list')
    print('Use' + suggest[0] + 'worth' + str(suggest[1]) + 'points.')
else:
    suggest = wordTable[len(wordTable)-1]
    print(doubleLetter,'is not in the list.')
    print('Use' + suggest[0] + 'worth' + str(suggest[1]) + 'points.')
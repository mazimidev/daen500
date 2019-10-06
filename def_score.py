def computegrade(rawscore):

    if s >= 0 and s <= 1:
        if s >= 0.9:
            grade = 'A'
        elif s >= 0.8:
            grade = 'B'
        elif s >= 0.7:
            grade = 'C'
        elif s >= 0.6:
            grade = 'D'
        elif s <0.6:
    	    grade = 'F'
    else:
        grade = 'Not valid input'
    return grade

score = input("Enter Score: ")


try:
    s = float(score)
    grade = computegrade(score)
    print(grade)
except:
    print (type(score))
    print (isinstance(score,float))
    print('must be number')

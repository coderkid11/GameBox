import array

pointsScoredA = 1
pointsScoredB = 1

score = array.array( 'u', ['0' ,'-', '0'] ) 

print (score[0], score[1], score[2])

score[0] = '1'

print (score[0], score[1], score[2])

score[2] = '1'

print (score[0], score[1], score[2])

pointsScoredA = pointsScoredA + 1
score[0] = str(pointsScoredA)

print (score[0], score[1], score[2])

pointsScoredB = pointsScoredB + 1
score[2] = str(pointsScoredB)

print (score[0], score[1], score[2])
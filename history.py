score = 0
print('Welcome to this very simply history quiz!')
print('You will be asked 5 question about some hisorical events, your score will be displayed at the end of the game.')

# The first Question
print('##############')
print('Question 1: What year did the first world war take place?')
an1 = int(input('Answer with a number: '))

if an1 == 1914:
  print('Great Job!')
  score += 1
else:
  print('Wrong answer! The correct answer was: 1914')

# The second Question
print('##############')
print('Question 2: Russia and serbia where in an allience')
an1 = input('Is this statement True or False: ')

if an1.lower() == 'true':
  print('Great Job!')
  score += 1
else:
  print('Wrong answer! The correct answer was: True')

# The third Question
print('##############')
print("Question : What year did WW2 start?")
an1 = int(input("Answer with a number: "))

if an1 == 1939:
  print('Great Job!')
  score += 1
else:
  print('Wrong answer! The correct answer was: 1939')

# The fourth Question
print('##############')
print("Question 4: What year did WW1 end?")
an1 = int(input("Answer with a number: "))

if an1 == 1918:
  print('Great Job!')
  score += 1
else:
  print('Wrong answer! The correct answer was: 1918' )

# The fifth Question
print('##############')
print("Question 5: What year did WW2 end?")
an1 = int(input("Answer with a number: "))

if an1 == 1945:
  print('Great Job!')
  score += 1
else:
  print('Wrong answer! The correct answer was: 1945')

print('##############')
print('Your score is %s/5. thanks a lot for playing! Hope you had fun and learned something new!' % score)

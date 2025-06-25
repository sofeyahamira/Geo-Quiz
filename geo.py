print('Hello! Welcome to Geo quiz!')

ans = input('ready to play?(yes/no)')
score = 0
total_q = 5

if ans.lower() == 'yes':
  ans = input('1. what country expiriences sunrise first?')
  if ans.lower() == 'japan':
    score += 1
    print('correct')
  else:
    print()

ans = input('2. How many countries are there?')
if ans == '195':
  score += 1
  print('correct')
else:
  print('incorrect')

ans = input('3. How many continents are there?')
if ans == '7':
  score += 1
  print('correct')
else:
  print('incorrect')

ans = input('4. which of these countries is NOT in Asia? Chile, India, Malaysia, Japan')
if ans.lower() == 'chile':
  score += 1
  print('correct')
else:
  print('incorrect')

ans = input('5. Witch of these counries is in Africa? North Korea, Egypt, Indonesia, Brazil')
if ans.lower() == 'egypt':
  score += 1
  print('correct')
else:
  print('incorrect')

  print('Thanks for playing, you got ' , score, 'answer(s) right')
  mark = (score/total_q)*100
  print('Your mark is' , mark,'%')
print('Goodbye')

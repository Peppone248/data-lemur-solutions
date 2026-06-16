def another_one(digits):
  if 9 not in digits:
    digits[-1]+=1
  elif (digits[0] == 9):
    digits.append(0)
    digits[0] = 1
  else:
    digits[0] += 1
  for i, value in enumerate(digits):
    if digits[i] == 9:
      digits[i] = value-9
  return digits

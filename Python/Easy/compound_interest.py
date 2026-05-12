def compound_interest(principal, rate, contribution, years):
  increase = 0.0
  for i in range(years):
    increase = ((rate*principal)/100) + contribution
    principal += increase
  
  return round(principal, 2)

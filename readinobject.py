from collections import Counter 

totals = Counter() 
for s in portfolio: 
    totals[s['name']] += s['shares']

print(totals["IBM"])
#z6 zestaw 3
 def long_seq(t):
 	l = len(t)
 	i = 1
 	max = 0
 	for n in range(l):
 		if t[n] < t[n+1]:
 			i += 1
 		else:
 			i = 1
 		if max < i:
 			max = i
 

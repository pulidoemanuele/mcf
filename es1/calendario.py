import numpy as np

ottobre = ["mercoledì", "giovedì", "venerdì", "sabato", "domenica", "lunedì", "martedì"]
calendario = {}
for i in range(32) :
	if i < 7 :
		calendario[i+1] = ottobre[i]
	else:
		a = i//7
		calendario[i+1] = ottobre[a]
print("inserire il giorno")
n = input()
m= int(n)
print(calendario[m])

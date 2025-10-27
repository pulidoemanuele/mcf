import numpy as np
from datetime import datetime, timedelta

data = input("inserire la propria data di nascita nel formato giorno-mese-anno: ")
mydate = datetime.strptime(data, "%d-%m-%Y")
timediff = datetime.now() - mydate
tots = timediff.total_seconds()
anni = tots // 31536000
giorni = tots // 86400
print("l'età in anni è: ", anni)
print("l'età in giorni è: ", giorni)
print("l'età in secondi è: ", tots)

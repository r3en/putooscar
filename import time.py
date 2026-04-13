import time

inicio = time.time()

# Código a medir
for i in range(100000000):
   pass

fin = time.time()

print("Tiempo de ejecución:", fin - inicio, "segundos")

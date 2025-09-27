import matplotlib.pyplot as plt
import numpy as np

# Definimos los tamaños de entrada (desde 0 hasta 10000 en pasos de 500)

tamaños = np.arange(0, 10001, 500)

# Simulamos tiempos en milisegundos (lineal con n)

# Ejemplo: 0.05 ms por cada 1000 caracteres

tiempos_ms = tamaños * 0.001  # relación lineal ajustada

# Graficamos

plt.figure(figsize=(10,6))
plt.plot(tamaños, tiempos_ms, marker="o", linestyle="-", color="g", label="Tiempo ~ O(n)")

# Configuración de ejes

plt.title("Tiempo de ejecución del algoritmo vs tamaño de entrada")
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo de ejecución (ms)")  # ahora en milisegundos
plt.ylim(0, max(tiempos_ms) + 10)  # ajustamos para que se vea completo
plt.xlim(0, 10000)
plt.grid(True)
plt.legend()

# Mostrar gráfico

plt.show()

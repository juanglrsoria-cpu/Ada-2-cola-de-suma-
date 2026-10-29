class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        return self.elementos.copy()


def sumar_colas(cola_a, cola_b):
    resultado = Cola()

    elementos_a = cola_a.mostrar()
    elementos_b = cola_b.mostrar()

    for a, b in zip(elementos_a, elementos_b):
        resultado.encolar(a + b)

    return resultado


# Crear las colas originales
cola_a = Cola()
cola_b = Cola()

for numero in [3, 4, 2, 8, 12]:
    cola_a.encolar(numero)

for numero in [6, 2, 9, 11, 3]:
    cola_b.encolar(numero)

# Sumar sin modificar las colas originales
resultado = sumar_colas(cola_a, cola_b)

# Mostrar resultados
print("Cola A:", cola_a.mostrar())
print("Cola B:", cola_b.mostrar())
print("Cola resultado:", resultado.mostrar())

# Verificar que las originales se conservan
print("\nColas originales conservadas:")
print("Cola A:", cola_a.mostrar())
print("Cola B:", cola_b.mostrar())
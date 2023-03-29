def encontrar_umbral_or(entradas, salidas_esperadas, umbral=0.5):
    if len(entradas) == 0:
        errores = 0
        for i in range(len(entradas)):
            entrada = entradas[i]
            salida_esperada = salidas_esperadas[i]
            salida_real = 1 if sum(entrada) > umbral else 0
            if salida_real != salida_esperada:
                errores += 1
        if errores == 0:
            return umbral
        else:
            return None
    else:
        entrada_actual = entradas[0]
        salidas_esperadas_actual = salidas_esperadas[0]
        entradas_restantes = entradas[1:]
        salidas_esperadas_restantes = salidas_esperadas[1:]
        umbral_con_entrada_actual = encontrar_umbral_or(
            entradas_restantes, salidas_esperadas_restantes, umbral)
        if umbral_con_entrada_actual is not None:
            return umbral_con_entrada_actual
        else:
            umbral_sin_entrada_actual = encontrar_umbral_or(
                entradas_restantes, salidas_esperadas_restantes, umbral+0.1)
            if umbral_sin_entrada_actual is not None:
                salida_real = 1 if sum(
                    entrada_actual) > umbral_sin_entrada_actual else 0
                if salida_real == salidas_esperadas_actual:
                    return umbral_sin_entrada_actual
            return None


# Ejemplo de uso de la función
# Tabla de verdad de la compuerta OR
entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
salidas_esperadas = [0, 1, 1, 1]  # Salidas esperadas de la compuerta OR
umbral_or = encontrar_umbral_or(entradas, salidas_esperadas)
print("El umbral de la compuerta OR es:", umbral_or)

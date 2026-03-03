def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC).

    Parámetros:
    peso (float): Peso en kilogramos.
    altura (float): Altura en metros.

    Retorna:
    float: Valor del IMC.

    Lanza:
    ValueError: Si los valores son menores o iguales a cero.
    TypeError: Si los valores no son numéricos.
    """

    if not isinstance(peso, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("Peso y altura deben ser números.")

    if peso <= 0 or altura <= 0:
        raise ValueError("Peso y altura deben ser mayores que cero.")

    return peso / (altura ** 2)
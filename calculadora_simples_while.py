def calculadora(operacao, a, b):
    if operacao == "soma":
        return a + b
    elif operacao == "subtracao":
        return a - b
    elif operacao == "multiplicacao":
        return a * b
    elif operacao == "divisao":
        if b != 0:
            return a / b
        else:
            return "Erro: divisão por zero"
    else:
        return "Operação inválida"

operacao = input("Escolha uma operação (soma, subtracao, multiplicacao, divisao): ").strip().lower()
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

resultado = calculadora(operacao, a, b)
print(f"Resultado: {resultado}")

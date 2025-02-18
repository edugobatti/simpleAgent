# função que faz as operações de maneira generica
def operacao_generica(operacao: str, num1: float, num2: float):
    try:
        if operacao == "soma":
            resultado = num1 + num2
        elif operacao == "subtracao":
            resultado = num1 - num2
        elif operacao == "multiplicacao":
            resultado = num1 * num2
        elif operacao == "divisao":
            if num2 == 0:
                return "Erro: Divisão por zero."
            resultado = num1 / num2
        else:
            return f"Erro: Operação '{operacao}' não suportada."
        return resultado
    except Exception as e:
        return f"Erro ao executar a operação: {str(e)}"
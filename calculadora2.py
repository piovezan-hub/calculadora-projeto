# Funções para cada operação (Boas práticas: dividir o código em blocos lógicos)
def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero não é permitida."
    return x / y

# Menu principal
print("--- Calculadora Python ---")
print("Selecione a operação:")
print("1. Adição (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")

# Captura a escolha do usuário
escolha = input("Digite sua escolha (1/2/3/4): ")

# Verifica se a escolha é válida
if escolha in ('1', '2', '3', '4'):
    try:
        # float permite números decimais (ex: 10.5), essencial para análise de dados
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
            
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")
else:
    print("Opção inválida!")

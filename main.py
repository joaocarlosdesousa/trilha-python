# Treino de Variáveis, Inputs e Estruturas de Decisão (if/else) 

nome = input("Digite seu nome :")

linguagem = input("Qual linguagem você está vendo?")

print(f"\nOlá, {nome}! Você está no Degrau 1 da sua jornada.")

if linguagem.lower() == "python":
    print("Excelente escolha! Python é fundamental para Backend, Automação e IA.")
else:
    print(f"Muito legal aprender {linguagem}! Mas continue firme no Python para fechar o Degrau 1.")
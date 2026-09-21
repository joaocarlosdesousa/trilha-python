# Degrau 1: Praticando Loops (while/for) e Listas

tarefas = []

while True  :

    materias = input("Digite a disciplia para adicionar à lista (para sair digite 'sair')\n")

    if materias.lower() == 'sair':
         break
    

    tarefas.append(materias)
    print(f"\n{materias} adicionado à lista\n")



print("---LISTA DE MATÉRIAS---\n")

for index, materia in enumerate(tarefas, 1):
  print(f"{index}. {materia}\n")

print(f"\n Total de matérias cadastradas: {len(tarefas)}")


faculdade = {

    "nome": "João",
    "curso": "Ciência da Computação",
    "semestre": 2
}

faculdade.pop("semestre")

print("Chaves que restaram:\n", list(faculdade.keys()))

aluno2 = {

    "nome": "Maria",
    "curso": "Design"
}

turma = [faculdade, aluno2]


for facu in turma:
    print(f"Nome:  Curso:\n {facu['nome']}   {facu['curso']}\n")
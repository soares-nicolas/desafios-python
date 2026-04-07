print("\n" + "=" * 50)
print("Exercicio 2 - Dicionário de Aluno")
print("=" * 50)
 
aluno = {
    "nome": "Ana",
    "idade": 22,
    "curso": "ADS"
}
 
print(f"Nome do aluno: {aluno['nome']}")
 
aluno["nota"] = 9.5
print(f"Dicionário atualizado com nota: {aluno}")
print("\n" + "=" * 50)
print("Exercicio 6 - Sistema de Notas")
print("=" * 50)
 
notas_alunos = {
    "Carlos": 8.5,
    "Nicolas": 9.0,
    "Felipe": 7.3
}
 
print("Alunos cadastrados:")
for aluno, nota in notas_alunos.items():
    print(f"  {aluno}: {nota}")
 
aluno_busca = "Nicolas"
print(f"\nNota de {aluno_busca}: {notas_alunos[aluno_busca]}")
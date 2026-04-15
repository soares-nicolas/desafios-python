# Média de Notas com Status
def situacao_aluno(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    status = "Aprovado" if media >= 7 else "Reprovado"
    return media, status


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media, status = situacao_aluno(nota1, nota2, nota3)
print(f"Média: {media:.1f} - {status}")

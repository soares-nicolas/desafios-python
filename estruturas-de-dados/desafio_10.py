print("\n" + "=" * 50)
print("Exercicio 10 - Linguagens de Programação")
print("=" * 50)
 
respostas = [
    "Python", "Java", "Python", "C++", "Java",
    "Python", "JavaScript", "Python", "C++"
]
 
# 1. Linguagens únicas
linguagens_unicas = set(respostas)
print(f"Linguagens únicas: {linguagens_unicas}")
 
# 2. Contagem de cada linguagem
contagem = {}
for linguagem in respostas:
    contagem[linguagem] = contagem.get(linguagem, 0) + 1
 
print("\nQuantidade de votos por linguagem:")
for linguagem, votos in sorted(contagem.items(), key=lambda x: x[1], reverse=True):
    print(f"  {linguagem}: {votos} voto(s)")
 
# 3. Linguagem mais escolhida
mais_escolhida = max(contagem, key=contagem.get)
print(f"\nLinguagem mais escolhida: {mais_escolhida} ({contagem[mais_escolhida]} votos)")
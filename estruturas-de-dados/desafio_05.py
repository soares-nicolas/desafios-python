print("\n" + "=" * 50)
print("Exercicio 5 - Dicionário de Produto")
print("=" * 50)
 
produto = {
    "nome": "Notebook",
    "preco": 3500.00
}
 
print(f"Preço atual do produto '{produto['nome']}': R$ {produto['preco']:.2f}")
 
desconto = 0.10  # 10% de desconto
produto["preco"] = produto["preco"] * (1 - desconto)
print(f"Preço após {int(desconto * 100)}% de desconto: R$ {produto['preco']:.2f}")
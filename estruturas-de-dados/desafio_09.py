print("\n" + "=" * 50)
print("Exercicio 9 - Cadastro de Funcionários")
print("=" * 50)
 
funcionarios = {
    "Alice": {"cargo": "Desenvolvedora", "salario": 7500.00},
    "Bruno": {"cargo": "Analista",       "salario": 6000.00},
    "Carla": {"cargo": "Gerente",        "salario": 9000.00}
}
 
def cadastrar_funcionario(nome, cargo, salario):
    if nome in funcionarios:
        print(f"  Funcionário '{nome}' já cadastrado!")
    else:
        funcionarios[nome] = {"cargo": cargo, "salario": salario}
        print(f"  Funcionário '{nome}' cadastrado com sucesso!")
 
def atualizar_salario(nome, novo_salario):
    if nome in funcionarios:
        funcionarios[nome]["salario"] = novo_salario
        print(f"  Salário de '{nome}' atualizado para R$ {novo_salario:.2f}")
    else:
        print(f"  Funcionário '{nome}' não encontrado.")
 
def exibir_funcionarios():
    print("\n  Lista de Funcionários:")
    for nome, dados in funcionarios.items():
        print(f"    {nome} | {dados['cargo']} | R$ {dados['salario']:.2f}")
 
print("Funcionários cadastrados inicialmente:")
exibir_funcionarios()
 
print("\nAtualizando salário da Alice:")
atualizar_salario("Alice", 8500.00)
 
print("\nTentando cadastrar funcionário duplicado:")
cadastrar_funcionario("Bruno", "Analista Sênior", 6500.00)
 
print("\nCadastrando novo funcionário:")
cadastrar_funcionario("Diego", "Suporte", 4500.00)
 
exibir_funcionarios()
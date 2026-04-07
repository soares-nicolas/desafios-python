print("\n" + "=" * 50)
print("EXERCÍCIO 7 - Sistema de Inscrição")
print("=" * 50)
 
participantes = ["João", "Ana", "Carlos", "Ana", "João", "Beatriz", "Carlos"]
print(f"Lista com repetições: {participantes}")
 
participantes_unicos = set(participantes)
print(f"Participantes únicos: {participantes_unicos}")
print(f"Total de inscritos (sem duplicatas): {len(participantes_unicos)}")
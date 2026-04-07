print("\n" + "=" * 50)
print("EXERCÍCIO 8 - Coordenadas Turísticas")
print("=" * 50)
 
coordenadas = (-23.55, -46.63)  
print(f"Coordenadas do ponto turístico:")
print(f"  Latitude:  {coordenadas[0]}")
print(f"  Longitude: {coordenadas[1]}")
 
coordenadas[0] = -22.90  # TypeError: 'tuple' object does not support item assignment

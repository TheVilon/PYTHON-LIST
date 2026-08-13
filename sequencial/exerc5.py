import math

area = float(input("Digite a área (m²): "))
litros = (area / 6) * 1.1  # Litros necessários com 10% de folga

# 1. Apenas latas (18L)
latas = math.ceil(litros / 18)

# 2. Apenas galões (3,6L)
galoes = math.ceil(litros / 3.6)

# 3. Mistura de latas e galões
latas_m = int(litros // 18)
galoes_m = math.ceil((litros % 18) / 3.6)

print(f"\nLitros necessários: {litros:.2f}L")
print(f"1. Apenas latas (18L): {latas} lata(s) - R$ {latas * 80:.2f}")
print(f"2. Apenas galões (3.6L): {galoes} galão(ões) - R$ {galoes * 25:.2f}")
print(f"3. Mistura: {latas_m} lata(s) e {galoes_m} galão(ões) - R$ {(latas_m * 80) + (galoes_m * 25):.2f}")
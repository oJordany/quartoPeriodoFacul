import math 
# Exemplo 1
PIs = [3.14, 3.1416, 3.141592654]
areasDaCircunferencia = {PI: PI * math.pow(100, 2) for PI in PIs}

for PI, area in areasDaCircunferencia.items() : 
  print(f'Área da circunferência para PI = {PI}: {area}')
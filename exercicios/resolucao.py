## LOAD

import numpy as np
dataset34 = np.load('dataset34.npy')

## Exercício 1
# Quantidade absoluta e relativa(%) de clientes por especialidade?

print('\nExercício 1')
print('Quantidade absoluta e relativa(%) de clientes por especialidade:')
print()

# INDEXACAO BOOLEANA
dataset_especialidade = dataset34[:, 1]
especialidade_clinico = dataset_especialidade == 1
especialidade_cardiologia = dataset_especialidade == 2
especialidade_pediatria = dataset_especialidade == 3

print(f'Quantidade absoluta de clientes para clínico geral: {sum(especialidade_clinico)}')
print(f'Quantidade relativa de clientes para clínico geral: {sum(especialidade_clinico) * 100 / len(dataset_especialidade): .2f}%.')
print(f'Quantidade absoluta de clientes para cardiologia: {sum(especialidade_cardiologia)}')
print(f'Quantidade relativa de clientes para cardiologia: {sum(especialidade_cardiologia) * 100 / len(dataset_especialidade): .2f}%.')
print(f'Quantidade absoluta de clientes para pediatria: {sum(especialidade_pediatria)}')
print(f'Quantidade relativa de clientes para pediatria: {sum(especialidade_pediatria) * 100 / len(dataset_especialidade): .2f}%.')

## Exercício 2
# Exibir a lista de especialidade, em ordem crescente, por tempo médio de atendimento:

print('\nExercício 2')
print('Lista de especialidade, em ordem crescente, por tempo médio de atendimento:')
print()

# INDEXAÇÃO SOFISTICADA

index_fancy = np.argsort(dataset34[:, 3])
subdataset = dataset34[index_fancy]

for especialidade in subdataset:
  print(f'Especialidade: {especialidade[1]}, Tempo: {especialidade[3]}')

## Exercício 3
# Quantidade absoluta e relativa (%) de clientes por especialidade que ficaram internados?

print('\nExercício 3')
print('Quantidade absoluta e relativa (%) de clientes por especialidade que ficaram internados:')
print()

# INDEXAÇÃO BOOLEANA

dataset_internacao = dataset34[:, 2] == 1

dataset_clinico_int = dataset_internacao[dataset_internacao & especialidade_clinico]
dataset_cardiologia_int = dataset_internacao[dataset_internacao & especialidade_cardiologia]
dataset_pediatria_int = dataset_internacao[dataset_internacao & especialidade_pediatria]

print(
  f'Quantidade absoluta de clientes atendidos pelo clínico geral que ficaram internados: {sum(dataset_clinico_int)}.')
print(
  f'Quantidade relativa de clientes atendidos pelo clínico geral que ficaram internados: {sum(dataset_clinico_int) / sum(dataset_internacao) * 100: .3f}%.')
print(
  f'Quantidade absoluta de clientes atendidos pela cardiologia que ficaram internados: {sum(dataset_cardiologia_int)}.')
print(
  f'Quantidade relativa de clientes atendidos pelo cardiologia que ficaram internados: {sum(dataset_cardiologia_int) / sum(dataset_internacao) * 100: .3f}%.')
print(
  f'Quantidade absoluta de clientes atendidos pela pediatria que ficaram internados: {sum(dataset_pediatria_int)}.')
print(
  f'Quantidade relativa de clientes atendidos pelo pediatria que ficaram internados: {sum(dataset_pediatria_int) / sum(dataset_internacao) * 100: .3f}%.')

## Exercício 4
# 4) Criar uma lista enumerada com o tempo de atendimento por cliente em segundos:

print('\nExercício 4')
print('Lista enumerada com o tempo de atendimento por cliente em segundos:')
print()

# VETORIZAÇÃO

quantidadeSegundos = dataset34[:, 3] * 60
for indice, segundo in enumerate(quantidadeSegundos):
  print(f'Cliente {indice + 1}: {segundo} segundos.')

## Exercício 5
# Exibir o tempo total de atendimento do setor cardiologia em segundos:

print('\nExercício 5')
print('Tempo total de atendimento do setor cardiologia em segundos:')
print()

# VETORIZAÇÃO

cardiologia = dataset34[dataset34[:, 1] == 2]
minutos_cardiologia = (cardiologia[:, 3])
segundos_cardiologia = minutos_cardiologia * 60
print(f'Tempo total de atendimento do setor cardiologia em segundos: {sum(segundos_cardiologia)}')

## Exercício 6
# Exibir o código dos 10 clientes que tiveram o menor tempo de atendimento, agrupando por 'Internação' e 'Alta após a consulta':

print('\nExercício 6')
print('Código dos 10 clientes que tiveram o menor tempo de atendimento, agrupando por "Internação" e "Alta após a consulta":')
print()

# INDEXAÇÃO SOFISTICADA

index_fancy = np.argsort(dataset34[:, 3])

subdataset = dataset34[index_fancy]
subdataset_internacao = subdataset[subdataset[:, 2] == 1][:10]
subdataset_n_internacao = subdataset[subdataset[:, 2] == 0][:10]

print('Clientes que tiveram menor tempo de atendimento e foram internados:\n')
for codigo in subdataset_internacao:
  print(f'Código: {codigo[0]:.0f}')

print('\nClientes que tiveram menor tempo de atendimento e tiveram alta após a consulta:\n')
for codigo in subdataset_n_internacao:
  print(f'Codigo: {codigo[0]:.0f}')
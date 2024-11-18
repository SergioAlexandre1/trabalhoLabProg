import numpy as np
from datetime import datetime

# 1) Leitura e preparação dos dados
my_data = np.genfromtxt('vendas.csv', delimiter=',', dtype=str, skip_header=1)

# Extraindo e convertendo colunas específicas
qtd_v = my_data[:, 3].astype(int)
produto_u = my_data[:, 4].astype(float)
valor_t = my_data[:, 5].astype(float)

# 2) Análise estatística
quantidades = qtd_v
produtos = my_data[:, 2]
regioes = my_data[:, 1]
datas = my_data[:, 0]

# Média, mediana e desvio padrão do valor total
media_valor_total = np.mean(valor_t)
mediana_valor_total = np.median(valor_t)
desvio_padrao_valor_total = np.std(valor_t)

# Produto com a maior quantidade vendida e produto com o maior valor total de vendas
produto_maior_quantidade = produtos[np.argmax(quantidades)]
produto_maior_valor_total = produtos[np.argmax(valor_t)]

# Valor total de vendas por região
regioes_unicas = np.unique(regioes)
vendas_totais_por_regiao = {
    regiao: np.sum(valor_t[regioes == regiao]) for regiao in regioes_unicas
}

# Venda média por dia
datas_unicas = np.unique(datas)
media_vendas_por_dia = np.sum(valor_t) / len(datas_unicas)

# Resultados
print(f"Média do Valor Total: {media_valor_total:.2f}")
print(f"Mediana do Valor Total: {mediana_valor_total:.2f}")
print(f"Desvio Padrão do Valor Total: {desvio_padrao_valor_total:.2f}")
print(f"Produto com maior quantidade vendida: {produto_maior_quantidade}")
print(f"Produto com maior valor total de vendas: {produto_maior_valor_total}")
print("\nValor total de vendas por região:")
for regiao, valor in vendas_totais_por_regiao.items():
    print(f"- {regiao}: {valor:.2f}")
print(f"\nVenda média por dia: {media_vendas_por_dia:.2f}")

# 3) Análise Temporal

# Extrair datas e valores totais (usando my_data original)
datas = my_data[:, 0]
valores_totais = valor_t

# Converter as datas para datetime
datas_datetime = np.array([datetime.strptime(data, "%Y-%m-%d") for data in datas])

# Determinar o dia da semana com maior número de vendas
dias_da_semana = [data.strftime("%A") for data in datas_datetime]
unicos, contagens = np.unique(dias_da_semana, return_counts=True)
dia_mais_vendas = unicos[np.argmax(contagens)]

# Calcular a variação diária no valor total de vendas
# Ordenar por data
ordenacao = np.argsort(datas_datetime)
datas_ordenadas = datas_datetime[ordenacao]
valores_totais_ordenados = valores_totais[ordenacao]

# Calcular diferenças entre dias consecutivos
variacao_diaria = np.diff(valores_totais_ordenados)

# Resultados
print(f"Dia da semana com maior número de vendas: {dia_mais_vendas}")
print("Variação diária no valor total de vendas:")
print(variacao_diaria)

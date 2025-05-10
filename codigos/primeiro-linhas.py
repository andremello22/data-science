from matplotlib import pyplot as plt

anos = [ 2019, 2020, 2021, 2022, 2023, 2024, 2025]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

 # cria um gráfico de linha, anos no eixo x, gdp no eixo y
plt.plot(anos, gdp, color='green', marker='o', linestyle='solid')

plt.title("GDP Nominal")

plt.xlabel("Anos")

 # adiciona um selo no eixo y
plt.ylabel("Bilhões de $")

plt.show()
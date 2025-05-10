from matplotlib import pyplot as plt

filmes =  ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]

num_oscars = [5, 11, 3, 8, 10]

# barras possuem o tamanho padrão de 0.8, então adicionaremos 0.1 às
 # coordenadas à esquerda para que cada barra seja centralizada
xs = [i + 0.1 for i, _ in enumerate(filmes)]
print(xs) # [0.1, 1.1, 2.1, 3.1, 4.1]
 # as barras do gráfico com as coordenadas x à esquerda [xs], alturas
plt.bar(xs, num_oscars)

plt.ylabel("# de premiações")

plt.title("Meus filmes favoritos")

 # nomeia o eixo x com nomes de filmes na barra central
plt.xticks([i + 0.1 for i, _ in enumerate(filmes)], filmes)

plt.show()
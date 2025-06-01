from collections import Counter
from matplotlib import pyplot as plt
from funcoes_algebra_linear import sum_of_squares
from math import sqrt
num_friends = [100, 49, 41, 40, 25, 25, 25, 24, 23, 22,
                21, 20, 20, 19, 19, 18, 18, 17, 17, 16,
                16, 15, 15, 14, 14, 13, 13, 12, 12, 11,
                11, 10, 10, 9, 9, 8, 8, 7, 7, 6]
friends_counts = Counter(num_friends)
num_points = len(num_friends)               
largest_value = max(num_friends)           
smallest_value = min(num_friends) 
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]            
second_smallest_value = sorted_values[1]     
second_largest_value = sorted_values[-2]   

def mean(x):
    from __future__ import division
    return sum(x) / len(x)

def median(x):
    n = len(x)
    sorted_x = sorted(x)
    midi_point = n // 2
    if n % 2 == 1:
        # se for ímpar, retorna o valor do meio
        return sorted_x[midi_point]
    else:
        # se for par, retorna a média dos dois valores do meio
        lo = midi_point - 1
        hi = midi_point
        return (sorted_x[lo] + sorted_x[hi]) / 2
    

def quantile(x, p):
 """retorna o valor percentual p-ésimo em x"""
 p_index = int(p * len(x))
 return sorted(x)[p_index]

quantile(num_friends, 0.10) # 1
quantile(num_friends, 0.25) # 3
quantile(num_friends, 0.75) # 9
quantile(num_friends, 0.90) # 13

def mode(x):
 """retorna uma lista, pode haver mais de uma moda"""
 counts = Counter(x)
 max_count = max(counts.values())
 return [x_i for x_i, count in counts.items() if count == max_count]


mode(num_friends)      
# 1 and 6


 # “amplitude” já possui significado em Python, então usaremos um nome diferente
def data_range(x):
 return max(x) - min(x)

data_range(num_friends) # 9

def mean(x):
    return sum(x) / len(x)

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
 """presume que x tem ao menos dois elementos"""
 n = len(x)
 deviations = de_mean(x)
 return sum_of_squares(deviations) / (n - 1)
variance(num_friends) # 81.5


def standard_deviation(x):
 return sqrt(variance(x))
standard_deviation(num_friends) # 9.03

def interquartile_range(x):
 return quantile(x, 0.75) - quantile(x, 0.25)
interquartile_range(num_friends) # 6

print(friends_counts)
xs = sorted(friends_counts.keys())
print(xs)
ys = [friends_counts[x] for x in xs]
plt.bar(xs, ys, width=1)
plt.axis([0, max(xs)+5, 0, max(ys)+1])
plt.title("Histograma de amigos")
plt.xlabel("Número de amigos")
plt.ylabel("Número de pessoas")
plt.show()
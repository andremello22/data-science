from math import sqrt

def add_vector(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]#soma de vetores

def subtract_vector(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
   result = vectors[0]
   for vactor in vectors[1:]:
       result = add_vector(result, vactor)
   return result

def scalar_multiply(c, v):
    return [c* v_i for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)

def magnitude(v):
    return sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(subtract_vector(v, w))

def distance(v, w):
    return magnitude(subtract_vector(v, w))
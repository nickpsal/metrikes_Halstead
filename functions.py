# Calculate Halstead Metrics
from math import log


def calc(n1, n2, N1, N2):
    values = []
    # calculate all the variables
    n = n1 + n2
    values.append(n)
    N = N1 + N2
    values.append(N)
    Nest = n1 * log(n1, 2) + n2 * log(n2, 2)
    values.append(Nest)
    V = N * log(n, 2)
    values.append(V)
    L = (2 * n2) / (n1 * N2)
    values.append(L)
    lamda = L * L * V
    values.append(lamda)
    D = 1 / L
    values.append(D)
    E = D * V
    values.append(E)
    T = E / 18
    values.append(T)
    B = pow(E, 2.0 / 3.0) / 3000
    values.append(B)
    return values


def print_values(n1, n2, N1, N2, values):
    print("--------------------------------------------------------------------------------------------------------")
    print("The calculated Variables are:")
    print(f"n1 = {n1}")
    print(f"n2 = {n2}")
    print(f"N1 = {N1}")
    print(f"N2 = {N2}")
    print(f"n = {values[0]}")
    print(f"N = {values[1]}")
    print(f"Nest = {values[2]}")
    print(f"V = {values[3]}")
    print(f"L = {values[4]}")
    print(f"lamda = {values[5]}")
    print(f"D = {values[6]}")
    print(f"E = {values[7]}")
    print(f"T = {values[8]}")
    print(f"B = {values[9]}")
    print("--------------------------------------------------------------------------------------------------------")

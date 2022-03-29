# Calculate Halstead Metrics
from math import log


def calc(n1, n2, N1, N2):
    values = []
    # calculate all the variables
    n = float(n1 + n2)
    values.append(n)
    N = float(N1 + N2)
    values.append(N)
    Nest = float(n1 * log(n1, 2) + n2 * log(n2, 2))
    values.append(Nest)
    V = float(N * log(n, 2))
    values.append(V)
    L = float((2 * n2) / (n1 * N2))
    values.append(L)
    lamda = float(L * L * V)
    values.append(lamda)
    D = float(1 / L)
    values.append(D)
    E = float(D * V)
    values.append(E)
    T = float(E / 18)
    values.append(T)
    B = float(pow(E, 2.0 / 3.0) / 3000)
    values.append(B)
    return values


def print_values(n1, n2, N1, N2, values):
    print("--------------------------------------------------------------------------------------------------------")
    print("The calculated Variables are:")
    print(f"n1 = {n1}")
    print(f"n2 = {n2}")
    print(f"N1 = {N1}")
    print(f"N2 = {N2}")
    print(f"Program Vocabulary Size = {values[0]}")
    print(f"Program Length = {values[1]}")
    print(f"Program Length Estimator  = {values[2]}")
    print(f"Program Volume = {values[3]}")
    print(f"Program Level = {values[4]}")
    print(f"Language Level = {values[5]}")
    print(f"Program Difficulty = {values[6]}")
    print(f"Program Effort = {values[7]}")
    print(f"Program Implementation Time = {values[8]}")
    print(f"Program Errors Estimator = {values[9]}")
    print("--------------------------------------------------------------------------------------------------------")


def write_to_file(n1, n2, N1, N2, values):
    filename = str(n1) + " , " + str(n2) + " , " + str(N1) + " , " + str(N2) + ".txt"
    f = open(filename, "w")
    f.write(" Export file values \n")
    f.write("---------------------------------------------------\n")
    f.write(f"n1 = {n1}\n")
    f.write(f"n2 = {n2}\n")
    f.write(f"N1 = {N1}\n")
    f.write(f"N2 = {N2}\n")
    f.write(f"Program Vocabulary Size = {values[0]}\n")
    f.write(f"Program Length = {values[1]}\n")
    f.write(f"Program Length Estimator  = {values[2]}\n")
    f.write(f"Program Volume = {values[3]}\n")
    f.write(f"Program Level = {values[4]}\n")
    f.write(f"Language Level = {values[5]}\n")
    f.write(f"Program Difficulty = {values[6]}\n")
    f.write(f"Program Effort = {values[7]}\n")
    f.write(f"Program Implementation Time = {values[8]}\n")
    f.write(f"Program Errors Estimator = {values[9]}\n")
    f.write("---------------------------------------------------\n")
    f.close()


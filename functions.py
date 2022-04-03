# Calculate Halstead Metrics
from math import log


def calc(n1, n2, N1, N2):
    # calculate all the variables
    values = {"n1": n1, "n2": n2, "N1": N1, "N2": N2}
    n = float(n1 + n2)
    values["n = n1 + n2 = "] = n
    N = float(N1 + N2)
    values["N = N1 + N2 = "] = N
    Nest = float(n1 * log(n1, 2) + n2 * log(n2, 2))
    values["Nest "] = Nest
    Nest_N = Nest / N
    values["Nest / N = "] = Nest_N
    V = float(N * log(n, 2))
    values["V = N*log2n = "] = V
    L = float((2 * n2) / (n1 * N2))
    values["L = Lest = "] = L
    lamda = float(L * L * V)
    values["λ = L * L * V = "] = lamda
    D = float(1 / L)
    values["D = 1 / L = "] = D
    E = float(D * V)
    values["E = D * V = "] = E
    T = float(E / 18)
    values["T = E / 18 = "] = T
    B = float(pow(E, 2.0 / 3.0) / 3000)
    values["B = E^(2/3) / 3000 = "] = B
    return values


def print_values(values):
    print("--------------------------------------------------------------------------------------------------------")
    print("The calculated Variables are:")
    for i in values.keys():
        print(f"{i} = {values[i]}")
    print("--------------------------------------------------------------------------------------------------------")


def write_to_file(values):
    filename = str(values["n1"]) + " , " + str(values["n2"]) + " , " + str(values["N1"]) + " , " + str(values["N2"]) + ".txt"
    f = open(filename, "w")
    f.write("Export file values \n")
    f.write("---------------------------------------------------\n")
    for i in values.keys():
        f.write(f"{i} = {values[i]}\n")
    f.write("---------------------------------------------------\n")
    f.close()

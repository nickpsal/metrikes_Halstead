# Calculate Halstead Metrics
from math import log


def calc(n1, n2, N1, N2):
    values = {}
    # calculate all the variables
    n = float(n1 + n2)
    values["Program Vocabulary Size"] = n
    N = float(N1 + N2)
    values["Program Length"] = N
    Nest = float(n1 * log(n1, 2) + n2 * log(n2, 2))
    values["Program Length Estimator"] = Nest
    V = float(N * log(n, 2))
    values["Program Volume"] = V
    L = float((2 * n2) / (n1 * N2))
    values["Program Level"] = L
    lamda = float(L * L * V)
    values["Language Level"] = lamda
    D = float(1 / L)
    values["Program Difficulty"] = D
    E = float(D * V)
    values["Program Effort"] = E
    T = float(E / 18)
    values["Program Implementation Time"] = T
    B = float(pow(E, 2.0 / 3.0) / 3000)
    values["Program Errors Estimator"] = B
    return values


def print_values(n1, n2, N1, N2, values):
    print("--------------------------------------------------------------------------------------------------------")
    print("The calculated Variables are:")
    print(f"n1 = {n1}")
    print(f"n2 = {n2}")
    print(f"N1 = {N1}")
    print(f"N2 = {N2}")
    for i in values.keys():
        print(f"{i} = {values[i]}")
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
    for i in values.keys():
        f.write(f"{i} = {values[i]}\n")
    f.write("---------------------------------------------------\n")
    f.close()

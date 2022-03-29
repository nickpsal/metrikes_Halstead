# Calculate Halstead Metrics
from math import log


def calc(n1, n2, N1, N2):
    # calculate all the variables
    values = {"n1": n1, "n2": n2, "N1": N1, "N2": N2}
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
    for i in values.keys():
        print(f"{i} = {values[i]}")
    print("--------------------------------------------------------------------------------------------------------")


def write_to_file(n1, n2, N1, N2, values):
    filename = str(n1) + " , " + str(n2) + " , " + str(N1) + " , " + str(N2) + ".txt"
    f = open(filename, "w")
    f.write(" Export file values \n")
    f.write("---------------------------------------------------\n")
    for i in values.keys():
        f.write(f"{i} = {values[i]}\n")
    f.write("---------------------------------------------------\n")
    f.close()

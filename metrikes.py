# Calculate Halstead Metrics
from math import log

while True:
    n1 = input("Δώσε το n1 ")
    n2 = input("Δώσε το n2 ")
    N1 = input("Δώσε το N1 ")
    N2 = input("Δώσε το N2 ")
    try:
        n1 = float(n1)
        n2 = float(n2)
        N1 = float(N1)
        N2 = float(N2)
        break
    except ValueError:
        print("Δεν δώσατε νούμερο σε κάποια απο τις μεταβλητές")
        continue

# calculate all the variables
n = n1 + n2
N = N1 + N2
Nest = n1*log(n1, 2) + n2*log(n2, 2)
V = N*log(n, 2)
L = (2*n2)/(n1*N2)
lamda = L*L*V
D = 1/L
E = D*V
T = E/18
B = pow(E, 2/3) / 3000

# print all the calculated variables
print("--------------------------------------------------------------------------------------------------------")
print("The calculated Variables are")
print(f"n1 = {n1}")
print(f"n2 = {n2}")
print(f"N1 = {N1}")
print(f"N2 = {N2}")
print(f"n = {n}")
print(f"N = {N}")
print(f"Nest = {Nest}")
print(f"V = {V}")
print(f"L = {L}")
print(f"lamda = {lamda}")
print(f"D = {D}")
print(f"E = {E}")
print(f"T = {T}")
print(f"B = {B}")
print("--------------------------------------------------------------------------------------------------------")
input("Πατήστε Κάποιο πλήκτρο για Έξοδο")
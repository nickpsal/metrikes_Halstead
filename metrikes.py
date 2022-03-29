# Calculate Halstead Metrics
from functions import *

print("----------------------------------- Halstead Metrics -----------------------------------")
print("We provide the numbers n1, n2, N1, N2 and the program calculates all the Halstead Metrics")

while True:
    n1 = input("Give n1 Value ")
    n2 = input("Gibe n2 Value ")
    N1 = input("Gibe the N1 Value ")
    N2 = input("Give the N2 Value ")
    try:
        n1 = float(n1)
        n2 = float(n2)
        N1 = float(N1)
        N2 = float(N2)
        if n1 <= 0 or n2 <= 0 or N1 <= 0 or N2 <= 0:
            print("You vive a negative Value or zero Please give a positive Value")
            continue
        else:
            break
    except ValueError as e:
        print(e)
        continue

values = calc(n1, n2, N1, N2)
# print all the calculated variables
write_to_file(n1, n2, N1, N2, values)
print_values(n1, n2, N1, N2, values)
input("Press any key for exit")
exit()

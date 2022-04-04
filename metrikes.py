# Calculate Halstead Metrics
from functions import *

print("----------------------------------- Halstead Metrics -----------------------------------")
print("We provide the numbers n1, n2, N1, N2 and the program calculates all the Halstead Metrics")
while True:
    try:
        n1, n2, N1, N2 = input("Give the n1, N2, N1, N2 values ").split(',')
        n1 = float(n1)
        n2 = float(n2)
        N1 = float(N1)
        N2 = float(N2)
        if n1 < 0 or n2 < 0 or N1 < 0 or N2 < 0:
            print("You vive a negative Value or zero Please give a positive Value")
            continue
        elif n1 == 0 and n2 == 0 and N1 == 0 and N2 == 0:
            break
        else:
            values = calc(n1, n2, N1, N2)
            # print all the calculated variables
            write_to_file(values)
            print_values(values)
            epil = input("Do you want to calculate again? y/n ")
            if epil == "Y" or epil == "y":
                continue
            else:
                break
    except ValueError as e:
        print(e)
        continue

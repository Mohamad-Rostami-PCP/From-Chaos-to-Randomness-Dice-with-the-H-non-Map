# Import libraries for numerical calculations
import numpy as np
from statistics import mean
from statistics import pstdev

# Receiving parameters from user
N_throws = int(input("How many dice you want us to throw?"))


# Data generation using Hénon map function
def Random_DataSet_Generator():
    # Define the parameters of the Hénon map
    a = 1.4
    b = 0.3

    # Define the initial values of x and y
    x0 = 0.1
    y0 = 0.3

    # Create an empty array to store the data points
    data = np.zeros((N_throws, 2))

    # Iterate the Hénon map for 10000 times
    for i in range(N_throws):
        # Apply the equations
        x1 = 1 - a * x0 ** 2 + y0
        y1 = b * x0
        # Store the data point
        data[i, 0] = x1
        data[i, 1] = y1
        # Update the values of x and y
        x0 = x1
        y0 = y1

    # Normalizing between (0,1)
    X = data[:, 0]
    Y = data[:, 1]

    data[:, 0] = (X - np.min(X)) / (np.max(X) - np.min(X))
    data[:, 1] = (Y - np.min(Y)) / (np.max(Y) - np.min(Y))

    # Save the data array into a text file named 'henon_data.txt'
    np.savetxt('henon_data.txt', data)


# Creating the dices funtion
def create_dice(data_set):
    Dice = [0, 0, 0, 0, 0, 0]
    break_points = [0, 0, 0, 0, 0, 0, 0]
    for i in range(7):
        step = 1 / 6
        break_points[i] = step * i

    for i in range(N_throws):
        rand_val = data_set[i]
        for j in range(6):
            if (rand_val >= break_points[j]) and (rand_val < break_points[j + 1]):
                Dice[j] += 1
                break

    dice_probability = [0, 0, 0, 0, 0, 0]
    for k in range(6):
        dice_probability[k] = Dice[k] / N_throws

    print(f"The probability set is: {dice_probability}")

    RMS = pstdev(dice_probability)

    print(f"The Root-Mean-Square is: {RMS}")

    validation = RMS < (N_throws ** (-0.5))

    print(f"Dose this RMS agree with Fluctuation-dissipation theorem? : {validation}")

    return dice_probability


# Monte-Carlo  function
# def Accept_Rejection(initial_D, initial_P, desired_P):
#
#     break_points = [0, 0, 0, 0, 0, 0, 0]
#     for i in range(7):
#         step = 1 / 6
#         break_points[i] = step * i
#
#     def classify(value):
#         for k in range(6):
#             if break_points[k] <= value < break_points[k + 1]:
#                 return k
#
#
#     for i in range(N_throws):
#         Dice_number = classify(initial_D[i])
#         if initial_P[Dice_number] <= 1/6:

    # return final_distribution

# Run section

#   phase-1 : Generate the data set
Random_DataSet_Generator()

#   phase-2 : Create Dices
Dice_1 = create_dice(np.loadtxt("henon_data.txt", dtype=float)[:, 0])
Dice_2 = create_dice(np.loadtxt("henon_data.txt", dtype=float)[:, 1])

print("\n-->This shows that the dice we have created is not uniform/n and this is what we will do in next homework to make a uniform distribution out of a nonuniform set.")






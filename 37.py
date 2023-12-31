# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1awBufCNftzXs3uwAvw39EpeerSrMzw7s
"""

import matplotlib.pyplot as plt

def f(x):
    return x**3 - x - 1

#first derivative

def f_prime(x):
    return 3*x**2 - 1

def newton_raphson(x0, max_iterations=300, tolerance=1e-7):
    xi = x0
    approximation_errors = []

    for i in range(max_iterations):
        f_xi = f(xi)
        f_prime_xi = f_prime(xi)

        if abs(f_prime_xi) < 1e-10:
            break

        xi_plus_1 = xi - f_xi / f_prime_xi
        approx_error = abs(xi_plus_1 - xi)
        relative_approx_error = abs(approx_error / xi_plus_1)

        approximation_errors.append(approx_error)

        print(f"Iteration {i+1}:")
        print(f"xi = {xi:.6f}, f(xi) = {f_xi:.6f}, f'(xi) = {f_prime_xi:.6f}")
        print(f"xi+1 = {xi_plus_1:.6f}, Approximation Error = {approx_error:.6f}, Relative Approx Error = {relative_approx_error:.6f}\n")

        xi = xi_plus_1

        if approx_error < tolerance:
            break

    return xi, approximation_errors

# Initial guess
x0 = 50

# Perform the Newton-Raphson method
root, approximation_errors = newton_raphson(x0)

# Visualize the approximation errors using a bar chart
plt.bar(range(1, len(approximation_errors)+1), approximation_errors, color='olive')
plt.xlabel("Iteration")
plt.ylabel("Approximation Error of the graph")
plt.title("Approximation Error vs Iteration Number Bar Chart")
plt.show()

print(f"The root of the given function is approximately: {root:.6f}")
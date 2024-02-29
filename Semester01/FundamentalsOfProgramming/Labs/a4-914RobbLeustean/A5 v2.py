import math

def original_series(n):
    return (-1) ** (n + 1) / n

n_values = [10000, 20000, 50000]  # Large values of n to study convergence

# Calculate the partial sums for different values of n
for n in n_values:
    partial_sum = sum(original_series(k) for k in range(1, n))
    print(f"Partial Sum for n = {n}: {partial_sum}")

# Calculate the exact value of ln(2)
ln2 = math.log(2)
print(f"Exact Value (ln(2)): {ln2}")

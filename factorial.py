# Read input
n = int(input("Enter an integer: "))

# Calculate the factorial
i = 1
for j in range(1, n + 1):
    i *= j
   
# Display result
print(f'i = {i}')

# Calculator for mean, variance and standard deviation for population

# Entering number of values (N)
num_of_values = int(input("Enter how many values: "))

# Making list of all values
values = list()
i = 0
while i <= num_of_values:
    value = float(input("Enter your values: "))
    values.append(value)
    i += 1

# Calculation for mean
mean = sum(values)/num_of_values

# Making list of "(y - mean) square" values
var_values = list()
x = 0
for value in values:
    var = ((values[x]-mean)**2)
    var_values.append(var)
    x += 1

choice = int(input("Population(1) or sample(2)? 1/2? "))

# Population calculation
if choice == 1:
    variance = sum(var_values) * 1/num_of_values
    std_dev = variance ** 0.5

# Sample calculation
elif choice == 2:
    variance = sum(var_values) * 1 / (num_of_values-1)
    std_dev = variance ** 0.5

else:
    print("Please enter 1 or 2")
    quit()

print("Mean:", round(mean, 3))
print("Variance:", round(variance, 3))
print("Standard deviation:", round(std_dev, 3))

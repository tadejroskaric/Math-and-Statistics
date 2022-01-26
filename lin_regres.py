# Linear regression calculator

# Size of the sample
n = int(input("Sample size: "))

# Values of variable X (ind = individual value)
x = []
i = 0
while i < n:
    x_ind = float(input("Value of x: "))
    i += 1
    x.append(x_ind)

# Values of variable Y
y = []
i = 0
while i < n:
    y_ind = float(input("Value of y: "))
    i += 1
    y.append(y_ind)

# Mean values
x_mean = (sum(x)/n)
y_mean = (sum(y)/n)

# Sum of x squared
x_square = 0
for value in x:
    x_square += value**2

# Sum of y squared (used in coefficient of correlation formula)
y_square = 0
for value in y:
    y_square += value**2

# Sum of products of x and y values
i = 0
summ = 0
product = 0
while i < n:
    product = x[i] * y[i]
    summ += product
    i += 1

# Calculation of intercept (b0) and slope (b1)
b1 = round((summ - n * x_mean * y_mean)/(x_square - n * x_mean**2), 4)
b0 = round(y_mean - b1 * x_mean, 4)

# Plus or minus sign for slope(b1)
if b1 >= 0:
    sign = "+"
else:
    sign = "-"

# Regression function
print("y =", b0, sign, abs(b1), "x")

# Coefficient of correlation (r) and determination (r_square)
r = (summ - n * x_mean * y_mean)/(((x_square - n * x_mean**2)**0.5) * ((y_square - n * y_mean**2)**0.5))
r_square = r**2

print("r =", r)
print("r^2 =", r_square)
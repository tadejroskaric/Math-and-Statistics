from scipy import stats
import numpy as np

# Calculation for interval estimation of mean (t-test)

# Sample size
n = int(input("Size of the sample: "))
i = 0

# Input of values
values = []
while i < n:
    value = int(input("Enter an integer value: "))
    values.append(value)
    i += 1

# Converting values list to NumPy array
values = np.array(values)

# Calculation of parameters (ddof=1 because it is a sample, not population)
mean = values.mean()
std_dev = values.std(ddof=1)
mean_error = (std_dev / (n**0.5))

# Interval estimation of mean (confidence interval of 95%, n-1 = dof)
test = stats.t.interval(0.95, n-1, mean, mean_error)

# Output
print("P(", round(test[0], 2), "< ȳ <", round(test[1], 2), ")", "= 95%")

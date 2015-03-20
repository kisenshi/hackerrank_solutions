"""
Problem: Basic Statistics Warmup (/stat-warmup)
"""

import sys, math

n = 0 #Contains the N
n_numbers = [] #Contains the list of numbers

Z_95 = 1.96

"""
The input in this problem is conformed by two lines:

N [10, 2500] => Which is the numbers to take into consideration for the calculus
x1 x2 x3 .... xn => N integers (0, 105] separated by a space that will be used for the calculus
"""
def readInput():
    global n_numbers, numbers
    
    s = sys.stdin
    n_numbers = int(s.readline())
    numbers = map(int, s.readline().split())

    #It will be helpful to have the numbers sorted
    numbers.sort()

"""
For both the mean and mode is needed to iterate over all the numbers, so they will be calculted at the same time
"""
def obtainMeanAndMode():
    numbers_sum = 0
    mean = 0

    #As the list is ordered, after the first iteration the mode will contain the first number which will always be the mode in the case that there are multiple values with the same criteria
    mode = {"number" : 0, "occurs" : 0} 
    last_mode = {"number" : 0, "occurs" : 0}    
    for x in numbers:
        numbers_sum += x #For the mean

        if last_mode["number"] == x:
            #It is increased the number of occurs by 1
            last_mode["occurs"] += 1
        else:
            #It is checked if the last_mode should replace the mode saved until this moment
            if last_mode["occurs"] > mode["occurs"]:
                mode["number"] = last_mode["number"]
                mode["occurs"] = last_mode["occurs"]
             #It is considered now the current number as last_mode
            last_mode["number"] = x
            last_mode["occurs"] = 1

        #It is needed to check if the last_mode considered should replace the mode saved until this moment
        if last_mode["occurs"] > mode["occurs"]:
            mode["number"] = last_mode["number"]
            mode["occurs"] = last_mode["occurs"]

        #It is obtained the mean
        mean = float(numbers_sum) / float(n_numbers)

    return {"mean" : mean, "mode" : mode["number"]}

"""
Returns the median from the group of numbers 
It depends on the total number of elements considered as if it is an odd value, it will be returned the middle number of the list
However, if there is an even number of elements, it is necessary to obtain the mean of the two elements that are in the middle
"""
def obtainMedian():
    """ The median depends on if the n_number is odd or even """
    if n_numbers % 2 == 0:
        #It is even, so it will be obtained the mean of the two numbers in the middle
        middle_index = n_numbers / 2
        median = (numbers[middle_index - 1] + numbers[middle_index]) / 2.0
    else:
        middle_index = n_numbers // 2 #floor calculation
        median = numbers[middle_index]

    return {"median" : median}

"""
Returns the standard derivation, which depends on the value calculated for the means
"""
def obtainStandardDerivation(mean):
    """ First it is needed to obtain the value of sum of all the (xi - m)^2 """
    sum_result = 0
    for x in numbers:
        sum_result += pow((x - mean), 2)

    #It is obtained the standard derivation didivind the obtained sum by n_numbers and powed to 0.5
    standard_derivation = pow((sum_result / float(n_numbers)), 0.5)
    return {"standard_derivation" : standard_derivation}

"""
Returns the lower and upper boundary of the 0.95 Confidence Interval for the mean.
It is needed the value calculated for the mean and the standard_derivation
the formula is as follows:

lower_boundary = mean - Z.95 * standard_error_mean
upper_boundary = mean + Z.95 * standard_error_mean

The standard_error_mean is obtained as follows

standard_error_mean = standard_derivation / sqrt(n_numbers)

The Z.95 has a standard value of 1.96
"""
def obtainLowerAndUpperBoundary(mean, standard_derivation):
    standard_error_mean = standard_derivation / math.sqrt(n_numbers)

    lower_boundary = mean - Z_95 * standard_error_mean
    upper_boundary = mean + Z_95 * standard_error_mean

    return {"lower_boundary" : lower_boundary, "upper_boundary" : upper_boundary}

"""
Prints the results with the correct format requested in the problem
Five lines required:

Mean (format:0.0) on the first line
Median (format: 0.0) on the second line
Mode(s) (Numerically smallest Integer in case of multiple integers)
Standard Deviation (format:0.0) 
Lower and Upper Boundary of Confidence Interval (format: 0.0) with a space between them.
"""
def printResults(results):
    print "%.1f" % results["mean"]
    print "%.1f" % results["median"]
    print "%d" % results["mode"]
    print "%.1f" % results["standard_derivation"]
    print "%.1f %.1f" % (results["lower_boundary"], results["upper_boundary"])

"""
Executes the code to be able to obtain the calculation
"""
def main():
    readInput()

    """ The mean, median and mode can be calculated in an unique iteration as they don't depend on any other calculation """
    results = obtainMeanAndMode()
    results.update(obtainMedian())

    """ The SD depends on the mean so it is calculated using the obtained value """
    results.update(obtainStandardDerivation(results["mean"]))

    """ Lower and Upper Boundary of the 0.95 Confidence Interval for the mean uses the mean and the SD obtained """
    results.update(obtainLowerAndUpperBoundary(results["mean"], results["standard_derivation"]))

    printResults(results)

"""
Solution
"""

main()
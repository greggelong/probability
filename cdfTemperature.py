import scipy.stats as stats

## Checkpoint 1
'''
The weather in the Galapagos islands follows a Normal distribution with a
mean of 20 degrees Celcius and a standard deviation of 3 degrees.

Uncomment temp_prob_1 and set the variable to equal the probability that the weather
on a randomly selected day will be between 18 to 25 degrees Celcius using the norm.cdf() method. 

'''
temp_prob_1 = stats.norm.cdf(25, 20,3)- stats.norm.cdf(18,20,3)
print(temp_prob_1)

## Checkpoint 2

'''
Using the same information about the Galapagos Islands, uncomment temp_prob_2 and assign
the variable to equal the probability that the weather on a randomly
selected day will be greater than 24 degrees Celsius.


'''

temp_prob_2 = 1- stats.norm.cdf(24,20,3)
print(temp_prob_2)
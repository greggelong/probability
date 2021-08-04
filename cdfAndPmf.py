import scipy.stats as stats

## Checkpoint 1
'''
Uncomment and assign the variable prob_1 to the probability of observing 3 or fewer heads from 10 fair coin flips using the cumulative distribution function. Then print prob_1.
'''
prob_1 = stats.binom.cdf(3,10,0.5)
print(prob_1)

# compare to pmf code
print(stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5) + stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5))


## Checkpoint 2
'''
Uncomment prob_2 and assign the variable to be the probability of observing more than 5 heads from 10 fair coin flips. Then print prob_2.
'''
prob_2 = 1 - stats.binom.cdf(5,10,0.5)
print(prob_2)


## Checkpoint 3
'''
Assign the object prob_3 the probability of observing between 2 and 5 heads from 10 fair coin flips. Then print prob_3
'''
prob_3 = stats.binom.cdf(5, 10, 0.5) - stats.binom.cdf(1, 10, 0.5)
print(prob_3)

# compare to pmf code
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5) + stats.binom.pmf(5, n=10, p=.5))
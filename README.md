# probability
a place to hold some code in python for calculating probability  with sets




## adding mutually exclusive or non mutually exclusive events

P(A or B) = P(A)+P(B) - P(A and B)

for non M.E. events  P(A and B) is the intersection of A and B

Which you can do with the set data structure in Python

eg:

A = rolling an odd number on a die

B = rolling a number > two

so in python that is 

a = {1,3,5}

b = {3,4,5,6}

they are not mutually exclusive as there intersection len is greater >0

```python
>>> a.intersection(b)
{3, 5}
```


## conditional probability 

a nice use of python sets to demonstrate independent and non-independent conditional prob

at this video:  https://youtu.be/KJFcwlMV764

check comments in conditionalProb.py for explanation

## random
(from codecademy)
Discrete and Continuous Random Variables

Discrete Random Variables

Random variables with a countable number of possible values are called discrete random variables. For example, rolling a regular 6-sided die would be considered a discrete random variable because the outcome options are limited to the numbers on the die.

Discrete random variables are also common when observing counting events, such as how many people entered a store on a randomly selected day. In this case, the values are countable in that they are limited to whole numbers (you can’t observe half of a person).
Continuous Random Variables

When the possible values of a random variable are uncountable, it is called a continuous random variable. These are generally measurement variables and are uncountable because measurements can always be more precise – meters, centimeters, millimeters, etc.

For example, the temperature in Los Angeles on a randomly chosen day is a continuous random variable. We can always be more precise about the temperature by expanding to another decimal place (96 degrees, 96.44 degrees, 96.437 degrees, etc.).


## review probability functions

see file probReview.py

introduction to probability distributions! To review, we have:

    - Learned about different types of random variables
    - Calculated the probability of specific events using probability mass functions (discrete random variable)
    - Calculated the probability of ranges using probability mass functions and cumulative distribution functions (discrete random variable)
    - Calculated the probability of ranges using probability density functions and cumulative distribution functions (continuous random variable)


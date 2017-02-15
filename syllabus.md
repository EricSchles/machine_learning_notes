```
Part 1 - the shape of data
Chapter 1. Understanding the shape of data discretely - A first look at PGMs
    Introduction
    A quick overview of probability - some first definitions w/ coded examples
    An introduction to discrete random variables and discrete probability distributions 
        The Binomial distribution
            Definition - Mathematical description and visualization w/ code
            Testing for binomial - with code and some examples and how to discrete analysis
        An introduction to probabilistic graphical models / networks  
making use of the binomial random variable to build a binomial graphical model
Chapter 2. Understanding the shape of data continuous - A first look at linear regression
    An introduction to continuous random variables and continuous probability distributions
        A definition of continuity 
    The Normal distribution
        Definition - Mathematical description and visualization w/ code
Testing for normality - with code and some examples
An introduction to descriptive statistics  
Definition of central tendency with reference to mean and median and lots of examples
Definition of spread with references to variance and standard deviation
Finer definitions of spread with reference to skew, kurtosis and higher order measures of the moment generating function
An introduction to Linear Regression
    A first example
The Algorithm with pseudocode
An original implementation based on the pseudo code
Making use of the implementation with some examples
Making use of statsmodels linear regression model with LOTS of examples
Chapter 3. Comparing Gamma and normal random variables
The Gamma distribution
Definition - Mathematical description and visualization w/ code
Testing for gamma - with code and some examples     
Making Gamma useful 
The Chi-squared distribution
            Definition - Mathematical description and visualization w/ code
            Some examples and use cases     
The Exponential distribution
        Definition - Mathematical description and visualization w/ code
            Some examples and use cases
    Introduction to the gamma generalized linear model 
The Gamma GLM versus the classical linear regression
    
Chapter 4. An introduction to bayesian inference 
    Bayes theorem
    Bayesian networks
        Conditional probability
        Explanation of directed acyclic graph
    Comparing Bayesian PGM versus linear regression
    Introduction to Logistic regression
    Understanding the deep power of bayes theorem - naive bayes for text classification
        A digression into feature transformations for text
            Understanding feature transformations generally
            Specific feature transformations with text (I’m blanking on the names of these right now)
        Naive bayes for text classification
        Trying logistic regression with text classification
        Comparison of results
Summary of what we’ve done so far and some more practical examples
Chapter 5. What happens when your data doesn’t follow a distribution - Enter decision trees
Decision tree 
Definition and importance of it being a universal approximator
Looking at the pseudo code for a decision tree
How machine learning algorithms learn (or get trained)
Definition Entropy
    Introduction of fitness functions
Implementing the pseudo code piecemeal / using the pieces of the implementation to understand data
Making use of decision trees
    Numerical examples
    Text classification examples
Chapter 6. Looking at other non-linear approximators - Discussion of error functions (WIP)
    Introduction of K-nearest neighbors
Compare contrast kNN with linear regression error function  
    kNN as a regressor
    Think of some numerical examples to use here
    Think of some nlp examples to use here
Chapter 7. A deeper look at classification (WIP)
Decision trees, Logistic regression, kNN as classifiers
Introduction to Markov chains
Introduction to Markov networks
Think of some classification examples here
Compare naive bayes, decision trees, logistic regression and kNN for text classification
Summary of what we’ve done so far and how it inter-relates with what we did in part 1
Chapter 8.  Time series analysis chapter
    The Poisson distribution and poisson process
Definition - Mathematical description and visualization w/ code
A quick introduction to time series data and visualization w/ code
        Testing for poisson - with code     
Monte Carlo simulation
The AR process
The MA process
The ARIMA process
    The gaussian process - PGM for time series
        Paper that examples what I’m thinking for this section: http://digitalassets.lib.berkeley.edu/sdtr/ucb/text/650.pdf
    Of course, I’m going to water down the paper like crazy.  
    Compare and contrast ARIMA versus gaussian PGM
Chapter 9. More classification 
    Introduction to Support Vector Machines
    Comparing SVMs to other Logistic regression
    Comparing SVMs to Decision Trees
    Comparing SVMs to kNN
    Introduction to computer vision
    Facial recognition
    Image classification
    
Chapter 10. Ensemble Methods
    An introduction to random trees
An introduction to random forests
    Expanding to multiple models instead of just random forests
Chapter 11. Neural networks (WIP)
    Introduction to neural networks
    NNs versus logistic regression
    NNs versus SVM
    NNs for linear regression
    NNs for text processing
    NNs for image processing
Summary of what we’ve done so far and next steps
Chapter 12. Kaggle competitions (WIP)
    20 examples (maybe less)
Chapter 13. Data for good competitions (WIP)
Chapter 13. Operationalizing your code for work (WIP)
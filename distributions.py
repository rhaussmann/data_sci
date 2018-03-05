# http://bigdata-madesimple.com/how-to-implement-these-5-powerful-probability-distributions-in-python/
# https://www.johndcook.com/blog/distributions_scipy/
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def binomial_dist():
    # E(X) = np, Var(X) = np(1−p)
    n = 10
    p = 0.3
    k = np.arange(0, 21)
    binomial = stats.binom.pmf(k, n, p)
    print(binomial)
    plt.plot(k, binomial, 'o-')
    plt.title('Binomial: n=%i,p=%.2f' % (n, p), fontsize=15)
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability of Successes', fontsize=15)
    plt.show()


def binomial_rand():
    binom_sim = stats.binom.rvs(n=10, p=0.3, size=1000)
    print('Mean %g' % np.std(binom_sim, ddof=1))
    print('SD: %g' % np.std(binom_sim, ddof=1))
    plt.hist(binom_sim, bins=10, normed=True)  # normed
    plt.xlabel('x')
    plt.ylabel('density')
    plt.show()


def poisson():
    # E(X) = λ, Var(X) = λ
    rate = 2
    n = np.arange(0, 10)
    y = stats.poisson.pmf(n, rate)
    print(y)
    plt.plot(n, y, 'o-')
    plt.title('Poisson: $/lambda$ =%i' % rate)
    plt.xlabel('Number of Accidents')
    plt.ylabel('Probability of number of accidents')
    plt.show()


def poisson_rand():
    data = stats.poisson.rvs(mu=2, loc=0, size=1000)
    print('Mean: %g' % np.mean(data))
    print('SD: %g' % np.std(data, ddof=1))

    plt.figure()
    plt.hist(data, bins=9, normed=True)
    plt.xlim(0, 10)
    plt.xlabel('Number of accidents')
    plt.title('Simulating Poisson Random Variables')
    plt.show()


def normal():
    mu = 0
    sigma = 1

    x = np.arange(-5, 5, 0.1)
    y = stats.norm.pdf(x, 0, 1)

    plt.plot(x, y)
    plt.title('Normal: $\mu$=%.1f, $\sigma^2=%.1f' % (mu, sigma))
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.show()


def beta():
    a = 0.5
    b = 0.5
    x = np.arange(0.01, 1, 0.01)
    y = stats.beta.pdf(x, a, b)
    plt.plot(x, y)
    plt.title('Beta: a=%.1f, b=%.1f' % (a, b))
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.show()


def exponential():
    lambd = 0.5
    x = np.arange(0, 15, 0.1)
    y = lambd * np.exp(-lambd * x)  # could also use stats.expon.pdf
    plt.plot(x, y)
    plt.title('Exponential: $\lambda$ =%.2f' % lambd)
    plt.xlabel('x')
    plt.ylabel('Probability density')
    plt.show()


def exponential_rand():
    data = stats.expon.rvs(scale=2, size=1000)
    print('Mean: %g' % np.mean(data))
    print('SD: %g' % np.std(data, ddof=1))

    plt.figure()
    plt.hist(data, bins=20, normed=True)
    plt.xlim(0, 15)
    plt.title('Simulating Exponential Random Variables')
    plt.show()

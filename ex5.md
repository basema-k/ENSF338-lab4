# Exercise 5 

## Question 1: timeit vs repeat

When timing code, two things can mess up your measurements:

1. **Random noise** — the OS randomly interrupts your program to do other things, making some runs randomly slower than they should be.

2. **Warmup** — the first few runs of a function are sometimes slower because the CPU cache is cold. After a few runs it settles down.

**timeit.timeit(number=N)** runs the function N times in a row and returns the total time. Running many times in a row averages out random noise - a few slow runs get
diluted across hundreds of runs. This is best when the function is very fast, because a single run would be too short to measure accurately - for example, if a function takes 0.0001 seconds, and the OS randomly interrupts it for 0.0001 seconds, your measurement is now doubled.

**timeit.repeat(repeat=R, number=N)** runs that block R separate times and returns a list of R times. This lets you see how consistent the results are across independent
runs. This is best when you want to compare two implementations and need to understand how much the results vary.

---

## Question 2: Average, Min, or Max?

**For timeit.timeit() : use the average**

It returns one total time for N runs. You divide by N which gives average. That's the whole point of running it many times.

**For timeit.repeat() : use the min**

It returns a list of measurements. You should take the minimum because:

- Noise can only make a run *slower*, never faster.
- So the fastest run is the one with the least noise, and closest to the true runtime.
- The average gets dragged up by occasional slow outliers.
- The max is just the worst noise spike and not useful.
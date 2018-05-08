# J - Janky Python Utilities

*_Tread carefully: This is an abomination_*

## Purpose
Some language constructs are common enough in quick Python scripts that the code duplication is time-consuming and frustrating. Yeah, sure, _proper_ code does not have these problems, with abstract factories of token tokens or encapsulated™-reactive docstring-commented modules, but sometimes research code need not be _proper_ code, and if trying out dozens of experiments, researcher time is often way more valuable.

This library aims to provide a set of sketchy functions that cover common functionality in quick scripts. It is a work in progress and contributions are welcome. In a tragically misguided attempt to make expressive shortcuts, the Python language is abused beyond recognition. Inspiration came from looking at a plate of spaghetti and realizing it didn't have enough regular expressions in it.

Some examples that this library tries to solve:
 - Easier interface for maps and functional constructs, for times when finishing statements with `))))))` seems excessive. An easier parallelization interface makes you ever so slightly more likely to parallelize your code.
```python
from J import * # only exports single letter, uppercase symbols

(F(complicated_function)/4) @ range(100) # Parallelizes complicated_function over 4 CPUs and maps int over the list range(100)
(F(f1, f2)/0) @ range(100) # Computes [f1(f2(a)), f1(f2(b)), ...] using as many cores as possible (sorry)
```
 - Easier plotting library.
```python
# Interface still to be finalized, pending remembering how Python precedenc eworks

(P.xy(x, y) % "plot title" & P.xly(x, y) % "semilogy plot")

P.plot()

P.tex('figure.pdf') # Exports in nice LaTeX
```
 - Timing utilities.

## Status
### In progress
 - F: functions, silly maps, etc.
 - T: timing utilities

### To do
 - P: plotting utilities.
 - W: Joseph "I hear you like 2π and conflicting array indexing conventions" Fourier utilities.
 - X: dummy variable, e.g. aspirationally `(float@X.lstrip().rstrip().split(',')) @ open('file').readlines()` would be a CSV reader; this might not be actually possible, but in that spirit.

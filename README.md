# J - Janky Python Utilities

*_Tread carefully: This is an abomination. Also, it's nowhere close to complete, and doesn't have setup utilities yet._*

## Purpose
Some language constructs are common enough in quick Python scripts that the code duplication is time-consuming and frustrating. Yeah, sure, _proper_ code does not have these problems, with abstract factories of token tokens or encapsulated™-reactive docstring-commented modules, but sometimes research code need not be _proper_ code, and if trying out dozens of experiments, researcher time is often way more valuable.

This library aims to provide a set of sketchy functions that cover common functionality in quick scripts. It is a work in progress and contributions are welcome. In a tragically misguided attempt to make expressive shortcuts, the Python language is abused beyond recognition. Inspiration came from looking at a plate of spaghetti and realizing it didn't have enough regular expressions in it.

Some examples that this library tries to solve:
 - Easier interface for maps and functional constructs, for times when finishing statements with `))))))` seems excessive. An easier parallelization interface makes you ever so slightly more likely to parallelize your code.
```python
from jank import * # only exports single letter, uppercase symbols

F(float) @ ['3.14', '2.71'] # returns [3.14, 2.71]
F(fn)/4 @ range(100) # Parallelizes fn over 4 CPUs and maps it over the list range(100)
F(f1, f2)/0 @ [a, b, ...] # Returns [f1(f2(a)), f1(f2(b)), ...] using as many cores as possible (sorry)

# Not implemented yet
F(lambda x: x > 5) % [1, 7, 2, 6] # returns [7, 6]
F(X > 7 or X % 2 == 0) % lst # using X syntax, see below
# Some similarly dumb syntax for reduce and others
```
 - Easier plotting library.
```python
# Interface still to be finalized, pending remembering how Python precedence works,
# and more messed up notation that could be abused.

(P.xy(x, y) % "plot title" & P.xly(x, y) % "semilogy plot")
P.legend()
P.colors('rainbow')
P.plot()
P.tex('figure.pdf') # Exports in nice LaTeX

# -----

with P as fig1:
    fig1.xy(x, y)
with P as fig2:
    fig2.xy(x, y)
with P as fig3:
    fig3.xy(x, y)
with P as fig4:
    fig4.xy(x, y)

(fig1 | fig2) % (fig3 | fig4)
# Subplots that look like
# fig1  fig2
# fig3  fig4
```
 - Timing utilities.
```python
T(time.sleep, 0.314) # Prints "Took 314.35 ms"
T(time.sleep, 666) # Prints "Took 11 min 6 s"
v, t = T.vt(lambda x: x**4, 1024)
print(v) # Prints some big number
print(t) # Prints time spent in seconds
```

## Status
### In progress
 - F: functions, silly maps, etc.
 - T: timing utilities

### To do
 - P: plotting utilities that overload Python operations a little too much.
 - W: Joseph "I hear you like 2π and conflicting array indexing conventions" Fourier utilities.
 - X: dummy variable, e.g. aspirationally `(float@X.lstrip().rstrip().split(',')) @ open('file').readlines()` would be a CSV reader; this might not be actually possible, but in that spirit.

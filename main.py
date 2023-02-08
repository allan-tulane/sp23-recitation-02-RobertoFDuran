"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
    """Compute the value of the recurrence $W(n) = aW(n/b) + n

    Params:
    n......input integer
    a......branching factor of recursion tree
    b......input split factor

    Returns: the value of W(n).
    """
    if n > 1:
        return a * simple_work_calc(n//b, a, b) + n
    else:
        return n
    pass

def test_simple_work():
    """ done. """
    assert work_calc(10, 2, 2) == 2
    assert work_calc(20, 3, 2) == 3
    assert work_calc(30, 4, 2) == 1

def work_calc(n, a, b, f):
    """Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

    Params:
    n......input integer
    a......branching factor of recursion tree
    b......input split factor
    f......a function that takes an integer and returns 
           the work done at each node 

    Returns: the value of W(n).
    """
    if n > 1:
        return a * work_calc(n//b, a, b, f) + f(n)
    else:
        return 1
    pass

def span_calc(n, a, b, f):
    """Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

    Params:
    n......input integer
    a......branching factor of recursion tree
    b......input split factor
    f......a function that takes an integer and returns 
           the work done at each node 

    Returns: the value of W(n).
    """
    if n > 1:
        return span_calc(n//b, a, b, f) + f(n)
    else:
        return 1
    pass

def test_work():
    """ done. """
    assert work_calc(10, 2, 2,lambda n: 1) == 1
    assert work_calc(20, 1, 2, lambda n: n*n) == 2
    assert work_calc(30, 3, 2, lambda n: n) == 3

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
    """
    Compare the values of different recurrences for 
    given input sizes.

    Returns:
    A list of tuples of the form
    (n, work_fn1(n), work_fn2(n), ...)
    
    """
    result = []
    for n in sizes:
        # compute W(n) using current a, b, f
        result.append((
            n,
            work_fn1(n),
            work_fn2(n)
            ))
    return result

def print_results(results):
    """ done """
    print(tabulate.tabulate(results,
                            headers=['n', 'W_1', 'W_2'],
                            floatfmt=".3f",
                            tablefmt="github"))


def test_compare_work():
    # curry work_calc to create multiple work
    # functions taht can be passed to compare_work
    
    # create work_fn1
    # create work_fn2
    
    def work_fn1(n):
        def x(a):
            def y(b):
                def z(f):
                    return work_calc(n, a, b, f)
                return z
            return y
        return x
    
    def work_fn2(n):
        def x(a):
            def y(b):
                def z(f):
                    return work_calc(n, a, b, f)
                return z
            return y
        return x

    res = compare_work(work_fn1, work_fn2)
    print(res)

def test_compare_span():
    assert span_calc(10, 2, 2, lambda n: 1) == 4
    assert span_calc(20, 1, 2, lambda n: n*n) == 426
    assert span_calc(30, 3, 2, lambda n: n) == 28
    def span_fn1(n):
        def x(a):
            def y(b):
                def z(f):
                    return span_calc(n, a, b, f)
                return z
            return y
        return x
    
    def span_fn2(n):
        def x(a):
            def y(b):
                def z(f):
                    return span_calc(n, a, b, f)
                return z
            return y
        return x
    
    def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
        """
        Compare the values of different recurrences for 
        given input sizes.

        Returns:
        A list of tuples of the form
        (n, work_fn1(n), work_fn2(n), ...)
        
        """
        result = []
        for n in sizes:
            # compute W(n) using current a, b, f
            result.append((
                n,
                span_fn1(n),
                span_fn2(n)
                ))
        return result
    
    res = compare_span(span_fn1, span_fn2)
    print_results(res)
    

# CMPS 2200  Recitation 02

**Name (Team Member 1):**_________________________  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.


## Setup
- Make sure you have a Github account.
- Login to Github.
- Login to repl.it, using "sign in with github"
- Click on the assignment link sent through canvas and accept the assignment.
- Click on your personal github repository for the assignment.
- Click on the "Work in Repl.it" button. This will launch an instance of `repl.it` initialized with the code from your repository.
- You'll work with a partner to complete this recitation. To do so, we'll break you into Zoom rooms. You will be able to code together in the same `repl.it` instance. You can choose whose repl.it instance you will share. This person will click the "Share" button in their repl.it instance and email the lab partner.

## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest main.py` will run all tests
  + `pytest main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Version Control" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.
    - $f(n) = 1$: 
    - $W(n) = aW(n/b) + f(x)$
    - $W(n) = 2W(n/2) + 1$ 
    - $W(n) = 2W(n/2) + k$
    - $n * W(1) + (n-1)k$
    - $2nk - k$
    - $O(n)$
      - When $n = 8, a = 2, b = 2,$ and $f(x) = 1$ 
        - $W(n) = 15$
  - $f(n) = n$:
    - $W(n) = aW(n/b) + f(x)$
    - $W(n) = 2W(n/2) + n$
    - $n + 2 (n/2 + 2W(n/2^{2}))$
    - $n + 2n/2 + 2^{2}W(n/2^{2})$
    - $n + 2n + 2^{2}n + 2^{3}n...$
    - $O(n^{2})$
      - When $n = 8, a = 2, b = 2,$ and $f(x) = n$
        - $W(n) = 32$

  - $f(n) = n^{2}$: 
    - $W(n) = aW(n/b) + f(x)$
    - $W(n) = 2W(n/2) + n^{2}$
    - $log_{b}^{a} = log_{2}(2)$
    - $O(n^{2})$
      - When $n = 8, a = 2, b = 2,$ and $f(x) = n^{2}$ 
        - $W(n) = 30$

|     n |   W_1 |   W_2 |
|-------|-------|-------|
|    10 |     4 |    18 |
|    20 |     5 |    38 |
|    50 |     6 |    97 |
|   100 |     7 |   197 |
|  1000 |    10 |  1994 |
|  5000 |    13 |  9995 |
| 10000 |    14 | 19995 |
<br>

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

  - For c < log a W(n) grows slower than f(n)
  - For c > log a W(n) grows faster than f(n)
  - For c = log a W(n) grows at the same rate as f(n)

|     n |       W_1 |           W_2 |
|-------|-----------|---------------|
|    10 |       100 |          1000 |
|    20 |       400 |          8000 |
|    50 |      2500 |        125000 |
|   100 |     10000 |       1000000 |
|  1000 |   1000000 |    1000000000 |
|  5000 |  25000000 |  125000000000 |
| 10000 | 100000000 | 1000000000000 |

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

  - $f(n) = 1$
      - $W(n) = O(log^2 n)$
  - $f(n) = log n$
      - $W(n) = O(log n)$
  - $f(n) = n$
      - $W(n) = O(n)$

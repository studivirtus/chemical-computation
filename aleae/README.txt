Source code for the stochastic simulation program. It should compile with any C compiler. The command-line parameters are:
 
aleae <file1> <file2> <trials> <time> <verbosity>
 
where <file1>     contains the name, initial quantity and threshold
for each molecular type
<file2>     contains the reactants, products and rate constant for each reaction
<trials>    specifies how many trials to perform
<time>      specifies a time limit (this is if random time steps are taken -- set it to -1 to ignore time)
<verbosity> specifies how detailed the output should be; choose a number between 0 and 15, inclusive.

I've included two models, "test" and "lambda". Here's a sample of the output:
 
   > ./aleae test.in test.r 1000 -1 0                                                                                                                          
   Initial Quantities and Thresholds
   a 5 (> 6) b 5 (>= 7) c 5 (< 2)
 
   Reactions
     0: a 1 b 1 : a -1 b -1 c 3 : 1.0000 : 0 1 2
     1: a 1 c 1 : a -1 c -1 b 2 : 2.0000 : 0 1 2
     2: b 1 c 1 : b -1 c -1 a 1 : 3.0000 : 0 1 2
 
   simulation stats:
   avg [4.7540, 5.5510, 3.1920]
   a >  6: 318 (31.8000%)
   b >= 7: 611 (61.1000%)
   c <  2: 169 (16.9000%)
   avg   events/trial 4.6960
   avg   runtime      0.0.920
   total runtime      0.920.41
 
Starting from the state [a, b, c] = [5, 5, 5], 1000 trials are performed. The average ending quantities are [4.75, 5.55, 3.19]. Of the 1000 trials,
- 32% ended when a > 6
- 61% ended when b >= 7
- 17% ended when c < 2
(Note that these numbers do not add up to 100%; in some cases, two thresholds were crossed simultaneously.)
 
Hope that this makes sense.
 
Regards,
Marc

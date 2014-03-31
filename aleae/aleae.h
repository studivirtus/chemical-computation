// -----------------------------------------------------------------------------------------------------------------
// file           | aleae.h
// description    | main header file 
// project        | Probabilistic Analysis of Chemical Reactions (Bio Ludo Aleae)
// author(s)      | Marc Riedel 
// affiliation(s) | Electrical and Computer Engineering, University of Minnesota 
// created        | 2006/01/11
// modified       | 2006/01/11
// copyright      | University of Minnesota (c) 2006
// ----------------------------------------------------------------------------------------------------------------

#  ifndef __ALEAE_H
#  define __ALEAE_H

// ------------------------------------------------------------------------------------------------
// system includes

# include <cstdlib>
# include <cmath>
# include <sys/time.h>

# include <iostream>
# include <fstream>
# include <sstream>
# include <iomanip>
# include <iterator>
# include <utility>
# include <algorithm>

# include <queue>
# include <vector>
# include <map>
# include <set>
# include <list>
# include <stack>

using namespace std;
 
// ------------------------------------------------------------------------------------------------
// includes

# include "comb.h"

// ------------------------------------------------------------------------------------------------
// constants

# define MAXLINE 1024     // maximum length of a line in an input file

// ------------------------------------------------------------------------------------------------
// classes

// a chemical reaction
class react_t 
{
   // e.g., given react = [[1,  3], [6,  2]],
   //       the reactants are 3 molecules of type 1 and 2 of type 6
   // e.g., given delta = [[1, -3], [3,  2]],
   //       3 molecules of type 1 are consumed and 2 molecules of type 3 are produced in the reaction.

public:
   vector< pair<unsigned, unsigned> > react;  // types and quantities of reactants 
   vector< pair<unsigned, int     > > delta;  // types and change 
   vector< unsigned                 > depend; // reactions that depend on types modified by this one
   double                             rate;   // rate constant
};

// threshold codes
# define THRESH_LT 0
# define THRESH_LE 1
# define THRESH_GE 2
# define THRESH_GT 3

// a threshold (N.B. should generalize this to a discrete-valued function on the state)
class thresh_t 
{
public:
   unsigned i; // type
   unsigned t; // threshold
   unsigned c; // code 
};

// a set of chemical reactions and thresholds
class biocr_t 
{
public:
   vector<string>   N; // names
   vector<react_t>  R; // reactions
   vector<thresh_t> T; // thresholds
};

// ------------------------------------------------------------------------------------------------
// stoch

// bit-field for verbosity
# define PRINT_TRIALS     1   
# define PRINT_TERMINAL   2   
# define PRINT_TRACE      4 
# define PRINT_STATES     8 

// simulation parameters 
class stoch_param_t
{
public:
   double   time_lt;  // time limit
   unsigned print;    // bit-field (see above)
};

// output statistics
class stoch_stats_t
{
public:
   unsigned event_ct; // length of trajectory
   double   time;     // time of trajectory
        thresh_t F;        // thresholds
};

// ------------------------------------------------------------------------------------------------
// inline procedures

// ------------------------------------------------------------------------------------------------
// procedure declarations

bool                                         
aleae_initial_in(ifstream           &file,
                 vector  <string  > &N, 
                 vector  <unsigned> &S, 
                 vector  <thresh_t> &T);

bool                                         
aleae_reactions_in(      ifstream        &file, 
                         vector<react_t> &R,
                   const vector<string > &N);   
void
aleae_initial_out(const vector<string  > &N,
                  const vector<unsigned> &S,
                  const vector<thresh_t> &T);

ostream &operator<<(ostream &os, const vector<unsigned> &S);


void
aleae_reactions_out(const vector<string > &N,
                    const vector<react_t> &R); 

// ----------------------------------------------------------------------------------------------------------------

void
aleae_stoch(const biocr_t        biocr, 
            const stoch_param_t  param, 
                                 vector<unsigned> &S,     
                                 stoch_stats_t    &stats); 

// ------------------------------------------------------------------------------------------------

# endif // ndef __ALEAE_H

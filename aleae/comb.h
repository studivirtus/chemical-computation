// -----------------------------------------------------------------------------------------------------------------
// file           | comb.h
// description    | inlined combinatorial functions
// project        | generic
// author(s)      | Marc Riedel 
// affiliation(s) | Electrical Engineering, California Institute of Technology
// created        | 2005/08/18
// modified       | 2005/08/18
// copyright      | California Institute of Technology (c) 2005
// ----------------------------------------------------------------------------------------------------------------

#  ifndef __COMB_H
#  define __COMB_H
# include <assert.h>

// ------------------------------------------------------------------------------------------------
// includes

// ------------------------------------------------------------------------------------------------
// system includes

// ------------------------------------------------------------------------------------------------
// constants

// ------------------------------------------------------------------------------------------------
// classes

// ------------------------------------------------------------------------------------------------
// inline procedures

// generalized factorial
inline unsigned fact(unsigned n, unsigned m)
{
   assert(n >= m);
   if (m == 0) 
      return 1;
   else
      return n*fact(n-1, m-1);
}

// binomoial coefficient
inline unsigned choose(unsigned n, unsigned m)
{
   assert(n >= m);
   if (n < 2*m) {
      return fact(n, n-m)/fact(n-m, n-m);
   } else {
      return fact(n, m)/fact(m, m);
   }
}

// n^m (generally much more efficient than pow(n, m)
inline int raise(int n, unsigned m)
{
   int v = 1;
   for (unsigned i = 0; i < m; i++) v *= n;
   return v;
}
 
// ------------------------------------------------------------------------------------------------
// procedure declarations

                   
// ------------------------------------------------------------------------------------------------

# endif // ndef __COMB_H

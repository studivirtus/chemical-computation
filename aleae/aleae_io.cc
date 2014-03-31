// ----------------------------------------------------------------------------------------------------------------
// file           | aleae_io.cc
// procedure(s)   | aleae_state_in, aleae_reaction_in, aleae_reaction_out, operator<<(vector<unsigned))
// project        | Probabilistic Analysis of Chemical Reactions (Bio Ludo Aleae)
// author(s)      | Marc Riedel 
// affiliation(s) | Electrical and Computer Engineering, University of Minnesota 
// created        | 2006/01/11
// modified       | 2006/01/11
// copyright      | University of Minnesota (c) 2006
// ----------------------------------------------------------------------------------------------------------------

# include "aleae.h"

// ----------------------------------------------------------------------------------------------------------------
// description  | reads names, quantities and thresholds for molecular types from a file
// calls        | nothing
// called by    | main
// ----------------------------------------------------------------------------------------------------------------

bool                                       // true on success, false on error
aleae_initial_in(ifstream           &file, // input file
                 vector  <string  > &N,    // returns names 
                 vector  <unsigned> &S,    // returns quantities 
                 vector  <thresh_t> &T)    // returns thresholds 
{
   // Each line specifies the name, quantity and threshold for a molecular type
   // The format is
   //    <type> <quantity> <GE/N>
   // for instance
   //    a 5 GE 12
   // specifies type "a" with initial state 5, and a threshold greater than 12

   bool error = false;
   bool done  = false;
   set <string> M;

   while(!error && !done) {
      string tmp1;
      if (file >> tmp1) {
         if (!(M.find(tmp1) == M.end())) {
            cerr << "error: duplicate entry for " << tmp1 << endl;
            error = true;
         } else {

            // name
            N.push_back(tmp1);
            M.insert   (tmp1);

            unsigned tmp2;
            if (file >> tmp2) {

               // quantity
               S.push_back(tmp2); 

               string tmp3;
               if (file >> tmp3) {

                  thresh_t tmp4;
                  if (tmp3 == "LT") {
                     tmp4.c = THRESH_LT;
                  } else if (tmp3 == "LE") {
                     tmp4.c = THRESH_LE;
                  } else if (tmp3 == "GE") {
                     tmp4.c = THRESH_GE;
                  } else if (tmp3 == "GT") {
                     tmp4.c = THRESH_GT;
                  } else if (tmp3 != "N") {
                     error = true;
                  }

                  if (!error && tmp3 != "N") {
                     unsigned tmp5;
                     if (file >> tmp5) {

                        // threshold
                        tmp4.i = S.size() - 1;
                        tmp4.t = tmp5;
                        T.push_back(tmp4);

                     } else {
                        error = true;
                     }
                  } 
               }
            } else {
               error = true;
            }
         }
         if (error) cerr << "error reading entry " << tmp1 << endl;
      } else {
         done = true;
      }
   
   }
   return !error;
}

// ----------------------------------------------------------------------------------------------------------------
// description  | reads chemical reactions from a file
// calls        | nothing
// called by    | main
// ----------------------------------------------------------------------------------------------------------------

bool                                            // return true on success, false on error
aleae_reactions_in(ifstream              &file, // input file
                         vector<react_t> &R,    // reactions
                   const vector<string > &N)    // the names of the molecular types
{
   // Each line specifies a reaction. The format is
   //    <reactants> : <products> : <rate>
   // where the reactants and products are specified as
   //    <type> <quantity>
   // For example
   //    a 1 b 1 : c 2 : 0.5
   
   char text[MAXLINE];
   bool error = false;
   unsigned  count = 0;

   vector< vector<unsigned> > depend;
   
   // for each reaction
   while(!error && file.getline(text, MAXLINE)) {

      istringstream stream(text);
      react_t reaction;
      
      // reactants
      bool done  = false;
      while(!error && !done) {

         string tmp1;
         unsigned    tmp2;

         if (stream >> tmp1) {
            if (tmp1 == ":") {
               done  = true;
            } else {

               unsigned  index;
               bool found = false;

               for (unsigned i = 0; !found && i < N.size(); i++) {
                  if (N[i] == tmp1) {
                     found = true;
                     index = i;
                  }
               }
               if (!found) {
                  cerr << "error reading reaction " << count << ": molecular type " << tmp1 << " not found" << endl;
                  error = true;
               } else {
                  if (stream >> tmp2) {
                     pair<unsigned, unsigned> tmp3(index,  tmp2);
                     pair<unsigned, int>      tmp4(index, -tmp2);
                     reaction.react.push_back(tmp3);
                     reaction.delta.push_back(tmp4);
                  } else {
                     cerr << "error reading reaction " << count << endl;
                     error = true;
                  } 
               }
            }

         } else {
            cerr << "error reading reactant in reaction " << count << endl;
            error = true;
         }
      }
      
      // products
      done = false;
      while(!error && !done) {

         string   tmp1;
         unsigned tmp2;

         if (stream >> tmp1) {
            if (tmp1 == ":") {
               done  = true;
            } else {

               unsigned index1;
               bool found1 = false;

               for (unsigned i = 0; !found1 && i < N.size(); i++) {
                  if (N[i] == tmp1) {
                     found1 = true;
                     index1 = i;
                  }
               }
               if (!found1) {
                  cerr << "error reading product in reaction " << count << ": molecular type " << tmp1 << " not found" << endl;
                  error = true;
               } else {
                  if (stream >> tmp2) {

                     unsigned index2;
                     bool found2 = false;

                     for (unsigned i = 0; !found2 && i < reaction.react.size(); i++) {
                        if (reaction.react[i].first == index1) {
                           found2 = true;
                           index2 = i;
                        }
                     }
                     if (found2) {
                        pair<unsigned, int> &tmp3 = reaction.delta[index2];
                        tmp3.second += tmp2;
                     } else {
                        pair<unsigned, int> tmp3(index1, tmp2);
                        reaction.delta.push_back(tmp3);
                     }
                     count++;

                  } else {
                     cerr << "error reading product in reaction " << count << endl;
                     error = true;
                  } 
               }
            } 

         } else {
            cerr << "error reading product in reaction " << count << endl;
            error = true;
         }
      }
      
      // rate constant
      if (!error) {
         if (!(stream >> reaction.rate)) {
            cerr << "error reading rate in reaction " << count << endl;
            error = true;
         }
      }
      if (!error) {
         R.push_back(reaction);
      }
   }

   if (!error) {

      // ----------------------------------------------------------------------------------------------------------
      // setup dependencies

      // for each reaction
      for (unsigned i = 0; i < R.size(); i++) {

         // for each reactant
         for (unsigned j = 0; j < R[i].react.size(); j++) {

            // for each other reaction
            for (unsigned k = 0; k < R.size(); k++) {

               // for each product
               for (unsigned l = 0; l < R[k].delta.size(); l++) {

                  if (R[i].react[j].first == R[k].delta[l].first &&
                      R[k].delta[l].second != 0) {
                     R[k].depend.push_back(i);
                  }
               }
            }
         }
      }
      // remove redundancies
      for (unsigned i = 0; i < R.size(); i++) {
         sort(R[i].depend.begin(), R[i].depend.end());
         R[i].depend.erase(unique(R[i].depend.begin(), R[i].depend.end()), R[i].depend.end());
      }
   }

   return !error;
}

// ----------------------------------------------------------------------------------------------------------------
// description  | prints molecular types, initial quantities and thresholds 
// calls        | nothing
// called by    | main, aleae_stoch
// ----------------------------------------------------------------------------------------------------------------

void
aleae_initial_out(const vector<string  > &N, // names of molecular types
                  const vector<unsigned> &S, // state
                  const vector<thresh_t> &T) // thresholds 
{
   for (unsigned i = 0; i < N.size(); i++) {
      cout << N[i] << " " << S[i] << " ";
      for (unsigned j = 0; j < T.size(); j++) {
      if (T[j].i == i) {
         switch(T[i].c) {
           case THRESH_LT:
              cout << "(< ";
              break;
           case THRESH_LE:
              cout << "(<= ";
              break;
           case THRESH_GE:
              cout << "(>= ";
              break;
           case THRESH_GT:
              cout << "(> ";
              break;
           default:
              cout << "error: invalid thresshold code" << endl;
              exit(1);
            }   
           cout << T[j].t << ") ";
         }
      }
   }
   cout << endl;
}

// ----------------------------------------------------------------------------------------------------------------
// description  | prints a state
// calls        | nothing
// called by    | main, aleae_stoch
// ----------------------------------------------------------------------------------------------------------------

ostream &operator<<(ostream &os, const vector<unsigned> &S)
{
   os << "[";
   for (unsigned k = 0; k < S.size(); k++) {
      os << setw(2) << S[k];
      if (k < S.size() - 1) os << ", ";
   }
   cout << "]";
   return os;
}

// ----------------------------------------------------------------------------------------------------------------
// description  | prints reactions
// calls        | nothing
// called by    | main
// ----------------------------------------------------------------------------------------------------------------

void
aleae_reactions_out(const vector<string > &N, // names of molecular types
                    const vector<react_t> &R) // reactions
{
   for (unsigned i = 0; i < R.size(); i++) {
      cout << setw(3) << i << ": ";
      if (R[i].react.size() == 0) {
         cout << "*";
      } else {
         for (unsigned j = 0; j < R[i].react.size(); j++) {
            cout << N[R[i].react[j].first] << " ";
            cout << R[i].react[j].second   << " ";
         }
      }
      cout << ": ";
      for (unsigned j = 0; j < R[i].delta.size(); j++) {
         cout << N[R[i].delta[j].first] << " "
              << R[i].delta[j].second   << " ";
      }
      cout << ": " << R[i].rate << " : ";
      copy(R[i].depend.begin(), R[i].depend.end(), ostream_iterator<unsigned>(cout, " "));
      cout << endl;
   }
}


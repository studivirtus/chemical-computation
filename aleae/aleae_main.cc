// ----------------------------------------------------------------------------------------------------------------
// file           | aleae_main.cc
// procedure(s)   | main
// project        | Probabilistic Analysis of Chemical Reactions (Bio Ludo Aleae)
// author(s)      | Marc Riedel 
// affiliation(s) | Electrical and Computer Engineering, University of Minnesota 
// created        | 2006/01/11
// modified       | 2006/01/11
// copyright      | University of Minnesota (c) 2006
// ----------------------------------------------------------------------------------------------------------------

# include "aleae.h"

int main(int argc, char **argv) 
{
   // -------------------------------------------------------------------------------------------------------------
   // description  | Reads initial state and reactions from files. Launches analysis
   // calls        | aleae_initial_in, aleae_reactions_in, aleae_initial_out, aleae_reaction_out, 
   //              | aleae_stoch
   // called by    | command line
   // -------------------------------------------------------------------------------------------------------------

   if (argc < 6 || argc > 6) {
      cerr << "usage: " << argv[0] << " <file1: state> <file2: reactions> <trials> <time> <verbosity>" << endl;
      exit(1);
   } 

   ifstream file1(argv[1]);
   if (!file1) {
      cerr << "could not open file " << argv[1] << endl;
      exit(1);
   } 

   ifstream file2(argv[2]);
   if (!file2) {
      cerr << "could not open file " << argv[2] << endl;
      exit(1);
   } 

   // ---------------------------------------------------------------------------------------------
   // read names, initial state, thresholds and reactions
   // ---------------------------------------------------------------------------------------------
   
   vector<unsigned> S;     // initial state
   biocr_t          biocr;
   
   if (!aleae_initial_in(file1, biocr.N, S, biocr.T)) {
      cerr << "error reading initial state from file " << argv[1] << endl;
      exit(1);
   }

   if (!aleae_reactions_in(file2, biocr.R, biocr.N)) {
      cerr << "error reading reactions from file "     << argv[2] << endl;
      exit(1);
   }
   unsigned event_ct = 0;
   double   time     = 0;

   cout << setiosflags(ios::fixed) << setprecision(4);
   cout << "Initial Quantities and Thresholds" << endl;
   aleae_initial_out  (biocr.N, S, biocr.T);
   cout << endl;
   cout << "Reactions" << endl;
   aleae_reactions_out(biocr.N, biocr.R);
   cout << endl;
   struct timeval start1;
   gettimeofday(&start1, NULL);

   // ------------------------------------------------------------------------------------------
   // stochastic simulation
   // ------------------------------------------------------------------------------------------

   vector<thresh_t> &T = biocr.T;           // thresholds
   vector<string >  &N = biocr.N;           // names
   vector<unsigned> F(T.size());            // count of number of times that thresholds were exceeded
   unsigned         trials = atoi(argv[3]); // number of trials to perform

   stoch_stats_t stats;
   stoch_param_t param;
   param.time_lt = atof(argv[4]);
   param.print   = atoi(argv[5]);

   // for each trial
   vector<unsigned> A(S.size()); 
   for (unsigned n = 0; n < trials; n++) {
      
      if (param.print & PRINT_TRIALS) {
            cout << "trial " << n << endl;
      }
      struct timeval start2;
      gettimeofday(&start2, NULL);
            
      vector<unsigned> I = S;
      stats.event_ct     = 0;
      stats.time         = 0;
            
      // ---------------------------------------------------------------------------------------
      // generate a trajectory
      // ---------------------------------------------------------------------------------------
            
      aleae_stoch(biocr, param, I, stats);
            
      // collect statistics
      event_ct += stats.event_ct;
      time     += stats.time;
            
      for (unsigned i = 0; i < A.size(); i++) {
         A[i] += I[i];
      }
            
      if (param.print & PRINT_TRIALS) {
         cout << "trial stats:" << endl;
      }
      for (unsigned i = 0; i < T.size(); i++) {
         switch(T[i].c) {
         case THRESH_LT:
           if (I[T[i].i] < T[i].t) { 
             if (param.print & PRINT_TRIALS) cout <<  N[T[i].i] << " < " << T[i].t << endl;
             F[i]++;
           }
           break;
         case THRESH_LE:
           if (I[T[i].i] <= T[i].t) { 
             if (param.print & PRINT_TRIALS) cout <<  N[T[i].i] << " <= " << T[i].t << endl;
             F[i]++;
           }
           break;
         case THRESH_GE:
           if (I[T[i].i] >= T[i].t) { 
             if (param.print & PRINT_TRIALS) cout <<  N[T[i].i] << " >= " << T[i].t << endl;
             F[i]++;
           }
           break;
         case THRESH_GT:
           if (I[T[i].i] > T[i].t) { 
             if (param.print & PRINT_TRIALS) cout <<  N[T[i].i] << " > " << T[i].t << endl;
             F[i]++;
           }
           break;
         default:
           cout << "error: invalid threshold code" << endl;
           exit(1);
         }  
      }
      if (param.print & PRINT_TRIALS) {
         cout << "events  " << stats.event_ct  << endl;
         if (param.time_lt >= 0) {
            cout << "time    " << stats.time  << endl;
         }
         struct timeval end2;
         gettimeofday(&end2, NULL);
         unsigned micro2 = end2.tv_sec*1000000 + end2.tv_usec  - start2.tv_sec*1000000 + start2.tv_usec;
         cout << "runtime " << micro2/1000000 << "." << (micro2 % 1000000)/1000 << "." << ((micro2 % 1000000) % 1000) << endl;
         if (n < trials - 1) cout << endl;
      }
   }
         
   // ------------------------------------------------------------------------------------------
      
   cout << endl << "simulation stats:" << endl;
   cout << "avg ";
   cout << "[";
   for (unsigned i = 0; i < A.size(); i++) {
      cout << A[i]/(double)trials;
      if (i < A.size() - 1) cout << ", ";
   }
   cout << "]" << endl;
   for (unsigned i = 0; i < T.size(); i++) {
      cout <<  N[T[i].i];
      switch(T[i].c) {
      case THRESH_LT:
         cout << " <  ";
         break;
      case THRESH_LE:
         cout << " <= ";
         break;
      case THRESH_GE:
         cout << " >= ";
         break;
      case THRESH_GT:
         cout << " >  ";
         break;
      default:
         cout << "error: invalid threshold code" << endl;
         exit(1);
      }  
      cout  << T[i].t << ": " <<  F[i] << " (" << (F[i]/(double)trials)*100 << "%)" << endl;
   }
   struct timeval end1;
   gettimeofday(&end1, NULL);
   unsigned micro1 = end1.tv_sec*1000000 + end1.tv_usec  - start1.tv_sec*1000000 + start1.tv_usec;
   unsigned micro2 = micro1/trials;
   cout << "avg   events/trial " << event_ct/(double)trials << endl;
   if (param.time_lt >= 0) {
       cout << "avg   time/trial   " << time/(double)trials     << endl;
   }
   cout << "avg   runtime      " << micro2/1000000  << "." << (micro2 % 1000000)/1000 << "." << ((micro2 % 1000000) % 1000) << endl;
   cout << "total runtime      " << micro1/1000000 << "." << (micro1 % 1000000)/1000 << "." << ((micro1 % 1000000) % 1000) << endl;
}

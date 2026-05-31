prob_st=0.2

prob_st_pos=0.2*0.85
prob_nst_pos=0.8*0.02
prob_pos=prob_st_pos+prob_nst_pos

prob_pos_given_st=0.85

prob_results=(prob_pos_given_st*prob_st)/prob_pos

print("Probability of having strep throat given a positive test result is:",prob_results)
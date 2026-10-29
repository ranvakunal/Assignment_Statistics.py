#       SESSON 6 : HYPOTHESIS TESTING(BASICS)


#       TASK : 2


import scipy.stats as stats


mean_a, std_a, n_a = 350, 50, 30
mean_b, std_b, n_b = 320, 50, 30


t_stat, p_value = stats.ttest_ind_from_stats(
    mean1=mean_a, std1=std_a, nobs1=n_a,
    mean2=mean_b, std2=std_b, nobs2=n_b,
    equal_var=True
)

print(f"Calculated t-statistic: {t_stat:.4f}")
print(f"Calculated p-value: {p_value:.4f}")


alpha = 0.05
if p_value < alpha:
    print("Decision: Reject the null hypothesis (H0). The new home page has a statistically significant impact.")
else:
    print("Decision: Fail to reject the null hypothesis (H0). The difference is not statistically significant.")
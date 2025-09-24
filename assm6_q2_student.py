import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import norm

def confidence_interval(N_samples=40, sample_size=30, true_mean=78, confidence=0.95,confidence_level=0.95):
    """
    Demonstrates 95% confidence intervals for the mean.
    Parameters:
    - N_samples: Number of independent samples (here 40)
    - sample_size: Number of observations per sample
    - true_mean: True population mean
    - true_std: True population standard deviation
    - confidence: Confidence level (default 0.95)
    """
    true_var = 0.15 * true_mean
    true_std = np.sqrt(true_var)
    
    # WRITE_YOUR_CODE HERE TO COMPUTE THE Z VALUE
    # Z value for the two-tailed confidence interval
    alpha = 1 - confidence_level
    z = stats.norm.ppf(1 - alpha / 2)
    # this code block ends here

    # Store the lower and upper bounds of each CI
    ci_lowers = []
    ci_uppers = []
    
    # Track intervals that do NOT contain the true mean
    misses = 0
    
    # Generate samples and compute CIs
    for i in range(N_samples):
        sample = np.random.normal(loc=true_mean, scale=true_std, size=sample_size)

        # WRITE_YOUR_CODE HERE TO COMPUTE SAMPLE MEAN, SAMPLE STANDARD ERROR, AND CI BOUNDS
        sample_mean =np.mean(sample)
        sample_se = np.std(sample, ddof=1) / np.sqrt(sample_size)
        margin_of_error = z * sample_se
        
        lower = sample_mean - margin_of_error   
        upper = sample_mean + margin_of_error
        # this code block ends here

        # append to CI lists        
        ci_lowers.append(lower)
        ci_uppers.append(upper)
        
        # WRITE_YOUR_CODE HERE TO CHECK IF THE TRUE MEAN IS WITHIN THE CI, INCREMENT misses IF NOT
        if not (lower <= true_mean <= upper):
            misses += 1
        # this code block ends here
    
    # Plot the CIs
    plt.figure(figsize=(8, 6))
    for i, (low, up) in enumerate(zip(ci_lowers, ci_uppers)):

        # WRITE_YOUR_CODE HERE TO cOLOR THE INTERVALS THAT MISS THE TRUE MEAN IN RED, OTHERS IN BLUE
        color = 'blue' if low <= true_mean <= up else 'red'
        # this code block ends here

        plt.plot([low, up], [i, i], color=color, lw=2)
        plt.plot([np.mean([low, up])], [i], 'o', color=color)  # mark sample mean
    
    plt.axvline(true_mean, color='magenta', linestyle='-', label='True Mean', lw=3)
    plt.xlabel("Value")
    plt.ylabel("Sample #")
    plt.title(f"{confidence*100:.0f}% Confidence Intervals for Sample Means\nMissed intervals: {misses}/{N_samples}")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # WRITE_YOUR_CODE HERE TO PRINT THE NUMBER OF MISSES AND THE PERCENTAGE
    print(f"Out of {N_samples} intervals, {misses} did NOT contain the true mean.")
    print(f"This is roughly {(misses/N_samples)*100}%, close to the expected 5% for a 95% CI.")
    # this code block ends here

# ================================
# Run main if this script is executed
# ================================
if __name__ == "__main__":
    confidence_interval()

    plt.show() # do not comment this out
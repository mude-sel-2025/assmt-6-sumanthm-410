import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def confidence_interval(N_samples=100, sample_size=40, true_mean=78, confidence=0.95): 
    """
    Demonstrates confidence intervals for the mean.
    Parameters: ## CHANGED: Docstring updated to be accurate
    - N_samples: Number of independent samples to generate.
    - sample_size: Number of observations per sample.
    - true_mean: True population mean.
    - confidence: Confidence level for the interval.
    """
   
    true_var = 0.15 * true_mean
    true_std = np.sqrt(true_var)
    

    alpha = 1 - confidence 
    z = stats.norm.ppf(1 - alpha / 2)

    ci_lowers = []
    ci_uppers = []
    misses = 0
    
    for i in range(N_samples):
        sample = np.random.normal(loc=true_mean, scale=true_std, size=sample_size)

        sample_mean = np.mean(sample)
        sample_se = true_std / np.sqrt(sample_size) 
        margin_of_error = z * sample_se
        
        lower = sample_mean - margin_of_error   
        upper = sample_mean + margin_of_error

        ci_lowers.append(lower)
        ci_uppers.append(upper)
        
        if not (lower <= true_mean <= upper):
            misses += 1
    
    # Plot the CIs
    plt.figure(figsize=(8, 6))
    for i, (low, up) in enumerate(zip(ci_lowers, ci_uppers)):
        color = 'blue' if low <= true_mean <= up else 'red'
        plt.plot([low, up], [i, i], color=color, lw=2)
        plt.plot(np.mean([low, up]), i, 'o', color=color) # mark sample mean
    
    plt.axvline(true_mean, color='magenta', linestyle='-', label=f'True Mean ({true_mean})', lw=3)
    plt.xlabel("Value")
    plt.ylabel("Sample #")
    plt.title(f"{confidence*100:.0f}% Confidence Intervals for the Mean\nMissed Intervals: {misses}/{N_samples}")
    plt.legend()
    plt.grid(axis='x', linestyle=':')
    plt.show()
    
    print(f"Out of {N_samples} intervals, {misses} did NOT contain the true mean.")
    print(f"This is roughly {misses/N_samples*100:.1f}%, close to the expected {alpha*100:.1f}%.")

# ================================
# Run main if this script is executed
# ================================
if __name__ == "__main__":
    confidence_interval()
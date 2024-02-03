import random
import matplotlib.pyplot as plt

def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def monte_carlo_simulation(num_trials):
    outcomes = {i: 0 for i in range(2, 13)}

    for _ in range(num_trials):
        total = roll_two_dice()
        outcomes[total] += 1

    probabilities = {key: value / num_trials * 100 for key, value in outcomes.items()}
    return probabilities

def plot_probabilities(analytical_probabilities, monte_carlo_probabilities):
    plt.bar(analytical_probabilities.keys(), analytical_probabilities.values(), label="Analytical", alpha=0.5)
    plt.bar(monte_carlo_probabilities.keys(), monte_carlo_probabilities.values(), label="Monte Carlo", alpha=0.5)
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability (%)')
    plt.title('Comparison of Analytical and Monte Carlo Probabilities')
    plt.legend()
    plt.show()

def main():
    num_trials = 100000
    analytical_probabilities = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67, 
                                8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78}

    monte_carlo_probabilities = monte_carlo_simulation(num_trials)

    print("Analytical Probabilities:")
    for key, value in analytical_probabilities.items():
        print(f"Sum = {key}, Probability = {value}%")

    print("\nMonte Carlo Probabilities:")
    for key, value in monte_carlo_probabilities.items():
        print(f"Sum = {key}, Probability = {value:.2f}%")

    plot_probabilities(analytical_probabilities, monte_carlo_probabilities)

if __name__ == "__main__":
    main()

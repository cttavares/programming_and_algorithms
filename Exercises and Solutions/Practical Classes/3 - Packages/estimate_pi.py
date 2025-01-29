import random

def monte_carlo_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(-1, 1)  # Randomly generate x-coordinate
        y = random.uniform(-1, 1)  # Randomly generate y-coordinate
        
        distance_to_origin = x**2 + y**2
        if distance_to_origin <= 1:
            inside_circle += 1

    return 4 * inside_circle / num_samples

num_samples = 100000
estimated_pi = monte_carlo_pi(num_samples)
print(f"Estimated value of π after {num_samples} samples: {estimated_pi}")

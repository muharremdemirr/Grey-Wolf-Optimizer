import random
import math

class GWO:
    def __init__(self, objective_function, num_dimensions, num_wolves=5, max_iter=1000):
        self.objective_function = objective_function
        self.num_dimensions = num_dimensions
        self.num_wolves = num_wolves
        self.max_iter = max_iter

    def optimize(self):
        # Kurtların pozisyonlarını rastgele olarak başlat
        wolves_positions = [[random.uniform(-10, 10) for _ in range(self.num_dimensions)] for _ in range(self.num_wolves)]

        # Alpha, beta ve delta pozisyonlarını başlat
        alpha_position = [0] * self.num_dimensions
        beta_position = [0] * self.num_dimensions
        delta_position = [0] * self.num_dimensions

        # Alpha, beta ve delta uygunluklarını başlat
        alpha_fitness = float('inf')
        beta_fitness = float('inf')
        delta_fitness = float('inf')

        for iteration in range(self.max_iter):
            for i in range(self.num_wolves):
                fitness = self.objective_function(wolves_positions[i])

                if fitness < alpha_fitness:
                    alpha_fitness = fitness
                    alpha_position = wolves_positions[i].copy()
                    print("Alpha position:", alpha_position, "Fitness Alpha:", alpha_fitness)

                elif fitness < beta_fitness:
                    beta_fitness = fitness
                    beta_position = wolves_positions[i].copy()
                    print("Beta position:", beta_position, "Fitness Beta:", beta_fitness)

                elif fitness < delta_fitness:
                    delta_fitness = fitness
                    delta_position = wolves_positions[i].copy()
                    print("Delta position:", delta_position, "Fitness Delta:", delta_fitness)

            a = 2 - 2 * iteration / self.max_iter  # a linearly decreases from 2 to 0

            for i in range(self.num_wolves):
                A1 = [2 * a * random.random() - a for _ in range(self.num_dimensions)]
                C1 = [2 * random.random() for _ in range(self.num_dimensions)]
                D_alpha = [abs(C1[j] * alpha_position[j] - wolves_positions[i][j]) for j in range(self.num_dimensions)]
                X1 = [alpha_position[j] - A1[j] * D_alpha[j] for j in range(self.num_dimensions)]

                A2 = [2 * a * random.random() - a for _ in range(self.num_dimensions)]
                C2 = [2 * random.random() for _ in range(self.num_dimensions)]
                D_beta = [abs(C2[j] * beta_position[j] - wolves_positions[i][j]) for j in range(self.num_dimensions)]
                X2 = [beta_position[j] - A2[j] * D_beta[j] for j in range(self.num_dimensions)]

                A3 = [2 * a * random.random() - a for _ in range(self.num_dimensions)]
                C3 = [2 * random.random() for _ in range(self.num_dimensions)]
                D_delta = [abs(C3[j] * delta_position[j] - wolves_positions[i][j]) for j in range(self.num_dimensions)]
                X3 = [delta_position[j] - A3[j] * D_delta[j] for j in range(self.num_dimensions)]

                wolves_positions[i] = [(X1[j] + X2[j] + X3[j]) / 3 for j in range(self.num_dimensions)]

        return alpha_position, alpha_fitness


# Example usage:
def sphere_function(x):
    Enemy1 = [10, 15]
    Enemy2 = [20, 15]
    Enemy3 = [18, 5]

    coordinates = [[random.randint(0, 50) for _ in range(2)] for _ in range(5)]

    total = 0

    for i in range(len(coordinates)):
        total += math.sqrt((coordinates[i][0] - Enemy1[0]) ** 2 + (coordinates[i][1] - Enemy1[1]) ** 2)
        total += math.sqrt((coordinates[i][0] - Enemy2[0]) ** 2 + (coordinates[i][1] - Enemy2[1]) ** 2)
        total += math.sqrt((coordinates[i][0] - Enemy3[0]) ** 2 + (coordinates[i][1] - Enemy3[1]) ** 2)

    print("E1: (10, 15), E2: (20, 15), E3: (18, 5)")
    for i in range(5):
        print(f"Wolf {i+1}:", coordinates[i])
    print("Fitness:", total)
    print(" ")
    print(" ")

    return total

gwo = GWO(sphere_function, num_dimensions=5)
best_position, best_fitness = gwo.optimize()
print("En iyi pozisyon:", best_position)
print("En iyi uygunluk:", best_fitness)

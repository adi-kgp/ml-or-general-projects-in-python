# leibniz approach
# import math

# def leibniz(n_terms):
#     pi_approx = 0
#     for k in range(n_terms):
#         pi_approx += (-1)**k / (2*k + 1)
#     return 4 * pi_approx

# n_terms = 100000

# print(leibniz(n_terms))
# print(4 * math.atan(1))
# print(math.pi)

# approach two
# import random 
# import math

# def monte_carlo_pi(n_points):
#     inside_circle = 0

#     for _ in range(n_points):
#         x, y = random.uniform(-1, 1), random.uniform(-1, 1)
#         if x ** 2 + y**2 <= 1:
#             inside_circle += 1

#     return 4 * inside_circle / n_points

# n_points = 1000000
# print(monte_carlo_pi(n_points))
# print(math.pi)

# Third Approach

# BUFFON's Needle
import math
import random

num_throws = 100000
line_spacing = 1
needle_length = 1

crosses = 0

for _ in range(num_throws):
    endpoint = random.uniform(0, line_spacing)
    angle_ = random.uniform(0, 180)

    angle_in_radians = math.radians(angle_)

    projection = needle_length * math.sin(angle_in_radians)

    if endpoint + projection > line_spacing:
        crosses += 1

print(2 * num_throws / crosses)
print(math.pi)


# J - JIT : Just In Time Compilation
# A - Automatic Differentiation
# X - XLA (Accelerated Linear Algebra)


# JAX as NumPy
import jax
import jax.numpy as jnp
import numpy as np

a = jnp.array([1, 2, 3])
b = jnp.array([4, 5, 6])

# print(a+b)
# print(jnp.sqrt(a))
# print(jnp.mean(a))
# print(a.reshape(-1, 1))


# JIT Compilation
import time

@jax.jit
def myfunction(x):
    return jnp.where(x % 2 == 0, x/2, 3*x + 1)  # Collatz

arr = jnp.arange(10)

_ = myfunction(arr) # warm up

start = time.perf_counter()
myfunction(arr).block_until_ready()
end = time.perf_counter()
# print(end-start)

# print(jax.make_jaxpr(myfunction)(arr))


# Automatic Differentiation
# def square(x):
#     return x**2

# value=10.0
# print(square(value))
# print(jax.grad(square)(value))
# print(jax.grad(jax.grad(square))(value))
# print(jax.grad(jax.grad(jax.grad(square)))(value))

def f(x, y, z):
    return x ** 2 + 2 * y ** 2 + 3 *z **2

x, y, z = 2.0, 2.0, 2.0

# x ^ 2 + 2y^2 + 3z^2
# df/dx = 2x = 4
# df/dy = 4x = 8
# df/dz = 6x = 12

print(f(x, y, z))
print(jax.grad(f, argnums=0)(x, y, z)) # partial derivative for x
print(jax.grad(f, argnums=1)(x, y, z)) # partial derivative for y
print(jax.grad(f, argnums=2)(x, y, z)) # partial derivative for z

# Similar example to above
def f(arr):
    return arr[0] ** 2 + 2 * arr[1] ** 2 + 3 *arr[2] **2

x, y, z = 2.0, 2.0, 2.0

# x ^ 2 + 2y^2 + 3z^2
# df/dx = 2x = 4
# df/dy = 4x = 8
# df/dz = 6x = 12

print(f([x, y, z]))
print(jax.grad(f)([x, y, z]))


# Automatic Vectorization

key = jax.random.key(42)

W = jax.random.normal(key, (150, 100)) # 100 values for input sample, 150 neurons in next layer
X = jax.random.normal(key, (10, 100))

def calculate_output(x):
    return jnp.dot(W, x)

def batched_calculation_loop(X):
    return jnp.stack([calculate_output(x) for x in X])

def batched_calculation_manual(X):
    return jnp.dot(X, W.T)

batched_calculation_vmap = jax.vmap(calculate_output)

start = time.perf_counter()
batched_calculation_loop(X)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
batched_calculation_manual(X)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
batched_calculation_vmap(X)
end = time.perf_counter()
print(end - start)

np.testing.assert_allclose(batched_calculation_loop(X), batched_calculation_manual(X), atol=1E-4, rtol=1E-4)
np.testing.assert_allclose(batched_calculation_manual(X), batched_calculation_vmap(X), atol=1E-4, rtol=1E-4)


# Randomness

key = jax.random.key(42)
keys = jax.random.split(key, 10)
print(keys)


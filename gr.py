import sympy
from einsteinpy.symbolic import MetricTensor, EinsteinTensor

# Define the symbols
t, r, theta, phi, M, Q = sympy.symbols('t r theta phi M Q')

# Define the Reissner-Nordström metric components
g_tt = -1 + 2 * M / r - Q**2 / r**2
g_rr = 1 / (1 - 2 * M / r + Q**2 / r**2)
g_theta_theta = r**2
g_phi_phi = (r * sympy.sin(theta))**2

# Create a MetricTensor object
metric_matrix = sympy.Matrix([
    [g_tt, 0, 0, 0],
    [0, g_rr, 0, 0],
    [0, 0, g_theta_theta, 0],
    [0, 0, 0, g_phi_phi]
])

# Convert the matrix to a multi-dimensional list
metric_components = metric_matrix.tolist()

# Create a MetricTensor object
metric = MetricTensor(metric_components, [t, r, theta, phi])

# Use EinsteinTensor to directly calculate the Einstein tensor from the metric
einstein_tensor = EinsteinTensor.from_metric(metric)

# Display the components of the Einstein tensor
print("Einstein Tensor Components:")
for i in range(4):
    for j in range(4):
        print(f'G_{i}{j} = {einstein_tensor[i, j].simplify()}')

import torch
import torch.nn as nn

# Define the parameters
v = 1.0 # kinematic viscosity
rho = 1.0 # density of the fluid
omega = 1.0 # frequency of the pressure gradient
L = 1.0 # length of the blood vessel
R = 1.0 # radius of the blood vessel

# Define the initial and boundary conditions
u_z0 = 0.0 # initial condition for u_z
delta_p = 1.0 # change in pressure

# Define the PDE as a neural network
class PDE_Model(nn.Module):
    def __init__(self):
        super(PDE_Model, self).__init__()
        self.fc1 = nn.Linear(2, 50)
        self.fc2 = nn.Linear(50, 50)
        self.fc3 = nn.Linear(50, 1)
    
    def forward(self, t, r):
        inputs = torch.cat((t, r), 1)
        x = torch.sin(self.fc1(inputs))
        x = torch.sin(self.fc2(x))
        x = self.fc3(x)
        return x

# Instantiate the model
model = PDE_Model()

# Define the loss function
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Train the model
for epoch in range(1000):
    # Generate the grid points for t and r
    t = torch.linspace(0, 1, 100).reshape(-1, 1)
    r = torch.linspace(0, R, 100).reshape(-1, 1)
    
    # Forward pass
    u_z = model(t, r)
    u_z_prime = torch.autograd.grad(u_z, r, grad_outputs=torch.ones_like(u_z), create_graph=True)[0]
    p = -delta_p * L / omega * torch.cos(omega * t)
    loss = criterion(v * rho / r * u_z_prime - p, torch.zeros_like(u_z))
    
    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 100 == 0:
        print("Epoch [{}/1000], Loss: {:.4f}".format(epoch + 1, loss.item()))















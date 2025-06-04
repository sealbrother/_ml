import torch
import torch.nn as nn
import matplotlib.pyplot as plt

torch.manual_seed(0)  

X = torch.linspace(0, 10, 100).unsqueeze(1) 
y = 2 * X + 3 + 0.5 * torch.randn_like(X)    

model = nn.Linear(in_features=1, out_features=1)

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

num_epochs = 1000
for epoch in range(num_epochs):
    pred = model(X)
    loss = criterion(pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

w, b = model.parameters()
print(f"Learned weight: {w.item():.4f}, bias: {b.item():.4f}")

plt.scatter(X.numpy(), y.numpy(), label='Data')
plt.plot(X.numpy(), pred.detach().numpy(), color='red', label='Fitted Line')
plt.legend()
plt.title("Linear Regression with PyTorch")
plt.show()
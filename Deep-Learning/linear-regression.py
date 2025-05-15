


import torch
import torch.nn as nn

from my_d2l import my_d2l
from torch.utils import data

net = nn.Linear(2, 1)
net.weight.data.normal_(0, 0.01)
net.bias.data.fill_(0)
loss = nn.MSELoss()
trainer = torch.optim.SGD(net.parameters(), lr=0.03)

def load_array(data_array, batch_size, is_train=True):
    dataset = data.TensorDataset(*data_array)
    return data.DataLoader(dataset, batch_size, shuffle=is_train)

true_w = torch.tensor([2, -3.4])
true_b = 4.2
features, labels = my_d2l.synthetic_data(true_w, true_b, 1000)

batch_size = 10
data_iter = load_array((features, labels), batch_size)

num_epochs = 3

for epoch in range(num_epochs):
    for x, y in data_iter:
        l = loss(net(x), y)

        trainer.zero_grad()
        l.backward()
        trainer.step()
    l = loss(net(features), labels)
    print(f"epoch {epoch + 1}, loss {l:f}")


import torch
from torch import nn
from d2l import torch as d2l
import chris_package

net = nn.Sequential(
        nn.Conv2d(1, 6, kernel_size=5, padding=2), 
        nn.Sigmoid(),
        nn.AvgPool2d(kernel_size=2, stride=2),
        nn.Conv2d(6, 16, kernel_size=5), 
        nn.Sigmoid(),
        nn.AvgPool2d(kernel_size=2, stride=2),
        nn.Flatten(),
        nn.Linear(16*5*5, 120), 
        nn.Sigmoid(),
        nn.Linear(120, 84), 
        nn.Sigmoid(),
        nn.Linear(84, 10)
)

batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size=batch_size)

def init_weights(m):
    if type(m) == nn.Linear or type(m) == nn.Conv2d:
        nn.init.xavier_uniform_(m.weight)
net.apply(init_weights)

loss=nn.CrossEntropyLoss
trainer=torch.optim.SGD(net.parameters(),lr=0.3)
epoch=10

train_loss=chris_package.train_model(net,train_iter,loss,epoch,trainer)
print(train_loss)
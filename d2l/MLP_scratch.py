# 导入模块
import torch
import matplotlib.pyplot as plt
from torch import nn
from d2l import torch as d2l
import chris_package

# 加载数据集
batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

# 初始化模型参数
num_inputs, num_outputs, num_hiddens = 784, 10, 256

W1 = nn.Parameter(torch.randn(num_inputs, num_hiddens, requires_grad=True) * 0.01)
b1 = nn.Parameter(torch.zeros(num_hiddens, requires_grad=True))
W2 = nn.Parameter(torch.randn(num_hiddens, num_outputs, requires_grad=True) * 0.01)
b2 = nn.Parameter(torch.zeros(num_outputs, requires_grad=True))

params = [W1, b1, W2, b2]

# 定义激活函数和模型
def relu(X):
    a = torch.zeros_like(X)
    return torch.max(X, a)

def net(X):
    X = X.reshape((-1, num_inputs))
    H = relu(X@W1 + b1)  # 这里“@”代表矩阵乘法
    return (H@W2 + b2)

# 损失函数
loss = nn.CrossEntropyLoss(reduction='none')

# 训练模型
num_epochs, lr = 10, 0.1
trainer = torch.optim.SGD(params, lr=lr)
train_loss=chris_package.train_model(net,train_iter,loss,num_epochs,trainer)
print(train_loss)
# 导入模块
import torch
from torch import nn
from d2l import torch as d2l
import chris_package

# 定义模型
net = nn.Sequential(nn.Flatten(),
                    nn.Linear(784, 256),
                    nn.ReLU(),
                    nn.Linear(256, 10))

def init_weights(m):
    if type(m) == nn.Linear:
        nn.init.normal_(m.weight, std=0.01)
net.apply(init_weights)

# 工具配置
batch_size, lr, num_epochs = 256, 0.1, 10
loss = nn.CrossEntropyLoss(reduction='none')
trainer = torch.optim.SGD(net.parameters(), lr=lr)

# 数据加载
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

# 训练
train_loss=chris_package.train_model(net, train_iter, loss, num_epochs, trainer)
print(train_loss)
import torch
from torch import nn
from d2l import torch as d2l

# 学习卷积核
def corr2d(X, K):
    h, w = K.shape
    Y = torch.zeros((X.shape[0] - h + 1, X.shape[1] - w + 1))
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            Y[i, j] = (X[i:i + h, j:j + w] * K).sum()
    return Y

X=torch.ones((6,8))
X[:,2:6]=0
K=torch.tensor([[1.0,-1.0]])
Y=corr2d(X,K)
print(Y)

conv=nn.Conv2d(1,1,kernel_size=[1,2],bias=False)
#conv2d = nn.Conv2d(1, 1, kernel_size=(3, 5), padding=(0, 1), stride=(3, 4))
X=X.reshape((1,1,6,8))
Y=Y.reshape((1,1,6,7))
lr=3e-2 #用的科学计数法，=0.03

for i in range(10):
    Y_hat=conv(X)
    l=(Y-Y_hat)**2
    conv.zero_grad()
    l.sum().backward()
    conv.weight.data[:]-=lr*conv.weight.grad
    print(f'epoch={i+1},loss={l.sum()}')

print(conv.weight.data)


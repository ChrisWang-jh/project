#导入模块
import torch
from torch.utils import data
from d2l import torch as d2l

#生成数据集
true_w=torch.tensor([2,-3.4])
true_b=4.2
features,labels=d2l.synthetic_data(true_w,true_b,1000)

#读取数据集
def load_array(data_array,batch_size,is_train=True):
    dataset=data.TensorDataset(*data_array)
    return data.DataLoader(dataset,batch_size,shuffle=is_train)
batch_size=10
data_iter=load_array([features,labels],batch_size)
#print(next(iter(data_iter)))

#定义模型
from torch import nn
net=nn.Sequential(nn.Linear(2,1))

#初始化参数
net[0].weight.data.normal_(0,0.01)
net[0].bias.data.fill_(0)

#定义损失函数
loss=nn.MSELoss()

#定义优化算法
trainer=torch.optim.SGD(net.parameters(),lr=0.03)

#训练
epoch=3
for i in range(epoch):
    for X,y in data_iter:
        l=loss(net(X),y)
        trainer.zero_grad()
        l.backward()
        trainer.step()
    l=loss(net(features),labels)
    print(f'epoch={i+1},loss={l}')

#参数比对
print(true_w-net[0].weight.data)
print(true_b-net[0].bias.data)
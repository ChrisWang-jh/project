#对fashion数据集实现dropout，并测试模型准确度

#导入模块
import torch
from torch import nn
from d2l import torch as d2l
import chris_package
#导入数据
batch_size=256
train_iter,test_iter=d2l.load_data_fashion_mnist(batch_size)
#定义模型&参数初始化
dropout1=0.2
dropout2=0.2
net=nn.Sequential(nn.Flatten(),
                nn.Linear(28*28,256),
                nn.ReLU(),
                nn.Dropout(dropout1),
                nn.Linear(256,256),
                nn.ReLU(),
                nn.Dropout(dropout2),
                nn.Linear(256,10)
                )
def initial_net(n):
    if type(n)==nn.Linear:
        nn.init.normal_(n.weight,std=0.01)
net.apply(initial_net)
#损失函数
loss=nn.CrossEntropyLoss(reduction='none')
#训练器
trainer=torch.optim.SGD(net.parameters(),lr=0.1)
#训练
epochs=10
train_loss=chris_package.train_model(net,train_iter,loss,epochs,trainer)
print(train_loss)
print('-'*20)
#测试
accurate_rate,average_loss=chris_package.test_model(net,test_iter,loss)
print(accurate_rate,'\n',average_loss)
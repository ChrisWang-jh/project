#导入模块
import torch
from torch import nn
from d2l import torch as d2l
import chris_package
#导入数据
batch_size=256
data_iter,test_iter=d2l.load_data_fashion_mnist(batch_size)
#建立模型&初始化参数
net=nn.Sequential(nn.Flatten(),
                nn.Linear(28*28,256),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(256,256),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(256,10))
def initial_net(n):
    if type(n)==nn.Linear:
        nn.init.normal_(n.weight,std=0.01)
net.apply(initial_net)
#损失函数
loss=nn.CrossEntropyLoss(reduction='none')
#训练器
trainer=torch.optim.SGD(net.parameters(),lr=0.15)
#训练
epoch=10
trainning_loss=chris_package.train_model(net,data_iter,loss,epoch,trainer)
print(trainning_loss)
print('-'*20)
#测试
accuracy_rate,average_loss=chris_package.test_model(net,test_iter,loss)
print(accuracy_rate,'\n',average_loss)
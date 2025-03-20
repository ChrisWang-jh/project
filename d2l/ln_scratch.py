import random
import torch
from d2l import torch as d2l

#生成数据集
def synthetic_data(w,b,num_example):
    X=torch.normal(0,1,(num_example,len(w)))
    y=torch.matmul(X,w)+b
    y+=torch.normal(0,0.01,y.shape)
    return X,y
true_w=torch.tensor([2,-3.4])
true_b=4.2
features,lable=synthetic_data(true_w,true_b,10)
#print(features,'\n',lable)

#定义数据切片器
def data_iter(X,y,batch_size):
    num_example=len(X)
    indices=list(range(num_example))
    random.shuffle(indices)
    for i in range(0,num_example,batch_size):
        batch_indices=torch.tensor(indices[i:min(i+batch_size,num_example)])
        yield X[batch_indices],y[batch_indices]
#batch_size = 10
#for X, y in data_iter(features,lable,batch_size):
#    print(X, '\n', y)
#    break

#定义模型
def linear_network(X,w,b):
    return torch.matmul(X,w)+b

#定义sgd
def sgd(paras,lr,batch_size):
    with torch.no_grad():
        for para in paras:
            para-=lr*para.grad/batch_size
            para.grad.zero_()

#定义loss函数
def lossfunction(y_label,y_real):
    return (y_label-y_real.reshape(y_label.shape))**2/2

#设置初始参数
w=torch.zeros((2,1),requires_grad=True)
b=torch.tensor(1.0,requires_grad=True)
batch_size=10
lr=1
epoch=3

#训练模型
for i in range(epoch):
    for X,y in data_iter(features,lable,batch_size):
        loss=lossfunction(linear_network(X,w,b),y)
        loss.sum().backward()
        sgd([w,b],lr,batch_size)
    with torch.no_grad():
        train_loss=lossfunction(linear_network(features,w,b),lable)
        print(f'epoch={i+1},train loss={train_loss.mean()}')
print(f'w的估计误差: {true_w - w.reshape(true_w.shape)}')
print(f'b的估计误差: {true_b - b}')
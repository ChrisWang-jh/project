import torch

def train_model(net, train_iter, loss, num_epochs, trainer):
    net.train()
    train_loss=[]
    for epoch in range(num_epochs):
        epoch_loss=0
        for X, y in train_iter:
            y_hat = net(X)
            l = loss(y_hat, y).mean()
            trainer.zero_grad()
            l.backward()
            trainer.step()
            epoch_loss+=l.item()
        train_loss.append(epoch_loss/len(train_iter))
    return train_loss

def test_model(net,test_iter,loss):
    '''
    我加入了准确度测试，该测试模型仅用于分类问题
    '''
    net.eval()
    test_loss=0
    num_accurate=0
    num_sample=0
    with torch.no_grad():
        for X,y in test_iter:
            l=loss(net(X),y).mean()
            test_loss+=l.item()
            _,predict=torch.max(net(X),1)
            num_accurate+=(predict==y).sum().item()
            num_sample+=y.size(0)
    average_accuracy=num_accurate/num_sample
    mean_loss=test_loss/len(test_iter)
    return average_accuracy,mean_loss
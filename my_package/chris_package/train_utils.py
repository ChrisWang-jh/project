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
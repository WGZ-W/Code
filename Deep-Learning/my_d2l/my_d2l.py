
import torch


def synthetic_data(w, b, num_examples):  #@save
    """生成y=Xw+b+噪声"""
    x = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(x, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return x, y.reshape((-1, 1))

import torch
import torch.nn as nn

# 输入数据（logits，无需手动Softmax）
logits = torch.tensor([[2.0, 1.0, 0.1], [0.5, 2.0, 0.3]], requires_grad=True)
y_true = torch.tensor([[0, 1, 0], [1, 0, 0]])  # one-hot标签或类别索引

# print(y_true.max(dim=0))
# print(logits.mean())

# 定义损失函数（自动处理Softmax）
criterion = nn.CrossEntropyLoss()
loss = criterion(logits, y_true.argmax(dim=1))  # 如果y_true是one-hot，需转成类别索引
print(f"PyTorch交叉熵损失: {loss.item():.4f}")
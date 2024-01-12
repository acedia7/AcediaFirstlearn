'''
Mnist手写数字识别：
 1. 导入相关包：如torch、numpy、matplotlib等；
 2. 数据集准备：训练集、测试集；
 3. 搭建网络架构；
 4. 训练目标：损失函数
 5. 优化器
 6. 网络训练；
 7. 保存网络模型；
'''
#  1. 导入相关包：如torch、numpy、matplotlib等
import os
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import transforms, datasets
import warnings

warnings.filterwarnings('ignore')

#  2. 数据集准备：训练集、测试集：可在这时进行数据预处理，包括归一化、随机旋转、随机裁剪等
'''
Pytorch自己内置了一些入门数据集：包括Mnist、Cifar10等，直接导入即可
'''
transform = transforms.Compose([
    transforms.ToTensor(),  # 可将PIL类型的图像或者Numpy数组转为Tensor，并将其像素值归一化到[0,1]
])

# 训练集、测试集
train_dataset = datasets.MNIST(
    root='./dataset',
    train=True,
    transform=transform,
    download=True
)

test_dataset = datasets.MNIST(
    root='./dataset',
    train=False,
    transform=transform,
    download=True
)

train_dataloader = DataLoader(
    dataset=train_dataset,
    batch_size=32,
    shuffle=True,
    num_workers=0,
    drop_last=False
)

test_dataloader = DataLoader(
    dataset=test_dataset,
    batch_size=32,
    shuffle=True,
    num_workers=0,
    drop_last=False
)


# 3.搭建网络架构：输入数据形状：（32,1,28,28）
class DemoModel(nn.Module):
    def __init__(self):
        super(DemoModel, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=8, kernel_size=3, padding='same'),
            nn.AvgPool2d(kernel_size=2),  # （32,1,14,14）
            nn.BatchNorm2d(num_features=8),
            nn.ReLU(),
            nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, padding='same'),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(in_features=14 * 14 * 16, out_features=10),
            nn.Softmax()
        )

    def forward(self, x):
        return self.model(x)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # 确定采用cpu还是gpu计算
model = DemoModel()
model = model.to(device)  # gpu加速
# img,label=next(iter(train_dataloader))
# # out=model(img)
# # print(out.shape)
# # print(model)
# writer=SummaryWriter('./logs')
# writer.add_graph(model,img)
# writer.close()
# 4.训练目标：损失函数
creation = nn.CrossEntropyLoss()  # 损失函数：分类任务常用交叉熵函数，二分类任务可用nn.BCELoss()
creation = creation.to(device)

# 5.优化器
learning_rate = 1e-2
beta1 = 0.9
beta2 = 0.999
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate, betas=(beta1, beta2))  # 优化器
lr_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=32)  # 学习率衰减：余弦退火策略

# 6.网络训练
model_save_path = './models/'
os.makedirs(model_save_path, exist_ok=True)

EPOCHS = 50
train_steps = 0
test_steps = 0
for epoch in range(EPOCHS):  # 0-99
    print("第{}轮训练过程：".format(epoch + 1))
    # 训练步骤
    model.train()  # 训练模式
    epoch_train_loss = 0.0
    for train_batch, (train_image, train_label) in enumerate(train_dataloader):
        print("第{}批数据进行训练".format(train_batch + 1))
        train_image, train_label = train_image.to(device), train_label.to(device)  # 将数据送到GPU
        train_predictions = model(train_image)
        batch_train_loss = creation(train_predictions, train_label)

        optimizer.zero_grad()  # 梯度清零
        batch_train_loss.backward()
        optimizer.step()
        epoch_train_loss += batch_train_loss.item()
        train_steps += 1
        if train_steps % 50 == 0:
            print("第{}次训练，训练损失为{}".format(train_steps, batch_train_loss.item()))

    # 测试步骤
    model.eval()
    epoch_test_loss = 0.0
    epoch_test_acc = 0.0
    with torch.no_grad():
        for test_batch, (test_image, test_label) in enumerate(test_dataloader):
            print("第{}批数据进行测试".format(test_batch + 1))
            test_image, test_label = test_image.to(device), test_label.to(device)
            predictions = model(test_image)
            test_loss = creation(predictions, test_label)
            epoch_test_loss += test_loss.item()
            test_steps += 1
            # 计算每个批次数据测试时的准确率
            batch_test_acc = (predictions.argmax(dim=1) == test_label).sum()
            epoch_test_acc += batch_test_acc
            if test_steps % 50 == 0:
                print("第{}次测试，测试损失为{}".format(test_steps, test_loss.item()))

    if (epoch + 1) % 10 == 0:
        print("第{}轮训练结束，训练损失为{}，测试损失为{}，测试准确率为{}".format
              (epoch + 1, epoch_train_loss, epoch_test_loss, epoch_test_acc / len(test_dataset)))

    # 7.保存模型
    torch.save(model.state_dict(), model_save_path + "model{}.pth".format(epoch + 1))
print("训练结束！")

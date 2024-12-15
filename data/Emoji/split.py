import random

# 输入文件路径
input_file = 'train.txt'  # 假设你的数据存储在这个文件中，每行包含一个图片文件名和标签
output_file_train = 'train_data.txt'
output_file_test = 'test_data.txt'

# 用于保存训练集和测试集的数据
train_data = []
test_data = []

# 按行读取文件并随机抽取 25% 的行作为测试集
with open(input_file, 'r') as f:
    for line in f:
        if random.random() < 0.15:  # 以 15% 的概率将该行放入测试集
            test_data.append(line)
        else:
            train_data.append(line)

# 保存到新文件
with open(output_file_train, 'w') as f_train:
    f_train.writelines(train_data)

with open(output_file_test, 'w') as f_test:
    f_test.writelines(test_data)

print(f"训练集保存到 {output_file_train}")
print(f"测试集保存到 {output_file_test}")

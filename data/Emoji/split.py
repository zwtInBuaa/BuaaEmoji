import random

# 输入文件路径
input_file = 'train.txt'  # 假设你的数据存储在这个文件中，每行包含一个图片文件名和标签
output_file_train = 'train_data.txt'
output_file_test = 'test_data.txt'

# 读取数据
with open(input_file, 'r') as f:
    data = f.readlines()  # 读取每一行数据

# 计算测试集大小 (25%)
test_size = int(len(data) * 0.25)

# 随机抽取 25% 的数据作为测试集
random.shuffle(data)  # 打乱数据
test_data = data[:test_size]  # 抽取前 25% 的数据作为测试集
train_data = data[test_size:]  # 剩余的 75% 作为训练集

# 保存到新文件
with open(output_file_train, 'w') as f_train:
    f_train.writelines(train_data)

with open(output_file_test, 'w') as f_test:
    f_test.writelines(test_data)

print(f"训练集保存到 {output_file_train}")
print(f"测试集保存到 {output_file_test}")

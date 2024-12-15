import os


def generate_class_ids(dataset_root, output_file):
    # 定义输出文件
    with open(output_file, "w") as out_file:


        # 遍历主目录中的类别文件夹
        class_id = 0
        for category in sorted(os.listdir(dataset_root)):
            category_path = os.path.join(dataset_root, category)
            if not os.path.isdir(category_path):
                continue  # 如果不是文件夹，跳过


            for image_name in sorted(os.listdir(category_path)):
                if not image_name.endswith(('.png', '.jpg', '.jpeg')):  # 过滤非图像文件
                    continue

                # 写入文件记录
                out_file.write(f"{image_name} {category} {class_id}\n")

            # 更新 Class ID
            class_id += 1


# 设置数据集根目录和输出文件路径
dataset_root = "../.data/Emoji/train"  # 数据集主目录
output_file = "../.data/Emoji/train.txt"  # 输出文件

# 生成数据集信息
generate_class_ids(dataset_root, output_file)

print(f"数据集信息已成功写入 {output_file}")

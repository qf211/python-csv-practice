import pandas as pd  # 导入 pandas（数据处理库）
from pathlib import Path  # 导入 Path（路径工具）

folder = Path(__file__).parent  # 获取当前 Python 文件所在的文件夹
input_file = folder / "summary_new.csv"  # 设置输入 CSV 文件路径
data = pd.read_csv(input_file)  # 读取 CSV，得到表格数据


def clean_data(table):
    """清洗年龄，并根据年龄生成状态列。"""
    table["年龄"] = pd.to_numeric(  # 把年龄转换为数字
        table["年龄"], errors="coerce"  # 无法转换的内容变为 NaN（缺失值）
    )
    table["状态"] = table["年龄"].apply(  # 对每个年龄应用判断规则
        lambda age: "年龄无效" if pd.isna(age) else "成年" if age >= 18 else "未成年"
    )
    return table  # 返回清洗后的表格


def remove_missing_age(table):
    """删除年龄缺失的行，并重新整理索引。"""
    valid_table = table.dropna(subset=["年龄"])  # 删除年龄为空的行
    return valid_table.reset_index(drop=True)  # 重置索引并丢弃旧索引


def calculate_average_age(table):
    """计算有效学生的平均年龄。"""
    return table["年龄"].mean()  # mean（平均值）计算平均年龄


def sort_by_age(table):
    """按照年龄从小到大排序。"""
    sorted_table = table.sort_values(
        by="年龄", ascending=True  # True（是）：升序，从小到大
    )
    return sorted_table.reset_index(drop=True)  # 重置排序后的索引


def save_csv(table, file_name):
    """把表格保存为 CSV 文件。"""
    output_file = folder / file_name  # 拼接完整输出路径
    table.to_csv(
        output_file,
        index=False,  # 不保存 pandas 索引
        encoding="utf-8-sig"  # 使用适合中文的编码
    )
    print(f"文件已保存：{output_file}")


data = clean_data(data)  # 第 1 步：清洗数据并生成状态
valid_data = remove_missing_age(data)  # 第 2 步：删除无效年龄
average_age = calculate_average_age(valid_data)  # 第 3 步：计算平均年龄
sorted_data = sort_by_age(valid_data)  # 第 4 步：排序并重置索引

print(f"有效学生人数：{len(valid_data)}")  # 打印有效学生数量
print(f"平均年龄：{average_age:.1f}")  # 打印保留 1 位小数的平均年龄
print(sorted_data)  # 打印最终表格

save_csv(sorted_data, "students_final.csv")  # 第 5 步：保存最终结果

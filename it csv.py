import csv
from pathlib import Path
folder = Path(__file__).parent
summary_folder = folder / 'summary_new.csv'
valid_folder = folder / 'valid.csv'
invalid_folder = folder / 'invalid.csv'
vilid_count = 0
with open(summary_folder, 'r', encoding='utf-8-sig', newline='') as file:
    with open(valid_folder, 'w', encoding='utf-8-sig', newline='') as valid:
        with open(invalid_folder, 'w', encoding='utf-8-sig', newline='') as invalid:
            filidnames_one = ['姓名', '年龄', '状态']
            filidnames = ['姓名', '年龄', '错误原因']
            write_valid = csv.DictWriter(valid, fieldnames=filidnames_one)
            write_valid.writeheader()
            write_invalid = csv.DictWriter(invalid, fieldnames=filidnames)
            write_invalid.writeheader()
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    student_age = int(row['年龄'])
                    if student_age >= 18:
                        status = '成年'
                    else:
                        status = '未成年'
                    write_valid.writerow({
                        '姓名': row['姓名'], 
                        '年龄': student_age, 
                        '状态': status
                    })
                    print(f"姓名: {row['姓名']}, 年龄: {student_age}, 状态: {status}")
                except ValueError:
                    write_invalid.writerow({
                        '姓名': row['姓名'], 
                        '年龄': row['年龄'], 
                        '错误原因': '年龄不是数字'
                    })
                    vilid_count = vilid_count + 1
                    print(f"姓名: {row['姓名']}, 年龄: 未知, 错误原因: 年龄不是数字")
                    continue
            print(f"年龄未知: {vilid_count}")

            
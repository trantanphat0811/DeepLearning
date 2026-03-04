import pandas as pd
import numpy as np
import re

# --- VẤN ĐỀ 1: Tải dữ liệu và xử lý thiếu Header ---
column_names = ["Id", "Name", "Age", "Weight", 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']
df = pd.read_csv("patient_heart_rate.csv", names=column_names)

print("Dữ liệu đã tải:")
print(df)
print("\nThông tin DataFrame:")
print(df.info())

# --- VẤN ĐỀ 2: Tách cột Name ---
print("\n" + "="*50)
print("VẤN ĐỀ 2: Tách cột Name")
print("="*50)

# Xử lý các giá trị NaN trong cột Name trước khi tách
df['Name'] = df['Name'].fillna('')

# Tách cột Name thành Firstname và Lastname
# Sử dụng str.split() với tham số n=1 để chỉ tách ở khoảng trắng đầu tiên
# Điều này giúp xử lý tốt các trường hợp tên có phần中间 (middle name)
df[['Firstname', 'Lastname']] = df['Name'].str.split(n=1, expand=True)

# Xóa cột Name gốc sau khi đã tách
df.drop('Name', axis=1, inplace=True)

print("\nDữ liệu sau khi tách cột Name:")
print(df)
print("\nCác cột sau khi tách:")
print(df.columns.tolist())


# --- VẤN ĐỀ 3: Chuẩn hóa đơn vị Weight (lbs -> kgs) ---
print("\n" + "="*50)
print("VẤN ĐỀ 3: Chuẩn hóa đơn vị Weight")
print("="*50)

def convert_weight(w):
    if pd.isna(w): return w
    w = str(w).lower()
    val = float(re.findall(r"\d+\.?\d*", w)[0])
    return round(val / 2.2, 2) if 'lbs' in w else val

df['Weight'] = df['Weight'].apply(convert_weight)

print("\nDữ liệu sau khi chuẩn hóa đơn vị Weight:")
print(df)
print("\nCác giá trị Weight duy nhất:")
print(df['Weight'].unique())

# --- VẤN ĐỀ 4 & 5: Xóa dòng trống và trùng lặp ---
print("\n" + "="*50)
print("VẤN ĐỀ 4: Xóa dòng trống")
print("="*50)

print(f"\nSố dòng trước khi xóa dòng trống: {len(df)}")
df.dropna(how='all', inplace=True)
print(f"Số dòng sau khi xóa dòng trống: {len(df)}")

print("\n" + "="*50)
print("VẤN ĐỀ 5: Xóa dòng trùng lặp")
print("="*50)

print(f"\nSố dòng trước khi xóa trùng lặp: {len(df)}")
df.drop_duplicates(subset=['Firstname', 'Lastname', 'Age', 'Weight'], inplace=True)
print(f"Số dòng sau khi xóa trùng lặp: {len(df)}")

# --- VẤN ĐỀ 6: Xóa ký tự Non-ASCII ---
print("\n" + "="*50)
print("VẤN ĐỀ 6: Loại bỏ ký tự Non-ASCII")
print("="*50)

print("\nTên trước khi xóa ký tự Non-ASCII:")
print(df[['Firstname', 'Lastname']])

df['Firstname'] = df['Firstname'].replace(r'[^\x00-\x7F]+', '', regex=True)
df['Lastname'] = df['Lastname'].replace(r'[^\x00-\x7F]+', '', regex=True)

print("\nTên sau khi xóa ký tự Non-ASCII:")
print(df[['Firstname', 'Lastname']])


# --- VẤN ĐỀ 7: Xử lý thiếu Age & Weight ---
print("\n" + "="*50)
print("VẤN ĐỀ 7: Xử lý dữ liệu thiếu (Age & Weight)")
print("="*50)

print("\nSố lượng giá trị thiếu trước khi xử lý:")
print(df.isnull().sum()[['Age', 'Weight']])

# Xóa dòng thiếu cả Age và Weight
df.dropna(subset=['Age', 'Weight'], how='all', inplace=True)

print("\nSố lượng giá trị thiếu sau khi xóa dòng thiếu cả 2:")
print(df.isnull().sum()[['Age', 'Weight']])

# Điền Age thiếu bằng trung bình
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

print(f"\nAge thiếu được điền bằng giá trị trung bình: {mean_age:.2f}")
print("\nSố lượng giá trị thiếu cuối cùng:")
print(df.isnull().sum()[['Age', 'Weight']])


# --- VẤN ĐỀ 8: Tái cấu trúc dữ liệu (Melt) ---
print("\n" + "="*50)
print("VẤN ĐỀ 8: Tái cấu trúc dữ liệu (Melt)")
print("="*50)

print("\nDữ liệu trước khi melt:")
print(df.head())

df = pd.melt(df, id_vars=['Id', 'Age', 'Weight', 'Firstname', 'Lastname'],
             var_name='sex_and_time', value_name='PulseRate')

print("\nDữ liệu sau khi melt:")
print(df.head(10))
print(f"\nKích thước sau khi melt: {df.shape}")

# --- VẤN ĐỀ 10: Phân rã cột sex_and_time ---
print("\n" + "="*50)
print("VẤN ĐỀ 10: Phân rã cột sex_and_time")
print("="*50)

print("\nGiá trị duy nhất trong cột sex_and_time:")
print(df['sex_and_time'].unique())

df['Sex'] = df['sex_and_time'].apply(lambda x: 'Male' if x[0] == 'm' else 'Female')
df['Time'] = df['sex_and_time'].apply(lambda x: x[1:3] + '-' + x[3:])

print("\nSau khi phân rã thành Sex và Time:")
print(df[['Sex', 'Time', 'PulseRate']].head(10))

print("\nCác giá trị Sex duy nhất:", df['Sex'].unique())
print("Các giá trị Time duy nhất:", sorted(df['Time'].unique()))

df.drop('sex_and_time', axis=1, inplace=True)


# --- VẤN ĐỀ 9: Xử lý giá trị bất thường (Outliers) của PulseRate ---
print("\n" + "="*50)
print("VẤN ĐỀ 9: Xử lý giá trị bất thường của PulseRate")
print("="*50)

print("\nThống kê PulseRate trước khi xử lý:")
print(df['PulseRate'].describe())
print("\nCác giá trị duy nhất trong PulseRate:")
print(df['PulseRate'].unique())

# Chuyển PulseRate sang dạng số, các giá trị không hợp lệ sẽ thành NaN
df['PulseRate'] = pd.to_numeric(df['PulseRate'], errors='coerce')

print("\nSau khi chuyển sang dạng số:")
print(f"Số lượng giá trị thiếu: {df['PulseRate'].isnull().sum()}")

# Xác định outliers: PulseRate < 30 hoặc > 200 là giá trị bất thường
print("\nSố lượng giá trị bất thường (< 30 hoặc > 200):")
print(f"  - PulseRate < 30: {(df['PulseRate'] < 30).sum()}")
print(f"  - PulseRate > 200: {(df['PulseRate'] > 200).sum()}")

# Chuyển outliers thành NaN
outliers = (df['PulseRate'] < 30) | (df['PulseRate'] > 200)
df.loc[outliers, 'PulseRate'] = np.nan

print(f"\nTổng số giá trị NaN (bao gồm outliers và giá trị không hợp lệ): {df['PulseRate'].isnull().sum()}")

# --- VẤN ĐỀ 11: Hệ thống điền PulseRate thiếu (Fallback Logic) ---
print("\n" + "="*50)

print("VẤN ĐỀ 11: Điền PulseRate thiếu (Fallback Logic)")
print("="*50)

print("\nSố lượng giá trị PulseRate thiếu trước khi điền:")
print(df['PulseRate'].isnull().sum())

def fill_pulse_fallback(row):
    """
    Logic điền PulseRate thiếu theo thứ tự ưu tiên:
    1. Giữ nguyên nếu có giá trị hợp lệ
    2. Điền bằng trung bình PulseRate cùng Sex và Time
    3. Điền bằng trung bình PulseRate cùng Sex
    4. Điền bằng trung bình toàn bộ
    """
    if not pd.isna(row['PulseRate']):
        return row['PulseRate']

    # Fallback 1: Trung bình cùng Sex và Time
    group_mean = df[(df['Sex'] == row['Sex']) &
                    (df['Time'] == row['Time'])]['PulseRate'].mean()
    if not pd.isna(group_mean):
        return group_mean

    # Fallback 2: Trung bình cùng Sex
    sex_mean = df[df['Sex'] == row['Sex']]['PulseRate'].mean()
    if not pd.isna(sex_mean):
        return sex_mean

    # Fallback 3: Trung bình toàn bộ
    global_mean = df['PulseRate'].mean()
    return global_mean

df['PulseRate'] = df.apply(fill_pulse_fallback, axis=1)

print(f"Số lượng giá trị PulseRate thiếu sau khi điền: {df['PulseRate'].isnull().sum()}")
print("\nThống kê PulseRate sau khi điền:")
print(df['PulseRate'].describe())


# --- VẤN ĐỀ 12: Rút gọn và Lưu trữ dữ liệu ---
print("\n" + "="*50)
print("VẤN ĐỀ 12: Rút gọn và Lưu trữ")
print("="*50)

# Sắp xếp lại thứ tự cột cho hợp lý
df = df[['Id', 'Firstname', 'Lastname', 'Age', 'Weight', 'Sex', 'Time', 'PulseRate']]

print("\nDữ liệu sau khi sắp xếp lại cột:")
print(df.head(20))

print("\nThong tin DataFrame cuối cùng:")
print(df.info())

print("\nThống kê mô tả:")
print(df.describe())

# Reset index
df.reset_index(drop=True, inplace=True)

# Xuất file CSV
output_file = "patient_heart_rate_clean.csv"
df.to_csv(output_file, index=False)
print(f"\n{'='*50}")
print(f"Đã xuất file sạch: {output_file}")
print(f"{'='*50}")

# Hiển thị một số thông tin tổng kết
print("\nTỔNG KẾT QUÁ TRÌNH LÀM SẠCH DỮ LIỆU:")
print(f"  - Số dòng dữ liệu cuối cùng: {len(df)}")
print(f"  - Số cột: {len(df.columns)}")
print(f"  - Không có giá trị thiếu: {df.isnull().sum().sum() == 0}")
print(f"  - File đã lưu: {output_file}")
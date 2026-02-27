import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('processed_dulieuxettuyendaihoc.csv')

# --- PHẦN 1: THỐNG KÊ DỮ LIỆU ---
# 1. Sắp xếp DH1 tăng dần [cite: 20]
df_sorted_dh1 = df.sort_values(by='DH1')

# 3. Pivot-table thống kê DH1 theo KT 
pivot_kt = df.groupby('KT')['DH1'].agg(['count', 'sum', 'mean', 'median', 'min', 'max', 'std'])
# Lưu ý: Q1, Q2, Q3 có thể tính riêng bằng .quantile([0.25, 0.5, 0.75])

# --- PHẦN 2: TRÌNH BÀY DỮ LIỆU ---
# 1. Tần số và tần suất biến GT [cite: 28, 29]
gt_counts = df['GT'].value_counts()
gt_pct = df['GT'].value_counts(normalize=True)

# Vẽ biểu đồ tròn cho giới tính
plt.figure(figsize=(6,6))
plt.pie(gt_counts, labels=gt_counts.index, autopct='%1.1f%%')
plt.title('Tần suất giới tính')
plt.show()


df_female = df[df['GT'] == 'F']
xl_data = df_female[['XL1', 'XL2', 'XL3']].apply(pd.Series.value_counts).T

xl_data.plot(kind='bar', stacked=False)
plt.title('Xếp loại của học sinh nữ qua các học kỳ')
plt.ylabel('Số lượng học sinh')
plt.show()

# --- PHẦN 4: TRỰC QUAN HÓA NÂNG CAO ---
# 2. Tạo biến phân loại phanlopt1 cho môn Toán (T1) 
def phan_lop(diem):
    if diem < 5: return 'k'
    elif diem < 7: return 'tb'
    elif diem < 8: return 'kh'
    else: return 'g'

df['phanlopt1'] = df['T1'].apply(phan_lop)

# --- PHẦN 5: MÔ TẢ DỮ LIỆU VÀ PHÂN PHỐI ---
# 1. Biểu đồ Box-Plot và Histogram cho T1 [cite: 13]
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(x=df['T1'])
plt.title('Box-plot của T1')

plt.subplot(1, 2, 2)
sns.histplot(df['T1'], kde=True)
plt.title('Histogram của T1')
plt.show()

# 3. Khảo sát tương quan giữa DH1 và T1 [cite: 14]
correlation = df['DH1'].corr(df['T1'])
print(f"Hệ số tương quan giữa DH1 và T1: {correlation}")

sns.scatterplot(x='T1', y='DH1', data=df)
plt.title('Tương quan giữa điểm Toán (T1) và điểm thi ĐH (DH1)')
plt.show()

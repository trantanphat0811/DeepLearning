# MÃ NGUỒN PYTHON GỢI Ý - LAB 2

Dưới đây là mã nguồn Python gợi ý cho các phần của Lab 2. 
Notebook `TranTanPhat_2274802010644_PTDLHS_Lab2.ipynb` đã thực hiện đầy đủ.

## Import Thư Viện

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import skew, kurtosis, shapiro, probplot
import warnings
warnings.filterwarnings('ignore')

# Cài đặt style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

# Đọc dữ liệu
df = pd.read_csv('processed_dulieuxettuyendaihoc.csv')
```

---

## PHẦN 1: THỐNG KÊ DỮ LIỆU

### 1.1 Sắp xếp DH1 tăng dần

```python
# Sắp xếp DH1 tăng dần
df_sorted_dh1 = df.sort_values(by='DH1', ascending=True)
print("DH1 sorted ascending:")
print(df_sorted_dh1[['STT', 'DH1']])
print(f"Min: {df['DH1'].min()}, Max: {df['DH1'].max()}")
```

### 1.2 Sắp xếp DH2 tăng dần theo giới tính

```python
df_sorted_dh2_gt = df.sort_values(['GT', 'DH2'], ascending=[True, True])
print("DH2 sorted by Gender and ascending:")
print(df_sorted_dh2_gt[['STT', 'GT', 'DH2']])
```

### 1.3 Pivot Table DH1 theo KT

```python
# Cách 1: Sử dụng groupby().agg()
pivot_kt = df.groupby('KT')['DH1'].agg(['count', 'sum', 'mean', 'median', 'min', 'max', 'std'])

# Thêm quantiles
pivot_kt['Q1'] = df.groupby('KT')['DH1'].quantile(0.25)
pivot_kt['Q2'] = df.groupby('KT')['DH1'].quantile(0.50)
pivot_kt['Q3'] = df.groupby('KT')['DH1'].quantile(0.75)

print("Statistics of DH1 by KT:")
print(pivot_kt.round(4))
```

### 1.4 Pivot Table DH1 theo KT và KV

```python
# Sử dụng custom function
def get_stats(x):
    return pd.Series({
        'count': x.count(),
        'sum': x.sum(),
        'mean': x.mean(),
        'median': x.median(),
        'min': x.min(),
        'max': x.max(),
        'std': x.std(),
        'Q1': x.quantile(0.25),
        'Q2': x.quantile(0.50),
        'Q3': x.quantile(0.75)
    })

pivot_kt_kv = df.groupby(['KT', 'KV'])['DH1'].apply(get_stats)
print("Statistics of DH1 by KT and KV:")
print(pivot_kt_kv.round(4))
```

### 1.5 Pivot Table DH1 theo KT, KV, DT

```python
pivot_kt_kv_dt = df.groupby(['KT', 'KV', 'DT'])['DH1'].apply(get_stats)
print("Statistics of DH1 by KT, KV, DT:")
print(pivot_kt_kv_dt.round(4))
```

---

## PHẦN 2: TRÌNH BÀY DỮ LIỆU

### 2.1 Tần số và tần suất biến GT

```python
# Tần số và tần suất
gt_counts = df['GT'].value_counts()
gt_pct = df['GT'].value_counts(normalize=True) * 100

freq_table_gt = pd.DataFrame({
    'Frequency': gt_counts,
    'Relative Frequency (%)': gt_pct.round(2)
})
print("Frequency and Relative Frequency Table for GT:")
print(freq_table_gt)

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart
gt_counts.plot(kind='bar', ax=axes[0], color=['#FF6B9D', '#4A90E2'])
axes[0].set_title('Frequency Distribution of Gender')
axes[0].set_ylabel('Count')

# Pie chart
colors = ['#FF6B9D', '#4A90E2']
axes[1].pie(gt_counts.values, labels=gt_counts.index, autopct='%1.1f%%', 
            colors=colors, startangle=90)
axes[1].set_title('Relative Frequency Distribution of Gender')

plt.tight_layout()
plt.show()
```

### 2.2 Trình bày US_TBM1, US_TBM2, US_TBM3

```python
us_vars = ['US_TBM1', 'US_TBM2', 'US_TBM3']
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for i, var in enumerate(us_vars):
    freq = df[var].value_counts().sort_index()
    axes[i].bar(freq.index, freq.values, color='skyblue', edgecolor='navy')
    axes[i].set_title(f'Frequency Distribution of {var}')
    axes[i].set_ylabel('Count')
    axes[i].grid(axis='y', alpha=0.3)
    
    print(f"\n{var} Frequency Table:")
    print(freq)

plt.tight_layout()
plt.show()
```

### 2.3 DT cho học sinh nam

```python
male_dt = df[df['GT'] == 'M']['DT']
print("DT (Ethnicity) for Male Students:")
print(male_dt.value_counts())

fig, ax = plt.subplots(figsize=(10, 6))
male_dt.value_counts().plot(kind='bar', ax=ax, color='steelblue')
ax.set_title('Ethnicity Distribution of Male Students')
ax.set_ylabel('Count')
plt.tight_layout()
plt.show()
```

### 2.4 KV cho nam, dân tộc Kinh, điểm ≥ tiêu chuẩn

```python
filtered_kv = df[(df['GT'] == 'M') & (df['DT'] == 0.0) & 
                  (df['DH1'] >= 5.0) & (df['DH2'] >= 4.0) & (df['DH3'] >= 4.0)]['KV']

print("KV for Male, Kinh Ethnicity, Meeting Score Conditions:")
print(filtered_kv.value_counts())
print(f"Total records: {len(filtered_kv)}")

if len(filtered_kv) > 0:
    fig, ax = plt.subplots(figsize=(10, 6))
    filtered_kv.value_counts().plot(kind='bar', ax=ax, color='coral')
    ax.set_title('Region (KV) Distribution - Male, Kinh, Meeting Conditions')
    plt.tight_layout()
    plt.show()
```

### 2.5 DH1, DH2, DH3 ≥ 5.0 trong khu vực 2NT

```python
filtered_2nt = df[(df['KV'] == '2NT') & (df['DH1'] >= 5.0) & 
                  (df['DH2'] >= 5.0) & (df['DH3'] >= 5.0)]
print("Students with scores >= 5.0 in region 2NT:")
print(f"Total: {len(filtered_2nt)} records")
print("\nStatistics:")
print(filtered_2nt[['DH1', 'DH2', 'DH3']].describe())

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for i, var in enumerate(['DH1', 'DH2', 'DH3']):
    axes[i].hist(filtered_2nt[var], bins=10, color='lightgreen', edgecolor='darkgreen')
    axes[i].set_title(f'Distribution of {var} (Region 2NT, >= 5.0)')
    axes[i].set_ylabel('Frequency')

plt.tight_layout()
plt.show()
```

---

## PHẦN 3: TRỰC QUAN HÓA THEO NHÓM

### 3.1 Học sinh nữ - Phân loại XL1, XL2, XL3

```python
df_female = df[df['GT'] == 'F']

xl_levels = ['XL1', 'XL2', 'XL3']
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

for idx, xl in enumerate(xl_levels):
    counts = df_female[xl].value_counts()
    axes[idx].bar(counts.index, counts.values, color='steelblue', edgecolor='navy')
    axes[idx].set_title(f'Female Students - {xl} Classification')
    axes[idx].set_ylabel('Number of Students')
    
    print(f"\n{xl} distribution for female students:")
    print(counts)

plt.tight_layout()
plt.show()
```

### 3.2-3.7 Phân tích KQXT theo các nhóm

```python
# Đậu/Rớt theo khối thi
kqxt_by_kt = pd.crosstab(df['KT'], df['KQXT'])
print("Pass/Fail by Exam Type:")
print(kqxt_by_kt)

fig, ax = plt.subplots(figsize=(12, 6))
kqxt_by_kt.plot(kind='bar', ax=ax, color=['#FF6B6B', '#90EE90'])
ax.set_title('Number of Passed and Failed Candidates by Exam Type')
ax.set_ylabel('Number of Candidates')
ax.legend(['Failed', 'Passed'])
plt.tight_layout()
plt.show()

# Tương tự cho KV, DT, GT...
```

---

## PHẦN 4: TRỰC QUAN HÓA NÂNG CAO

### 4.1 Biểu đồ đường Simple cho T1

```python
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(range(len(df)), df['T1'].values, marker='o', linestyle='-', 
        markersize=4, color='#2E86AB', alpha=0.8)
ax.set_title('T1 (Math) Scores - Simple Line Chart')
ax.set_xlabel('Student Index')
ax.set_ylabel('T1 Score')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("T1 Statistics:")
print(df['T1'].describe())
```

### 4.2 Tạo biến phân loại phanloait1

```python
def classify_t1(score):
    if score < 5:
        return 'k'      # kém
    elif score < 7:
        return 'tb'     # trung bình
    elif score < 8:
        return 'kh'     # khá
    else:
        return 'g'      # giỏi

df['phanloait1'] = df['T1'].apply(classify_t1)

print("Classification of T1:")
print(df['phanloait1'].value_counts())
print("\nFirst few rows with classification:")
print(df[['STT', 'T1', 'phanloait1']].head(20))
```

### 4.3 Bảng tần số cho phanloait1

```python
phanloait1_freq = df['phanloait1'].value_counts()
phanloait1_relative = df['phanloait1'].value_counts(normalize=True) * 100

freq_table = pd.DataFrame({
    'Classification': phanloait1_freq.index,
    'Frequency': phanloait1_freq.values,
    'Relative Frequency (%)': phanloait1_relative.values
}).sort_index()

print("Frequency Table for phanloait1:")
print(freq_table)
```

### 4.4 Multiple Line Chart

```python
fig, ax = plt.subplots(figsize=(14, 6))

colors = {'k': '#FF6B6B', 'tb': '#4ECDC4', 'kh': '#95E1D3', 'g': '#FFD700'}
for classification in ['k', 'tb', 'kh', 'g']:
    data = df[df['phanloait1'] == classification]
    ax.plot(data.index, data['T1'].values, marker='o', linestyle='-', 
            linewidth=1.5, markersize=5, label=classification, 
            color=colors.get(classification, '#999999'), alpha=0.7)

ax.set_title('T1 Scores by Classification - Multiple Line Chart')
ax.set_xlabel('Student Index')
ax.set_ylabel('T1 Score')
ax.legend(title='Classification')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 4.5 Drop-line Chart

```python
fig, ax = plt.subplots(figsize=(14, 6))

colors = {'k': '#FF6B6B', 'tb': '#4ECDC4', 'kh': '#95E1D3', 'g': '#FFD700'}
for classification in ['k', 'tb', 'kh', 'g']:
    data = df[df['phanloait1'] == classification]
    ax.vlines(data.index, 0, data['T1'].values, colors=colors.get(classification), 
              linewidth=2, alpha=0.7, label=classification)
    ax.scatter(data.index, data['T1'].values, color=colors.get(classification), s=40)

ax.axhline(y=0, color='black', linewidth=1)
ax.set_title('T1 Scores by Classification - Drop-line Chart')
ax.set_xlabel('Student Index')
ax.set_ylabel('T1 Score')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()
```

---

## PHẦN 5: MÔ TẢ DỮ LIỆU VÀ PHÂN TÍCH PHÂN PHỐI

### 5.1 Phân tích phân phối T1

#### 5.1.1 Thống kê mô tả

```python
t1_data = df['T1']

print("Descriptive Statistics for T1:")
print(f"Mean: {t1_data.mean():.4f}")
print(f"Median: {t1_data.median():.4f}")
print(f"Std Dev: {t1_data.std():.4f}")
print(f"Variance: {t1_data.var():.4f}")
print(f"Skewness: {skew(t1_data):.4f}")
print(f"Kurtosis: {kurtosis(t1_data):.4f}")

# Shapiro-Wilk test
stat, p_value = shapiro(t1_data)
print(f"\nShapiro-Wilk Test:")
print(f"Statistic: {stat:.4f}, p-value: {p_value:.6f}")
```

#### 5.1.2 Box Plot

```python
fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(t1_data, vert=True, patch_artist=True)
bp['boxes'][0].set_facecolor('lightblue')
ax.set_ylabel('T1 Score')
ax.set_title('Box Plot of T1 (Math) Scores')
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

#### 5.1.3 Histogram

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(t1_data, bins=20, color='skyblue', edgecolor='navy', alpha=0.7)
ax.axvline(t1_data.mean(), color='red', linestyle='--', linewidth=2, 
           label=f'Mean: {t1_data.mean():.2f}')
ax.axvline(t1_data.median(), color='green', linestyle='--', linewidth=2, 
           label=f'Median: {t1_data.median():.2f}')
ax.set_title('Histogram of T1 (Math) Scores')
ax.set_xlabel('T1 Score')
ax.set_ylabel('Frequency')
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

#### 5.1.4 QQ-Plot

```python
fig, ax = plt.subplots(figsize=(10, 6))
probplot(t1_data, dist="norm", plot=ax)
ax.set_title('QQ-Plot of T1 (Math) Scores')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("QQ-Plot Interpretation:")
print("- Points close to diagonal = normal distribution")
print("- Deviations from diagonal = non-normality")
```

### 5.2 Phân phối T1 theo từng nhóm phanloait1

```python
classifications = ['k', 'tb', 'kh', 'g']
fig, axes = plt.subplots(4, 3, figsize=(16, 14))

for idx, classification in enumerate(classifications):
    data = df[df['phanloait1'] == classification]['T1']
    
    # Box plot
    axes[idx, 0].boxplot(data, vert=True)
    axes[idx, 0].set_title(f'Box Plot - {classification}')
    axes[idx, 0].set_ylabel('T1 Score')
    
    # Histogram
    axes[idx, 1].hist(data, bins=10, color='lightblue', edgecolor='navy')
    axes[idx, 1].set_title(f'Histogram - {classification}')
    axes[idx, 1].set_ylabel('Frequency')
    
    # QQ-Plot
    probplot(data, dist="norm", plot=axes[idx, 2])
    axes[idx, 2].set_title(f'QQ-Plot - {classification}')

plt.tight_layout()
plt.show()
```

### 5.3 Tương quan DH1 vs T1

```python
# Tính tương quan
covariance = np.cov(df['DH1'], df['T1'])[0, 1]
correlation = df['DH1'].corr(df['T1'])

print(f"Covariance (DH1, T1): {covariance:.4f}")
print(f"Pearson Correlation: {correlation:.4f}")

# Scatter plot
fig, ax = plt.subplots(figsize=(12, 7))
ax.scatter(df['T1'], df['DH1'], alpha=0.6, s=50, color='#2E86AB')

# Regression line
z = np.polyfit(df['T1'], df['DH1'], 1)
p = np.poly1d(z)
ax.plot(df['T1'].sort_values(), p(df['T1'].sort_values()), 
        "r--", linewidth=2, label=f'y={z[0]:.3f}x+{z[1]:.3f}')

ax.set_title(f'Scatter Plot: DH1 vs T1 (r={correlation:.4f})')
ax.set_xlabel('T1 (Independent Variable)')
ax.set_ylabel('DH1 (Dependent Variable)')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 5.4 Tương quan DH1 vs T1 theo từng khu vực

```python
regions = df['KV'].unique()
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
axes = axes.flatten()

for idx, region in enumerate(sorted(regions)):
    region_data = df[df['KV'] == region]
    corr = region_data['DH1'].corr(region_data['T1'])
    
    axes[idx].scatter(region_data['T1'], region_data['DH1'], 
                     alpha=0.6, s=50, color='#2E86AB')
    
    if len(region_data) > 1:
        z = np.polyfit(region_data['T1'], region_data['DH1'], 1)
        p = np.poly1d(z)
        x_sorted = region_data['T1'].sort_values()
        axes[idx].plot(x_sorted, p(x_sorted), "r--", linewidth=2)
    
    axes[idx].set_title(f'Region {region} (n={len(region_data)}, r={corr:.4f})')
    axes[idx].set_xlabel('T1')
    axes[idx].set_ylabel('DH1')
    axes[idx].grid(True, alpha=0.3)

axes[-1].set_visible(False)
plt.tight_layout()
plt.show()
```

### 5.5 Ma trận tương quan DH1, DH2, DH3

```python
dh_data = df[['DH1', 'DH2', 'DH3']]

# Correlation matrix
corr_matrix = dh_data.corr()
print("Pearson Correlation Matrix:")
print(corr_matrix.round(4))

# Covariance matrix
cov_matrix = dh_data.cov()
print("\nCovariance Matrix:")
print(cov_matrix.round(4))

# Heatmap
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=2, vmin=-1, vmax=1, ax=ax, fmt='.3f')
ax.set_title('Correlation Matrix: DH1, DH2, DH3')
plt.tight_layout()
plt.show()

# Scatter plot matrix
fig, axes = plt.subplots(3, 3, figsize=(14, 12))

for i, var1 in enumerate(['DH1', 'DH2', 'DH3']):
    for j, var2 in enumerate(['DH1', 'DH2', 'DH3']):
        ax = axes[i, j]
        
        if i == j:
            ax.hist(df[var1], bins=15, color='lightblue', edgecolor='navy')
        else:
            ax.scatter(df[var2], df[var1], alpha=0.5, s=30, color='#2E86AB')
            z = np.polyfit(df[var2], df[var1], 1)
            p = np.poly1d(z)
            ax.plot(df[var2].sort_values(), p(df[var2].sort_values()), 
                   "r--", linewidth=1.5, alpha=0.7)
        
        ax.grid(True, alpha=0.3)

plt.suptitle('Scatter Plot Matrix: DH1, DH2, DH3')
plt.tight_layout()
plt.show()
```

---

## Ghi Chú Quan Trọng

1. **Pivot Table**: Tính nhiều chỉ số cùng lúc bằng `.agg(['count', 'sum', 'mean', ...])`
2. **Lọc dữ liệu**: Sử dụng điều kiện trước khi visualize: `df[df['GT'] == 'F']`
3. **Phân loại**: Sử dụng `.apply()` để chuyển dữ liệu định lượng → định tính
4. **Interpretation**: 
   - Skewness < -0.5 (left), -0.5-0.5 (symmetric), > 0.5 (right)
   - Kurtosis: < 3 (flat), = 3 (normal), > 3 (peaked)
   - Shapiro-Wilk: p > 0.05 (normal), p < 0.05 (not normal)
   - Correlation: |r| < 0.3 (weak), 0.3-0.7 (moderate), > 0.7 (strong)

---

**Hoàn thành Lab 2 với mã gợi ý này!**

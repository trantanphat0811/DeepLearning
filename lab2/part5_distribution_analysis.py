#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHẦN 5: MỐ TẢ DỮ LIỆU VÀ KHẢO SÁT DẠNG PHÂN PHỐI
Lab 2 - Trực quan hóa dữ liệu xử lý điểm thi đại học
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis, shapiro, probplot, linregress
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10

# Load data
df = pd.read_csv('processed_dulieuxettuyendaihoc.csv')

# Create phanloait1 classification
def classify_t1(score):
    if score < 5:
        return 'kém (k)'
    elif score < 7:
        return 'trung bình (tb)'
    elif score < 8:
        return 'khá (k)'
    else:
        return 'giỏi (g)'

df['phanloait1'] = df['T1'].apply(classify_t1)

print("="*80)
print("PHẦN 5: MỐ TẢ DỮ LIỆU VÀ KHẢO SÁT DẠNG PHÂN PHỐI")
print("="*80)

# ============= YÊU CẦU 1: MỐ TẢ VÀ KHẢO SÁT PHÂN PHỐI T1 =============
print("\n📊 YÊU CẦU 1: Mô tả và khảo sát phân phối cho biến T1")
print("="*80)

t1_data = df['T1']

# 1.1 Độ tập trung và phân tán
print("\n1.1️ 📈 ĐỘ TẬP TRUNG VÀ PHÂN TÁN:")
print(f"  Mean (Trung bình): {t1_data.mean():.4f}")
print(f"  Median (Trung vị): {t1_data.median():.4f}")
try:
    mode_val = t1_data.mode()[0]
    print(f"  Mode (Yếu vị): {mode_val:.4f}")
except:
    print(f"  Mode (Yếu vị): Không xác định")

print(f"\n  Variance (Phương sai): {t1_data.var():.4f}")
print(f"  Std Dev (Độ lệch chuẩn): {t1_data.std():.4f}")
print(f"  Range (Khoảng): {t1_data.max() - t1_data.min():.4f}")
print(f"  Min: {t1_data.min():.4f}")
print(f"  Max: {t1_data.max():.4f}")

# 1.2 Percentiles
print(f"\n1.2️ 📊 PERCENTILES VÀ QUARTILES:")
q1 = t1_data.quantile(0.25)
q2 = t1_data.quantile(0.50)
q3 = t1_data.quantile(0.75)
p10 = t1_data.quantile(0.10)
p90 = t1_data.quantile(0.90)
iqr = q3 - q1

print(f"  P10 (10th percentile): {p10:.4f}")
print(f"  Q1 (25th percentile): {q1:.4f}")
print(f"  Q2 (50th percentile - Median): {q2:.4f}")
print(f"  Q3 (75th percentile): {q3:.4f}")
print(f"  P90 (90th percentile): {p90:.4f}")
print(f"  IQR (Q3-Q1): {iqr:.4f}")

# 1.3 Box-plot analysis
print(f"\n1.3️ 📦 BOX-PLOT ANALYSIS (10 Đại lượng chính):")
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr
outliers_lower = t1_data[t1_data < lower_fence]
outliers_upper = t1_data[t1_data > upper_fence]

print(f"  1. Minimum (excluding outliers): {max(t1_data.min(), lower_fence):.4f}")
print(f"  2. Lower Fence (Q1 - 1.5*IQR): {lower_fence:.4f}")
print(f"  3. Q1 (First Quartile): {q1:.4f}")
print(f"  4. Q2 (Median): {q2:.4f}")
print(f"  5. Q3 (Third Quartile): {q3:.4f}")
print(f"  6. Upper Fence (Q3 + 1.5*IQR): {upper_fence:.4f}")
print(f"  7. Maximum (excluding outliers): {min(t1_data.max(), upper_fence):.4f}")
print(f"  8. IQR (Q3-Q1): {iqr:.4f}")
print(f"  9. Range (Max-Min): {t1_data.max() - t1_data.min():.4f}")
print(f"  10. Outliers count: {len(outliers_lower) + len(outliers_upper)}")

# 1.4 Skewness & Kurtosis
print(f"\n1.4️ 🔍 ĐẶC TRƯNG PHÂN PHỐI:")
skewness = skew(t1_data)
kurt = kurtosis(t1_data)

print(f"  Skewness (Độ lệch): {skewness:.4f}")
if abs(skewness) < 0.5:
    print(f"    → Phân phối gần đối xứng")
elif skewness > 0.5:
    print(f"    → Phân phối lệch phải (right-skewed)")
else:
    print(f"    → Phân phối lệch trái (left-skewed)")

print(f"\n  Kurtosis (Độ nhọn): {kurt:.4f}")
if kurt > 3:
    print(f"    → Phân phối leptokurtic (nhiều dữ liệu ở tâm, đuôi dài)")
elif kurt < 3:
    print(f"    → Phân phối platykurtic (phẳng hơn bình thường)")
else:
    print(f"    → Phân phối mesokurtic (bình thường)")

# 1.5 Normality test
print(f"\n1.5️ ✅ KIỂM ĐỊNH CHUẨN (Shapiro-Wilk Test):")
stat, p_value = shapiro(t1_data)
print(f"  Test Statistic: {stat:.6f}")
print(f"  P-value: {p_value:.6f}")
if p_value > 0.05:
    print(f"  → ✓ Dữ liệu tuân theo phân phối chuẩn (p > 0.05)")
else:
    print(f"  → ✗ Dữ liệu KHÔNG tuân theo phân phối chuẩn (p < 0.05)")

# 1.6 Box-plot visualization
fig, ax = plt.subplots(figsize=(10, 7))
bp = ax.boxplot(t1_data, vert=True, patch_artist=True, widths=0.5,
                boxprops=dict(facecolor='lightblue', color='black', linewidth=2),
                whiskerprops=dict(color='black', linewidth=1.5),
                capprops=dict(color='black', linewidth=1.5),
                medianprops=dict(color='red', linewidth=2))
ax.set_ylabel('T1 Score', fontsize=12, fontweight='bold')
ax.set_title('1.6: Box-Plot của T1 (Điểm Toán) - 10 Đại lượng chính', 
             fontsize=13, fontweight='bold')
ax.grid(axis='y', alpha=0.3)

# Thêm text hiển thị các giá trị
ax.text(1.15, q3, f'Q3={q3:.2f}', fontsize=10, fontweight='bold')
ax.text(1.15, q2, f'Q2={q2:.2f}', fontsize=10, fontweight='bold', color='red')
ax.text(1.15, q1, f'Q1={q1:.2f}', fontsize=10, fontweight='bold')
ax.text(1.15, upper_fence, f'UF={upper_fence:.2f}', fontsize=9)
ax.text(1.15, lower_fence, f'LF={lower_fence:.2f}', fontsize=9)

plt.tight_layout()
plt.savefig('Part5_Q1_BoxPlot_T1.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: Part5_Q1_BoxPlot_T1.png\n")
plt.close()

# 1.7 Histogram with density
fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(t1_data, bins=20, color='skyblue', edgecolor='navy', alpha=0.7, density=True)
ax.axvline(t1_data.mean(), color='red', linestyle='--', linewidth=2, 
           label=f'Mean: {t1_data.mean():.2f}')
ax.axvline(t1_data.median(), color='green', linestyle='--', linewidth=2, 
           label=f'Median: {t1_data.median():.2f}')
ax.set_title('1.7: Histogram của T1 - Hình dáng phân phối', fontsize=13, fontweight='bold')
ax.set_xlabel('T1 Score')
ax.set_ylabel('Density')
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('Part5_Q1_Histogram_T1.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part5_Q1_Histogram_T1.png\n")
plt.close()

# 1.8 QQ-plot
fig, ax = plt.subplots(figsize=(10, 8))
probplot(t1_data, dist="norm", plot=ax)
ax.set_title('1.8: QQ-Plot của T1 - Kiểm chứng phân phối chuẩn', 
             fontsize=13, fontweight='bold')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('Part5_Q1_QQPlot_T1.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part5_Q1_QQPlot_T1.png\n")
plt.close()

# ============= YÊU CẦU 2: PHÂN PHỐI T1 THEO NHÓM phanloait1 =============
print("\n📊 YÊU CẦU 2: Phân phối T1 theo nhóm phân lớp (phanloait1)")
print("="*80)

classifications = sorted(df['phanloait1'].unique())
num_classes = len(classifications)

fig, axes = plt.subplots(num_classes, 3, figsize=(16, 4*num_classes))
if num_classes == 1:
    axes = axes.reshape(1, -1)

for idx, classification in enumerate(classifications):
    data = df[df['phanloait1'] == classification]['T1']
    
    print(f"\n  {classification}:")
    print(f"    n = {len(data)}")
    print(f"    Mean = {data.mean():.4f}, Std = {data.std():.4f}")
    
    # Box plot
    bp = axes[idx, 0].boxplot(data, vert=True, patch_artist=True)
    bp['boxes'][0].set_facecolor('lightblue')
    axes[idx, 0].set_ylabel('T1 Score')
    axes[idx, 0].set_title(f'{classification} - Box Plot\n(n={len(data)})', 
                           fontsize=11, fontweight='bold')
    axes[idx, 0].grid(axis='y', alpha=0.3)
    
    # Histogram
    axes[idx, 1].hist(data, bins=10, color='lightblue', edgecolor='navy', alpha=0.7)
    axes[idx, 1].axvline(data.mean(), color='red', linestyle='--', linewidth=2)
    axes[idx, 1].set_title(f'{classification} - Histogram\n(Mean={data.mean():.2f})', 
                           fontsize=11, fontweight='bold')
    axes[idx, 1].set_ylabel('Frequency')
    axes[idx, 1].grid(axis='y', alpha=0.3)
    
    # QQ-plot
    probplot(data, dist="norm", plot=axes[idx, 2])
    axes[idx, 2].set_title(f'{classification} - QQ-Plot', fontsize=11, fontweight='bold')
    axes[idx, 2].grid(True, alpha=0.3)

plt.suptitle('YÊU CẦU 2: Phân phối T1 theo nhóm phân lớp (phanloait1)', 
             fontsize=14, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig('Part5_Q2_Distribution_By_Classification.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: Part5_Q2_Distribution_By_Classification.png\n")
plt.close()

# ============= YÊU CẦU 3: TƯƠNG QUAN DH1 VS T1 =============
print("\n📊 YÊU CẦU 3: Khảo sát tương quan giữa DH1 và T1")
print("="*80)

covariance = np.cov(df['DH1'], df['T1'])[0, 1]
correlation = df['DH1'].corr(df['T1'])

print(f"\n  Covariance (DH1, T1): {covariance:.6f}")
print(f"  Pearson Correlation: {correlation:.6f}")

if abs(correlation) < 0.3:
    print(f"  → Tương quan yếu")
elif abs(correlation) < 0.7:
    print(f"  → Tương quan vừa phải")
else:
    print(f"  → Tương quan mạnh")

if correlation > 0:
    print(f"  → Tương quan dương: Khi T1 tăng, DH1 có xu hướng tăng")
else:
    print(f"  → Tương quan âm: Khi T1 tăng, DH1 có xu hướng giảm")

# Scatter plot with regression line
fig, ax = plt.subplots(figsize=(12, 7))
ax.scatter(df['T1'], df['DH1'], alpha=0.6, s=50, color='#2E86AB', edgecolors='black', linewidth=0.5)

# Regression line
z = np.polyfit(df['T1'], df['DH1'], 1)
p = np.poly1d(z)
x_sorted = df['T1'].sort_values()
ax.plot(x_sorted, p(x_sorted), "r--", linewidth=2.5, 
        label=f'Regression: DH1={z[0]:.3f}*T1+{z[1]:.3f}')

# Slope and R-squared
slope = z[0]
r_squared = correlation ** 2

ax.set_title(f'YÊU CẦU 3: Scatter Plot - DH1 vs T1\n(r={correlation:.4f}, R²={r_squared:.4f}, slope={slope:.4f})', 
             fontsize=13, fontweight='bold')
ax.set_xlabel('T1 (Independent Variable)', fontsize=11)
ax.set_ylabel('DH1 (Dependent Variable)', fontsize=11)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('Part5_Q3_Scatter_DH1_vs_T1.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part5_Q3_Scatter_DH1_vs_T1.png\n")
plt.close()

# ============= YÊU CẦU 4: TƯƠNG QUAN DH1 VS T1 THEO KHU VỰC =============
print("\n📊 YÊU CẦU 4: Tương quan DH1 vs T1 theo từng nhóm khu vực")
print("="*80)

regions = sorted(df['KV'].unique())
num_regions = len(regions)

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
axes = axes.flatten()

for idx, region in enumerate(regions):
    region_data = df[df['KV'] == region]
    corr = region_data['DH1'].corr(region_data['T1'])
    
    axes[idx].scatter(region_data['T1'], region_data['DH1'], 
                     alpha=0.6, s=50, color='#2E86AB', edgecolors='black', linewidth=0.5)
    
    # Regression line
    if len(region_data) > 1:
        z = np.polyfit(region_data['T1'], region_data['DH1'], 1)
        p = np.poly1d(z)
        x_sorted = region_data['T1'].sort_values()
        axes[idx].plot(x_sorted, p(x_sorted), "r--", linewidth=2, alpha=0.8)
    
    axes[idx].set_title(f'Region {region}\n(n={len(region_data)}, r={corr:.4f})', 
                       fontsize=11, fontweight='bold')
    axes[idx].set_xlabel('T1')
    axes[idx].set_ylabel('DH1')
    axes[idx].grid(True, alpha=0.3)
    
    print(f"  Region {region}:")
    print(f"    Count: {len(region_data)}")
    print(f"    Correlation: {corr:.6f}")

# Hide extra subplots
for idx in range(num_regions, len(axes)):
    axes[idx].set_visible(False)

plt.suptitle('YÊU CẦU 4: Tương quan DH1 vs T1 theo Khu vực (KV)', 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('Part5_Q4_Correlation_By_Region.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: Part5_Q4_Correlation_By_Region.png\n")
plt.close()

# ============= YÊU CẦU 5: TƯƠNG QUAN DH1, DH2, DH3 =============
print("\n📊 YÊU CẦU 5: Khảo sát tương quan giữa DH1, DH2, DH3")
print("="*80)

dh_data = df[['DH1', 'DH2', 'DH3']]

# Correlation matrix
corr_matrix = dh_data.corr()
print("\n  CORRELATION MATRIX:")
print(corr_matrix.round(4))

# Covariance matrix
cov_matrix = dh_data.cov()
print("\n  COVARIANCE MATRIX:")
print(cov_matrix.round(4))

print("\n  Nhận xét tương quan:")
print(f"    - DH1 & DH2: r = {corr_matrix.loc['DH1', 'DH2']:.4f}", end="")
if abs(corr_matrix.loc['DH1', 'DH2']) < 0.3:
    print(" (yếu)")
elif abs(corr_matrix.loc['DH1', 'DH2']) < 0.7:
    print(" (vừa phải)")
else:
    print(" (mạnh)")

print(f"    - DH1 & DH3: r = {corr_matrix.loc['DH1', 'DH3']:.4f}", end="")
if abs(corr_matrix.loc['DH1', 'DH3']) < 0.3:
    print(" (yếu)")
elif abs(corr_matrix.loc['DH1', 'DH3']) < 0.7:
    print(" (vừa phải)")
else:
    print(" (mạnh)")

print(f"    - DH2 & DH3: r = {corr_matrix.loc['DH2', 'DH3']:.4f}", end="")
if abs(corr_matrix.loc['DH2', 'DH3']) < 0.3:
    print(" (yếu)")
elif abs(corr_matrix.loc['DH2', 'DH3']) < 0.7:
    print(" (vừa phải)")
else:
    print(" (mạnh)")

# 5.1 Heatmap
fig, ax = plt.subplots(figsize=(8, 7))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=2, cbar_kws={"shrink": 0.8},
            vmin=-1, vmax=1, ax=ax, fmt='.3f', cbar=True)
ax.set_title('5.1: Correlation Matrix - DH1, DH2, DH3', fontsize=13, fontweight='bold')

plt.tight_layout()
plt.savefig('Part5_Q5a_Correlation_Matrix.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: Part5_Q5a_Correlation_Matrix.png\n")
plt.close()

# 5.2 Scatter plot matrix
fig, axes = plt.subplots(3, 3, figsize=(14, 14))

variables = ['DH1', 'DH2', 'DH3']
for i, var1 in enumerate(variables):
    for j, var2 in enumerate(variables):
        ax = axes[i, j]
        
        if i == j:
            # Diagonal: histogram
            ax.hist(df[var1], bins=15, color='lightblue', edgecolor='navy', alpha=0.7)
            ax.set_ylabel('Frequency')
        else:
            # Off-diagonal: scatter plot
            ax.scatter(df[var2], df[var1], alpha=0.5, s=30, color='#2E86AB', edgecolors='black', linewidth=0.3)
            
            # Regression line
            z = np.polyfit(df[var2], df[var1], 1)
            p = np.poly1d(z)
            x_sorted = df[var2].sort_values()
            ax.plot(x_sorted, p(x_sorted), "r--", linewidth=1.5, alpha=0.7)
        
        if i == 2:
            ax.set_xlabel(var2)
        if j == 0:
            ax.set_ylabel(var1)
        ax.grid(True, alpha=0.3)

plt.suptitle('5.2: Scatter Plot Matrix - DH1, DH2, DH3', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('Part5_Q5b_Scatter_Matrix.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part5_Q5b_Scatter_Matrix.png\n")
plt.close()

# ============= BIỂU ĐỒ TỔNG HỢP =============
print("\n📊 Tạo biểu đồ tổng hợp toàn bộ Phần 5...")

fig = plt.figure(figsize=(20, 14))
gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.35)

# Q1 - Box plot
ax1 = fig.add_subplot(gs[0, 0])
bp = ax1.boxplot(t1_data, vert=True, patch_artist=True)
bp['boxes'][0].set_facecolor('lightblue')
ax1.set_title('Q1a: Box Plot - T1', fontsize=11, fontweight='bold')
ax1.grid(axis='y', alpha=0.3)

# Q1 - Histogram
ax2 = fig.add_subplot(gs[0, 1])
ax2.hist(t1_data, bins=15, color='skyblue', edgecolor='navy', alpha=0.7)
ax2.axvline(t1_data.mean(), color='red', linestyle='--', linewidth=1.5, label='Mean')
ax2.set_title('Q1b: Histogram - T1', fontsize=11, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)
ax2.legend(fontsize=9)

# Q1 - QQ-plot
ax3 = fig.add_subplot(gs[0, 2])
probplot(t1_data, dist="norm", plot=ax3)
ax3.set_title('Q1c: QQ-Plot - T1', fontsize=11, fontweight='bold')
ax3.grid(True, alpha=0.3)

# Q3 - Scatter DH1 vs T1
ax4 = fig.add_subplot(gs[1, :2])
ax4.scatter(df['T1'], df['DH1'], alpha=0.6, s=30, color='#2E86AB', edgecolors='black', linewidth=0.3)
z = np.polyfit(df['T1'], df['DH1'], 1)
p = np.poly1d(z)
x_sorted = df['T1'].sort_values()
ax4.plot(x_sorted, p(x_sorted), "r--", linewidth=2)
ax4.set_title(f'Q3: Scatter - DH1 vs T1 (r={correlation:.4f})', fontsize=11, fontweight='bold')
ax4.set_xlabel('T1')
ax4.set_ylabel('DH1')
ax4.grid(True, alpha=0.3)

# Q5 - Correlation heatmap
ax5 = fig.add_subplot(gs[1, 2])
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, ax=ax5, fmt='.2f', cbar=False)
ax5.set_title('Q5: Correlation Matrix', fontsize=11, fontweight='bold')

# Q2 - Classification distributions (3 subplots)
for idx, classification in enumerate(classifications[:3]):
    ax = fig.add_subplot(gs[2, idx])
    data = df[df['phanloait1'] == classification]['T1']
    ax.hist(data, bins=8, color='lightblue', edgecolor='navy', alpha=0.7)
    ax.set_title(f'Q2: {classification}\n(n={len(data)})', fontsize=10, fontweight='bold')
    ax.set_ylabel('Frequency')
    ax.grid(axis='y', alpha=0.3)

plt.suptitle('PHẦN 5: MỐ TẢ DỮ LIỆU VÀ KHẢO SÁT DẠNG PHÂN PHỐI', 
             fontsize=16, fontweight='bold', y=0.995)

plt.savefig('Part5_Summary_All_Questions.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part5_Summary_All_Questions.png\n")
plt.close()

print("\n" + "="*80)
print("✓ TẤT CẢ CÁC BIỂU ĐỒ PHẦN 5 ĐÃ ĐƯỢC XUẤT THÀNH CÔNG!")
print("="*80)
print("\nDanh sách biểu đồ Phần 5:")
print("1. Part5_Q1_BoxPlot_T1.png - Box-plot của T1 (10 đại lượng)")
print("2. Part5_Q1_Histogram_T1.png - Histogram của T1")
print("3. Part5_Q1_QQPlot_T1.png - QQ-Plot của T1")
print("4. Part5_Q2_Distribution_By_Classification.png - Phân phối T1 theo nhóm")
print("5. Part5_Q3_Scatter_DH1_vs_T1.png - Scatter plot: DH1 vs T1")
print("6. Part5_Q4_Correlation_By_Region.png - Tương quan DH1 vs T1 theo khu vực")
print("7. Part5_Q5a_Correlation_Matrix.png - Ma trận tương quan DH1, DH2, DH3")
print("8. Part5_Q5b_Scatter_Matrix.png - Scatter plot matrix")
print("9. Part5_Summary_All_Questions.png - Tóm tắt tất cả yêu cầu")
print("="*80)

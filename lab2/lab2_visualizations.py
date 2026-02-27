#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis, shapiro, probplot
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

print("Tạo biểu đồ Lab 2...")

# ============= PHẦN 1: THỐNG KÊ DỮ LIỆU =============
fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(df['DH1'], bins=15, color='steelblue', edgecolor='navy', alpha=0.7)
ax.axvline(df['DH1'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["DH1"].mean():.2f}')
ax.axvline(df['DH1'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: {df["DH1"].median():.2f}')
ax.set_title('PHẦN 1: Phân phối DH1 (Exam Score Distribution)', fontsize=14, fontweight='bold')
ax.set_xlabel('DH1 Score')
ax.set_ylabel('Frequency')
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('Chart_1_DH1_Distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Chart_1_DH1_Distribution.png")
plt.close()

# ============= PHẦN 2: TRÌNH BÀY DỮ LIỆU - GT (GIỚI TÍNH) =============
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart
gt_freq = df['GT'].value_counts()
gt_freq.plot(kind='bar', ax=axes[0], color=['#FF6B9D', '#4A90E2'], edgecolor='black', linewidth=1.5)
axes[0].set_title('2.1: Tần số Giới tính (Gender)', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Gender')
axes[0].set_ylabel('Count')
axes[0].set_xticklabels(['Nam (M)', 'Nữ (F)'], rotation=0)
axes[0].grid(axis='y', alpha=0.3)

# Pie chart
colors = ['#FF6B9D', '#4A90E2']
axes[1].pie(gt_freq.values, labels=['Nam (M)', 'Nữ (F)'], autopct='%1.1f%%', 
            colors=colors, startangle=90, textprops={'fontsize': 11})
axes[1].set_title('2.1: Tỷ lệ Giới tính (%)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('Chart_2_Gender_Distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Chart_2_Gender_Distribution.png")
plt.close()

# ============= PHẦN 2: US_TBM1, US_TBM2, US_TBM3 =============
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
us_vars = ['US_TBM1', 'US_TBM2', 'US_TBM3']

for i, var in enumerate(us_vars):
    freq = df[var].value_counts().sort_index()
    axes[i].bar(freq.index, freq.values, color='skyblue', edgecolor='navy', linewidth=1.5)
    axes[i].set_title(f'2.2: Distribution of {var}', fontsize=11, fontweight='bold')
    axes[i].set_xlabel(var)
    axes[i].set_ylabel('Frequency')
    axes[i].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('Chart_3_US_TBM_Distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Chart_3_US_TBM_Distribution.png")
plt.close()

# ============= PHẦN 3: CROSSTAB - KQXT (PASS/FAIL) =============
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# By Gender
kqxt_by_gt = pd.crosstab(df['GT'], df['KQXT'])
kqxt_by_gt.plot(kind='bar', ax=axes[0, 0], color=['#FF6B6B', '#90EE90'], width=0.6)
axes[0, 0].set_title('3.1: KQXT (Pass/Fail) by Gender', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Gender')
axes[0, 0].set_ylabel('Count')
axes[0, 0].legend(['Failed', 'Passed'])
axes[0, 0].tick_params(axis='x', rotation=0)
axes[0, 0].grid(axis='y', alpha=0.3)

# By Exam Type
kqxt_by_kt = pd.crosstab(df['KT'], df['KQXT'])
kqxt_by_kt.plot(kind='bar', ax=axes[0, 1], color=['#FF6B6B', '#90EE90'], width=0.7)
axes[0, 1].set_title('3.2: KQXT (Pass/Fail) by Exam Type', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Exam Type (KT)')
axes[0, 1].set_ylabel('Count')
axes[0, 1].legend(['Failed', 'Passed'])
axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].grid(axis='y', alpha=0.3)

# By Region
kqxt_by_kv = pd.crosstab(df['KV'], df['KQXT'])
kqxt_by_kv.plot(kind='bar', ax=axes[1, 0], color=['#FF6B6B', '#90EE90'], width=0.7)
axes[1, 0].set_title('3.3: KQXT (Pass/Fail) by Region', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Region (KV)')
axes[1, 0].set_ylabel('Count')
axes[1, 0].legend(['Failed', 'Passed'])
axes[1, 0].tick_params(axis='x', rotation=45)
axes[1, 0].grid(axis='y', alpha=0.3)

# Candidates by Region and Exam Type
candidates_by_kv_kt = pd.crosstab(df['KV'], df['KT'])
candidates_by_kv_kt.plot(kind='bar', ax=axes[1, 1], width=0.7)
axes[1, 1].set_title('3.4: Candidates by Region & Exam Type', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Region (KV)')
axes[1, 1].set_ylabel('Count')
axes[1, 1].legend(title='Exam Type', loc='upper right')
axes[1, 1].tick_params(axis='x', rotation=0)
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('Chart_4_KQXT_Analysis.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Chart_4_KQXT_Analysis.png")
plt.close()

# ============= PHẦN 4: BIỂU ĐỒ ĐƯỜNG & PHÂN LOẠI T1 =============
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# 4.1 Simple line chart for T1
axes[0, 0].plot(range(len(df)), df['T1'].values, marker='o', linestyle='-', linewidth=1.5, 
        markersize=4, color='#2E86AB', alpha=0.8)
axes[0, 0].set_title('4.1: Simple Line Chart - T1 Scores', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Student Index')
axes[0, 0].set_ylabel('T1 Score')
axes[0, 0].grid(True, alpha=0.3)

# 4.2 Frequency of phanloait1
phanloait1_freq = df['phanloait1'].value_counts()
colors_map = {'kém (k)': '#FF6B6B', 'trung bình (tb)': '#87CEEB', 'khá (k)': '#FFD700', 'giỏi (g)': '#90EE90'}
colors = [colors_map.get(level, '#CCCCCC') for level in phanloait1_freq.index]
axes[0, 1].bar(phanloait1_freq.index, phanloait1_freq.values, color=colors, edgecolor='black', linewidth=1.5)
axes[0, 1].set_title('4.2: T1 Classification Distribution (phanloait1)', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Classification')
axes[0, 1].set_ylabel('Count')
axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].grid(axis='y', alpha=0.3)

# 4.3 Multiple line chart by classification
colors_line = {'kém (k)': '#FF6B6B', 'trung bình (tb)': '#4ECDC4', 'giỏi (g)': '#95E1D3'}
for classification in df['phanloait1'].unique():
    data = df[df['phanloait1'] == classification]
    axes[1, 0].plot(data.index, data['T1'].values, marker='o', linestyle='-', linewidth=1.5,
            markersize=5, label=classification, color=colors_line.get(classification, '#999999'), alpha=0.7)
axes[1, 0].set_title('4.3: Multiple Line Chart - T1 by Classification', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Student Index')
axes[1, 0].set_ylabel('T1 Score')
axes[1, 0].legend(loc='best')
axes[1, 0].grid(True, alpha=0.3)

# 4.4 Drop-line chart
x_baseline = np.arange(len(df))
for classification in df['phanloait1'].unique():
    data = df[df['phanloait1'] == classification]
    axes[1, 1].vlines(data.index, 0, data['T1'].values, colors=colors_line.get(classification, '#999999'), 
              linewidth=2, alpha=0.7, label=classification)
    axes[1, 1].scatter(data.index, data['T1'].values, color=colors_line.get(classification, '#999999'), 
               s=40, zorder=3)
axes[1, 1].axhline(y=0, color='black', linewidth=1)
axes[1, 1].set_title('4.4: Drop-line Chart - T1 by Classification', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Student Index')
axes[1, 1].set_ylabel('T1 Score')
axes[1, 1].legend(loc='best')
axes[1, 1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('Chart_5_Advanced_Visualization.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Chart_5_Advanced_Visualization.png")
plt.close()

# ============= PHẦN 5: PHÂN PHỐI VÀ TƯƠNG QUAN =============
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 5.1 Box plot
bp = axes[0, 0].boxplot(df['T1'], vert=True, patch_artist=True, widths=0.5)
bp['boxes'][0].set_facecolor('lightblue')
axes[0, 0].set_ylabel('T1 Score')
axes[0, 0].set_title('5.1: Box Plot - T1 Distribution', fontsize=12, fontweight='bold')
axes[0, 0].grid(axis='y', alpha=0.3)

# 5.2 Histogram with normal curve
axes[0, 1].hist(df['T1'], bins=20, color='skyblue', edgecolor='navy', alpha=0.7, density=True)
axes[0, 1].axvline(df['T1'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["T1"].mean():.2f}')
axes[0, 1].axvline(df['T1'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: {df["T1"].median():.2f}')
axes[0, 1].set_title('5.2: Histogram - T1 Scores', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('T1 Score')
axes[0, 1].set_ylabel('Density')
axes[0, 1].legend()
axes[0, 1].grid(axis='y', alpha=0.3)

# 5.3 QQ-Plot
probplot(df['T1'], dist="norm", plot=axes[1, 0])
axes[1, 0].set_title('5.3: QQ-Plot - T1 vs Normal Distribution', fontsize=12, fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)

# 5.4 Scatter plot - DH1 vs T1 with regression line
axes[1, 1].scatter(df['T1'], df['DH1'], alpha=0.6, s=50, color='#2E86AB')
z = np.polyfit(df['T1'], df['DH1'], 1)
p = np.poly1d(z)
x_sorted = df['T1'].sort_values()
axes[1, 1].plot(x_sorted, p(x_sorted), "r--", linewidth=2, label=f'Regression: y={z[0]:.3f}x+{z[1]:.3f}')
correlation = df['DH1'].corr(df['T1'])
axes[1, 1].set_title(f'5.4: Scatter Plot - DH1 vs T1 (r={correlation:.4f})', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('T1 Score')
axes[1, 1].set_ylabel('DH1 Score')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('Chart_6_Distribution_Analysis.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Chart_6_Distribution_Analysis.png")
plt.close()

# ============= PHẦN 5.5: CORRELATION MATRIX & SCATTER MATRIX =============
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Correlation heatmap
dh_data = df[['DH1', 'DH2', 'DH3']]
corr_matrix = dh_data.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=2, cbar_kws={"shrink": 0.8},
            vmin=-1, vmax=1, ax=axes[0], fmt='.3f')
axes[0].set_title('5.5: Correlation Matrix - DH1, DH2, DH3', fontsize=12, fontweight='bold')

# Scatter matrix (manual)
dh_vars = ['DH1', 'DH2', 'DH3']
axes[1].scatter(df['DH1'], df['DH2'], alpha=0.6, s=50, color='#2E86AB', label='DH1 vs DH2')
axes[1].scatter(df['DH1'], df['DH3'], alpha=0.6, s=50, color='#FF6B6B', label='DH1 vs DH3', marker='^')
axes[1].scatter(df['DH2'], df['DH3'], alpha=0.6, s=50, color='#90EE90', label='DH2 vs DH3', marker='s')
axes[1].set_title('5.5: Multi-Scatter Plot - DH1, DH2, DH3', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Exam Scores')
axes[1].set_ylabel('Exam Scores')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('Chart_7_Correlation_Matrix.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Chart_7_Correlation_Matrix.png")
plt.close()

# ============= PHẦN 5: DISTRIBUTION BY phanloait1 =============
classifications = sorted(df['phanloait1'].unique())
num_classes = len(classifications)
fig, axes = plt.subplots(1, num_classes, figsize=(5*num_classes, 5))
if num_classes == 1:
    axes = [axes]

for idx, classification in enumerate(classifications):
    data = df[df['phanloait1'] == classification]['T1']
    axes[idx].hist(data, bins=10, color='lightblue', edgecolor='navy', alpha=0.7)
    axes[idx].axvline(data.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {data.mean():.2f}')
    axes[idx].set_title(f'Distribution - {classification}\n(n={len(data)})', fontsize=11, fontweight='bold')
    axes[idx].set_xlabel('T1 Score')
    axes[idx].set_ylabel('Frequency')
    axes[idx].legend()
    axes[idx].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('Chart_8_Distribution_by_Classification.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Chart_8_Distribution_by_Classification.png")
plt.close()

# ============= CORRELATION BY REGION =============
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
axes = axes.flatten()

regions = sorted(df['KV'].unique())
for idx, region in enumerate(regions):
    region_data = df[df['KV'] == region]
    corr = region_data['DH1'].corr(region_data['T1'])
    
    axes[idx].scatter(region_data['T1'], region_data['DH1'], 
                     alpha=0.6, s=50, color='#2E86AB')
    
    if len(region_data) > 1:
        z = np.polyfit(region_data['T1'], region_data['DH1'], 1)
        p = np.poly1d(z)
        x_sorted = region_data['T1'].sort_values()
        axes[idx].plot(x_sorted, p(x_sorted), "r--", linewidth=2)
    
    axes[idx].set_title(f'Region {region}\n(n={len(region_data)}, r={corr:.4f})', 
                       fontsize=11, fontweight='bold')
    axes[idx].set_xlabel('T1')
    axes[idx].set_ylabel('DH1')
    axes[idx].grid(True, alpha=0.3)

# Hide extra subplot
axes[-1].set_visible(False)

plt.tight_layout()
plt.savefig('Chart_9_Correlation_by_Region.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Chart_9_Correlation_by_Region.png")
plt.close()

print("\n" + "="*70)
print("✓ TẤT CẢ CÁC BIỂU ĐỒ ĐÃ ĐƯỢC XUẤT THÀNH CÔNG!")
print("="*70)
print("\nDanh sách biểu đồ:")
print("1. Chart_1_DH1_Distribution.png - Phần 1: Phân phối DH1")
print("2. Chart_2_Gender_Distribution.png - Phần 2: Giới tính (Bar + Pie)")
print("3. Chart_3_US_TBM_Distribution.png - Phần 2: US_TBM1, US_TBM2, US_TBM3")
print("4. Chart_4_KQXT_Analysis.png - Phần 3: KQXT theo Gender, KT, KV")
print("5. Chart_5_Advanced_Visualization.png - Phần 4: Line, Multi-line, Drop-line")
print("6. Chart_6_Distribution_Analysis.png - Phần 5: Box, Histogram, QQ, Scatter")
print("7. Chart_7_Correlation_Matrix.png - Phần 5.5: Correlation & Multi-scatter")
print("8. Chart_8_Distribution_by_Classification.png - Phần 5: Distribution by phanloait1")
print("9. Chart_9_Correlation_by_Region.png - Phần 5: Correlation by Region")
print("="*70)

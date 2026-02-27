#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHẦN 4: TRỰC QUAN HÓA DỮ LIỆU NÂNG CAO
Lab 2 - Trực quan hóa dữ liệu xử lý điểm thi đại học
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10

# Load data
df = pd.read_csv('processed_dulieuxettuyendaihoc.csv')

print("="*70)
print("PHẦN 4: TRỰC QUAN HÓA DỮ LIỆU NÂNG CAO")
print("="*70)

# ============= YÊU CẦU 1: SIMPLE LINE CHART CHO T1 =============
print("\n📊 Yêu cầu 1: Vẽ biểu đồ đường Simple cho biến T1...")

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(range(len(df)), df['T1'].values, marker='o', linestyle='-', linewidth=1.5, 
        markersize=4, color='#2E86AB', alpha=0.8)
ax.fill_between(range(len(df)), df['T1'].values, alpha=0.2, color='#2E86AB')
ax.set_title('Yêu cầu 1: Simple Line Chart - T1 (Điểm Toán) của từng học sinh', 
             fontsize=13, fontweight='bold')
ax.set_xlabel('Student Index')
ax.set_ylabel('T1 Score')
ax.grid(True, alpha=0.3)

# Thêm min, max, mean line
ax.axhline(y=df['T1'].mean(), color='red', linestyle='--', linewidth=2, 
           label=f'Mean: {df["T1"].mean():.2f}')
ax.axhline(y=df['T1'].max(), color='green', linestyle='--', linewidth=1.5, 
           label=f'Max: {df["T1"].max():.2f}', alpha=0.7)
ax.axhline(y=df['T1'].min(), color='orange', linestyle='--', linewidth=1.5, 
           label=f'Min: {df["T1"].min():.2f}', alpha=0.7)
ax.legend(loc='best', fontsize=10)

plt.tight_layout()
plt.savefig('Part4_Q1_Simple_Line_Chart_T1.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part4_Q1_Simple_Line_Chart_T1.png\n")
plt.close()

# ============= YÊU CẦU 2: TẠO BIẾN PHÂN LOẠI phanloait1 =============
print("📊 Yêu cầu 2: Tạo biến phân loại (phanloait1) cho T1...")
print("  Tiêu chí phân loại:")
print("    a. 0 ≤ T1 < 5  => kém (k)")
print("    b. 5 ≤ T1 < 7  => trung bình (tb)")
print("    c. 7 ≤ T1 < 8  => khá (k)")
print("    d. T1 ≥ 8      => giỏi (g)")

def classify_t1(score):
    """Phân loại T1 theo tiêu chí"""
    if score < 5:
        return 'kém (k)'
    elif score < 7:
        return 'trung bình (tb)'
    elif score < 8:
        return 'khá (k)'
    else:
        return 'giỏi (g)'

df['phanloait1'] = df['T1'].apply(classify_t1)

print("\n  Phân loại đã được tạo!")
print(f"  Sample classification:")
print(df[['STT', 'T1', 'phanloait1']].head(15).to_string(index=False))

# ============= YÊU CẦU 3: BẢNG TẦN SỐ CHO phanloait1 =============
print("\n📊 Yêu cầu 3: Lập bảng tần số cho biến phanloait1...")

phanloait1_freq = df['phanloait1'].value_counts().sort_index()
phanloait1_relative = df['phanloait1'].value_counts(normalize=True).sort_index() * 100

freq_table = pd.DataFrame({
    'Phân loại': phanloait1_freq.index,
    'Tần số': phanloait1_freq.values,
    'Tần suất (%)': phanloait1_relative.values
}).reset_index(drop=True)

print("\n  Bảng tần số - Phân loại T1:")
print(freq_table.to_string(index=False))

# Visualize frequency table as bar chart
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart for frequency
colors_list = ['#FF6B6B', '#90EE90', '#FFD700', '#87CEEB']
axes[0].bar(phanloait1_freq.index, phanloait1_freq.values, color=colors_list, 
            edgecolor='black', linewidth=1.5)
axes[0].set_title('Yêu cầu 3a: Bảng Tần số - Phân loại T1', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Phân loại')
axes[0].set_ylabel('Tần số')
axes[0].grid(axis='y', alpha=0.3)

# Thêm số lượng trên các cột
for i, (idx, val) in enumerate(phanloait1_freq.items()):
    axes[0].text(i, val, f'{int(val)}', ha='center', va='bottom', fontweight='bold', fontsize=11)

# Pie chart for relative frequency
axes[1].pie(phanloait1_freq.values, labels=phanloait1_freq.index, autopct='%1.1f%%',
            colors=colors_list, startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'})
axes[1].set_title('Yêu cầu 3b: Tỷ lệ (%) - Phân loại T1', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('Part4_Q3_Frequency_Table_phanloait1.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: Part4_Q3_Frequency_Table_phanloait1.png\n")
plt.close()

# ============= YÊU CẦU 4: MULTIPLE LINE CHART =============
print("📊 Yêu cầu 4: Vẽ biểu đồ đường Multiple Line cho T1 phân loại bởi phanloait1...")

fig, ax = plt.subplots(figsize=(14, 7))

# Define colors for each classification
colors_map = {
    'kém (k)': '#FF6B6B',
    'trung bình (tb)': '#4ECDC4',
    'khá (k)': '#FFD700',
    'giỏi (g)': '#90EE90'
}

# Plot line for each classification
for classification in sorted(df['phanloait1'].unique()):
    data = df[df['phanloait1'] == classification]
    ax.plot(data.index, data['T1'].values, marker='o', linestyle='-', linewidth=2,
            markersize=6, label=classification, color=colors_map.get(classification, '#999999'), 
            alpha=0.8)

ax.set_title('Yêu cầu 4: Multiple Line Chart - T1 theo Phân loại (phanloait1)', 
             fontsize=13, fontweight='bold')
ax.set_xlabel('Student Index')
ax.set_ylabel('T1 Score')
ax.legend(loc='best', fontsize=11, title='Phân loại T1', title_fontsize=11)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('Part4_Q4_Multiple_Line_Chart_T1.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part4_Q4_Multiple_Line_Chart_T1.png\n")
plt.close()

# ============= YÊU CẦU 5: DROP-LINE CHART =============
print("📊 Yêu cầu 5: Vẽ biểu đồ Drop-line cho T1 phân loại bởi phanloait1...")

fig, ax = plt.subplots(figsize=(14, 7))

# Plot vertical lines (drop lines) for each student
for classification in sorted(df['phanloait1'].unique()):
    data = df[df['phanloait1'] == classification]
    ax.vlines(data.index, 0, data['T1'].values, colors=colors_map.get(classification, '#999999'), 
              linewidth=2.5, alpha=0.8, label=classification)
    ax.scatter(data.index, data['T1'].values, color=colors_map.get(classification, '#999999'), 
               s=60, zorder=3, edgecolors='black', linewidth=1)

ax.axhline(y=0, color='black', linewidth=1)
ax.set_title('Yêu cầu 5: Drop-line Chart - T1 theo Phân loại (phanloait1)', 
             fontsize=13, fontweight='bold')
ax.set_xlabel('Student Index')
ax.set_ylabel('T1 Score')
ax.legend(loc='best', fontsize=11, title='Phân loại T1', title_fontsize=11)
ax.grid(True, alpha=0.3, axis='y')
ax.set_ylim(bottom=-0.5)

plt.tight_layout()
plt.savefig('Part4_Q5_DropLine_Chart_T1.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part4_Q5_DropLine_Chart_T1.png\n")
plt.close()

# ============= BIỂU ĐỒ TỔNG HỢP PHẦN 4 =============
print("📊 Tạo biểu đồ tổng hợp toàn bộ Phần 4...")

fig = plt.figure(figsize=(18, 12))
gs = fig.add_gridspec(3, 2, hspace=0.35, wspace=0.3)

# Q1 - Simple Line Chart (top, spanning 2 columns)
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(range(len(df)), df['T1'].values, marker='o', linestyle='-', linewidth=1.5, 
         markersize=3, color='#2E86AB', alpha=0.8)
ax1.axhline(y=df['T1'].mean(), color='red', linestyle='--', linewidth=1.5, 
            label=f'Mean: {df["T1"].mean():.2f}', alpha=0.7)
ax1.set_title('Q1: Simple Line Chart - T1 Scores', fontsize=12, fontweight='bold')
ax1.set_ylabel('T1 Score')
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)

# Q3a - Frequency Bar Chart
ax2 = fig.add_subplot(gs[1, 0])
colors_list = ['#FF6B6B', '#90EE90', '#FFD700', '#87CEEB']
ax2.bar(phanloait1_freq.index, phanloait1_freq.values, color=colors_list, 
        edgecolor='black', linewidth=1.2)
ax2.set_title('Q3a: Frequency Table - phanloait1', fontsize=11, fontweight='bold')
ax2.set_ylabel('Frequency')
ax2.grid(axis='y', alpha=0.3)
for i, (idx, val) in enumerate(phanloait1_freq.items()):
    ax2.text(i, val, f'{int(val)}', ha='center', va='bottom', fontweight='bold', fontsize=10)

# Q3b - Pie Chart
ax3 = fig.add_subplot(gs[1, 1])
ax3.pie(phanloait1_freq.values, labels=phanloait1_freq.index, autopct='%1.1f%%',
        colors=colors_list, startangle=90, textprops={'fontsize': 9, 'fontweight': 'bold'})
ax3.set_title('Q3b: Percentage - phanloait1', fontsize=11, fontweight='bold')

# Q4 - Multiple Line Chart
ax4 = fig.add_subplot(gs[2, 0])
for classification in sorted(df['phanloait1'].unique()):
    data = df[df['phanloait1'] == classification]
    ax4.plot(data.index, data['T1'].values, marker='o', linestyle='-', linewidth=1.5,
            markersize=4, label=classification, color=colors_map.get(classification, '#999999'), 
            alpha=0.7)
ax4.set_title('Q4: Multiple Line Chart - T1 by Classification', fontsize=11, fontweight='bold')
ax4.set_ylabel('T1 Score')
ax4.legend(fontsize=8, loc='best')
ax4.grid(True, alpha=0.3)

# Q5 - Drop-line Chart
ax5 = fig.add_subplot(gs[2, 1])
for classification in sorted(df['phanloait1'].unique()):
    data = df[df['phanloait1'] == classification]
    ax5.vlines(data.index, 0, data['T1'].values, colors=colors_map.get(classification, '#999999'), 
              linewidth=1.5, alpha=0.7, label=classification)
    ax5.scatter(data.index, data['T1'].values, color=colors_map.get(classification, '#999999'), 
               s=30, zorder=3)
ax5.axhline(y=0, color='black', linewidth=1)
ax5.set_title('Q5: Drop-line Chart - T1 by Classification', fontsize=11, fontweight='bold')
ax5.set_ylabel('T1 Score')
ax5.legend(fontsize=8, loc='best')
ax5.grid(True, alpha=0.3, axis='y')

plt.suptitle('PHẦN 4: TRỰC QUAN HÓA DỮ LIỆU NÂNG CAO', 
             fontsize=15, fontweight='bold', y=0.995)

plt.savefig('Part4_Summary_All_Questions.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part4_Summary_All_Questions.png\n")
plt.close()

# ============= THỐNG KÊ CHI TIẾT =============
print("="*70)
print("THỐNG KÊ CHI TIẾT PHẦN 4")
print("="*70)

print("\n📈 Thống kê T1 (Điểm Toán):")
print(f"  Mean: {df['T1'].mean():.4f}")
print(f"  Median: {df['T1'].median():.4f}")
print(f"  Std Dev: {df['T1'].std():.4f}")
print(f"  Min: {df['T1'].min():.4f}")
print(f"  Max: {df['T1'].max():.4f}")
print(f"  Q1 (25%): {df['T1'].quantile(0.25):.4f}")
print(f"  Q3 (75%): {df['T1'].quantile(0.75):.4f}")

print("\n📊 Phân loại phanloait1:")
for classification in sorted(df['phanloait1'].unique()):
    count = (df['phanloait1'] == classification).sum()
    percentage = (count / len(df)) * 100
    t1_stats = df[df['phanloait1'] == classification]['T1']
    print(f"\n  {classification}:")
    print(f"    Số lượng: {count} ({percentage:.1f}%)")
    print(f"    T1 range: [{t1_stats.min():.2f}, {t1_stats.max():.2f}]")
    print(f"    T1 mean: {t1_stats.mean():.4f}")
    print(f"    T1 std: {t1_stats.std():.4f}")

print("\n" + "="*70)
print("✓ TẤT CẢ CÁC BIỂU ĐỒ PHẦN 4 ĐÃ ĐƯỢC XUẤT THÀNH CÔNG!")
print("="*70)
print("\nDanh sách biểu đồ Phần 4:")
print("1. Part4_Q1_Simple_Line_Chart_T1.png - Simple line chart cho T1")
print("2. Part4_Q3_Frequency_Table_phanloait1.png - Bảng tần số & tỷ lệ")
print("3. Part4_Q4_Multiple_Line_Chart_T1.png - Multiple line chart theo phân loại")
print("4. Part4_Q5_DropLine_Chart_T1.png - Drop-line chart theo phân loại")
print("5. Part4_Summary_All_Questions.png - Tóm tắt tất cả yêu cầu")
print("="*70)

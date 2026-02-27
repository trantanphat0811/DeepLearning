#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHẦN 3: TRỰC QUAN HÓA DỮ LIỆU THEO NHÓM PHÂN LOẠI
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

# Load data
df = pd.read_csv('processed_dulieuxettuyendaihoc.csv')

print("="*70)
print("PHẦN 3: TRỰC QUAN HÓA DỮ LIỆU THEO NHÓM PHÂN LOẠI")
print("="*70)

# ============= CÂU 1: HỌC SINH NỮ THEO XL1, XL2, XL3 (UNSTACKED) =============
print("\n📊 Câu 1: Trực quan dữ liệu học sinh nữ trên các nhóm XL1, XL2, XL3...")

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

female_data = df[df['GT'] == 'F']
xl_vars = ['XL1', 'XL2', 'XL3']
colors_map = {'Y': '#FFD700', 'TB': '#87CEEB', 'K': '#90EE90', 'G': '#FF6B6B', 'XS': '#FFA500'}
colors_order = ['Y', 'TB', 'K', 'G', 'XS']

for idx, xl_var in enumerate(xl_vars):
    counts = female_data[xl_var].value_counts().reindex(colors_order, fill_value=0)
    colors = [colors_map.get(level, '#CCCCCC') for level in counts.index]
    
    bars = axes[idx].bar(counts.index, counts.values, color=colors, edgecolor='black', linewidth=1.5)
    axes[idx].set_title(f'Học sinh nữ - {xl_var}\n(Unstacked)', fontsize=12, fontweight='bold')
    axes[idx].set_xlabel('Xếp loại')
    axes[idx].set_ylabel('Số lượng học sinh')
    axes[idx].grid(axis='y', alpha=0.3)
    
    # Thêm số lượng trên các cột
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            axes[idx].text(bar.get_x() + bar.get_width()/2., height,
                          f'{int(height)}', ha='center', va='bottom', fontweight='bold')
    
    print(f"  {xl_var} distribution for female students:")
    print(f"    {counts.to_dict()}")

plt.tight_layout()
plt.savefig('Part3_Q1_Female_XL_Classification.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part3_Q1_Female_XL_Classification.png\n")
plt.close()

# ============= CÂU 2: KQXT THEO KHỐI A, A1, B TRONG KHU VỰC 1, 2 =============
print("📊 Câu 2: Trực quan KQXT cho khối A, A1, B thuộc khu vực 1, 2...")

filtered_aab_kv12 = df[
    (df['KT'].isin(['A', 'A1', 'B'])) & 
    (df['KV'].isin([1, 2, '1', '2']))
]

kqxt_counts = pd.crosstab(filtered_aab_kv12['KT'], filtered_aab_kv12['KQXT'])
print(f"  Total records: {len(filtered_aab_kv12)}")
print(f"  KQXT distribution:\n{kqxt_counts}\n")

fig, ax = plt.subplots(figsize=(12, 6))
kqxt_counts.plot(kind='bar', ax=ax, color=['#FF6B6B', '#90EE90'], width=0.7, edgecolor='black', linewidth=1.5)
ax.set_title('Câu 2: Kết quả xét tuyển (KQXT) - Khối A, A1, B trong Khu vực 1, 2', 
             fontsize=13, fontweight='bold')
ax.set_xlabel('Khối thi (KT)')
ax.set_ylabel('Số lượng thí sinh')
ax.legend(['Rớt (0.0)', 'Đậu (1.0)'], loc='upper right', fontsize=10)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.grid(axis='y', alpha=0.3)

# Thêm số lượng trên các cột
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('Part3_Q2_KQXT_By_KT_Region.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part3_Q2_KQXT_By_KT_Region.png\n")
plt.close()

# ============= CÂU 3: SỐ LƯỢNG THÍ SINH THEO KHU VỰC & KHỐI THI =============
print("📊 Câu 3: Trực quan số lượng thí sinh theo khu vực và khối thi...")

candidates_by_kv_kt = pd.crosstab(df['KV'], df['KT'])
print(f"  Candidates by Region (KV) and Exam Type (KT):\n{candidates_by_kv_kt}\n")

fig, ax = plt.subplots(figsize=(12, 6))
candidates_by_kv_kt.plot(kind='bar', ax=ax, width=0.8, edgecolor='black', linewidth=1.5)
ax.set_title('Câu 3: Số lượng thí sinh theo Khu vực (KV) và Khối thi (KT)', 
             fontsize=13, fontweight='bold')
ax.set_xlabel('Khu vực (KV)')
ax.set_ylabel('Số lượng thí sinh')
ax.legend(title='Khối thi (KT)', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('Part3_Q3_Candidates_By_Region_KT.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part3_Q3_Candidates_By_Region_KT.png\n")
plt.close()

# ============= CÂU 4: SỐ LƯỢNG ĐẬU, RỚT THEO KHỐI THI =============
print("📊 Câu 4: Trực quan số lượng thí sinh đậu, rớt theo khối thi...")

kqxt_by_kt = pd.crosstab(df['KT'], df['KQXT'])
print(f"  Pass/Fail by Exam Type (KT):\n{kqxt_by_kt}\n")

fig, ax = plt.subplots(figsize=(12, 6))
kqxt_by_kt.plot(kind='bar', ax=ax, color=['#FF6B6B', '#90EE90'], width=0.7, edgecolor='black', linewidth=1.5)
ax.set_title('Câu 4: Số lượng thí sinh Đậu/Rớt theo Khối thi (KT)', 
             fontsize=13, fontweight='bold')
ax.set_xlabel('Khối thi (KT)')
ax.set_ylabel('Số lượng thí sinh')
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.legend(['Rớt (0.0)', 'Đậu (1.0)'], loc='upper left', fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Thêm số lượng trên các cột
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('Part3_Q4_PassFail_By_KT.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part3_Q4_PassFail_By_KT.png\n")
plt.close()

# ============= CÂU 5: SỐ LƯỢNG ĐẬU, RỚT THEO KHU VỰC =============
print("📊 Câu 5: Trực quan số lượng thí sinh đậu, rớt theo khu vực...")

kqxt_by_kv = pd.crosstab(df['KV'], df['KQXT'])
print(f"  Pass/Fail by Region (KV):\n{kqxt_by_kv}\n")

fig, ax = plt.subplots(figsize=(12, 6))
kqxt_by_kv.plot(kind='bar', ax=ax, color=['#FF6B6B', '#90EE90'], width=0.7, edgecolor='black', linewidth=1.5)
ax.set_title('Câu 5: Số lượng thí sinh Đậu/Rớt theo Khu vực (KV)', 
             fontsize=13, fontweight='bold')
ax.set_xlabel('Khu vực (KV)')
ax.set_ylabel('Số lượng thí sinh')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.legend(['Rớt (0.0)', 'Đậu (1.0)'], loc='upper left', fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Thêm số lượng trên các cột
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('Part3_Q5_PassFail_By_KV.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part3_Q5_PassFail_By_KV.png\n")
plt.close()

# ============= CÂU 6: SỐ LƯỢNG ĐẬU, RỚT THEO DÂN TỘC =============
print("📊 Câu 6: Trực quan số lượng thí sinh đậu, rớt theo dân tộc...")

kqxt_by_dt = pd.crosstab(df['DT'], df['KQXT'])
print(f"  Pass/Fail by Ethnicity (DT):\n{kqxt_by_dt}\n")

fig, ax = plt.subplots(figsize=(12, 6))
kqxt_by_dt.plot(kind='bar', ax=ax, color=['#FF6B6B', '#90EE90'], width=0.7, edgecolor='black', linewidth=1.5)
ax.set_title('Câu 6: Số lượng thí sinh Đậu/Rớt theo Dân tộc (DT)', 
             fontsize=13, fontweight='bold')
ax.set_xlabel('Dân tộc (DT)')
ax.set_ylabel('Số lượng thí sinh')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.legend(['Rớt (0.0)', 'Đậu (1.0)'], loc='upper left', fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Thêm số lượng trên các cột
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('Part3_Q6_PassFail_By_DT.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part3_Q6_PassFail_By_DT.png\n")
plt.close()

# ============= CÂU 7: SỐ LƯỢNG ĐẬU, RỚT THEO GIỚI TÍNH =============
print("📊 Câu 7: Trực quan số lượng thí sinh đậu, rớt theo giới tính...")

kqxt_by_gt = pd.crosstab(df['GT'], df['KQXT'])
print(f"  Pass/Fail by Gender (GT):\n{kqxt_by_gt}\n")

fig, ax = plt.subplots(figsize=(10, 6))
kqxt_by_gt.plot(kind='bar', ax=ax, color=['#FF6B6B', '#90EE90'], width=0.5, edgecolor='black', linewidth=1.5)
ax.set_title('Câu 7: Số lượng thí sinh Đậu/Rớt theo Giới tính (GT)', 
             fontsize=13, fontweight='bold')
ax.set_xlabel('Giới tính (GT)')
ax.set_ylabel('Số lượng thí sinh')
ax.set_xticklabels(['Nữ (F)', 'Nam (M)'], rotation=0)
ax.legend(['Rớt (0.0)', 'Đậu (1.0)'], loc='upper left', fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Thêm số lượng trên các cột
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('Part3_Q7_PassFail_By_GT.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part3_Q7_PassFail_By_GT.png\n")
plt.close()

# ============= TÓMLẠI - BIỂU ĐỒ TỔNG HỢP =============
print("📊 Tạo biểu đồ tổng hợp toàn bộ Phần 3...")

fig = plt.figure(figsize=(18, 12))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# Câu 1 - Female XL1, XL2, XL3 (simplified version)
ax1 = fig.add_subplot(gs[0, :2])
female_xl1_counts = female_data['XL1'].value_counts().reindex(colors_order, fill_value=0)
colors_q1 = [colors_map.get(level, '#CCCCCC') for level in female_xl1_counts.index]
ax1.bar(female_xl1_counts.index, female_xl1_counts.values, color=colors_q1, edgecolor='black', linewidth=1.5)
ax1.set_title('Q1: Học sinh nữ - XL1 Classification', fontsize=11, fontweight='bold')
ax1.set_ylabel('Count')
ax1.grid(axis='y', alpha=0.3)

# Tỷ lệ đậu rớt
ax2 = fig.add_subplot(gs[0, 2])
total_passed = df[df['KQXT'] == 1.0].shape[0]
total_failed = df[df['KQXT'] == 0.0].shape[0]
ax2.pie([total_failed, total_passed], labels=['Rớt', 'Đậu'], autopct='%1.1f%%',
        colors=['#FF6B6B', '#90EE90'], startangle=90)
ax2.set_title('Overall Pass Rate', fontsize=11, fontweight='bold')

# Câu 3 - Candidates by Region & KT (simplified)
ax3 = fig.add_subplot(gs[1, :])
candidates_by_kv_kt.plot(kind='bar', ax=ax3, width=0.8, edgecolor='black', linewidth=1)
ax3.set_title('Q3: Candidates by Region (KV) & Exam Type (KT)', fontsize=11, fontweight='bold')
ax3.set_ylabel('Count')
ax3.legend(title='KT', loc='upper left', ncol=5, fontsize=8)
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=0)
ax3.grid(axis='y', alpha=0.3)

# Câu 4, 5, 7
ax4 = fig.add_subplot(gs[2, 0])
kqxt_by_kt.plot(kind='bar', ax=ax4, color=['#FF6B6B', '#90EE90'], width=0.7, edgecolor='black', linewidth=1)
ax4.set_title('Q4: Pass/Fail by KT', fontsize=10, fontweight='bold')
ax4.set_ylabel('Count')
ax4.legend(['Fail', 'Pass'], fontsize=8)
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45)
ax4.grid(axis='y', alpha=0.3)

ax5 = fig.add_subplot(gs[2, 1])
kqxt_by_kv.plot(kind='bar', ax=ax5, color=['#FF6B6B', '#90EE90'], width=0.7, edgecolor='black', linewidth=1)
ax5.set_title('Q5: Pass/Fail by Region', fontsize=10, fontweight='bold')
ax5.set_ylabel('Count')
ax5.legend(['Fail', 'Pass'], fontsize=8)
ax5.set_xticklabels(ax5.get_xticklabels(), rotation=45)
ax5.grid(axis='y', alpha=0.3)

ax6 = fig.add_subplot(gs[2, 2])
kqxt_by_gt.plot(kind='bar', ax=ax6, color=['#FF6B6B', '#90EE90'], width=0.5, edgecolor='black', linewidth=1)
ax6.set_title('Q7: Pass/Fail by Gender', fontsize=10, fontweight='bold')
ax6.set_ylabel('Count')
ax6.legend(['Fail', 'Pass'], fontsize=8)
ax6.set_xticklabels(['Female', 'Male'], rotation=0)
ax6.grid(axis='y', alpha=0.3)

plt.suptitle('PHẦN 3: TRỰC QUAN HÓA DỮ LIỆU THEO NHÓM PHÂN LOẠI', 
             fontsize=15, fontweight='bold', y=0.995)

plt.savefig('Part3_Summary_All_Questions.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Part3_Summary_All_Questions.png\n")
plt.close()

print("="*70)
print("✓ TẤT CẢ CÁC BIỂU ĐỒ PHẦN 3 ĐÃ ĐƯỢC XUẤT THÀNH CÔNG!")
print("="*70)
print("\nDanh sách biểu đồ Phần 3:")
print("1. Part3_Q1_Female_XL_Classification.png - Học sinh nữ theo XL1, XL2, XL3")
print("2. Part3_Q2_KQXT_By_KT_Region.png - KQXT cho khối A, A1, B - Khu vực 1, 2")
print("3. Part3_Q3_Candidates_By_Region_KT.png - Số lượng thí sinh theo KV & KT")
print("4. Part3_Q4_PassFail_By_KT.png - Số lượng đậu/rớt theo khối thi")
print("5. Part3_Q5_PassFail_By_KV.png - Số lượng đậu/rớt theo khu vực")
print("6. Part3_Q6_PassFail_By_DT.png - Số lượng đậu/rớt theo dân tộc")
print("7. Part3_Q7_PassFail_By_GT.png - Số lượng đậu/rớt theo giới tính")
print("8. Part3_Summary_All_Questions.png - Tóm tắt tất cả câu hỏi")
print("="*70)

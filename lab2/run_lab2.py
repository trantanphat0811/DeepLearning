#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import skew, kurtosis, shapiro
import warnings
warnings.filterwarnings('ignore')

# Load data
df = pd.read_csv('processed_dulieuxettuyendaihoc.csv')

print('='*70)
print('PHẦN 1: THỐNG KÊ DỮ LIỆU - LAB 2')
print('='*70)
print('\nDataset Shape:', df.shape)
print('\nColumn names:', df.columns.tolist())
print('\n--- Basic Statistics ---')
print(df.describe())

print('\n' + '='*70)
print('PHẦN 1.1: SẮP XẾP DH1 TĂNG DẦN')
print('='*70)
sorted_dh1 = df.sort_values('DH1', ascending=True)[['STT', 'DH1']].head(10)
print(sorted_dh1)
print(f'Min DH1: {df["DH1"].min()}, Max DH1: {df["DH1"].max()}')

print('\n' + '='*70)
print('PHẦN 1.2: SẮP XẾP DH2 TĂNG DẦN THEO GIỚI TÍNH')
print('='*70)
sorted_dh2_gt = df.sort_values(['GT', 'DH2'], ascending=[True, True])[['STT', 'GT', 'DH2']].head(10)
print(sorted_dh2_gt)
print('\nCount by Gender:')
print(df['GT'].value_counts())

print('\n' + '='*70)
print('PHẦN 1.3: PIVOT TABLE THỐNG KÊ DH1 THEO KT')
print('='*70)
pivot_dh1_kt = pd.pivot_table(
    df, 
    values='DH1', 
    index='KT',
    aggfunc=['count', 'mean', 'median', 'min', 'max', 'std']
)
print(pivot_dh1_kt.round(4))

print('\n' + '='*70)
print('PHẦN 2: TRÌNH BÀY DỮ LIỆU - TẦN SỐ GT (GIỚI TÍNH)')
print('='*70)
gt_freq = df['GT'].value_counts()
gt_relative = df['GT'].value_counts(normalize=True) * 100
freq_table_gt = pd.DataFrame({
    'Frequency': gt_freq,
    'Relative Freq (%)': gt_relative.round(2)
})
print(freq_table_gt)

print('\n' + '='*70)
print('PHẦN 3: CROSSTAB - KQXT THEO GIỚI TÍNH')
print('='*70)
kqxt_by_gt = pd.crosstab(df['GT'], df['KQXT'])
print(kqxt_by_gt)

print('\n' + '='*70)
print('PHẦN 4: TẠO BIẾN PHÂN LOẠI phanloait1 TỪ T1')
print('='*70)

def classify_t1(score):
    if score < 5:
        return 'k'
    elif score < 7:
        return 'tb'
    elif score < 8:
        return 'k'
    else:
        return 'g'

df['phanloait1'] = df['T1'].apply(classify_t1)
print('Classification distribution:')
print(df['phanloait1'].value_counts())
print('\nSample classifications:')
print(df[['STT', 'T1', 'phanloait1']].head(15))

print('\n' + '='*70)
print('PHẦN 5: PHÂN TÍCH PHÂN PHỐI T1')
print('='*70)
t1_data = df['T1']
print(f'Mean: {t1_data.mean():.4f}')
print(f'Median: {t1_data.median():.4f}')
print(f'Std Dev: {t1_data.std():.4f}')
print(f'Variance: {t1_data.var():.4f}')
print(f'Min: {t1_data.min():.4f}')
print(f'Q1: {t1_data.quantile(0.25):.4f}')
print(f'Q2: {t1_data.quantile(0.50):.4f}')
print(f'Q3: {t1_data.quantile(0.75):.4f}')
print(f'Max: {t1_data.max():.4f}')

skewness = skew(t1_data)
kurt = kurtosis(t1_data)
print(f'\nSkewness: {skewness:.4f}')
print(f'Kurtosis: {kurt:.4f}')

stat, p_value = shapiro(t1_data)
print(f'\nShapiro-Wilk Test:')
print(f'  Test Statistic: {stat:.4f}')
print(f'  P-value: {p_value:.6f}')
print(f'  Normal Distribution: {"Yes" if p_value > 0.05 else "No"}')

print('\n' + '='*70)
print('PHẦN 5.3: TƯƠNG QUAN DH1 VỀ T1')
print('='*70)
correlation = df['DH1'].corr(df['T1'])
covariance = np.cov(df['DH1'], df['T1'])[0, 1]
print(f'Covariance: {covariance:.4f}')
print(f'Pearson Correlation: {correlation:.4f}')
print(f'Correlation Interpretation: ', end='')
if abs(correlation) < 0.3:
    print('Weak')
elif abs(correlation) < 0.7:
    print('Moderate')
else:
    print('Strong')

print('\n' + '='*70)
print('PHẦN 5.5: CORRELATION MATRIX DH1, DH2, DH3')
print('='*70)
dh_data = df[['DH1', 'DH2', 'DH3']]
corr_matrix = dh_data.corr()
print(corr_matrix.round(4))

print('\n' + '='*70)
print('LAB 2 COMPLETED SUCCESSFULLY ✓')
print('='*70)

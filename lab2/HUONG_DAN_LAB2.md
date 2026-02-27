# HƯỚNG DẪN CHI TIẾT LAB 2: TRỰC QUAN HÓA DỮ LIỆU

## 1. Ý Nghĩa của Lab 2

Lab 2 tập trung vào kỹ năng xử lý, thống kê và trực quan hóa dữ liệu thực tế (điểm thi đại học). Thông qua bài tập này, sinh viên sẽ nắm vững:

### 1.1 Thống Kê Mô Tả (Descriptive Statistics)
- Biết cách sắp xếp dữ liệu theo các tiêu chí khác nhau
- Tính toán các chỉ số đặc trưng: trung bình (mean), trung vị (median), phân vị (quantiles: Q1, Q2, Q3)
- Sử dụng Pivot Table để tổng hợp dữ liệu theo nhiều nhóm cùng lúc
- Kỹ thuật: `df.sort_values()`, `groupby().agg()`, `pd.pivot_table()`, `.quantile()`

### 1.2 Trực Quan Hóa Cơ Bản (Basic Visualization)
- Sử dụng biểu đồ cột (bar chart) và biểu đồ tròn (pie chart) để mô tả tần số/tần suất
- Phân tích các biến định tính như Giới tính (GT), Khu vực (KV), Dân tộc (DT)
- Kỹ thuật: `value_counts()`, `plt.pie()`, `plt.bar()`, `sns.countplot()`

### 1.3 Phân Tích Nhóm (Group Analysis)
- So sánh dữ liệu giữa các nhóm đối tượng khác nhau
- Ví dụ: xếp loại học lực của học sinh nữ so với nam
- Lọc dữ liệu theo điều kiện: `df[df['GT'] == 'F']`
- So sánh thống kê giữa các nhóm

### 1.4 Phân Tích Phân Phối (Distribution Analysis)
- Xác định hình dáng phân phối của điểm số qua các biểu đồ
- Box Plot: xác định median, quartiles, outliers
- Histogram: xem phân phối tần số
- QQ-Plot: kiểm tra tính chuẩn của dữ liệu
- Kiểm định Shapiro-Wilk: xác định dữ liệu có tuân theo phân phối chuẩn hay không
- Kỹ thuật: `sns.boxplot()`, `plt.hist()`, `scipy.stats.probplot()`, `scipy.stats.shapiro()`

### 1.5 Phân Tích Tương Quan (Correlation Analysis)
- Khảo sát mối liên hệ giữa các biến định lượng
- Tính hệ số tương quan Pearson
- Vẽ scatter plot để thấy mối quan hệ
- Ma trận tương quan giữa các biến
- Kỹ thuật: `df.corr()`, `sns.scatterplot()`, `sns.heatmap()`

---

## 2. Cấu Trúc Bài Tập (5 Phần Chính)

### PHẦN 1: THỐNG KÊ DỮ LIỆU (Descriptive Statistics)

**Mục tiêu**: Làm quen với sắp xếp dữ liệu và tính toán các thống kê mô tả.

**Nhiệm vụ**:
1. Sắp xếp dữ liệu DH1 tăng dần: `df.sort_values(by='DH1')`
2. Sắp xếp DH2 tăng dần theo giới tính (GT)
3. Pivot Table thống kê DH1 theo KT (khối thi) với các chỉ số: count, sum, mean, median, min, max, std, Q1, Q2, Q3
4. Pivot Table thống kê DH1 theo KT và KV (khu vực)
5. Pivot Table thống kê DH1 theo KT, KV, và DT (dân tộc)

**Kỹ thuật**:
```python
# Sắp xếp
df_sorted = df.sort_values(by='DH1')
df_sorted = df.sort_values(['GT', 'DH2'], ascending=[True, True])

# Groupby với nhiều chỉ số
pivot_kt = df.groupby('KT')['DH1'].agg(['count', 'sum', 'mean', 'median', 'min', 'max', 'std'])
pivot_kt['Q1'] = df.groupby('KT')['DH1'].quantile(0.25)
pivot_kt['Q2'] = df.groupby('KT')['DH1'].quantile(0.50)
pivot_kt['Q3'] = df.groupby('KT')['DH1'].quantile(0.75)

# Hoặc sử dụng custom function
def get_stats(x):
    return pd.Series({
        'count': x.count(),
        'mean': x.mean(),
        'median': x.median(),
        'Q1': x.quantile(0.25),
        'Q2': x.quantile(0.50),
        'Q3': x.quantile(0.75)
    })
pivot_kt = df.groupby('KT')['DH1'].apply(get_stats)
```

---

### PHẦN 2: TRÌNH BÀY DỮ LIỆU (Data Presentation)

**Mục tiêu**: Biết cách trình bày dữ liệu bằng bảng tần số và biểu đồ.

**Nhiệm vụ**:
1. Trình bày dữ liệu biến GT (giới tính) bằng bảng tần số và biểu đồ tròn
2. Trình bày US_TBM1, US_TBM2, US_TBM3 (xếp loại theo học kỳ)
3. Trình bày DT (dân tộc) cho học sinh nam
4. Trình bày KV (khu vực) cho nam, dân tộc Kinh, điểm thỏa điều kiện (DH1, DH2, DH3 >= 5 hoặc >= 4)
5. Trình bày DH1, DH2, DH3 >= 5.0 thuộc khu vực 2NT

**Kỹ thuật**:
```python
# Tần số và tần suất
gt_counts = df['GT'].value_counts()
gt_pct = df['GT'].value_counts(normalize=True) * 100

# Lọc dữ liệu
male_students = df[df['GT'] == 'M']
filtered = df[(df['GT'] == 'M') & (df['DT'] == 0.0) & (df['DH1'] >= 5.0)]

# Visualize
plt.figure(figsize=(6, 6))
plt.pie(gt_counts, labels=gt_counts.index, autopct='%1.1f%%')
plt.title('Phân bố giới tính')
plt.show()
```

---

### PHẦN 3: TRỰC QUAN HÓA THEO NHÓM (Grouped Visualization)

**Mục tiêu**: So sánh dữ liệu giữa các nhóm bằng các biểu đồ.

**Nhiệm vụ**:
1. Trực quan học sinh nữ theo các nhóm phân loại XL1, XL2, XL3 (unstacked bar chart)
2. KQXT (kết quả xét tuyển) cho khối A, A1, B trong khu vực 1, 2
3. Số lượng thí sinh theo khu vực (KV) và khối thi (KT)
4. Số thí sinh đậu, rớt theo khối thi
5. Số thí sinh đậu, rớt theo khu vực
6. Số thí sinh đậu, rớt theo dân tộc
7. Số thí sinh đậu, rớt theo giới tính

**Kỹ thuật**:
```python
# Crosstab để tạo bảng phân bổ
cross = pd.crosstab(df['KV'], df['KQXT'])
cross.plot(kind='bar')

# Filter và visualize
female_data = df[df['GT'] == 'F']
cross_female = pd.crosstab(female_data['XL1'], columns='count')
```

---

### PHẦN 4: TRỰC QUAN HÓA NÂNG CAO (Advanced Visualization)

**Mục tiêu**: Sử dụng các biểu đồ phức tạp hơn và tạo biến phân loại.

**Nhiệm vụ**:
1. Biểu đồ đường (line chart) Simple cho T1 (toán)
2. Tạo biến phân loại `phanloait1` từ T1:
   - < 5: 'k' (kém)
   - 5-7: 'tb' (trung bình)
   - 7-8: 'kh' (khá)
   - >= 8: 'g' (giỏi)
3. Bảng tần số cho `phanloait1`
4. Biểu đồ đường Multiple (multiple line chart) cho T1 phân loại bởi `phanloait1`
5. Biểu đồ Drop-line (lollipop chart) cho T1 phân loại bởi `phanloait1`

**Kỹ thuật**:
```python
# Tạo biến phân loại
def phan_lop(diem):
    if diem < 5:
        return 'k'
    elif diem < 7:
        return 'tb'
    elif diem < 8:
        return 'kh'
    else:
        return 'g'

df['phanloait1'] = df['T1'].apply(phan_lop)

# Line chart
for group in ['k', 'tb', 'kh', 'g']:
    data = df[df['phanloait1'] == group]
    plt.plot(data.index, data['T1'], marker='o', label=group)
plt.legend()
plt.show()

# Drop-line chart
for idx, row in df.iterrows():
    plt.vlines(idx, 0, row['T1'], alpha=0.5)
    plt.scatter(idx, row['T1'])
```

---

### PHẦN 5: MÔ TẢ DỮ LIỆU VÀ KHẢO SÁT PHÂN PHỐI (Distribution & Correlation Analysis)

**Mục tiêu**: Phân tích chi tiết phân phối và mối tương quan giữa các biến.

**Nhiệm vụ**:
1. Mô tả và khảo sát phân phối cho T1:
   - Tính các thống kê: mean, median, std, variance, skewness, kurtosis
   - Kiểm định Shapiro-Wilk
   - Vẽ Box Plot, Histogram, QQ-Plot

2. Phân phối T1 theo từng nhóm `phanloait1` (3x3 subplot: box plot, histogram, QQ-plot cho mỗi nhóm)

3. Tương quan giữa DH1 và T1:
   - Tính hệ số tương quan Pearson
   - Tính covariance
   - Vẽ scatter plot với regression line

4. Tương quan DH1 vs T1 theo từng khu vực (KV) - 6 biểu đồ con (2x3)

5. Tương quan giữa DH1, DH2, DH3:
   - Ma trận tương quan (correlation matrix)
   - Ma trận hiệp phương sai (covariance matrix)
   - Heatmap của ma trận tương quan
   - Scatter plot matrix (3x3 với regression lines)

**Kỹ thuật**:
```python
# Thống kê phân phối
from scipy.stats import skew, kurtosis, shapiro, probplot

mean_val = df['T1'].mean()
median_val = df['T1'].median()
std_val = df['T1'].std()
skewness = skew(df['T1'])
kurt = kurtosis(df['T1'])
stat, p_value = shapiro(df['T1'])

# Box plot
sns.boxplot(x=df['T1'])

# Histogram
plt.hist(df['T1'], bins=20, kde=True)

# QQ-plot
probplot(df['T1'], dist="norm", plot=plt)
plt.show()

# Correlation
corr = df['DH1'].corr(df['T1'])
cov = np.cov(df['DH1'], df['T1'])[0, 1]

# Scatter plot
plt.scatter(df['T1'], df['DH1'])
z = np.polyfit(df['T1'], df['DH1'], 1)
plt.plot(df['T1'].sort_values(), np.poly1d(z)(df['T1'].sort_values()))

# Ma trận tương quan
corr_matrix = df[['DH1', 'DH2', 'DH3']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
```

---

## 3. Các Điểm Lưu Ý Quan Trọng

### 3.1 Sử Dụng Pivot Table
- Pivot Table giúp tính toán nhiều chỉ số cùng lúc cho một biến
- Có thể nhóm theo một hoặc nhiều cột cùng lúc: `groupby(['KT', 'KV'])`
- Thể tùy chỉnh các hàm aggregation: `agg(['count', 'sum', 'mean', ...])`

### 3.2 Lọc Dữ Liệu
- Sử dụng toán tử điều kiện trước khi visualize để tập trung vào nhóm đối tượng cụ thể
- Ví dụ: `df[df['GT'] == 'F']` để lấy học sinh nữ
- Có thể kết hợp nhiều điều kiện: `df[(df['GT'] == 'M') & (df['DT'] == 0.0) & (df['DH1'] >= 5.0)]`

### 3.3 Phân Loại Dữ Liệu
- Sử dụng `apply()` với lambda hoặc hàm để chuyển đổi dữ liệu định lượng thành định tính
- Ví dụ: Chuyển điểm số sang xếp loại (kém, trung bình, khá, giỏi)

### 3.4 Interpretation
- **Skewness**:
  - < -0.5: lệch trái (left-skewed)
  - -0.5 to 0.5: xấp xỉ đối xứng (symmetric)
  - > 0.5: lệch phải (right-skewed)

- **Kurtosis**:
  - < 3: phẳng (platykurtic)
  - ≈ 3: bình thường (mesokurtic)
  - > 3: nhọn (leptokurtic)

- **Shapiro-Wilk Test**:
  - p-value > 0.05: dữ liệu tuân theo phân phối chuẩn
  - p-value < 0.05: dữ liệu không tuân theo phân phối chuẩn

- **Correlation**:
  - |r| < 0.3: tương quan yếu
  - 0.3 ≤ |r| < 0.7: tương quan vừa phải
  - |r| ≥ 0.7: tương quan mạnh

---

## 4. Thứ Tự Thực Hiện

1. **Cài đặt thư viện**: pandas, numpy, matplotlib, seaborn, scipy
2. **Load dữ liệu**: Đọc CSV file
3. **Phần 1**: Thống kê dữ liệu
4. **Phần 2**: Trình bày dữ liệu
5. **Phần 3**: Trực quan hóa theo nhóm
6. **Phần 4**: Trực quan hóa nâng cao
7. **Phần 5**: Phân tích phân phối và tương quan
8. **Kết luận**: Tóm tắt các phát hiện chính

---

## 5. Gợi Ý Về Cấu Trúc Code

Trong notebook, mỗi phần nên có:
- **Tiêu đề rõ ràng**: Phần X, mục X.Y
- **Giải thích**: Mô tả những gì sẽ làm
- **Mã code**: Python code thực hiện
- **Kết quả**: In ra bảng, biểu đồ, số liệu
- **Ghi chú**: Giải thích kết quả

---

## 6. File Dữ Liệu

- **File**: `processed_dulieuxettuyendaihoc.csv`
- **Số hàng**: 100 sinh viên
- **Các cột chính**:
  - `STT`: Số thứ tự
  - `T1-T6`: Điểm 6 môn học (không bắt buộc)
  - `L1-L6`: Điểm thực hành hoặc học kỳ khác
  - `GT`: Giới tính (M/F)
  - `DT`: Dân tộc (0=Kinh, 1=Khác)
  - `KV`: Khu vực (1, 2, 2NT, ...)
  - `DH1, DH2, DH3`: Điểm thi đại học 3 môn
  - `KT`: Khối thi (A, A1, B, D, ...)
  - `XL1, XL2, XL3`: Xếp loại từng học kỳ
  - `US_TBM1, US_TBM2, US_TBM3`: Điểm ưu tiên
  - `KQXT`: Kết quả xét tuyển (0=Rớt, 1=Đậu)

---

## 7. Tài Liệu Tham Khảo

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [SciPy Statistics](https://docs.scipy.org/doc/scipy/reference/stats.html)

---

**Chúc bạn hoàn thành bài Lab 2 thành công!**

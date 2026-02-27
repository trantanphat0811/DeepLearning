# TÓM TẮT NHANH LAB 2

## 📚 Các File Tài Liệu

| File | Mục Đích |
|------|----------|
| **TranTanPhat_2274802010644_PTDLHS_Lab2.ipynb** | Notebook chính với 70+ cells, toàn bộ code & visualizations |
| **HUONG_DAN_LAB2.md** | Hướng dẫn chi tiết 5 phần + kỹ thuật + interpretation |
| **MAU_CODE_LAB2.md** | Mã Python gợi ý cho từng phần (copy-paste ready) |
| **CAU_TRUC_NOTEBOOK.md** | Cấu trúc chi tiết từng cell trong notebook |
| **README.md** | Tóm tắt thông tin cơ bản |

---

## 🎯 5 Phần Chính của Lab 2

### PHẦN 1: THỐNG KÊ DỮ LIỆU (5 subsections)
- 1.1: Sắp xếp DH1 tăng dần
- 1.2: Sắp xếp DH2 tăng dần theo giới tính
- 1.3-1.5: Pivot tables thống kê DH1 theo KT, KV, DT

**Kỹ thuật**: `sort_values()`, `groupby().agg()`, custom aggregate functions

---

### PHẦN 2: TRÌNH BÀY DỮ LIỆU (5 subsections)
- 2.1: Tần số/tần suất GT + biểu đồ cột & tròn
- 2.2: US_TBM1, US_TBM2, US_TBM3
- 2.3-2.5: Lọc dữ liệu và phân tích theo điều kiện

**Kỹ thuật**: `value_counts()`, `normalize=True`, `plt.pie()`, `plt.bar()`, filtering

---

### PHẦN 3: TRỰC QUAN HÓA THEO NHÓM (7 subsections)
- 3.1: Học sinh nữ - XL1, XL2, XL3
- 3.2-3.7: KQXT theo KT, KV, DT, GT

**Kỹ thuật**: `pd.crosstab()`, grouped bar charts, stacked charts

---

### PHẦN 4: TRỰC QUAN HÓA NÂNG CAO (5 subsections)
- 4.1: Line chart Simple cho T1
- 4.2-4.3: Tạo biến phân loại `phanloait1`
- 4.4-4.5: Multiple line chart & drop-line chart

**Kỹ thuật**: `apply()`, custom classification functions, multiple series plotting

---

### PHẦN 5: MÔ TẢ DỮ LIỆU & PHÂN PHỐI (5 subsections)
- 5.1: Phân tích T1 (thống kê + box plot + histogram + QQ-plot)
- 5.2: Phân phối T1 theo phanloait1 (3x3 subplot)
- 5.3: Tương quan DH1 vs T1
- 5.4: Tương quan DH1 vs T1 theo từng khu vực
- 5.5: Ma trận tương quan DH1, DH2, DH3

**Kỹ thuật**: `skew()`, `kurtosis()`, `shapiro()`, `probplot()`, `sns.heatmap()`, `np.polyfit()`

---

## 🔑 Các Khái Niệm Quan Trọng

### Thống Kê Mô Tả
| Khái niệm | Công thức / Hàm |
|-----------|-------------------|
| Trung bình | `.mean()` |
| Trung vị | `.median()` |
| Phương sai | `.var()` |
| Độ lệch chuẩn | `.std()` |
| Phân vị Q1, Q2, Q3 | `.quantile(0.25)`, `.quantile(0.5)`, `.quantile(0.75)` |
| Skewness | `skew()` từ scipy.stats |
| Kurtosis | `kurtosis()` từ scipy.stats |
| Kiểm định chuẩn | `shapiro()` từ scipy.stats |

### Interpretation Guidelines

**Skewness**:
- < -0.5: Lệch trái (left-skewed)
- -0.5 to 0.5: Xấp xỉ đối xứng
- > 0.5: Lệch phải (right-skewed)

**Kurtosis**:
- < 3: Phẳng (platykurtic)
- = 3: Bình thường (mesokurtic)
- > 3: Nhọn (leptokurtic)

**Shapiro-Wilk Test**:
- p-value > 0.05: Dữ liệu tuân theo phân phối chuẩn ✅
- p-value < 0.05: Dữ liệu không tuân theo phân phối chuẩn ❌

**Correlation Coefficient**:
- |r| < 0.3: Tương quan yếu
- 0.3 ≤ |r| < 0.7: Tương quan vừa phải
- |r| ≥ 0.7: Tương quan mạnh

---

## 💻 Quick Code Reference

### Sắp xếp
```python
df.sort_values('DH1')  # Tăng dần
df.sort_values(['GT', 'DH2'], ascending=[True, True])  # Multi-column
```

### Pivot Table
```python
df.groupby('KT')['DH1'].agg(['count', 'sum', 'mean', 'median', 'min', 'max', 'std'])
df.groupby(['KT', 'KV'])['DH1'].apply(get_stats)  # Multi-level
```

### Lọc Dữ Liệu
```python
df[df['GT'] == 'M']  # Nam
df[(df['GT'] == 'M') & (df['DH1'] >= 5.0)]  # Multiple conditions
```

### Tạo Biến Phân Loại
```python
def classify(score):
    if score < 5: return 'k'
    elif score < 7: return 'tb'
    else: return 'g'

df['category'] = df['T1'].apply(classify)
```

### Biểu Đồ
```python
df['GT'].value_counts().plot(kind='bar')  # Bar chart
plt.pie(data, labels=labels, autopct='%1.1f%%')  # Pie chart
ax.plot(x, y, marker='o')  # Line chart
ax.vlines(x, 0, y)  # Drop-line chart
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')  # Heatmap
```

### Thống Kê & Kiểm Định
```python
from scipy.stats import skew, kurtosis, shapiro, probplot

skewness = skew(data)
kurt = kurtosis(data)
stat, p_value = shapiro(data)
probplot(data, dist="norm", plot=plt)
```

### Tương Quan
```python
correlation = df['DH1'].corr(df['T1'])
covariance = np.cov(df['DH1'], df['T1'])[0, 1]
corr_matrix = df[['DH1', 'DH2', 'DH3']].corr()
```

---

## 📊 Biến Dữ Liệu Quan Trọng

| Biến | Ý Nghĩa |
|------|---------|
| DH1, DH2, DH3 | Điểm thi đại học 3 môn |
| T1-T6 | Điểm 6 môn học |
| L1-L6 | Điểm thực hành/học kỳ khác |
| GT | Giới tính (M/F) |
| DT | Dân tộc (0=Kinh, 1=Khác) |
| KV | Khu vực (1, 2, 2NT) |
| KT | Khối thi (A, A1, B, D) |
| XL1, XL2, XL3 | Xếp loại từng học kỳ |
| US_TBM1-3 | Điểm ưu tiên |
| KQXT | Kết quả xét tuyển (0=Rớt, 1=Đậu) |

---

## ✨ Lưu Ý Quan Trọng

1. **Sử dụng Pivot Table**:
   - Tính nhiều chỉ số cùng lúc
   - Nhóm theo một hoặc nhiều cột
   - Linh hoạt với custom functions

2. **Lọc Dữ Liệu**:
   - Trước khi visualize để tập trung vào nhóm cụ thể
   - Kết hợp nhiều điều kiện với `&` hoặc `|`

3. **Phân Loại Dữ Liệu**:
   - Chuyển đổi định lượng → định tính bằng `apply()`
   - Dùng lambda hoặc custom functions

4. **Interpretation**:
   - Luôn đọc kỹ giá trị thống kê
   - So sánh giữa các nhóm
   - Rút ra nhận xét có ý nghĩa

---

## 🎓 Mục Tiêu Học Tập

Sau hoàn thành Lab 2, bạn sẽ có kỹ năng:
- ✅ Sắp xếp & thống kê dữ liệu
- ✅ Tạo pivot tables phức tạp
- ✅ Lọc & phân tích dữ liệu theo nhóm
- ✅ Vẽ các loại biểu đồ khác nhau
- ✅ Phân tích phân phối dữ liệu
- ✅ Tính & giải thích tương quan
- ✅ Làm việc với dữ liệu thực tế

---

## 🔗 Quick Links

Để xem chi tiết:
- **Hướng dẫn đầy đủ**: Mở `HUONG_DAN_LAB2.md`
- **Mã gợi ý**: Mở `MAU_CODE_LAB2.md`
- **Cấu trúc notebook**: Mở `CAU_TRUC_NOTEBOOK.md`
- **Chạy notebook**: Mở `TranTanPhat_2274802010644_PTDLHS_Lab2.ipynb` trong Jupyter

---

**Chúc bạn hoàn thành Lab 2 thành công! 🎉**

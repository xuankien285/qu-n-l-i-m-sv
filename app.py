import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Tiêu đề Web App
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 2. Dữ liệu và xử lý tính toán
data = {
    'Họ và tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyên cần': [8.0, 9.0, 7.0, 8.5, 7.5, 6.0, 8.0, 7.0, 7.5, 9.0],
    'Giữa kỳ': [7.5, 8.0, 6.5, 9.0, 7.0, 5.5, 8.5, 7.5, 7.0, 8.5],
    'Cuối kỳ': [8.0, 8.5, 7.0, 9.5, 7.5, 6.5, 8.5, 7.0, 8.0, 9.5]
}
df = pd.DataFrame(data)

df['Tong_ket'] = (df['Chuyên cần'] * 0.2) + (df['Giữa kỳ'] * 0.3) + (df['Cuối kỳ'] * 0.5)
df['Tong_ket'] = df['Tong_ket'].round(2)

def xep_loai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# 3. Hiển thị bảng điểm
st.subheader("Bảng điểm chi tiết")
st.dataframe(df)

# 4. Hiển thị thống kê cơ bản
st.subheader("Thống kê chung")
dtb_lop = df['Tong_ket'].mean()
sv_cao_nhat = df.loc[df['Tong_ket'].idxmax()]
sv_thap_nhat = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Điểm trung bình lớp", value=f"{dtb_lop:.2f}")
    st.metric(label="Số sinh viên đạt", value=so_sv_dat)
with col2:
    st.metric(label="Điểm cao nhất", value=f"{sv_cao_nhat['Họ và tên']} ({sv_cao_nhat['Tong_ket']}đ)")
    st.metric(label="Điểm thấp nhất", value=f"{sv_thap_nhat['Họ và tên']} ({sv_thap_nhat['Tong_ket']}đ)")

# 5. Danh sách xổ xuống (Selectbox) chọn sinh viên
st.subheader("Tra cứu thông tin sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên:", df['Họ và tên'])
student_info = df[df['Họ và tên'] == selected_student].iloc[0]

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Chuyên cần", student_info['Chuyên cần'])
c2.metric("Giữa kỳ", student_info['Giữa kỳ'])
c3.metric("Cuối kỳ", student_info['Cuối kỳ'])
c4.metric("Tổng kết", student_info['Tong_ket'])
c5.metric("Xếp loại", student_info['Xep_loai'])

# 6. Hiển thị biểu đồ cột
st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(df['Họ và tên'], df['Tong_ket'], color='skyblue', edgecolor='black')
ax.set_ylim(0, 10)
for i, diem in enumerate(df['Tong_ket']):
    ax.text(i, diem + 0.1, str(diem), ha='center', fontsize=9)
st.pyplot(fig)

# 7. Thông tin người tạo (Cuối trang, chữ nhỏ)
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Họ tên: Nguyễn Xuân Kiên | MSSV:  001208036092</p>", unsafe_allow_html=True)

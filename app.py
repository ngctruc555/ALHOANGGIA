import streamlit as st
import pandas as pd

# Cấu hình giao diện trang
st.set_page_config(
    page_title="AL HOÀNG GIA - Quản Lý & Báo Giá Nhôm Đúc Cao Cấp",
    page_icon="👑",
    layout="wide"
)

# Khởi tạo Session State để lưu danh sách đơn hàng/báo giá
if 'orders' not in st.session_state:
    st.session_state['orders'] = []

def main():
    # Header ứng dụng
    st.title("👑 HỆ THỐNG QUẢN LÝ & BÁO GIÁ - NHÔM AL HOÀNG GIA")
    st.markdown("---")

    # Menu điều hướng sidebar
    menu = ["Trang Chủ & Thư Viện Mẫu", "Lập Báo Giá & Tính Tiền", "Quản Lý Đơn Hàng"]
    choice = st.sidebar.selectbox("📂 Chọn chức năng", menu)

    if choice == "Trang Chủ & Thư Viện Mẫu":
        show_home_page()
    elif choice == "Lập Báo Giá & Tính Tiền":
        show_quotation_page()
    elif choice == "Quản Lý Đơn Hàng":
        show_management_page()

def show_home_page():
    st.subheader("🌟 Chào mừng đến với Phần mềm Quản Lý Nhôm AL Hoàng Gia")
    st.write("Ứng dụng chuyên dụng hỗ trợ Chủ nhà và Chủ thầu tính toán, tra cứu đơn giá, lựa chọn mẫu thiết kế và quản lý đơn hàng nhôm đúc cao cấp.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Phong cách thiết kế đa dạng**\n\n* Nhà hiện đại[cite: 1, 2]\n* Cổ điển & Tân cổ điển[cite: 3]\n* Nhà thờ, Nhà chùa, Nhà tổ[cite: 5, 9, 10]")
    with col2:
        st.success("**Màu sơn cao cấp**\n\n* Đồng giả cổ\n* Mạ vàng\n* Xám khói\n* Màu đen & Đen điểm vàng")
    with col3:
        st.warning("**Sản phẩm & Phụ kiện**\n\n* Cổng, Lan can, Hàng rào, Cột\n* Khóa thông minh, Chốt, Motor tự động")

    st.markdown("### 📸 Thư viện mẫu thiết kế tiêu biểu")
    tab1, tab2, tab3 = st.tabs(["Nhà Hiện Đại & Cổ Điển", "Cổng & Lan Can", "Nhà Thờ & Công Trình Tâm Linh"])
    
    with tab1:
        st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80", caption="Mẫu nhà hiện đại & biệt thự cao cấp[cite: 1, 2]")
    with tab2:
        st.image("https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=800&q=80", caption="Mẫu cửa cổng và lan can tinh xảo[cite: 6, 8]")
    with tab3:
        st.image("https://images.unsplash.com/photo-1548625361-167a23c3330b?auto=format&fit=crop&w=800&q=80", caption="Kiến trúc nhà thờ, từ đường, nhà tổ[cite: 5, 9, 10]")

def show_quotation_page():
    st.subheader("📝 Lập Báo Giá Sản Phẩm Nhôm AL Hoàng Gia")

    with st.form("quotation_form"):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 1. Thông tin khách hàng & Công trình")
            customer_name = st.text_input("Tên Khách hàng / Chủ thầu", placeholder="Nhập họ tên...")
            customer_type = st.selectbox("Đối tượng cung cấp", ["Chủ nhà", "Chủ thầu"])
            project_type = st.selectbox("Loại công trình", [
                "Nhà hiện đại", "Nhà cổ điển", "Nhà tân cổ điển", 
                "Nhà thờ", "Nhà chùa", "Nhà tổ / Từ đường", "Khác"
            ])

        with col2:
            st.markdown("#### 2. Cấu hình sản phẩm")
            product_category = st.selectbox("Hạng mục sản phẩm", [
                "Cổng", "Lan can", "Hàng rào", "Cột", "Chông rào", "Hạng mục khác"
            ])
            paint_color = st.selectbox("Màu sơn", [
                "Đồng giả cổ", "Mạ vàng", "Xám khói", "Màu đen", "Đen điểm vàng"
            ])
            unit_price = st.number_input(
                "Đơn giá (VNĐ / m² hoặc m tới)", 
                min_value=7000000, 
                max_value=10000000, 
                value=8000000, 
                step=100000,
                format="%d"
            )

        st.markdown("---")
        col3, col4 = st.columns(2)

        with col3:
            st.markdown("#### 3. Khối lượng & Phụ kiện")
            quantity_m2 = st.number_input("Diện tích / Khối lượng (m² hoặc m)", min_value=0.1, value=10.0, step=0.5)
            
            accessories = st.multiselect(
                "Phụ kiện đi kèm",
                ["Ổ khóa cơ cao cấp", "Chốt cổng âm sàn/trên", "Motor cổng tự động", "Bản lề thủy lực", "Chụp đầu cột"]
            )
            # Ước tính chi phí phụ kiện đơn giản cho demo
            accessory_cost = len(accessories) * 1500000 

        with col4:
            st.markdown("#### 4. Chính sách thuế & Thanh toán")
            vat_option = st.radio("Chính sách thuế VAT", ["Không thuế", "Có thuế VAT (8%)"])
            notes = st.text_area("Ghi chú thêm", placeholder="Yêu cầu đặc biệt về kỹ thuật, tiến độ...")

        submitted = st.form_submit_button("🧮 Tính Toán & Lưu Báo Giá")

        if submitted:
            subtotal = (unit_price * quantity_m2) + accessory_cost
            vat_amount = subtotal * 0.08 if "Có thuế" in vat_option else 0
            total_amount = subtotal + vat_amount

            order_data = {
                "Khách hàng": customer_name if customer_name else "Khách lẻ",
                "Đối tượng": customer_type,
                "Công trình": project_type,
                "Hạng mục": product_category,
                "Màu sơn": paint_color,
                "Đơn giá": unit_price,
                "Khối lượng": quantity_m2,
                "Phụ kiện": ", ".join(accessories) if accessories else "Không",
                "Tiền phụ kiện": accessory_cost,
                "Thuế VAT": "8%" if "Có thuế" in vat_option else "Không",
                "Tổng tiền": total_amount,
                "Ghi chú": notes
            }

            st.session_state['orders'].append(order_data)
            st.success("✅ Đã lập và lưu báo giá thành công!")

    # Hiển thị kết quả tính toán ngay bên dưới nếu có đơn hàng gần nhất
    if st.session_state['orders']:
        latest = st.session_state['orders'][-1]
        st.markdown("### 📊 Chi Tiết Báo Giá Gần Nhất")
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("Khách hàng / Đối tượng", f"{latest['Khách hàng']} ({latest['Đối tượng'])")
        res_col2.metric("Tổng diện tích", f"{latest['Khối lượng']} m²")
        res_col3.metric("Tổng thành tiền", f"{latest['Tổng tiền']:,.0f} VNĐ")

def show_management_page():
    st.subheader("📋 Quản Lý Danh Sách Báo Giá & Đơn Hàng")

    if not st.session_state['orders']:
        st.info("Chưa có báo giá hay đơn hàng nào được lưu. Vui lòng tạo báo giá ở mục bên cạnh.")
    else:
        df = pd.DataFrame(st.session_state['orders'])
        st.dataframe(df, use_container_width=True)

        # Nút xóa danh sách
        if st.button("🗑️ Xóa Tất Cả Dữ Liệu Đơn Hàng"):
            st.session_state['orders'] = []
            st.rerun()

if __name__ == '__main__':
    main()

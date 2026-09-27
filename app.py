import streamlit as st
import mysql.connector
from mysql.connector import Error

# ============================================================
# 1. CẤU HÌNH TRANG
# ============================================================

st.set_page_config(
    page_title="Cổng Nhôm Đúc Cao Cấp",
    page_icon="🏰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# 2. KẾT NỐI MYSQL AIVEN
# ============================================================

try:
    DB_USER = st.secrets["mysql"]["user"]
    DB_PASSWORD = st.secrets["mysql"]["password"]
    DB_HOST = st.secrets["mysql"]["host"]
    DB_PORT = st.secrets["mysql"]["port"]
    DB_NAME = st.secrets["mysql"]["database"]

except Exception:
    # ========================================================
    # CẤU HÌNH LOCAL
    # KHÔNG NÊN ĐỂ PASSWORD THẬT TRONG SOURCE CODE KHI
    # ĐƯA WEBSITE LÊN INTERNET.
    # ========================================================

    DB_USER = "avnadmin"
    DB_PASSWORD = "YOUR_MYSQL_PASSWORD"
    DB_HOST = "mysql-25a34fbe-ngctruc5-4830.e.aivencloud.com"
    DB_PORT = 26716
    DB_NAME = "defaultdb"


# ============================================================
# 3. HÀM KẾT NỐI DATABASE
# ============================================================

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        if conn.is_connected():
            return conn

    except Error as e:
        st.error(f"Lỗi kết nối MySQL: {e}")

    return None


# ============================================================
# 4. CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f7f5f1;
}

.hero {
    padding: 60px 40px;
    border-radius: 20px;
    background:
        linear-gradient(
            rgba(0,0,0,0.45),
            rgba(0,0,0,0.45)
        ),
        url("https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1800&q=80");

    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    margin-bottom: 35px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 15px;
}

.hero p {
    font-size: 21px;
}

.section-title {
    font-size: 32px;
    font-weight: 800;
    margin-top: 35px;
    margin-bottom: 20px;
    color: #222;
}

.product-card {
    background: white;
    border-radius: 15px;
    padding: 12px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}

.price {
    color: #a66a16;
    font-size: 22px;
    font-weight: bold;
}

.info-box {
    background: white;
    border-radius: 15px;
    padding: 25px;
    text-align: center;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
}

.footer {
    background: #222;
    color: white;
    padding: 35px;
    border-radius: 15px;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# 5. HEADER
# ============================================================

st.markdown("""
<div class="hero">

    <h1>CỔNG NHÔM ĐÚC CAO CẤP</h1>

    <p>
        Sang trọng • Bền đẹp • Thiết kế theo kích thước thực tế
    </p>

    <p>
        Cổng • Lan can • Hàng rào • Cột • Chông rào • Phụ kiện
    </p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# 6. MENU
# ============================================================

menu = st.columns(5)

with menu[0]:
    st.button("🏠 Trang chủ", use_container_width=True)

with menu[1]:
    st.button("🚪 Cổng nhôm", use_container_width=True)

with menu[2]:
    st.button("🏛️ Công trình", use_container_width=True)

with menu[3]:
    st.button("💰 Bảng giá", use_container_width=True)

with menu[4]:
    st.button("📞 Liên hệ", use_container_width=True)


# ============================================================
# 7. CHỌN KIỂU CÔNG TRÌNH
# ============================================================

st.markdown(
    '<div class="section-title">🏠 CHỌN CỔNG THEO KIẾN TRÚC</div>',
    unsafe_allow_html=True
)

architecture = st.columns(6)

types = [
    ("🏠", "Nhà hiện đại"),
    ("🏛️", "Tân cổ điển"),
    ("🏰", "Cổ điển"),
    ("⛪", "Nhà thờ"),
    ("🛕", "Nhà chùa"),
    ("🏡", "Nhà tổ")
]

for col, (icon, name) in zip(architecture, types):
    with col:
        st.markdown(
            f"""
            <div class="info-box">
                <div style="font-size:35px">{icon}</div>
                <b>{name}</b>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# 8. SIDEBAR - BỘ LỌC
# ============================================================

st.sidebar.header("🔎 TÌM KIẾM SẢN PHẨM")

product_type = st.sidebar.selectbox(
    "Loại sản phẩm",
    [
        "Tất cả",
        "Cổng",
        "Lan can",
        "Hàng rào",
        "Cột cổng",
        "Chông rào",
        "Phụ kiện"
    ]
)

architecture_filter = st.sidebar.selectbox(
    "Kiểu kiến trúc",
    [
        "Tất cả",
        "Hiện đại",
        "Tân cổ điển",
        "Cổ điển",
        "Nhà thờ",
        "Nhà chùa",
        "Nhà tổ"
    ]
)

color_filter = st.sidebar.selectbox(
    "Màu sơn",
    [
        "Tất cả",
        "Đồng giả cổ",
        "Mạ vàng",
        "Xám khói",
        "Đen",
        "Đen điểm vàng"
    ]
)

price_filter = st.sidebar.selectbox(
    "Khoảng giá",
    [
        "Tất cả",
        "7 - 10 triệu",
        "10 - 20 triệu",
        "20 - 30 triệu",
        "30 - 50 triệu",
        "Trên 50 triệu"
    ]
)


# ============================================================
# 9. DỮ LIỆU SẢN PHẨM DEMO
# ============================================================

products = [

    {
        "name": "Cổng nhôm đúc mẫu Hoàng Gia",
        "type": "Cổng",
        "architecture": "Tân cổ điển",
        "color": "Đen điểm vàng",
        "price": 15000000,
        "image": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=900&q=80"
    },

    {
        "name": "Cổng nhôm đúc hiện đại",
        "type": "Cổng",
        "architecture": "Hiện đại",
        "color": "Đen",
        "price": 8500000,
        "image": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=900&q=80"
    },

    {
        "name": "Cổng nhôm đúc Đồng Giả Cổ",
        "type": "Cổng",
        "architecture": "Cổ điển",
        "color": "Đồng giả cổ",
        "price": 25000000,
        "image": "https://images.unsplash.com/photo-1600607688969-a5bfcd646154?auto=format&fit=crop&w=900&q=80"
    },

    {
        "name": "Lan can nhôm đúc cao cấp",
        "type": "Lan can",
        "architecture": "Tân cổ điển",
        "color": "Mạ vàng",
        "price": 12000000,
        "image": "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=900&q=80"
    },

    {
        "name": "Hàng rào nhôm đúc biệt thự",
        "type": "Hàng rào",
        "architecture": "Cổ điển",
        "color": "Đen điểm vàng",
        "price": 18000000,
        "image": "https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?auto=format&fit=crop&w=900&q=80"
    },

    {
        "name": "Cổng nhà thờ nhôm đúc",
        "type": "Cổng",
        "architecture": "Nhà thờ",
        "color": "Đồng giả cổ",
        "price": 30000000,
        "image": "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=900&q=80"
    }
]


# ============================================================
# 10. LỌC SẢN PHẨM
# ============================================================

filtered_products = []

for p in products:

    if product_type != "Tất cả" and p["type"] != product_type:
        continue

    if architecture_filter != "Tất cả" and p["architecture"] != architecture_filter:
        continue

    if color_filter != "Tất cả" and p["color"] != color_filter:
        continue

    if price_filter == "7 - 10 triệu":
        if not 7_000_000 <= p["price"] <= 10_000_000:
            continue

    elif price_filter == "10 - 20 triệu":
        if not 10_000_000 <= p["price"] <= 20_000_000:
            continue

    elif price_filter == "20 - 30 triệu":
        if not 20_000_000 <= p["price"] <= 30_000_000:
            continue

    elif price_filter == "30 - 50 triệu":
        if not 30_000_000 <= p["price"] <= 50_000_000:
            continue

    elif price_filter == "Trên 50 triệu":
        if p["price"] <= 50_000_000:
            continue

    filtered_products.append(p)


# ============================================================
# 11. HIỂN THỊ SẢN PHẨM
# ============================================================

st.markdown(
    '<div class="section-title">🔥 MẪU CỔNG & SẢN PHẨM</div>',
    unsafe_allow_html=True
)

if not filtered_products:

    st.warning("Không tìm thấy sản phẩm phù hợp.")

else:

    cols = st.columns(3)

    for index, product in enumerate(filtered_products):

        with cols[index % 3]:

            st.image(
                product["image"],
                use_container_width=True
            )

            st.markdown(
                f"""
                <div class="product-card">

                    <h3>{product["name"]}</h3>

                    <p>
                        <b>Kiểu:</b>
                        {product["architecture"]}
                    </p>

                    <p>
                        <b>Màu:</b>
                        {product["color"]}
                    </p>

                    <p class="price">
                        Từ {product["price"]:,} đ
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "📋 Nhận báo giá",
                key=f"quote_{index}",
                use_container_width=True
            ):
                st.session_state["selected_product"] = product["name"]


# ============================================================
# 12. BẢNG GIÁ THAM KHẢO
# ============================================================

st.markdown(
    '<div class="section-title">💰 BẢNG GIÁ THAM KHẢO</div>',
    unsafe_allow_html=True
)

price_cols = st.columns(5)

price_data = [
    ("7 - 10 triệu", "Mẫu cơ bản"),
    ("10 - 20 triệu", "Mẫu phổ thông"),
    ("20 - 30 triệu", "Mẫu cao cấp"),
    ("30 - 50 triệu", "Biệt thự"),
    ("50 triệu+", "Thiết kế riêng")
]

for col, (price, desc) in zip(price_cols, price_data):

    with col:

        st.markdown(
            f"""
            <div class="info-box">

                <h3>{price}</h3>

                <p>{desc}</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# 13. MÀU SƠN
# ============================================================

st.markdown(
    '<div class="section-title">🎨 MÀU SƠN</div>',
    unsafe_allow_html=True
)

colors = st.columns(5)

color_names = [
    "Đồng giả cổ",
    "Mạ vàng",
    "Xám khói",
    "Màu đen",
    "Đen điểm vàng"
]

for col, color in zip(colors, color_names):

    with col:

        st.markdown(
            f"""
            <div class="info-box">
                <h3>{color}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# 14. PHỤ KIỆN
# ============================================================

st.markdown(
    '<div class="section-title">⚙️ PHỤ KIỆN ĐI KÈM</div>',
    unsafe_allow_html=True
)

accessories = [
    ("🔐", "Ổ khóa"),
    ("🔩", "Chốt cổng"),
    ("⚙️", "Motor tự động"),
    ("📡", "Điều khiển từ xa"),
    ("🚪", "Bản lề"),
]

acc_cols = st.columns(5)

for col, (icon, name) in zip(acc_cols, accessories):

    with col:

        st.markdown(
            f"""
            <div class="info-box">

                <div style="font-size:30px">
                    {icon}
                </div>

                <h4>{name}</h4>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# 15. CHỦ NHÀ / CHỦ THẦU
# ============================================================

st.markdown(
    '<div class="section-title">🤝 DÀNH CHO CHỦ NHÀ & CHỦ THẦU</div>',
    unsafe_allow_html=True
)

customer_cols = st.columns(2)

with customer_cols[0]:

    st.markdown("""
    <div class="info-box">

        <h2>🏠 CHỦ NHÀ</h2>

        <p>
        Tư vấn mẫu cổng phù hợp kiến trúc.
        </p>

        <p>
        Tư vấn màu sơn và kích thước.
        </p>

        <p>
        Báo giá sản phẩm và phụ kiện.
        </p>

    </div>
    """, unsafe_allow_html=True)


with customer_cols[1]:

    st.markdown("""
    <div class="info-box">

        <h2>👷 CHỦ THẦU</h2>

        <p>
        Báo giá số lượng công trình.
        </p>

        <p>
        Chính sách dành cho đối tác.
        </p>

        <p>
        Hỗ trợ mẫu và phối hợp công trình.
        </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# 16. TÍNH VAT
# ============================================================

st.markdown(
    '<div class="section-title">🧾 TÍNH GIÁ CÓ VAT 8%</div>',
    unsafe_allow_html=True
)

amount = st.number_input(
    "Nhập giá sản phẩm",
    min_value=0,
    value=10_000_000,
    step=500_000
)

include_vat = st.checkbox(
    "Tính thêm VAT 8%"
)

if include_vat:

    vat = amount * 0.08
    total = amount + vat

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Giá chưa VAT",
        f"{amount:,.0f} đ"
    )

    c2.metric(
        "VAT 8%",
        f"{vat:,.0f} đ"
    )

    c3.metric(
        "Tổng thanh toán",
        f"{total:,.0f} đ"
    )

else:

    st.success(
        f"Giá tham khảo: {amount:,.0f} đ"
    )


# ============================================================
# 17. FORM NHẬN BÁO GIÁ
# ============================================================

st.markdown(
    '<div class="section-title">📋 NHẬN BÁO GIÁ</div>',
    unsafe_allow_html=True
)

with st.form("quote_form"):

    customer_name = st.text_input(
        "Họ và tên"
    )

    phone = st.text_input(
        "Số điện thoại"
    )

    customer_type = st.selectbox(
        "Bạn là",
        [
            "Chủ nhà",
            "Chủ thầu",
            "Kiến trúc sư",
            "Đơn vị thiết kế",
            "Khác"
        ]
    )

    width = st.number_input(
        "Chiều rộng cổng (m)",
        min_value=0.0,
        step=0.1
    )

    height = st.number_input(
        "Chiều cao cổng (m)",
        min_value=0.0,
        step=0.1
    )

    message = st.text_area(
        "Yêu cầu khác"
    )

    submitted = st.form_submit_button(
        "📩 GỬI YÊU CẦU BÁO GIÁ",
        use_container_width=True
    )

    if submitted:

        if not customer_name or not phone:

            st.error(
                "Vui lòng nhập họ tên và số điện thoại."
            )

        else:

            conn = get_connection()

            if conn:

                try:

                    cursor = conn.cursor()

                    sql = """
                    INSERT INTO quote_requests
                    (
                        customer_name,
                        phone,
                        customer_type,
                        width,
                        height,
                        message
                    )
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """

                    values = (
                        customer_name,
                        phone,
                        customer_type,
                        width,
                        height,
                        message
                    )

                    cursor.execute(sql, values)

                    conn.commit()

                    cursor.close()
                    conn.close()

                    st.success(
                        "Đã gửi yêu cầu! Chúng tôi sẽ liên hệ báo giá."
                    )

                except Error as e:

                    st.error(
                        f"Không thể lưu yêu cầu: {e}"
                    )

            else:

                st.warning(
                    "Chưa kết nối được cơ sở dữ liệu."
                )


# ============================================================
# 18. FOOTER
# ============================================================

st.markdown("""
<div class="footer">

<h2>CỔNG NHÔM ĐÚC CAO CẤP</h2>

<p>
Cổng nhôm • Lan can • Hàng rào • Cột • Chông rào
</p>

<p>
Nhận thiết kế và gia công theo kích thước thực tế.
</p>

<p>
☎ Hotline: 09xx xxx xxx
</p>

<p>
💬 Zalo: 09xx xxx xxx
</p>

</div>
""", unsafe_allow_html=True)

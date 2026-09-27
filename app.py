import streamlit as st
import mysql.connector

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Cổng Nhôm Hoàng Gia",
    page_icon="🏰",
    layout="wide"
)

# =========================
# MYSQL AIVEN
# =========================
DB_HOST = "mysql-25a34fbe-ngctruc5-4830.e.aivencloud.com"
DB_PORT = 26716
DB_USER = "avnadmin"
DB_PASSWORD = "THAY_MAT_KHAU_MYSQL_CUA_BAN"
DB_NAME = "defaultdb"


def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        ssl_disabled=False
    )


# =========================
# CSS
# =========================
st.markdown("""
<style>

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

.hero {
    height: 430px;
    border-radius: 20px;
    background:
    linear-gradient(rgba(0,0,0,.35),rgba(0,0,0,.55)),
    url("https://product.hstatic.net/200000277379/product/cong_nhom_duc_co_dien_7b2bc46d54ae410186904f588aedae38.jpg");
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: white;
}

.hero h1 {
    font-size: 48px;
    margin-bottom: 8px;
}

.hero p {
    font-size: 20px;
}

.card {
    border-radius: 16px;
    overflow: hidden;
    background: white;
    box-shadow: 0 3px 15px rgba(0,0,0,.10);
    margin-bottom: 20px;
}

.card img {
    width: 100%;
    height: 230px;
    object-fit: cover;
}

.card-content {
    padding: 15px;
}

.price {
    color: #9a6b00;
    font-weight: 700;
    font-size: 18px;
}

.section-title {
    text-align: center;
    margin: 45px 0 25px;
}

.small-box {
    padding: 18px;
    border-radius: 14px;
    background: #f7f7f7;
    text-align: center;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# HERO
# =========================
st.markdown("""
<div class="hero">
    <div>
        <h1>CỔNG NHÔM HOÀNG GIA</h1>
        <p>Cổng nhôm đúc • Lan can • Hàng rào • Biệt thự</p>
    </div>
</div>
""", unsafe_allow_html=True)


# =========================
# SẢN PHẨM
# =========================
st.markdown(
    '<h2 class="section-title">Mẫu nổi bật</h2>',
    unsafe_allow_html=True
)

products = [
    {
        "name": "Cổng Hoàng Gia",
        "type": "Tân cổ điển",
        "color": "Đen điểm vàng",
        "price": "Từ 15 triệu",
        "image": "https://product.hstatic.net/200000277379/product/cong_nhom_duc_co_dien_7b2bc46d54ae410186904f588aedae38.jpg"
    },
    {
        "name": "Cổng Nhà Thờ",
        "type": "Nhà thờ",
        "color": "Đồng vàng",
        "price": "Từ 20 triệu",
        "image": "https://cms.congducdep.com/data/a13f277c-6a7b-47fd-bcaa-dac07bb6e3ec/cong-nha-tho-dep%20%284%29.jpg"
    },
    {
        "name": "Cổng Hiện Đại",
        "type": "Hiện đại",
        "color": "Xám khói",
        "price": "Từ 8 triệu",
        "image": "https://image.made-in-china.com/2f0j00wLsvSkHEfpci/Elegant-Outdoor-Garden-Decorative-Cast-Aluminium-Grill-Residential-Exterior-Double-Swing-Metal-Door-Main-Gate-Design-Pivot-Steel-2188371215.webp"
    },
    {
        "name": "Cổng Biệt Thự",
        "type": "Cổ điển",
        "color": "Đen điểm vàng",
        "price": "Từ 25 triệu",
        "image": "https://www.nhomducanthinhphat.com/images/uploads/products/cong_nhom_duc_1356854649_2100046274.jpeg"
    }
]

cols = st.columns(4)

for col, p in zip(cols, products):
    with col:
        st.markdown(f"""
        <div class="card">
            <img src="{p['image']}">
            <div class="card-content">
                <h3>{p['name']}</h3>
                <p>{p['type']} • {p['color']}</p>
                <div class="price">{p['price']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# =========================
# BẢNG GIÁ
# =========================
st.markdown(
    '<h2 class="section-title">Bảng giá</h2>',
    unsafe_allow_html=True
)

price_data = {
    "Mức giá": [
        "7 – 10 triệu",
        "10 – 20 triệu",
        "20 – 30 triệu",
        "30 – 50 triệu",
        "50+ triệu"
    ],
    "Phân khúc": [
        "Cơ bản",
        "Tiêu chuẩn",
        "Cao cấp",
        "Biệt thự",
        "Thiết kế riêng"
    ]
}

st.table(price_data)


# =========================
# LOẠI SẢN PHẨM
# =========================
st.markdown(
    '<h2 class="section-title">Sản phẩm</h2>',
    unsafe_allow_html=True
)

cols = st.columns(6)

items = [
    "Cổng",
    "Lan can",
    "Hàng rào",
    "Cột",
    "Chông rào",
    "Phụ kiện"
]

for col, item in zip(cols, items):
    with col:
        st.markdown(
            f'<div class="small-box"><b>{item}</b></div>',
            unsafe_allow_html=True
        )


# =========================
# MÀU SƠN
# =========================
st.markdown(
    '<h2 class="section-title">Màu sơn</h2>',
    unsafe_allow_html=True
)

cols = st.columns(5)

colors = [
    "Đồng giả cổ",
    "Mạ vàng",
    "Xám khói",
    "Đen",
    "Đen điểm vàng"
]

for col, color in zip(cols, colors):
    with col:
        st.markdown(
            f'<div class="small-box">{color}</div>',
            unsafe_allow_html=True
        )


# =========================
# BÁO GIÁ
# =========================
st.markdown(
    '<h2 class="section-title">Nhận báo giá</h2>',
    unsafe_allow_html=True
)

with st.form("quote_form"):

    name = st.text_input("Họ tên")
    phone = st.text_input("Số điện thoại")

    product = st.selectbox(
        "Sản phẩm",
        [
            "Cổng nhôm đúc",
            "Lan can",
            "Hàng rào",
            "Cột",
            "Chông rào",
            "Phụ kiện"
        ]
    )

    width = st.number_input(
        "Rộng (m)",
        min_value=0.0,
        step=0.1
    )

    height = st.number_input(
        "Cao (m)",
        min_value=0.0,
        step=0.1
    )

    message = st.text_area("Ghi chú")

    submit = st.form_submit_button(
        "GỬI YÊU CẦU"
    )

    if submit:

        if not name or not phone:
            st.warning("Vui lòng nhập họ tên và số điện thoại.")

        else:
            try:

                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute("""
                    INSERT INTO quote_requests
                    (
                        customer_name,
                        phone,
                        product,
                        width,
                        height,
                        message
                    )
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    name,
                    phone,
                    product,
                    width,
                    height,
                    message
                ))

                conn.commit()

                cursor.close()
                conn.close()

                st.success("Đã gửi yêu cầu báo giá!")

            except Exception as e:
                st.error(f"Lỗi kết nối MySQL: {e}")


# =========================
# FOOTER
# =========================
st.markdown("""
<hr>

<div style="text-align:center;color:#777">
CỔNG NHÔM HOÀNG GIA<br>
Cổng nhôm đúc • Lan can • Hàng rào
</div>
""", unsafe_allow_html=True)

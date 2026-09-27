import streamlit as st
import mysql.connector
from mysql.connector import Error


# ============================================================
# CẤU HÌNH
# ============================================================

st.set_page_config(
    page_title="Cổng Nhôm Hoàng Gia",
    page_icon="🏰",
    layout="wide"
)


# ============================================================
# MYSQL AIVEN
# ============================================================

try:
    DB_USER = st.secrets["mysql"]["user"]
    DB_PASSWORD = st.secrets["mysql"]["password"]
    DB_HOST = st.secrets["mysql"]["host"]
    DB_PORT = int(st.secrets["mysql"]["port"])
    DB_NAME = st.secrets["mysql"]["database"]

except Exception as e:
    st.error("Chưa cấu hình MySQL trong Streamlit Secrets.")
    st.stop()


def get_connection():

    try:
        return mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            connection_timeout=10
        )

    except Error as e:
        st.error(f"Lỗi MySQL: {e}")
        return None


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #f7f5f0;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

/* HEADER */

.hero {
    height: 480px;
    border-radius: 18px;

    background:
    linear-gradient(
        rgba(0,0,0,.38),
        rgba(0,0,0,.45)
    ),
    url("https://product.hstatic.net/200000277379/product/cong_nhom_duc_co_dien_7b2bc46d54ae410186904f588aedae38.jpg");

    background-size: cover;
    background-position: center;

    display: flex;
    align-items: center;
    justify-content: center;

    text-align: center;
    color: white;

    margin-bottom: 35px;
}

.hero-box h1 {
    font-size: 48px;
    margin-bottom: 8px;
    font-weight: 800;
}

.hero-box p {
    font-size: 20px;
    margin-bottom: 22px;
}

.hero-price {
    font-size: 24px;
    font-weight: bold;
}


/* TITLE */

.title {
    text-align: center;
    font-size: 30px;
    font-weight: 800;
    margin: 38px 0 22px;
}


/* CARD */

.card {
    background: white;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 3px 15px rgba(0,0,0,.08);
    margin-bottom: 20px;
}

.card-content {
    padding: 15px 17px 18px;
}

.card-title {
    font-size: 19px;
    font-weight: 700;
}

.card-info {
    color: #777;
    font-size: 14px;
    margin-top: 5px;
}

.price {
    color: #a06b20;
    font-size: 21px;
    font-weight: 800;
    margin-top: 10px;
}


/* PRICE */

.price-box {
    background: white;
    border-radius: 14px;
    padding: 25px 10px;
    text-align: center;
    box-shadow: 0 3px 12px rgba(0,0,0,.07);
}

.price-box h2 {
    color: #9a641d;
    margin-bottom: 5px;
}

.price-box p {
    color: #777;
    margin: 0;
}


/* CATEGORY */

.category {
    background: white;
    border-radius: 14px;
    padding: 22px 8px;
    text-align: center;
    box-shadow: 0 3px 12px rgba(0,0,0,.07);
    min-height: 100px;
}

.category-icon {
    font-size: 30px;
}

.category-name {
    font-weight: 700;
    margin-top: 8px;
}


/* FOOTER */

.footer {
    margin-top: 45px;
    padding: 35px;
    background: #202020;
    color: white;
    border-radius: 15px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="hero">

    <div class="hero-box">

        <h1>CỔNG NHÔM HOÀNG GIA</h1>

        <p>
            Cổng nhôm đúc • Lan can • Hàng rào
        </p>

        <div class="hero-price">
            Mẫu đẹp từ 7 triệu
        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# KIỂU NHÀ
# ============================================================

st.markdown(
    '<div class="title">CHỌN THEO KIỂU NHÀ</div>',
    unsafe_allow_html=True
)

categories = [
    ("🏠", "Hiện đại"),
    ("🏛️", "Tân cổ điển"),
    ("🏰", "Cổ điển"),
    ("⛪", "Nhà thờ"),
    ("🛕", "Nhà chùa"),
    ("🏡", "Nhà tổ"),
]

cols = st.columns(6)

for col, item in zip(cols, categories):

    with col:

        st.markdown(
            f"""
            <div class="category">

                <div class="category-icon">
                    {item[0]}
                </div>

                <div class="category-name">
                    {item[1]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# SẢN PHẨM
# ============================================================

st.markdown(
    '<div class="title">MẪU CỔNG NỔI BẬT</div>',
    unsafe_allow_html=True
)


products = [

    {
        "name": "Cổng Hoàng Gia",
        "type": "Tân cổ điển",
        "color": "Đen điểm vàng",
        "price": "Từ 15 triệu",
        "image":
        "https://product.hstatic.net/200000277379/product/cong_nhom_duc_co_dien_7b2bc46d54ae410186904f588aedae38.jpg"
    },

    {
        "name": "Cổng nhà thờ",
        "type": "Nhà thờ",
        "color": "Đồng vàng",
        "price": "Từ 20 triệu",
        "image":
        "https://cms.congducdep.com/data/a13f277c-6a7b-47fd-bcaa-dac07bb6e3ec/cong-nha-tho-dep%20%284%29.jpg"
    },

    {
        "name": "Cổng hiện đại",
        "type": "Hiện đại",
        "color": "Xám khói",
        "price": "Từ 8 triệu",
        "image":
        "https://image.made-in-china.com/2f0j00wLsvSkHEfpci/Elegant-Outdoor-Garden-Decorative-Cast-Aluminium-Grill-Residential-Exterior-Double-Swing-Metal-Door-Main-Gate-Design-Pivot-Steel-2188371215.webp"
    },

    {
        "name": "Cổng biệt thự",
        "type": "Cổ điển",
        "color": "Đen điểm vàng",
        "price": "Từ 25 triệu",
        "image":
        "https://www.nhomducanthinhphat.com/images/uploads/products/cong_nhom_duc_1356854649_2100046274.jpeg"
    },

]


cols = st.columns(4)

for col, product in zip(cols, products):

    with col:

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.image(
            product["image"],
            use_container_width=True
        )

        st.markdown(
            f"""
            <div class="card-content">

                <div class="card-title">
                    {product["name"]}
                </div>

                <div class="card-info">
                    {product["type"]} · {product["color"]}
                </div>

                <div class="price">
                    {product["price"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# BẢNG GIÁ
# ============================================================

st.markdown(
    '<div class="title">BẢNG GIÁ THAM KHẢO</div>',
    unsafe_allow_html=True
)

prices = [
    ("7–10 triệu", "Mẫu cơ bản"),
    ("10–20 triệu", "Mẫu đẹp"),
    ("20–30 triệu", "Mẫu cao cấp"),
    ("30–50 triệu", "Biệt thự"),
    ("50+ triệu", "Thiết kế riêng")
]

cols = st.columns(5)

for col, item in zip(cols, prices):

    with col:

        st.markdown(
            f"""
            <div class="price-box">

                <h2>{item[0]}</h2>

                <p>{item[1]}</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# MÀU SƠN
# ============================================================

st.markdown(
    '<div class="title">MÀU SƠN</div>',
    unsafe_allow_html=True
)

colors = [
    "Đồng giả cổ",
    "Mạ vàng",
    "Xám khói",
    "Đen",
    "Đen điểm vàng"
]

cols = st.columns(5)

for col, color in zip(cols, colors):

    with col:

        st.markdown(
            f"""
            <div class="category">

                <div class="category-name">
                    {color}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# SẢN PHẨM
# ============================================================

st.markdown(
    '<div class="title">HẠNG MỤC</div>',
    unsafe_allow_html=True
)

items = [
    ("🚪", "Cổng"),
    ("〰️", "Lan can"),
    ("🏡", "Hàng rào"),
    ("🏛️", "Cột"),
    ("⚜️", "Chông rào"),
    ("⚙️", "Phụ kiện")
]

cols = st.columns(6)

for col, item in zip(cols, items):

    with col:

        st.markdown(
            f"""
            <div class="category">

                <div class="category-icon">
                    {item[0]}
                </div>

                <div class="category-name">
                    {item[1]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# BÁO GIÁ
# ============================================================

st.markdown(
    '<div class="title">NHẬN BÁO GIÁ</div>',
    unsafe_allow_html=True
)

with st.form("quote_form"):

    c1, c2 = st.columns(2)

    with c1:

        name = st.text_input(
            "Họ tên"
        )

    with c2:

        phone = st.text_input(
            "Số điện thoại"
        )

    product = st.selectbox(
        "Sản phẩm",
        [
            "Cổng nhôm",
            "Lan can",
            "Hàng rào",
            "Cột",
            "Chông rào",
            "Phụ kiện"
        ]
    )

    note = st.text_area(
        "Kích thước / yêu cầu"
    )

    submit = st.form_submit_button(
        "GỬI BÁO GIÁ",
        use_container_width=True
    )


if submit:

    if not name or not phone:

        st.warning(
            "Vui lòng nhập họ tên và số điện thoại."
        )

    else:

        connection = get_connection()

        if connection:

            try:

                cursor = connection.cursor()

                sql = """
                INSERT INTO quote_requests
                (
                    customer_name,
                    phone,
                    customer_type,
                    product,
                    message
                )
                VALUES (%s, %s, %s, %s, %s)
                """

                cursor.execute(
                    sql,
                    (
                        name,
                        phone,
                        "Khách hàng",
                        product,
                        note
                    )
                )

                connection.commit()

                cursor.close()
                connection.close()

                st.success(
                    "Đã gửi. Chúng tôi sẽ liên hệ sớm."
                )

            except Error as e:

                st.error(
                    f"Lỗi lưu báo giá: {e}"
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    <h2>CỔNG NHÔM HOÀNG GIA</h2>

    <p>
        Cổng nhôm đúc · Lan can · Hàng rào · Phụ kiện
    </p>

    <p>
        📞 Hotline: 09xx xxx xxx
        &nbsp;&nbsp; | &nbsp;&nbsp;
        💬 Zalo: 09xx xxx xxx
    </p>

</div>
""", unsafe_allow_html=True)

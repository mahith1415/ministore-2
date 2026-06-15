import streamlit as st

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛒",
    layout="wide"
)

# ---------------------------
# Product Data
# ---------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 2499,
        "description": "High-quality Bluetooth headphones with noise cancellation.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 3999,
        "description": "Track fitness, heart rate, and notifications on the go.",
        "category": "Electronics"
    },
    {
        "name": "Running Shoes",
        "price": 2999,
        "description": "Comfortable and lightweight shoes for daily workouts.",
        "category": "Fashion"
    },
    {
        "name": "Laptop Backpack",
        "price": 1499,
        "description": "Stylish backpack with padded laptop compartment.",
        "category": "Accessories"
    },
    {
        "name": "Coffee Maker",
        "price": 5499,
        "description": "Brew delicious coffee with one-touch operation.",
        "category": "Home"
    },
    {
        "name": "Gaming Mouse",
        "price": 1299,
        "description": "RGB gaming mouse with adjustable DPI settings.",
        "category": "Electronics"
    }
]

# ---------------------------
# CSS
# ---------------------------
st.markdown("""
<style>

.hero {
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    color:white;
    padding:2rem;
    border-radius:15px;
    text-align:center;
    margin-bottom:20px;
}

.product-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.price{
    color:green;
    font-size:22px;
    font-weight:bold;
}

/* Floating Chat Button */
.chat-btn{
    position:fixed;
    bottom:30px;
    right:30px;
    background:#2563eb;
    color:white;
    padding:15px 25px;
    border-radius:50px;
    text-decoration:none;
    font-weight:bold;
    box-shadow:0px 4px 15px rgba(0,0,0,0.3);
    z-index:999;
}

.chat-btn:hover{
    background:#1d4ed8;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(
    list(set(p["category"] for p in products))
)

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")
st.sidebar.subheader("🛒 Cart Summary")
st.sidebar.metric("Items", 3)
st.sidebar.metric("Total", "₹6,797")

# ---------------------------
# Hero Section
# ---------------------------
st.markdown("""
<div class="hero">
<h1>🛒 Welcome to MiniStore</h1>
<p>Quality Products. Affordable Prices.</p>
</div>
""", unsafe_allow_html=True)

st.header("Featured Products")

# ---------------------------
# Filter Products
# ---------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# ---------------------------
# Product Grid
# ---------------------------
cols = st.columns(3)

for i, product in enumerate(filtered_products):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="product-card">
            <h3>{product['name']}</h3>
            <p>{product['description']}</p>
            <div class="price">₹{product['price']}</div>
            <br>
            <b>{product['category']}</b>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Add to Cart",
            key=product["name"]
        )

# ---------------------------
# Floating Support Button
# ---------------------------
st.markdown("""
<a class="chat-btn"
href="/Support_Chatbot"
target="_self">
💬 Support
</a>
""", unsafe_allow_html=True)
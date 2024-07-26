import streamlit as st

# Define possible waste products and their uses and potential revenue
waste_product_info = {
    "Crop Residues": {
        "uses": ["Mulch", "Compost", "Animal Feed"],
        "revenue_per_unit": {"Mulch": 10, "Compost": 20, "Animal Feed": 15}
    },
    "Animal Manure": {
        "uses": ["Fertilizer", "Compost"],
        "revenue_per_unit": {"Fertilizer": 25, "Compost": 30}
    },
    "Prunings and Trimmings": {
        "uses": ["Mulch", "Compost"],
        "revenue_per_unit": {"Mulch": 10, "Compost": 20}
    },
    "Cover Crop Biomass": {
        "uses": ["Green Manure", "Compost"],
        "revenue_per_unit": {"Green Manure": 15, "Compost": 20}
    },
    "Processing Byproducts": {
        "uses": ["Compost", "Bioenergy Production"],
        "revenue_per_unit": {"Compost": 20, "Bioenergy Production": 35}
    },
    "Organic Waste from Weeding": {
        "uses": ["Compost", "Mulch"],
        "revenue_per_unit": {"Compost": 20, "Mulch": 10}
    },
    "Food Waste": {
        "uses": ["Compost", "Animal Feed"],
        "revenue_per_unit": {"Compost": 20, "Animal Feed": 15}
    },
    "Straw and Hay": {
        "uses": ["Animal Bedding", "Mulch", "Compost"],
        "revenue_per_unit": {"Animal Bedding": 15, "Mulch": 10, "Compost": 20}
    },
    "Wood Chips and Sawdust": {
        "uses": ["Mulch", "Composting"],
        "revenue_per_unit": {"Mulch": 10, "Composting": 20}
    }
}

# Function to calculate potential revenue
def calculate_revenue(product, amount):
    uses = waste_product_info[product]["uses"]
    revenue_info = waste_product_info[product]["revenue_per_unit"]
    revenue_estimates = {use: amount * revenue_info[use] for use in uses}
    return revenue_estimates

# Streamlit App
st.title("Regenerative Farm Waste Product Utilization")

# Input for waste product type and amount
product = st.selectbox("Select a waste product", list(waste_product_info.keys()))
amount = st.number_input("Enter amount of waste product (in kg)", min_value=0)

if st.button("Get Suggestions and Revenue"):
    if amount > 0:
        suggestions = waste_product_info[product]["uses"]
        revenue_estimates = calculate_revenue(product, amount)
        st.subheader(f"Suggestions for {product}:")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")

        st.subheader("Potential Revenue Estimates:")
        for use, revenue in revenue_estimates.items():
            st.write(f"{use}: ₹{revenue:.2f}")
    else:
        st.write("Please enter a valid amount.")


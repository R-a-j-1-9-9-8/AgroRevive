import streamlit as st
from streamlit_card import card

st.title("AgroRevive: Sustainable Farming Solutions")

st.write("Welcome to AgroRevive! Click on the cards below to navigate to different sections of the application.")


card2 = card(
  title="Carbon Credits Estimator",
  text="Turning Sustainable Practices into Tangible Rewards",
  image="https://149358052.v2.pressablecdn.com/wp-content/uploads/2024/01/24_1.jpg",
)
card3 = card(
  title="Waste Products Utilization",
  text="Sustainable Strategies for Waste Conversion",
  image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTNDEv2RpbPDy19eSQS9mR97fOdS_63LvRGpe6wB340iyCppiBClaqJOqWNQ&s",
)
card4 = card(
  title="Plan Agricultural Practices",
  text=" Strategize for a Sustainable Future",
  image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-xM6v6NqboyrjWqlhm3xPjz5anULsRQqXNUXTzFXAHEjZjrQKaUUL4fOl8w&s",
)
card5 = card(
  title="Knowledge Hub",
  text="A comprehensive hub of resources and information on regenerative agriculture.",
  image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTY8Tdb7NsaEu25DPe44ERB8ZbU3zswWla-YrDmc__MHTqMciwvUq1D3tDHMw&s",
)
card1 = card(
  title="Chatbot Assistance",
  text="Ask all your queries to your chatbot Neko!",
  image="https://media.istockphoto.com/id/1488335095/vector/3d-vector-robot-chatbot-ai-in-science-and-business-technology-and-engineering-concept.jpg?s=612x612&w=0&k=20&c=MSxiR6V1gROmrUBe1GpylDXs0D5CHT-mn0Up8D50mr8=",
)

if card1:
    st.switch_page("pages/RegenFarm_Assistance.py")
if card2:
    st.switch_page("pages/Carbon_Credits_Estimator.py")
if card3:
    st.switch_page("pages/Waste_Products_Utilization.py")
if card4:
    st.switch_page("pages/Regenerative_Farming_Planner.py")
if card5:
    st.switch_page("pages/Knowledge_Hub.py")


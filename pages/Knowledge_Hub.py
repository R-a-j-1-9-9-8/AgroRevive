import streamlit as st

st.title("Knowledge Hub")
    
st.subheader("Types of Regenerative Agricultural Practices")
    
option = st.selectbox(
    "Select the Regenerative Agriculture",
    ("Agroforestry", "Crop Rotation", "Cover Cropping","No-till Farming"),
)

if option == "Agroforestry":
    st.image("https://viagroforestry.org/app/uploads/2021/11/beatrice_wamalwa-vi_agroforestry-15-1-1-2000x1332.jpg", caption="Sustainable Agriculture and Agroforestry ")
    st.title("Agroforestry")
    st.write("### What is Agroforestry?")
    st.write("Agroforestry is a sustainable land management practice that integrates trees and shrubs into agricultural landscapes. This approach combines agricultural and forestry technologies to create more diverse, productive, profitable, healthy, and sustainable land-use systems. Agroforestry systems offer multiple benefits for both the environment and agricultural productivity.")

    st.write("### Key Components of Agroforestry:")
    st.write("- **Trees and Shrubs**: These are deliberately planted or maintained on agricultural land to provide various benefits, including shade, windbreaks, soil enrichment, and habitat for wildlife.")
    st.write("- **Crops and Livestock**: Agroforestry systems typically include traditional agricultural crops and livestock, which can benefit from the improved microclimate and soil conditions created by trees and shrubs.")
    st.write("- **Integrated Management**: The practice involves managing the interactions between trees, crops, and livestock to optimize the overall productivity and sustainability of the land.")

    st.write("### Types of Agroforestry Systems:")
    st.write("- **Silvopasture**: Combining trees and pastureland for livestock grazing. This system improves pasture productivity, animal welfare, and carbon sequestration.")
    st.write("- **Alley Cropping**: Planting rows of trees or shrubs alongside rows of crops. This can enhance soil fertility, reduce erosion, and provide additional income from tree products.")
    st.write("- **Forest Farming**: Growing high-value crops such as medicinal plants, mushrooms, or nuts under the canopy of a managed forest. This practice can diversify income and make use of forest understory.")
    st.write("- **Riparian Buffers**: Planting trees and shrubs along waterways to protect water quality by filtering runoff, reducing erosion, and providing habitat for wildlife.")
    st.write("- **Windbreaks and Shelterbelts**: Rows of trees or shrubs planted to protect crops and livestock from wind, reduce soil erosion, and enhance biodiversity.")

    st.write("### Benefits of Agroforestry:")
    st.write("**Environmental**:")
    st.write("- **Biodiversity**: Enhances habitat for wildlife and promotes biodiversity.")
    st.write("- **Soil Health**: Improves soil structure, fertility, and prevents erosion.")
    st.write("- **Climate Resilience**: Sequesters carbon, reduces greenhouse gas emissions, and improves the resilience of agricultural systems to climate change.")
    st.write("- **Water Management**: Improves water infiltration, reduces runoff, and protects water quality.")

    st.write("**Economic**:")
    st.write("- **Diversified Income**: Provides multiple revenue streams from timber, fruits, nuts, and other tree products.")
    st.write("- **Resource Efficiency**: Enhances resource use efficiency, leading to increased overall productivity and profitability.")
    st.write("- **Risk Reduction**: Reduces financial risk by diversifying farm outputs.")

    st.write("**Social**:")
    st.write("- **Community Benefits**: Enhances food security and provides resources for local communities.")
    st.write("- **Cultural Practices**: Preserves and integrates traditional land management practices.")

    st.write("### How to Implement Agroforestry:")
    st.write("1. **Assess the Site**: Evaluate soil quality, climate, and topography.")
    st.write("2. **Define Goals and Objectives**: Set productivity, conservation, and economic goals.")
    st.write("3. **Choose Appropriate Species**: Select suitable trees, shrubs, crops, and livestock.")
    st.write("4. **Design the System**: Plan the spatial arrangement and layering of components.")
    st.write("5. **Prepare the Land**: Clear unwanted vegetation and prepare the soil.")
    st.write("6. **Planting**: Plant trees, shrubs, and crops at the right time and with proper techniques.")
    st.write("7. **Management and Maintenance**: Prune, weed, irrigate, and manage pests and diseases.")
    st.write("8. **Monitor and Evaluate**: Track growth, yield, soil and water quality, and biodiversity.")
    st.write("9. **Adjust and Adapt**: Make iterative improvements based on monitoring results.")
    st.write("10. **Education and Outreach**: Participate in training and networks, and document and share knowledge.")
    st.video("https://www.youtube.com/watch?v=jLZ0KtNx354")

if option == "Crop Rotation":
    st.image("https://cmv360.s3.ap-southeast-1.amazonaws.com/Crop_Rotation_7b875027b0.png", caption="Crop Rotation: Advantages of Crop Rotation")
    st.title("Crop Rotation")
    st.write("### What is Crop Rotation?")
    st.write("Crop rotation is the practice of growing different types of crops in the same area in sequential seasons. It helps in maintaining soil health, reducing pest and disease cycles, and improving crop yields.")

    st.write("### Benefits of Crop Rotation:")
    st.write("- **Soil Health**: Prevents soil depletion and maintains soil fertility.")
    st.write("- **Pest and Disease Control**: Breaks the lifecycle of pests and diseases.")
    st.write("- **Nutrient Management**: Different crops have different nutrient requirements and contributions to the soil.")
    st.write("- **Improved Yield**: Leads to better overall productivity and crop health.")

    st.write("### How to Implement Crop Rotation:")
    st.write("1. **Plan Your Rotation**: Choose crops based on their families and nutrient needs. Avoid planting the same family in the same spot consecutively.")
    st.write("2. **Soil Preparation**: Ensure the soil is prepared and enriched with organic matter.")
    st.write("3. **Monitor Crops**: Keep track of crop health and soil condition. Adjust plans as necessary based on observations.")
    st.write("4. **Adapt and Adjust**: Modify the rotation plan based on pest and disease occurrence, and soil health indicators.")
    st.video("https://www.youtube.com/watch?v=XeNA6XdMoF8")

if option == "Cover Cropping":
    st.image("https://iffconanos3images.s3.ap-south-1.amazonaws.com/public/admin/news/TgHkQiX3rmJ5MXjwtQOoVxIFXhfzSHGyUyFKZduo.jpg", caption="The Benefits of Cover Crops for Soil Health and Fertility")
    st.title("Cover Cropping")
    st.write("### What is Cover Cropping?")
    st.write("Cover cropping involves planting specific crops, such as grasses, legumes, or brassicas, primarily for the benefit of the soil rather than for harvest. Cover crops are grown to protect and enhance the soil.")

    st.write("### Benefits of Cover Cropping:")
    st.write("- **Soil Protection**: Reduces erosion and protects the soil surface.")
    st.write("- **Soil Fertility**: Adds organic matter and improves nutrient cycling.")
    st.write("- **Weed Suppression**: Outcompetes weeds, reducing the need for herbicides.")
    st.write("- **Water Management**: Improves soil structure and water infiltration.")

    st.write("### How to Implement Cover Cropping:")
    st.write("1. **Select Cover Crops**: Choose species based on your goals (e.g., nitrogen fixation, weed suppression).")
    st.write("2. **Planting**: Plant cover crops during fallow periods or between regular crops.")
    st.write("3. **Management**: Mow or incorporate cover crops into the soil before they set seed.")
    st.write("4. **Monitor and Evaluate**: Observe the impact on soil health, pest and weed pressure, and adjust species selection and management practices as needed.")
    st.video("https://www.youtube.com/watch?v=XQMJK9UYOF4")

if option == "No-till Farming":
    st.image("https://eos.com/wp-content/uploads/2020/09/no-till-farming.png", caption="No-Till Farming: Benefits, Challenges, And Sustainable Effects")
    st.title("No-till Farming")
    st.write("### What is No-till Farming?")
    st.write("No-till farming is a conservation agriculture practice where the soil is not disturbed by tillage. Instead, seeds are directly drilled into the soil, preserving soil structure and organic matter.")

    st.write("### Benefits of No-till Farming:")
    st.write("- **Soil Health**: Preserves soil structure and increases organic matter.")
    st.write("- **Erosion Control**: Reduces soil erosion by maintaining soil cover.")
    st.write("- **Water Conservation**: Improves water infiltration and retention.")
    st.write("- **Carbon Sequestration**: Enhances carbon storage in the soil.")

    st.write("### How to Implement No-till Farming:")
    st.write("1. **Equipment**: Use no-till planters or drills to plant seeds directly into the soil.")
    st.write("2. **Cover Crops**: Incorporate cover crops to maintain soil cover and improve soil health.")
    st.write("3. **Weed Management**: Utilize integrated weed management strategies, including cover crops and crop rotation.")
    st.write("4. **Monitor Soil Health**: Regularly check soil health indicators such as organic matter content, structure, and moisture levels.")

    st.video("https://www.youtube.com/watch?v=hNyu4_RWGZo")
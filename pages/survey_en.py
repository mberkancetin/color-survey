import streamlit as st
import pandas as pd
import numpy as np

options_for_pairwise = [[
    "Employee Welfare and Working Conditions",
    "Product Quality and Consumer Value",
    "Resource Management and Production Efficiency",
    "Ethical Governance and Business Integrity"
],
[
    "Social Equity and Inclusion",
    "Circular Economy and Anti-Consumption",
    "Respect for Labor and Union Rights",
    "Public Image and Social Communication"
],
[
    "Occupational Health and Safety Compliance",
    "Environmental Compliance and Pollution Control",
    "Product Standards and Certifications",
    "Transparency, Auditing, and Reporting"
],
[
    "Local Community and Economic Partnership",
    "Stakeholder Dialogue and Feedback Mechanisms",
    "Partnerships for Innovation and Development",
    "Consumer and Public Empowerment"
],
[
    "Operational Integrity",
    "Societal Alignment",
    "Regulatory Compliance",
    "Stakeholder Collaboration"
]
]

options_explanations = [
[
    [
        "The textile sector needs to make its job opportunities attractive. Just like in the automotive sector, it should create a desire for people to want to work there.",
        "Social facilities such as nurseries and daycare centers for workers' children increase the sense of belonging, especially for female employees.",
        "Various activities should be organized to improve and protect the mental and emotional health of employees, and a family atmosphere should be created in the company. It should make its employees feel that they are valued citizens.",
        "Providing a fair working environment: fair wages and reasonable working hours."
    ],
    [
        "By using quality materials, the lifespan of textile products should be improved. Products that deform after washing should not cause problems for customers.",
        "The materials used should not be derived from animals; equivalent alternatives should be used.",
        "Budgets allocated to advertising should be reduced and invested in quality instead.",
        "Regarding customers, producing high-quality products, ensuring a reasonable price-to-value ratio, and manufacturing durable items should be the main responsibilities of companies."
    ],
    [
        "The product's sales channels must also be respectful of nature and people. Stores should be designed to be resource-efficient and thoughtful, and recycled materials should be preferred for boxes and packaging in online sales.",
        "Innovative water-saving projects, such as rainwater harvesting, should be developed against the risk of water scarcity in the region.",
        "Artificial intelligence should be utilized at every stage of textile production. With the help of technology, the burden on both humans and the environment should be reduced.",
        "Investment should be made in production technologies that reduce recycling, water, and energy consumption."
    ],
    [
        "No one believes in the tactic of raising prices and then lowering them for a 'discount' anymore. Real campaigns should be run.",
        "Upholding integrity and ethical practices (i.e., when you copy a design, credit/compensation needs to be given to the original designer).",
        "Advancement within the company should be based on the individual merits of employees, not through nepotism.",
        "The marketing should actually reflect the product. No false claims."
    ]
],
[
    [
        "Promote body positivity, diversity, and inclusion representing real people, not unrealistic beauty standards.",
        "Employees should have the right to fair wages without discrimination or disability, and there should be equality in the workplace.",
        "There should be no loss of rights due to pregnancy, parenthood, or family circumstances.",
        "Supporting women and equal opportunities."
    ],
    [
        "High-quality, repairable, classic-style products should be produced; this way, the products are not affected by 'fast fashion'.",
        "Possible reward program if customers send in their old clothes - discount for new products.",
        "Establish a separate unit in the production center to make products from recycled materials",
        "Production should be carried out with emphasis on recycling."
    ],
    [
        "Introduce unions to represent the working force",
        "Complying with laws regarding employee rights, allowing union organization, and creating a corporate culture should be a core responsibility.",
        "Practices such as OHS officers, unions, and sick leave should be implemented and regulated in accordance with EU standards.",
        "Manufacturers must respect the legal and human rights of their employees. People should not be forced to work under harsh conditions for the sole purpose of profit."
    ],
    [
        "Textile manufacturers must change their negative public perception. This begins with environmental responsibilities. Significant regulations must be implemented in the near future.",
        "Social and environmental sensitivity should not be used as a marketing tool.",
        "Advertising campaigns should be conducted to ensure that being local is perceived as a sign of privilege. Using celebrities as brand ambassadors who are unlikely to use the product or brand should be avoided.",
        "Textile companies should take a leading role in social responsibility projects (e.g., clothing aid to child protection agencies, etc.)."
    ],
],
[
    [
        "Occupational health should be a priority, and traceability should be ensured with a balance of conscience and quality.",
        "Employing a workplace doctor regardless of the number of employees.",
        "Conduct regular, proactive risk assessments within the scope of occupational health and safety.",
        "Workers should be given regular occupational safety training and the necessary equipment for their safety should be provided."
    ],
    [
        "Pollution of waterways, in particular, affects the entire ecosystem in the water cycle. This impacts water quality, and therefore agricultural quality, leading to droughts that can eventually dry up rivers. Textile waste must not be discharged into waterways.",
        "The microplastic output from textiles should be reduced.",
        "The water consumption of factories and the extent to which chemicals like dyes mix with nature during production should be monitored, and more environmentally friendly criteria should be introduced.",
        "Wastewater should not be released into nature without treatment."
    ],
    [
        "The same size varies from brand to brand. This needs to be standardized.",
        "Regulations should be made nationwide to determine size and production standards; they should be supported by regular inspections and high penalties.",
        "Products that comply with ZDHC standards must be used.",
        "Textile products should be produced by taking user health into consideration."
    ],
    [
        "Regular audits from a third-party company will ensure the industry meets working, governance, and legal standards.",
        "A tracking system showing the entire flow of the product can be transparently embedded into product labels with a QR code, making it accessible to consumers and other stakeholders. This way, everyone knows what stages the product has gone through and consumes with awareness.",
        "The company can employ its own internal auditor at the factory.",
        "The company must be transparent and demonstrate this to everyone."
    ],
],
[
    [
        "Establishing a local football team in the city where they operate, or sponsoring an existing team, can help them gain sympathy in the local community.",
        "Large companies should support the growth of small workshops that produce for them, rather than putting them out of business.",
        "Implementing social projects that support local handicrafts and cultural heritage (e.g., the tradition of cotton craftsmanship).",
        "In recruitment, priority should be given to candidates residing in local among those with similar qualifications."
    ],
    [
        "Consumer satisfaction surveys should be conducted by going into the field.",
        "While producing products, opinions can be obtained from the local people in the factory's area",
        "Communicating regularly with employees, local communities, and stakeholders ensures that problems are recognized early and sustainable solutions are produced.",
        "Contact with the customer should be ensured, and feedback and satisfaction should be taken into account."
    ],
    [
        "Collaboration with civil society organizations should be established for social awareness. Clothing is a basic need, and it is a social responsibility to support those in need.",
        "Competition should be maintained in solidarity with companies operating in the same field. The creation of common values regarding employee rights should be ensured, etc.",
        "Support should be provided for training qualified personnel for the sector by preparing protocols with the relevant departments of universities and vocational high schools.",
        "Supporting sectoral education and providing support to design and fashion schools."
    ],
    [
        "Washing and care instructions can also include environmentally friendly methods that save water and energy (e.g., washing at low temperatures, using natural detergents, etc.).",
        "Promoting a culture of fashion and taste to show people that fashion can be sustainable and long-lasting. For example, holding master classes on combining clothes, teaching how to care for an item to make it last as long as possible.",
        "All stakeholders should be regularly informed through training that supports social awareness about the sector.",
        "Conducting informative studies for the correct use of products."
    ],
],
[
    [
        "Employee Welfare and Working Conditions",
        "Product Quality and Consumer Value",
        "Resource Management and Production Efficiency",
        "Ethical Governance and Business Integrity"
    ],
    [
        "Social Equity and Inclusion",
        "Circular Economy and Anti-Consumption",
        "Respect for Labor and Union Rights",
        "Public Image and Social Communication"
    ],
    [
        "Occupational Health and Safety Compliance",
        "Environmental Compliance and Pollution Control",
        "Product Standards and Certifications",
        "Transparency, Auditing, and Reporting"
    ],
    [
        "Local Community and Economic Partnership",
        "Stakeholder Dialogue and Feedback Mechanisms",
        "Partnerships for Innovation and Development",
        "Consumer and Public Empowerment"
    ],
]]




pairwise_comparisons = [
    [0, 1], [0, 2], [0, 3],
    [1, 2], [1, 3],
    [2, 3]
]

if "results" not in st.session_state:
    if "userID" in st.session_state:
        st.session_state.results = {"userID": st.session_state.userID}
    else:
        st.warning("User name has not been given. Please start from the main page.")
        st.stop()

def create_preference_survey(index, matrix_index):
    if index < len(pairwise_comparisons):
        i = pairwise_comparisons[index][0]
        j = pairwise_comparisons[index][1]

        comparisons = {
            "1- Equally Important": 1,
            "2- Almost equally important": 2,
            "3- Slightly more important": 3,
            "4- Somewhat more important": 4,
            "5- Moderately more important": 5,
            "6- Strongly more important": 6,
            "7- Significantly more important": 7,
            "8- Exceptionally more important": 8,
            "9- Extremely More Important": 9
        }

        @st.dialog("Degree of importance")
        def vote(item, y):
            degree = st.radio(label=f"To what degree is '{item}' more important?", options=list(comparisons.keys()), index=0)
            if degree:
                if st.button("Confirm", key=f"onayla1{matrix_index}{i}{j}"):
                    if y:
                        st.session_state.results[f"Q{st.session_state.question_index}"] = comparisons[degree]
                        # st.session_state.results.append(comparisons[degree])
                    else:
                        st.session_state.results[f"Q{st.session_state.question_index}"] = 1/comparisons[degree]
                        # st.session_state.results.append(1/comparisons[degree])
                    st.session_state.current_index += 1  # Move to the next comparison
                    st.session_state.question_index += 1
                    st.rerun()  # Rerun the app to show the next comparison


        if len(st.session_state.results) < 32:
            st.write(f"{st.session_state.question_index}/30 - {options_for_pairwise[matrix_index][i]} ile {options_for_pairwise[matrix_index][j]} kıyaslandığınızda hangisinin ne derecede önemli olduğunu belirtiniz.")

            # Create two columns for the options
            col1, col2 = st.columns(2)

            option1 = col1.container(height=250)
            if option1.button(f"**{options_for_pairwise[matrix_index][i]}**", use_container_width=True, key=f"option1{matrix_index}{i}{j}"):
                vote(f"{options_for_pairwise[matrix_index][i]}", True)
            option1.caption(f"""
                * {options_explanations[matrix_index][i][0]}
                * {options_explanations[matrix_index][i][1]}
                * {options_explanations[matrix_index][i][2]}
                * {options_explanations[matrix_index][i][3]}
                """)

            option2 = col2.container(height=250)
            if option2.button(f"**{options_for_pairwise[matrix_index][j]}**", use_container_width=True, key=f"option2{matrix_index}{i}{j}"):
                vote(f"{options_for_pairwise[matrix_index][j]}", False)
            option2.caption(f"""
                * {options_explanations[matrix_index][j][0]}
                * {options_explanations[matrix_index][j][1]}
                * {options_explanations[matrix_index][j][2]}
                * {options_explanations[matrix_index][j][3]}
                """)



if __name__ == "__main__":
    # Set page config
    st.set_page_config(
        page_title="Corporate Responsibility Pairwise Comparison Survey",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    if "current_index" not in st.session_state:
        st.session_state.current_index = 0
    if "current_matrix" not in st.session_state:
        st.session_state.current_matrix = 0
    if "question_index" not in st.session_state:
        st.session_state.question_index = 1

    # Display results after all comparisons
    if st.session_state.current_index >= 6:
        st.session_state.current_matrix += 1
        st.session_state.current_index = 0
        # Display results after all comparisons
        if st.session_state.current_matrix >= 5:
        # if st.session_state.question_index == 5:
            from streamlit_gsheets import GSheetsConnection
            st.warning("Saving your answers.")
            conn = st.connection("gsheets", type=GSheetsConnection)

            df1 = conn.read(
                worksheet="cevaplar"
            )
            # Display our Spreadsheet as st.dataframe
            # st.dataframe(df1)

            dct = {k:[v] for k,v in st.session_state.results.items()} 
            results_dict = pd.DataFrame.from_dict(dct)
            # st.dataframe(results_dict)
            df_appended = pd.concat([df1, results_dict], ignore_index=True)
            # st.dataframe(df_appended)
            df = conn.update(
                    worksheet="cevaplar",
                    data=df_appended,
                )
            st.success("Your answers has been successfully saved.")
            st.success("Thank you for participating this research.")
            st.warning("You can close this window.")
            st.cache_data.clear()
            st.stop()

    # Call the survey function
    create_preference_survey(st.session_state.current_index, st.session_state.current_matrix)

import streamlit as st

st.header("Kurumsal Sorumluluk Anketi / Corporate Responsibility Survey")

# Language Selection
lang = st.radio("Dil Seçin / Select Language", ("Türkçe", "English"))

# Display text based on selected language
if lang == "Türkçe":
    st.markdown('''
    Şirketlerin sorumlulukları konusunda kişisel deneyimlerinizi göz önünde bulundurarak, özellikle yerel tekstil şirketlerinin, toplum ve çevreye karşı sorumluluklarını göstermek için hangi eylemleri veya kriterleri ön planda tutmalarını beklersiniz? Bu tür eylemleri nasıl değerlendirebiliriz ve deneyimleriniz ışığında hangi eylemler birbirleriyle kıyaslandığında daha önemli olabilir?
    ''')
    user_id = st.text_input("Lütfen ankete başlamak için size verilen katılımcı kimliğini giriniz:")
    button_text = "Ankete Başla"
    error_message = "Lütfen başlamadan önce bir katılımcı kimliği girin."

else: # English
    st.markdown('''
    Considering your personal experiences, what actions or criteria would you expect local textile companies to prioritize to demonstrate their responsibility towards society and the environment? How can we evaluate such actions, and in light of your experiences, which actions might be more important when compared to each other?
    ''')
    user_id = st.text_input("Please enter the participant ID given to you to start the survey:")
    button_text = "Start Survey"
    error_message = "Please enter a participant ID before starting."


if st.button(button_text):
    if user_id:  # Check if the user_id string is not empty
        # Save the user ID to the session state to be used in the survey page
        st.session_state.userID = user_id
        
        # Switch to the correct survey page based on language
        if lang == "Türkçe":
            st.switch_page("pages/survey.py")
        else:
            # As you mentioned, you will create this file
            st.switch_page("pages/survey_en.py") 
    else:
        st.error(error_message)

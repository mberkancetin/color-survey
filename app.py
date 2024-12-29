import streamlit as st

st.header("Kurumsal Sorumluluk Anketi")

st.markdown('''
Kurumsal Sosyal Sorumluluk (KSS), şirketlerin toplum, çevre ve ekonomi üzerindeki etkilerini nasıl yönettikleriyle ilgilidir. Bu, şirketlerin çevresel sürdürülebilirlik, adil iş gücü uygulamaları ve topluluklara katkı gibi alanlarda etik davranışlar sergileyerek, farklı paydaşların (çalışanlar, müşteriler, tedarikçiler, yatırımcılar vb.) çıkarlarını dengelemelerini içerir.
''')

st.markdown('''
Bu konuda kişisel deneyimlerinizi göz önünde bulundurarak, özellikle Adana’daki tekstil şirketlerinin, toplum ve çevreye karşı sorumluluklarını göstermek için hangi eylemleri veya kriterleri ön planda tutmalarını beklersiniz? Bu tür eylemleri nasıl değerlendirebiliriz ve deneyimleriniz ışığında hangi eylemler birbirleriyle kıyaslandığında daha önemli olabilir?
''')


if st.button('Ankete başla'):
    
    st.switch_page("pages/survey.py")

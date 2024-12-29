import streamlit as st
import pandas as pd
import numpy as np

options_for_pairwise = [[
    "Çalışan Refahı",
    "Adil Maaş ve Yan Haklar",
    "Mesleki Gelişim ve Destek",
    "Uygun Fiyatlılık ve Adil Fiyatlandırma"
],
[
    "Fırsat Eşitliği ve İstihtamın Desteklenmesi",
    "Sendikal Haklar ve Örgütlenme Özgürlüğü",
    "STK ile İş Birliği",
    "Projelerin Toplumla İletişimi"
],
[
    "İş Sağlığı ve Güvenliği",
    "Ürünlerin Kalitesi ve Standartlara Uygunluğu",
    "Bağımsız Denetim ve Raporlama",
    "Kaynakların Verimli Kullanımı ve Yenilikçi Teknolojilere Yatırım"
],
[
    "Tüketici Eğitimi ve Farkındalığı",
    "Toplumu ve Çalışanları Biliçlendirme Etkinlikleri",
    "Yerel Ekonomik Destek ve Tedarik Zinciri Sorumlulğu",
    "Paydaş Katılımının Sağlanması"
],
[
    "Çömertlik ve İyilikseverlik",
    "Toplumsal Talebi Gerçekleştirme",
    "Kurallara ve Standartlara Uygunluk",
    "Paydaşlarla Birlikte Karar Alma"
]
]

options_explanations = [
[
    [
        "Çalışanların yaşam standartlarını iyileştirmek için projeler oluşturulmalı.",
        "Şirketler, işçilerin haklarını, sağlığını ve güvenliğini ön planda tutmalı.",
        "Çalışanlar için aile dostu izin politikaları uygulanmalı.",
        "Çalışanlar için yemek ve dinlenme alanları sağlanmalı."
    ],
    [
        "Enflasyonla mücadele için çalışanlara destek sağlanmalı.",
        "Fazla mesai ödemelerinin garantisi verilmeli ve ihbar - tazminat hakları güçlendirilmeli.",
        "Çalışanlar için uzun vadeli sağlık ve emeklilik planları yapılmalı.",
        "Çalışanlar için ödüllendirme ve teşvik programları oluşturulmalı."
    ],
    [
        "Çalışanlar için psikolojik destek hizmetleri sunulmalı.",
        "Çalışanlar için eğitim programları ile iş gücü kalitesi artırılmalı.",
        "Çalışanlar için mesleki gelişim fırsatları artırılmalı.",
        "Yöneticilere liderlik ve yönetim becerilerini geliştirecek eğitimler verilmeli."
    ],
    [
        "Fiyatlar, kaliteyle uyumlu olmalı.",
        "Fiyat artışlarının sebepleri şeffaf bir şekilde açıklanmalı.",
        "Ürün fiyatları, düşük gelirli ailelerin alabileceği seviyede tutulmalı.",
        "Fiyat artışlarına karşı esnek ödeme planları sunulmalı."
    ]
],
[
    [
        "Çalışanlar için eşit fırsatlar sağlanmalı.",
        "Cinsiyet, yaş veya köken gibi faktörlere dayalı ayrımcılık yapılmamalı.",
        "Şirket içi kadın hakları farkındalık projeleri uygulanmalı.",
        "Şirket, yerel halkı daha fazla istihdam etmeli."
    ],
    [
        "Sendikal haklara saygı gösterilmeli (toplu sözleşme, grev, lokavt).",
        "Örgütlenme hakkını kullanan işçilere ayrımcılık uygulanması önlenmeli.",
        "Sendikal faaliyetlere katılan işçilerin işten çıkarılması engellenmeli.",
        "Sendika ile şirket arasında açık iletişim olmalı."
    ],
    [
        "Şirketin topluma katkı sağlamak için gönüllü projelere katılması sağlanmalı.",
        "Çalışanlar, topluma duyarlı projelerde yer almalı.",
        "Şirket, sosyal sorumluluk projelerinde yerel STK'larla işbirliği yapmalı.",
        "Şirket, toplumun farklı ihtiyaçlarına yönelik projeler başlatmalı."
    ],
    [
        "Şirketin sosyal sorumluluk projelerinin tanıtımı yapılmalı.",
        "Etik üretim süreçleri topluma duyurulmalı.",
        "Şirketin başarıları hakkında kamuoyuna bilgilendirme yapılmalı.",
        "Şirketin etik ve toplumsal sorumluluklarına dair düzenli olarak halkla ilişkiler çalışmaları yapılmalı."
    ],
],
[
    [
        "Yüksek standartlarda iş güvenliği uygulamaları yapılmalı.",
        "Çalışma koşullarında uluslararası standartlara uyum sağlanmalı.",
        "Tehlikeli kimyasallar ve maddelerle ilgili düzenlemeler artırılmalı.",
        "Çalışanların fiziksel ve ruhsal sağlığını desteklemek için hizmetler sağlanmalı."
    ],
    [
        "Ürünlerin kalitesinde süreklilik sağlanmalı, markalar güven oluşturmalı.",
        "Kumaşlar uzun ömürlü ve dayanıklı olmalı, geri dönüşümü sağlanmalı.",
        "Çevre dostu paketleme olmalı, ambalaj atıkları minimize edilmeli.",
        "Şirketler, ürünlerinin etiketlerinde çevresel etkileri açıklamalı."
    ],
    [
        "Şirketin katkıları düzenli olarak raporlanmalı ve toplumla paylaşılmalı.",
        "Tedarikçilerin etik uygunluğunun kontrolünü yapmalı.",
        "Şirket denetimler ve raporlamalarla şeffaflık sağlamalı.",
        "Çevresel etkileri düzenli olarak kontrol etmeli."
    ],
    [
        "Şirket, çevreyi kirleten atıklar için geri dönüşüm programları oluşturmalı.",
        "Sürdürülebilir teknoloji geliştirme süreçlerine yatırım yapılmalı.",
        "Üretim süreçlerinde enerji verimliliği artırılmalı.",
        "Çevre dostu kimyasal alternatiflerin kullanımı sağlanmalı."
    ],
],
[
    [
        "Tüketiciler, geri dönüşüm hakkında bilgilendirilmeli.",
        "Fiyat artışlarının altındaki sebepler şeffaf bir şekilde açıklanmalı.",
        "Ürünlerin etiketlerinde üretim süreci hakkında bilgi vermeli.",
        "Şirketler, çevre bilincini artırmak için kampanyalar yapmalı."
    ],
    [
        "Şirket, çevreyi koruma konusunda toplumu bilgilendirici etkinlikler düzenlemeli.",
        "Eğitim ve mesleki beceri geliştirme programları yerel halka sunulmalı.",
        "Çalışanlar için insan hakları ve ayrımcılık karşıtı eğitimler yapılmalı.",
        "İş yerinde mobbing ve taciz önleyici eğitimler sunmalı ve politikalar geliştirilmeli."
    ],
    [
        "Yerel üreticiler desteklenmeli, ithalat yerine yerli üretim teşvik edilmeli.",
        "İş birliği yapılan tedarikçilerin etik kurallara uygunluğu denetlenmeli.",
        "Şirketler, yerel ekonomiyi destekleyecek projelere yatırım yapmalı.",
        "Fabrikalar, yerel halka eğitim ve iş olanakları sunmalı."
    ],
    [
        "Anonim şikayet sistemi kurulmalı ve ücretsiz hukuk danışmanlığı imkanı sunulmalı.",
        "Paydaşların şikayetlerini dinleme mekanizması.",
        "Moda markaları, sosyal sorumluluk projelerine dahil olmalı.",
        "Yatırımcılar, şirketin sosyal sorumluluk projelerine katılımını teşvik etmeli."
    ],
],
[
    [
        "Çalışan Refahı",
        "Adil Maaş ve Yan Haklar",
        "Mesleki Gelişim ve Destek",
        "Uygun Fiyatlılık ve Adil Fiyatlandırma"
    ],
    [
        "Fırsat Eşitliği ve İstihtamın Desteklenmesi",
        "Sendikal Haklar ve Örgütlenme Özgürlüğü",
        "STK ile İş Birliği",
        "Projelerin Toplumla İletişimi"
    ],
    [
        "İş Sağlığı ve Güvenliği",
        "Ürünlerin Kalitesi ve Standartlara Uygunluğu",
        "Bağımsız Denetim ve Raporlama",
        "Kaynakların Verimli Kullanımı ve Yenilikçi Teknolojilere Yatırım"
    ],
    [
        "Tüketici Eğitimi ve Farkındalığı",
        "Toplumu ve Çalışanları Biliçlendirme Etkinlikleri",
        "Yerel Ekonomik Destek ve Tedarik Zinciri Sorumlulğu",
        "Paydaş Katılımının Sağlanması"
    ],
]]

pairwise_comparisons = [
    [0, 1], [0, 2], [0, 3],
    [1, 2], [1, 3],
    [2, 3]
]

if "results" not in st.session_state:
    # st.session_state.results = [np.random.randint(1000000, 9999999), ]
    st.session_state.results = {"userID": np.random.randint(1000000, 9999999)}

def create_preference_survey(index, matrix_index):
    if index < len(pairwise_comparisons):
        i = pairwise_comparisons[index][0]
        j = pairwise_comparisons[index][1]

        comparisons = {
            "1- Eşit derecede": 1,
            "2- Biraz daha önemli": 2,
            "3- Belirgin derecede önemli": 3,
            "4- Güçlü derecede daha önemli": 4,
            "5- Aşırı derecede daha önemli": 5
        }

        @st.dialog("Önem derecesi")
        def vote(item, y):
            degree = st.radio(label=f"{item} ne derecede daha önemli?", options=list(comparisons.keys()), index=0)
            if degree:
                if st.button("Onayla", key=f"onayla1{matrix_index}{i}{j}"):
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
        page_title="Kurumsal Sorumluluk Anketi",
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
            st.warning("Cevabınız kaydediliyor")
            conn = st.connection("gsheets", type=GSheetsConnection)

            df1 = conn.read(
                worksheet="cevaplar"
            )
            # Display our Spreadsheet as st.dataframe
            # st.dataframe(df1)

            dct = {k:[v] for k,v in st.session_state.results.items()}  # WORKAROUND
            results_dict = pd.DataFrame.from_dict(dct)
            # st.dataframe(results_dict)
            df_appended = pd.concat([df1, results_dict], ignore_index=True)
            # st.dataframe(df_appended)
            df = conn.update(
                    worksheet="cevaplar",
                    data=df_appended,
                )
            st.success("Cevabınız kaydedilmiştir.")
            st.success("Anketimize katıldığınız için teşekkür ederiz.")
            st.warning("Bu pencereyi kapatabilirsiniz.")
            st.cache_data.clear()
            st.stop()

    # Call the survey function
    create_preference_survey(st.session_state.current_index, st.session_state.current_matrix)

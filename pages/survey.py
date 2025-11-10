import streamlit as st
import pandas as pd
import numpy as np

options_for_pairwise = [[
    "Çalışan Refahı ve Çalışma Koşulları",
    "Ürün Kalitesi ve Tüketici Değeri",
    "Kaynak Yönetimi ve Üretim Verimliliği",
    "Etik Yönetişim ve İş Ahlakı"
],
[
    "Sosyal Adalet ve Kapsayıcılık",
    "Döngüsel Ekonomi ve Tüketim Karşıtlığı",
    "Emek ve Sendika Haklarına Saygı",
    "Kamu İmajı ve Sosyal İletişim"
],
[
    "İş Sağlığı ve Güvenliği Uyumu",
    "Çevresel Uyum ve Kirlilik Kontrolü",
    "Ürün Standartları ve Sertifikalar",
    "Şeffaflık, Denetim ve Raporlama"
],
[
    "Yerel Toplum ve Ekonomik Ortaklık",
    "Paydaş Diyaloğu ve Geri Bildirim Mekanizmaları",
    "Yenilik ve Kalkınma İçin Ortaklıklar",
    "Tüketici ve Kamu Katılımı"
],
[
    "Operasyonel Bütünlük",
    "Toplumla Uyumluluk",
    "Mevzuata Uygunluk",
    "Paydaşlarla İş Birliği"
]
]

options_explanations = [
[
    [
        "Tekstil sektörünün çalışma olanaklarını cazip hale getirmesi gerekir. Tıpkı otomotiv sektöründe olduğu gibi, insanların orada çalışma isteği duyması sağlanmalı",
        "İşçilerin çocukları için kreş ve gündüz bakım evi gibi sosyal imkanlar, özellikle kadın çalışanların aidiyet hissini arttırır",
        "Şirkette çalışanların akıl ve ruh sağlığını geliştirmeleri ve korumaları için çeşitli etkinlikler düzenlenmeli, şirkette aile ortamı oluşturulmalıdır. Çalışanlarına değerli bir vatandaş olduğunu hissettirmelidir",
        "Adil çalışma ortamı sağlama: adil ücret ve makul çalışma saatleri"
    ],
    [
        "Kaliteli malzemeler kullanılarak tekstil ürünlerinin kullanım ömürleri göz önünde bulundurulmalı. Yıkama sonrası deforme olan ürünler müşterileri mağdur etmemeli",
        "Kullanılan malzemeler hayvansal kaynaklı olmamalı, onlara eşdeğer alternatifler kullanılmalıdır",
        "Reklamlara ayrılan bütçeler azaltılmalı, onun yerine kaliteye yatırılmalıdır",
        "Müşterilere ilişkin ise kaliteli ürünler üretilmesi, fiyat-değer oranının makul olması ve dayanıklı ürünler üretilmesi firmaların ana sorumlulukları olmalıdır"
    ],
    [
        "Ürünün satış kanalları da doğaya saygılı ve insana uyumlu olmalıdır. Mağazalar tasarruflu ve özenle tasarlanmalı, online satışlarda ise kutu ve paketlemede geri dönüştürülmüş ürünler tercih edilmelidir",
        "Bölgedeki su kıtlığı riskine karşı, yağmur suyu hasadı gibi yenilikçi su tasarrufu projeleri geliştirmeli",
        "Tekstil üretiminin her aşamasında yapay zekadan faydalanılmalıdır. Teknoloji yardımı ile insan yükü ve doğa yükü azaltılmalıdır",
        "Geri dönüşüm, su ve enerji tüketimini azaltacak üretim teknolojilerine yatırım yapılmalı"
    ],
    [
        "Fiyatları arttırıp sonra 'indirim' diye düşürme taktiğine artık kimse inanmıyor. Gerçek kampanyalar yapılmalı",
        "Dürüstlük ve etik uygulamaları korumak (yani, bir tasarımı kopyaladığınızda, orijinal tasarımcıya kredi/tazminat verilmesi gerekir).",
        "Şirket içinde yükselme, torpil yoluyla değil, çalışanların bireysel liyakatlerine göre olmalıdır",
        "Pazarlama, ürünü doğru bir şekilde yansıtmalıdır. Gerçeğe aykırı veya yanıltıcı iddialarda bulunulmamalıdır"
    ]
],
[
    [
        "Gerçekçi olmayan güzellik standartlarını değil, gerçek insanları temsil eden beden olumlamasını, çeşitliliği ve kapsayıcılığı teşvik edilmeli",
        "Ayrımcılık veya engellilik durumu ayrımı yapılmadan çalışanlar adil ücret alma hakkına sahip olmalı, iş yerinde eşitlik olmalı",
        "Hamilelik, ebeveynlik veya aile durumları nedeniyle hak kaybı yaşanmamalı",
        "Kadınları ve fırsat eşitliğini desteklemek"
    ],
    [
        "Yüksek kalitede, tamir edilebilen, klasik tarzda ürünler üretilmeli; bu şekilde ürünler 'hızlı moda'dan etkilenmez",
        "Müşterilerin eski kıyafetlerini göndermeleri halinde ödül programı uygulanabilir - yeni ürünlerde indirim gibi",
        "Geri dönüştürülmüş malzemelerden ürünler yapmak için üretim merkezinde ayrı bir birim daha kurmalı",
        "Geri dönüşüme önem vererek üretim yapılmalıdır"
    ],
    [
        "İşçi gücünü temsil etmek için sendikalar teşvik edilmeli",
        "Çalışan haklarında yasalara uymak, sendikal örgütlenmeye izin vermek ve kurumsal bir kültür oluşturmak esas bir sorumluluk olmalıdır",
        "İSG görevlileri, sendikalar, hastalık izinleri gibi uygulamalar hayata geçirilmeli ve AB standartlarına uygun şekilde düzenlenmeli",
        "Üreticiler çalışanlarının yasal ve insani haklarını gözetmelidir. Fazla kar amacı ile zor şartlarda insanlar çalıştırılmamalıdır"
    ],
    [
        "Tekstil üreticileri toplumdaki negatif izlenimi değiştirmelidir. Bu da doğaya olan sorumluluklarla başlayacaktır. Yakın gelecekte ciddi düzenlemeler yapılmalıdır",
        "Toplumsal ve çevreye karşı duyarlılığın bir pazarlama aracı olarak kullanılmaması gerekir",
        "Yerelliğin bir ayrıcalık göstergesi olarak algılanmasını sağlayacak reklam kampanyaları yapılmalı. O ürünü veya markayı kullanmayacağı bariz olan kişilerin reklam yüzü olmasından kaçınılmalı",
        "Sosyal sorumluluk projelerinde tekstil şirketleri ön plana çıkmalı (örneğin Çocuk Esirgeme Kurumu'na giyecek yardımı vb.)"
    ],
],
[
    [
        "İş sağlığı öncelikli olmalı, vicdan ve kalite dengesi ile izlenebilirlik sağlanmalıdır",
        "Herhangi bir çalışan sayısı kriteri olmaksızın iş yeri hekimi çalıştırmak",
        "İş sağlığı ve güvenliği kapsamında düzenli, proaktif risk değerlendirmeleri yapmalı",
        "İşçilere düzenli olarak iş güvenliği eğitimi verilmeli, güvenlikleri için gerekli ekipmanlar temin edilmelidir"
    ],
    [
        "Özellikle su yollarının kirletilmesi, su döngüsünde yer alan tüm ekosistemi etkilemektedir. Bu durum su kalitesini, dolayısıyla tarım kalitesini etkiler ve zamanla nehirlerin kurumasına kadar giden kuraklığa sebep olur. Tekstil atıkları su yollarına atılmamalıdır",
        "Tekstildeki mikroplastik çıktısı azaltılmalı",
        "Üretim aşamasında fabrikaların su tüketimi ve boya gibi kimyasalların doğaya ne kadar karıştığı denetlenmeli ve daha çevreci kriterler getirilmelidir",
        "Atık suların arıtılmadan doğaya salınmaması gerekir"
    ],
    [
        "Aynı beden markadan markaya farklılık gösteriyor. Bunun standartlaştırılması gerekir",
        "Beden ve üretim standartlarının belirlenmesi için ülke genelinde düzenlemeler yapılmalı; düzenli denetimler ve yüksek cezalarla desteklenmeli",
        "ZDHC standartlarına uygun ürün kullanılmalı",
        "Tekstilde üretilen ürünlerin kullanıcı sağlığı göz önüne alınarak üretilmesi"
    ],
    [
        "Üçüncü taraf bir şirket tarafından yapılan düzenli denetimler, sektörün çalışma, yönetim ve yasal standartlara uymasını sağlayacaktır",
        "Ürünün bütün akışını gösteren bir takip sistemi, şeffaf biçimde ürünlerin etiketlerine QR kod ile işlenip tüketici ve diğer paydaşların erişimine açılabilir. Bu sayede herkes ürünün hangi aşamalardan geçtiğini bilir ve bilinçle tüketir",
        "Firma, fabrikada kendi iç denetçisini çalıştırabilir",
        "Şirketin şeffaf olması ve bunu herkese göstermesi gerekir"
    ],
],
[
    [
        "Faaliyet gösterilen şehirde yerel bir futbol takımı kurmaları veya halihazırdaki takıma sponsor olmaları, yerel toplumdaki sempatiyi kazanmalarını sağlayabilir",
        "Büyük firmalar kendilerine üretim yapan küçük atölyeleri yok etmek yerine büyümelerini desteklemelidir",
        "Yerel el sanatlarını ve kültürel mirası (örneğin pamuk işçiliği geleneği) destekleyen sosyal projeler yapmalıdır",
        "İşe alımlarda, benzer niteliklere sahip adaylar arasından yerelde ikamet edenlere öncelik vermeli"
    ],
    [
        "Sahaya çıkılarak tüketiciye memnuniyet anketleri yapılmalı",
        "Ürünler üretilirken fabrikanın olduğu bölgedeki halktan fikir alınabilir",
        "Çalışanlar, yerel topluluklar ve paydaşlarla düzenli iletişim kurmak, sorunların erken fark edilmesini ve sürdürülebilir çözümler üretilmesini sağlar",
        "Müşteri ile irtibat sağlanmalı, geri bildirim ve memnuniyet dikkate alınmalıdır"
    ],
    [
        "Toplumsal bilinçlendirme için sivil toplum örgütleriyle iş birliği yapılmalıdır. Giyinme zorunlu bir ihtiyaçtır ve sosyal sorumluluk olarak ihtiyaç sahiplerine destek olmaları gerekir",
        "Aynı alanda faaliyet gösteren firmalarla dayanışma halinde rekabet sürdürülmeli. Çalışan hakları konusunda ortak değerler yaratılması sağlanmalı vb",
        "Üniversiteler ve meslek liselerinin ilgili bölümleriyle protokoller hazırlayarak sektöre kalifiye eleman yetiştirilmesi konusunda destek olunmalı",
        "Sektörel eğitimi desteklemeli, tasarım ve moda okullarına destek vermelidir"
    ],
    [
        "Yıkama ve bakım talimatları, su ve enerji tasarrufu sağlayan çevreye duyarlı yöntemleri de kapsayabilir (Örneğin, düşük sıcaklıkta yıkama, doğal deterjan kullanımı vb.)",
        "Modanın ekolojik ve uzun ömürlü olabileceğini göstermek için moda ve zevk kültürünü teşvik etmek. Örneğin, kıyafetleri birleştirme üzerine atölyeler düzenlemek, bir eşyaya daha uzun süre dayanması için nasıl bakılacağını öğretmek",
        "Sektör hakkında toplumsal bilinci destekleyici eğitimler ile tüm paydaşlar düzenli olarak bilgilendirilmeli",
        "Ürünlerin doğru kullanımı için bilgilendirici çalışmalar yapmak"
    ],
],
[
    [
        "Çalışan Refahı ve Çalışma Koşulları",
        "Ürün Kalitesi ve Tüketici Değeri",
        "Kaynak Yönetimi ve Üretim Verimliliği",
        "Etik Yönetişim ve İş Ahlakı"
    ],
    [
        "Sosyal Adalet ve Kapsayıcılık",
        "Döngüsel Ekonomi ve Tüketim Karşıtlığı",
        "Emek ve Sendika Haklarına Saygı",
        "Kamu İmajı ve Sosyal İletişim"
    ],
    [
        "İş Sağlığı ve Güvenliği Uyumu",
        "Çevresel Uyum ve Kirlilik Kontrolü",
        "Ürün Standartları ve Sertifikalar",
        "Şeffaflık, Denetim ve Raporlama"
    ],
    [
        "Yerel Toplum ve Ekonomik Ortaklık",
        "Paydaş Diyaloğu ve Geri Bildirim Mekanizmaları",
        "Yenilik ve Kalkınma İçin Ortaklıklar",
        "Tüketici ve Kamu Katılımı"
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
            "2- Neredeyse eşit derecede önemli": 2,
            "3- Biraz daha önemli": 3,
            "4- Daha fazla önemli": 4,
            "5- Orta derecede önemli": 5,
            "6- Belirgin derecede önemli": 6,
            "7- Güçlü derecede  derecede önemli": 7,
            "8- Olağanüstü şekilde daha önemli": 8,
            "9- Aşırı derecede daha önemli": 9
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

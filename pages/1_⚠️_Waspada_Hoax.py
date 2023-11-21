import streamlit as st
import requests
import pandas as pd


def waspada_hoax():

    tab1, tab2 = st.tabs(["Hoax Terbaru", "Keterangan"])

    with tab1:
        st.write('# :blue[10 Hoax Terbaru]')
        st.write('_Bijak menyikapi, cek dulu sebelum sebar!_')
        
        response = requests.get("https://yudistira.turnbackhoax.id/Antihoax/latest/20/528b20z21891dd30b0ac2")
        data = response.json()

        df = pd.DataFrame.from_dict(data)

        df = df[df['classification'].isin(['Manipulated Content',
                'Misleading Content',
                'False Context',
                'Impostor Content',
                'False Connection',
                'Fabricated Content',
                'Satire'])].reset_index(drop=True)
        
        df = df.head(10).reset_index(drop=True)

        df['title'] = df['title'].str.replace(r"\[.*\]","")
        # df['title'] = df['title'].str.replace(r"\(.*\)","")
        # df['title'] = df['title'].apply(lambda x: re.sub(r'[^\w\s]','',x))

        for i in range(10):
            st.subheader(str(i+1) + '. ' + df['title'].loc[i], divider='rainbow')
            st.caption('Kategori: ' + df['classification'].loc[i])

            st.markdown(df['conclusion'].loc[i])
    
    with tab2:
        st.header("Panduan mengenai misinformation")
        st.image("images/misinformation_matrix.png")


waspada_hoax()
import pandas as pd
import streamlit as st
import joblib
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import keras

modelo = keras.models.load_model('data/multilayer-perceptron.keras')

scaler = joblib.load("data/scaler.joblib")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://raw.githubusercontent.com/FIAP-Tech-Challenge/datathon/c36b8f489d9bf07499bb33fb17052ca123066db9/data/1.jpg");
background-size: 15%;
background-position: right;
background-repeat: no-repeat;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("SIMULADOR DE BOLSA 🤖")

st.markdown(
                """Digite as notas abaixo para simular os indicadores de performance do aluno, em seguida clique em **:blue[Simular]**. O modelo determinará se o aluno obteve a concessão da bolsa de estudos ou não."""
            )

st.divider()

def predict(aluno: pd.DataFrame):
        aluno_scaled = scaler.transform(aluno)
        pred = modelo.predict(aluno_scaled)

        if pred.round()[0] > 0:
            st.balloons()
            st.success(
                ":white_check_mark: **Resultado:** **Parabéns** o aluno **foi aprovado** para receber sua bolsa de estudos :grinning:"
            )
        else:
            st.error(
                ":x: **Resultado:** O aluno **ainda não está em condições** de receber a bolsa de estudos :disappointed:"
            )

with st.container():
                col0, col1, col2, col3 = st.columns(4)

                with col0:
                    indicador_inde = st.number_input(
                        label="**:blue[ Índice de Desenvolvimento Educacional]**",
                        key="inde",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

                with col1:
                    indicador_ian = st.number_input(
                        label="**:blue[Indicador de Adequação ao Nível]**",
                        key="ian",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

                with col2:
                    indicador_ida = st.number_input(
                        label="**:blue[Indicador de Aprendizagem]**",
                        key="ida",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

                with col3:
                    indicador_ieg = st.number_input(
                        label="**:blue[Indicador de Engajamento]**",
                        key="ieg",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

with st.container():
                col0, col1, col2, col3 = st.columns(4)

                with col0:
                    indicador_iaa = st.number_input(
                        label="**:blue[Indicador Auto Avaliação]**",
                        key="iaa",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

                with col1:
                    indicador_ips = st.number_input(
                        label="**:blue[Indicador Psicossocial]**",
                        key="ips",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

                with col2:
                    indicador_ipp = st.number_input(
                        label="**:blue[Indicador Psicopedagógico]**",
                        key="ipp",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

                with col3:
                    indicador_ipv = st.number_input(
                        label="**:blue[Indicador Ponto de Virada]**",
                        key="ipv",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

aluno = pd.DataFrame(
                {
                    "IAA": indicador_iaa,
                    "IAN": indicador_ian,
                    "IDA": indicador_ida,
                    "IEG": indicador_ieg,
                    "INDE": indicador_inde,
                    "IPP": indicador_ipp,
                    "IPS": indicador_ips,
                    "IPV": indicador_ipv,
                },
                index=[0],
            )

if st.button(":crystal_ball: Simular", key="btn_predict_mlp"):
                with st.spinner("Processando..."):
                    st.subheader(":blue[Matriz de entrada do modelo]", divider="blue")
                    st.dataframe(aluno, hide_index=True)

                    st.subheader(":blue[Previsão do modelo]", divider="blue")
                    predict(aluno)


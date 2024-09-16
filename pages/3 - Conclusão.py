import streamlit as st

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

st.title("CONCLUSÃO 📝")
st.markdown(
    """ 
    Neste projeto, desenvolvemos uma Rede Neural de Perceptron Multicamadas (MLP) para otimizar a concessão de bolsas de estudo na ONG Passos Mágicos. A rede se mostrou eficaz, oferecendo insights valiosos para decisões estratégicas. A ONG, com 30 anos de atuação, apoia crianças e adolescentes em vulnerabilidade social através de educação, cultura, esporte e lazer.
    """,
    unsafe_allow_html=True,           
)

st.markdown(
    """ 
    Durante a análise de dados, verificamos que a maioria dos alunos atendidos frequenta escolas públicas e muitos ingressaram em ensino superior, destacando o impacto positivo da ONG. No modelo de rede neural usa dados históricos e simulados para identificar candidatos ideais para bolsas, com o usuário apenas inserindo as notas dos alunos. 
    """,
    unsafe_allow_html=True,           
)

st.markdown(
    """ 
    Este projeto evidencia a eficácia das redes neurais e reforça o papel essencial da ONG Passos Mágicos no apoio ao desenvolvimento educacional e social dos jovens. 
    """,
    unsafe_allow_html=True,           
)

image_url = "https://raw.githubusercontent.com/FIAP-Tech-Challenge/datathon/c40fbe18f0cd270ded8c6cfa9c2d4ce1fdafe3f8/data/2.jpg"

st.image(image_url, caption=None, width=None, use_column_width=False, clamp=False, channels="RGB", output_format="auto")

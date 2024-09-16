import pandas as pd
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
st.title("DASHBOARD ONG PASSOS MÁGICOS ILUMINANDO VIDAS ✨")

st.divider()

st.markdown(
    """
    A **:blue[Passos Mágicos]**, é uma organização não governamental com três décadas de atuação, dedica-se a promover o desenvolvimento integral de crianças e adolescentes em situação de vulnerabilidade social. Com ênfase nas áreas de educação, cultura, esporte e lazer, a ONG oferece um amplo espectro de atividades que visam ao crescimento pessoal e social desses jovens. Além disso, a entidade proporciona suporte emocional e social, criando um ambiente favorável para um desenvolvimento saudável e seguro.

Os programas da organização são amplos e abrangentes, englobando oficinas culturais, iniciativas esportivas, eventos comunitários e ações de conscientização sobre direitos. A organização também disponibiliza assistência psicológica, jurídica e social, com o objetivo de promover a inclusão social e elevar a qualidade de vida dos beneficiários. Para saber mais sobre os projetos, parcerias e formas de colaborar, convidamos a visitar o site oficial ou as redes sociais da ONG.

Fundada por Michelle Flues e Dimetri Ivanoff em 1992, a **:blue[Passos Mágicos]** iniciou suas atividades em orfanatos. Em 2016, a organização ampliou seu alcance, implementando um programa abrangente que integra educação de qualidade, apoio psicológico, ampliação de horizontes e incentivo ao protagonismo juvenil.
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    Neste trabalho, desenvolvemos e aplicamos uma rede neural para explorar e implementar soluções para a ONG. Utilizamos redes de **:blue[Perceptron Multilayer (MLP)]**  para sugerir concessões de bolsas de estudo. Esse modelo mostrou-se eficaz para fornecer insights valiosos e suporte à tomada de decisões.<br/><br/>
    
    Visando a melhoria contínua, aconselhamos que sejam realizados maiores ajustes no modelo treinado e validado para garantir uma precisão e desempenho ainda maiores.
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """ 
    **:blue[Análise Exploratória de Dados:]** Nesta etapa inicial, coletamos e preparamos dados fornecidos pela ONG Passos Mágicos. Posteriormente realizamos uma análise exploratória para identificar padrões e tendências, utilizando ferramentas de visualização para entender a distribuição dos dados e detectar possíveis desvios.
    """,
    unsafe_allow_html=True,           
)

st.markdown(
    """ 
    **:blue[Rede Neural:]** A proposta do nosso modelo é identificar alunos que podem ser indicados para receber uma bolsa de estudos. Utilizamos dados históricos de 2022 e dados simulados para melhorar a base de treinamento. O usuário será responsável apenas por inserir as notas do aluno e o restante ficará a cargo do modelo.
    """,
    unsafe_allow_html=True,           
)


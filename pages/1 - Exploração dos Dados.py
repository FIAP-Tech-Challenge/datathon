import pandas as pd
import streamlit as st
import plotly.graph_objs as go
import plotly.express as px  

df_2020 = pd.read_csv('data/processado_base_2020.csv', sep=';')
df_2021 = pd.read_csv('data/processado_base_2021.csv', sep=';')
df_2022 = pd.read_csv('data/processado_base_2022.csv', sep=';')
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
st.title("EXPLORAÇÃO DOS DADOS 📊")

aba1, aba2 = st.tabs(['Instituições de ensino', 'Idade dos alunos'])

with aba1:
    st.markdown("A seguir serão apresentados dados referentes à instiuições de ensino dos alunos da **:blue[Passos Mágicos]** .")
    st.subheader('**:blue[Instituições de ensino dos estudantes]**')
    st.subheader(f":blue[2020]", divider="blue")

    def plot_bar(df, col, titulo, xaxis, yaxis='Quantidade'):
        grupos = df[col].value_counts()
        fig = go.Figure(
            go.Bar(
                x=grupos.index,
                y=grupos,
                text=grupos,
                textposition='auto'
            )
        )
        fig.update_layout(
            title=titulo,
            xaxis=dict(tickmode='linear'),
            xaxis_title=xaxis,
            yaxis_title=yaxis,
        )
        return fig

    fig1 = plot_bar(df_2020, "INSTITUICAO_ENSINO_ALUNO", "Instituições de ensino dos alunos em 2020", xaxis="Instituição de ensino")
    fig2 = plot_bar(df_2021, "INSTITUICAO_ENSINO_ALUNO", "Instituições de ensino dos alunos em 2021", xaxis="Instituição de ensino")

    st.plotly_chart(fig1, use_container_width=True)
    st.subheader(f":blue[2021]", divider="blue")
    st.plotly_chart(fig2, use_container_width=True)

    print(type(fig1))
    print(type(fig2))

    st.markdown("A partir desses gráficos foi possível concluir que a maioria dos estudantes atendidos pela ONG estudam em escolas públicas. Refletindo a importância da **:blue[Passos Mágicos]** na vida dessas pessoas, que na maioria dos casos, não possuem um ensino de qualidade. Parte dos alunos atendidos pela ONG ingressaram na **:blue[FIAP]** ou outras instituições de ensino superior, deixando claro o compromisso com uma educação de qualidade.")

with aba2:
    df_2020["IDADE_ALUNO"] = pd.to_numeric(df_2020["IDADE_ALUNO"], errors="coerce")

    st.subheader(f":blue[Distribuição das idades]", divider="blue")
    st.markdown("Nas próximas seções, analisaremos a distribuição das idades dos alunos, de forma a obtermos insights valiosos.")

    fig = plot_bar(df_2020, "IDADE_ALUNO", "Idade dos alunos", xaxis="Idade")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("A partir dessa visualização foi possível analisar que a maioria dos alunos atendidos pela **:blue[Passos Mágicos]** possuem idade entre **:blue[10]** e **:blue[14]** anos, com aproximadamente **:blue[60%]** do total dos estudantes, podemos assegurar que o maior impacto da ONG pode ser observado em crianças que estão da metade para o fim do Ensino Fundamental. Os alunos de (**:blue[15]** anos ou mais) que estão no Ensino Médio também são beneficiados pela ONG, mas em quantidade menor comparado à faixa de alunos mais jovens, em torno de **:blue[25%]** do total.")

    def plot_boxplot(df, col, titulo):
        fig = px.box(df, y=col, points="all", title=titulo)  
        fig.update_layout(yaxis_title='Valor')
        return fig

    fig = plot_boxplot(df_2020, "IDADE_ALUNO", "Boxplot das idades dos alunos")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("Esse boxplot representa de forma visual a distribuição de alunos em cada idade. A faixa com maior quantidade de alunos gira em torno dos 10 aos 14 anos. É fornecido nessa visualização a idade mínima de 7 anos de idade, a mediana da idade dos alunos que é de 12 anos, e a idade máxima de 20 anos. Sendo assim confirma-se insights levantados anteriormente na outra visualização")


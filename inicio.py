import pandas as pd
import streamlit as st

df = pd.DataFrame(
    [
        {"aluno": "José", "nota": 0, "bolsista": False},
        {"aluno": "Marcelo", "nota": 0, "bolsista": False},
        {"aluno": "Micheli", "nota": 0, "bolsista": True},
        {"aluno": "Rafael", "nota": 0, "bolsista": False},
    ]
)
st.markdown("### Avaliação de alunos 2024")
df_editado = st.data_editor(
    df,
    column_config={
        "aluno": "Aluno",
        "nota": st.column_config.NumberColumn(
            "Avaliação",
            help="Qual a nota para o quesito (1-10)?",
            min_value=1,
            max_value=10,
            step=1,
            format="%d ⭐",
        ),
        "bolsista": "Bolsista 2024?",
    },
    disabled=["aluno", "bolsista"],
    hide_index=True,
)

bolsistas = df_editado.loc[df_editado["nota"] >= 6,["aluno","nota","bolsista"]]
bolsistas["bolsista"] = True

st.markdown("### Resultado dos alunos 2025")
#st.markdown(bolsistas.to_markdown())
st.data_editor(bolsistas, column_config={
        "aluno": "Aluno",
        "nota": st.column_config.NumberColumn(
            "Avaliação",
            help="Qual a nota para o quesito (1-10)?",
            min_value=1,
            max_value=10,
            step=1,
            format="%d ⭐",
        ),
        "bolsista": "Bolsista 2025?",
    },
    disabled=["aluno", "bolsista"],
    hide_index=True,)
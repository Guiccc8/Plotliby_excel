import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output


app = Dash()

Tabela = pd.read_excel("Vendas.xlsx")   

opcoes = list(Tabela['ID Loja'].unique())
opcoes.append("Todas as lojas")

Figura = px.bar(Tabela, x='Produto', y='Quantidade', color='ID Loja', title="Vendas de roupas", barmode="group")

app.layout = html.Div(children=[
    
    dcc.Dropdown(opcoes, id='Lista_Lojas'),
        
    dcc.Graph(
        id="Figura_Roupas",
        figure=Figura
)
    ])


@app.callback(
    Output('Figura_Roupas', 'figure'),
    Input('Lista_Lojas', 'value')
)

def update_output(value):
    if value == "Todas as lojas":
         Figura = px.bar(Tabela, x='Produto', y='Quantidade', color='ID Loja', title="Vendas de roupas", barmode="group", )
    else:
        tabela_filtrada = Tabela.loc[Tabela['ID Loja']== value, ]
        Figura = px.bar(tabela_filtrada, x='Produto', y='Quantidade', color='ID Loja', title="Vendas de roupas", barmode="group", )

    return Figura

if __name__ == "__main__":
    app.run(debug=True)


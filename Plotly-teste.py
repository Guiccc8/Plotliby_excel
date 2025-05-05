#Resposável pelo site HTML
from dash import Dash, html, dcc

#Responsável pelos gráficos
import plotly.express as px

#Para ler dados (xlsx, csv)
import pandas as pd

#Inicializando o nosso aplicativo
app = Dash()

'''
Dataframe: é uma estrutura de dados bidimensional, semelhante a uma planilha ou tabela, 
usada para armazenar e manipular dados em programas como Python
'''

Tabela = pd.DataFrame(
    #Criando uma tabela com dicionário:
      
    {
    "Frutas": ["Maçãs", "Laranjas", "Bananas", "Maçãs", "Laranjas", "Bananas"],
    "Quantidade": [4, 1, 2, 2, 4, 5],
    "Cidade": ["São Paulo", "São Paulo", "São Paulo", "Cotia", "Cotia", "Cotia"]
    }
    
    )

'''Dicionário: Em Python, um dicionário é uma estrutura de dados que 
armazena pares de valores (chave-valor). Cada chave é única e associada a um valor específico.'''



#Exemplo de Dicionário
'''Usuario = { 
    "Nome": "Guilherme Rodrigues da Silva",
    "Email": "guilherme@gmail.com",
    "CPF": "476.509.578-96",
    "RG": "57641829-8"
}

print(Guilherme["Nome"])'''


print(Tabela)

Figura = px.bar(
    Tabela, #A tabela que será analisada
    x="Quantidade", #X da tabela: Quantidade de frutas
    y="Frutas", #Y da tabela: Tipo de frutas
    color="Cidade", #Classificação de acordo com a cidade 
    title="Frutas em cada cidade", #Título da tabela
    barmode="group" #Forma de organização
                )

#Construindo o estilo do site
app.layout = html.Div(
    #div: Divisão como uma caixa
    
    #children: elementos dentro da div
    children=[
        
    #h1: Letra maior 
    html.H1(children='Hello Dash'),
    
    #style: Estiliza a div e os elementos
    html.Div(style={'color': "green"}, children='''
        Um exemplo de site com gráfico:
    '''),
    
    
    #dashboard: um painel de controlo visual e interativo que apresenta informações, indicadores e métricas
    
    #dcc: dashboard; comando responsável para a criação de nosso gráfico   
    dcc.Graph(
        #Identificador
        id='grafico-frutas',
        #
        figure=Figura
    )
])



if __name__ == '__main__':
#Inicia o apicativo
    app.run(debug=True)
    
# debug: processo de encontrar e corrigir erros (bugs) num programa ou aplicação

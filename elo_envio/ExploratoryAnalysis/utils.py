import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def boxplot(df, title, y):
    plt.figure(figsize=(20, 6))
    plt.boxplot(df)
    plt.title(title)
    plt.ylabel(y)

    plt.show()

def histogram(df):
    num_colunas = 4
    dfColumn = len(df.columns)
    num_linhas = (dfColumn // num_colunas) + (dfColumn % num_colunas > 0)

    if (dfColumn <= 4):
        fig, axs = plt.subplots(num_linhas, num_colunas, figsize=(20, 4))
    else:
         fig, axs = plt.subplots(num_linhas, num_colunas, figsize=(20, 15))

    if len(df.columns) > 1:
        axs = axs.flatten()
    else:
        axs = [axs]

    for i, col in enumerate(df.columns):
        axs[i].hist(df[col], bins=10, color='skyblue', edgecolor='black')
        axs[i].set_title(f'Histograma de {col}')
        axs[i].set_xlabel('População')
        axs[i].set_ylabel('Frequência')
        axs[i].grid(True)

    plt.tight_layout()
    plt.show()

def distribuicaoSingle (df, title):
    plt.figure(figsize=(10, 6))
    sns.histplot(df)
    plt.title(title)
    plt.xlabel(df.name)
    plt.ylabel('Frequência')
    plt.show()

def distribuicaoSingle2 (df, column, title):
    plt.figure(figsize=(10, 6))
    sns.countplot(x=column, data=df)
    plt.title(title)
    plt.xlabel(df.name)
    plt.ylabel('Frequência')
    plt.show()

def pizza(df, category, values):
    
    category_revenue = df.groupby(category)[values].sum()
        
    plt.figure(figsize=(10, 8))
    plt.pie(category_revenue, labels=category_revenue.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição de Receita por ' + category)
    plt.axis('equal')
    plt.show()

def dezMaiores(df, colunas):
    analysis_dfs = []  

    for column in colunas[1:]:
        total_population = df[column].sum()
        # Ordene os valores em ordem decrescente
        df_sorted = df.sort_values(by=column, ascending=False)
        
        # Pegue os 10 maiores e agrupe o restante como 'Outros'
        top_10 = df_sorted.head(10)
        others_population = total_population - top_10[column].sum()
        others_row = pd.DataFrame([[f'Outros({column})', others_population]], columns=[colunas[0], column])
        
        # Concatene os 10 maiores e 'Outros'
        result = pd.concat([top_10, others_row])
        
        # Adicione uma coluna com o percentual da base que a coluna representa
        result['Percentage'] = (result[column] / total_population) * 100
        
        # Adicione o DataFrame resultante à lista
        analysis_dfs.append(result)

    # Imprima as tabelas lado a lado
    for i in range(len(analysis_dfs)):
        print(analysis_dfs[i])
        if i < len(analysis_dfs) - 1:
            print("\n\n\n")  



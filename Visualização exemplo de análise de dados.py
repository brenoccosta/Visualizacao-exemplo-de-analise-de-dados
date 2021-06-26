#!/usr/bin/env python
# coding: utf-8

# # Visualização: exemplo de análise de dados

# ## Limpeza e processamento dos dados

import pandas as pd


# ###### Importação do dataset teste de 15.120 amostras

treino = pd.read_csv(filepath_or_buffer='C:/.../train.csv')


# ###### Adição da categoria "Área"

treinoarea = treino
treinoarea = treinoarea.assign(Area=0)

for i in range(1, 5):
    treinoarea['Area'].loc[treinoarea[f'Wilderness_Area{i}'] == 1] = i

    
# ###### Adição da categoria "Solo"

treinosolo = treinoarea
treinosolo = treinosolo.assign(Solo=0)

for i in range(1, 41):
    treinosolo['Solo'].loc[treinosolo[f'Soil_Type{i}'] == 1] = i


# ###### Remoção das colunas excessivas

treinofinal = treinosolo
treinofinal = treinofinal.drop(columns=treinofinal.columns[11:55])
treinofinal = treinofinal.drop(columns=treinofinal.columns[2])
treinofinal = treinofinal.drop(columns=treinofinal.columns[0])


# ###### Normalização dos dados

tabelanormal = treinofinal

colunas = []
for coluna in tabelanormal.columns:
    colunas.append(coluna)

colunas.pop()
colunas.pop()
colunas.pop()

for coluna in colunas:
    tabelanormal[coluna] = (tabelanormal[coluna] - tabelanormal[coluna].min()) / (tabelanormal[coluna].max() - tabelanormal[coluna].min())


# ## Tabelas

# ### Dispersão das árvores por área

# Informações que comporão "dados":
# 
# print('1 - Rawah Wilderness Area', treino['Wilderness_Area1'].value_counts()[1])
# print(treino.query('Wilderness_Area1 == 1')['Cover_Type'].value_counts())
# print(treino.query('Wilderness_Area1 == 1')['Cover_Type'].value_counts() * 100 / treino['Wilderness_Area1'].value_counts()[1],
#       end = '\n\n')
# 
# print('2 - Neota Wilderness Area',treino['Wilderness_Area2'].value_counts()[1])
# print(treino.query('Wilderness_Area2 == 1')['Cover_Type'].value_counts())
# print(treino.query('Wilderness_Area2 == 1')['Cover_Type'].value_counts() * 100 / treino['Wilderness_Area2'].value_counts()[1],
#       end = '\n\n')
# 
# print('3 - Comanche Peak Wilderness Area',treino['Wilderness_Area3'].value_counts()[1])
# print(treino.query('Wilderness_Area3 == 1')['Cover_Type'].value_counts())
# print(treino.query('Wilderness_Area3 == 1')['Cover_Type'].value_counts() * 100 / treino['Wilderness_Area3'].value_counts()[1],
#       end = '\n\n')
# 
# print('4 - Cache la Poudre Wilderness Area',treino['Wilderness_Area4'].value_counts()[1])
# print(treino.query('Wilderness_Area4 == 1')['Cover_Type'].value_counts())
# print(treino.query('Wilderness_Area4 == 1')['Cover_Type'].value_counts() * 100 / treino['Wilderness_Area4'].value_counts()[1],
#       end = '\n\n')


dados = ([23.79, 3597, None, 3.3, 499, None, 41.99, 6349, None, 30.92, 4675, None, 15120],
         [49.17, 1062, 29.52, 8.38, 181, 36.27, 42.45, 917, 14.44, None, None, None, 2160],
         [52.5, 1134, 31.53, 3.06, 66, 13.27, 43.52, 940, 14.81, 0.93, 20, 0.43, 2160],
         [None, None, None, None, None, None, 39.95, 863, 13.59, 60.05, 1297, 27.74, 2160],
         [None, None, None, None, None, None, None, None, None, 100, 2160, 46.20, 2160],
         [39.63, 856, 23.78, None, None, None, 60.37, 1304, 20.54, None, None, None, 2160],
         [None, None, None, None, None, None, 44.54, 962, 15.15, 55.46, 1198, 25.63, 2160],
         [25.23, 545, 15.15, 11.67, 252, 50.50, 63.10, 1363, 21.47, None, None, None, 2160])

indice = ('Total', '1 - Spruce/Fir', '2 - Lodgepole Pine','3 - Ponderosa Pine','4 - Cottonwood/Willow', '5 - Aspen',
          '6 - Douglas-fir', '7 - Krummholz')
colunas = ('1 - Espécie %%', '1 - Rawah Wilderness Area', '1 - Área %%',
           '2 - Espécie %%', '2 - Neota Wilderness Area', '2 - Área %%',
           '3 - Espécie %%', '3 - Comanche Peak Wilderness Area', '3 - Área %%',
           '4 - Espécie %%', '4 - Cache la Poudre Wilderness Area', '4 - Área %%',
           'Total')
especiesareas = pd.DataFrame(dados, indice, colunas)
especiesareas = especiesareas.convert_dtypes()

especiesareas


# ### Dispersão do solo por área e espécie

dados = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])

# total
treinoarea.iloc[:, 15:55].sum()
for i in range(40):
    dados[i].append(treinoarea.iloc[:, 15 + i].sum())

# Área 1    
for i in range(40):
    dados[i].append(treinoarea.query('Area == 1').iloc[:, 15 + i].sum())
    
# Área 2    
for i in range(40):
    dados[i].append(treinoarea.query('Area == 2').iloc[:, 15 + i].sum())

# Área 3    
for i in range(40):
    dados[i].append(treinoarea.query('Area == 3').iloc[:, 15 + i].sum())
    
# Área 4    
for i in range(40):
    dados[i].append(treinoarea.query('Area == 4').iloc[:, 15 + i].sum())
    
# Espécie 1    
for i in range(40):
    dados[i].append(treinoarea.query('Cover_Type == 1').iloc[:, 15 + i].sum())
     
# Espécie 2    
for i in range(40):
    dados[i].append(treinoarea.query('Cover_Type == 2').iloc[:, 15 + i].sum())
     
# Espécie 3    
for i in range(40):
    dados[i].append(treinoarea.query('Cover_Type == 3').iloc[:, 15 + i].sum())
     
# Espécie 4    
for i in range(40):
    dados[i].append(treinoarea.query('Cover_Type == 4').iloc[:, 15 + i].sum())
     
# Espécie 5    
for i in range(40):
    dados[i].append(treinoarea.query('Cover_Type == 5').iloc[:, 15 + i].sum())
     
# Espécie 6    
for i in range(40):
    dados[i].append(treinoarea.query('Cover_Type == 6').iloc[:, 15 + i].sum())
     
# Espécie 7    
for i in range(40):
    dados[i].append(treinoarea.query('Cover_Type == 7').iloc[:, 15 + i].sum())

# Índice
indice = []
for solo in treinoarea.columns[15:55]:
    indice.append(solo)

# Colunas
colunas = [['', 'Áreas', 'Áreas', 'Áreas', 'Áreas', 'Espécies', 'Espécies', 'Espécies', 'Espécies', 'Espécies', 'Espécies',
            'Espécies'], 
           ['Total', '1 - Rawah Wilderness Area', '2 - Neota Wilderness Area', '3 - Comanche Peak Wilderness Area', 
           '4 - Cache la Poudre Wilderness Area', '1 - Spruce/Fir', '2 - Lodgepole Pine', '3 - Ponderosa Pine',
           '4 - Cottonwood/Willow', '5 - Aspen',  '6 - Douglas-fir', '7 - Krummholz']]

multiindice = pd.MultiIndex.from_arrays(colunas)

solos = pd.DataFrame(dados, indice, multiindice)
solos = solos.convert_dtypes()

solos


# ## Gráficos

import matplotlib.pyplot as plt
import seaborn as sns


# ### Dispersão da água

titulos = ['1 - Rawah Wilderness Area', '2 - Neota Wilderness Area', '3 - Comanche Peak Wilderness Area',
           '4 - Cache la Poudre Wilderness Area']

c = ['#0504aa', '#029386', '#677a04', '#bf77f6', '#d1b26f', 'brown', '#c20078']
c = [['#0504aa', '#029386', '#d1b26f', '#c20078'], ['#0504aa', '#029386', '#c20078'],
     ['#0504aa', '#029386', '#677a04', '#d1b26f', 'brown', '#c20078'], ['#029386', '#677a04', '#bf77f6', 'brown']]

fig, ax = plt.subplots(2, 2, figsize=(12, 12), sharex=True, sharey=True)

plt.rcParams.update({'font.size':14})
plt.subplots_adjust(wspace = 0.3, hspace = 0.15)
plt.suptitle('Áreas geográficas - proximidade com a água', fontsize=20)

b = 0
for i in range(2):
    for k in range(2):
        b += 1
        sns.scatterplot(ax=ax[i, k], data=treino[treino[f'Wilderness_Area{b}'] != 0], x='Horizontal_Distance_To_Hydrology',
                        y='Vertical_Distance_To_Hydrology', hue='Cover_Type', palette=c[b - 1], legend=True)
        ax[i, k].set_title(titulos[b - 1])
        ax[i, k].spines['left'].set_position('zero')
        ax[i, k].spines['right'].set_color('none')
        ax[i, k].spines['bottom'].set_position('zero')
        ax[i, k].spines['top'].set_color('none')
        ax[i, k].tick_params(axis='x', pad=70)
        ax[i, k].tick_params(axis='y', pad=10)
        ax[i, k].set_xlim(0, 1400)
        ax[i, k].set_ylim(-150, 450)
        ax[i, k].grid(ls='--', lw=0.5)
        ax[i, k].set_xlabel(xlabel='Distância horizontal', labelpad=20, fontsize=14)
        ax[i, k].set_ylabel(ylabel='Distância vertical', labelpad=10, fontsize=14)
        ax[i, k].legend(loc=(1.05, 0.4), title='Tipos')

plt.show()


# ### Inclinação

# #### Por área

plt.figure(figsize=(6, 5))

c = ['blue', 'green', 'red', 'black']
for b in range(1, 5):
    sns.kdeplot(data=treino[treino[f'Wilderness_Area{b}'] != 0], x='Slope', lw=3, color=c[b - 1])

plt.title('Inclinação por área', fontsize=20)
plt.ylabel('Frequência')
plt.xlabel('Inclinação')
plt.legend(['Um', 'Dois', 'Três', 'Quatro'], title='Áreas')

plt.show()


# #### Por espécie

fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

plt.subplots_adjust(wspace = 0.1)
plt.suptitle('Inclinação por espécie', fontsize=20)

c = ['#0504aa', '#029386', '#677a04', '#bf77f6', '#d1b26f', 'brown', '#c20078']

# figura 1
sns.kdeplot(ax=axes[0], data=treino[treino['Cover_Type'] == 1], x='Slope', lw=3, c=c[0])
sns.kdeplot(ax=axes[0], data=treino[treino['Cover_Type'] == 2], x='Slope', lw=3, c=c[1])
sns.kdeplot(ax=axes[0], data=treino[treino['Cover_Type'] == 7], x='Slope', lw=3, c=c[6])

axes[0].set_xlim(-10, 60)
axes[0].grid(lw=0.3)
axes[0].set_ylabel('Frequência', labelpad=20)
axes[0].set_xlabel('Inclinação')
axes[0].legend(['Um', 'Dois', 'Sete'], title='Espécie')

# figura 2
for b in range(3, 7):  # [3, ..., 6]
    sns.kdeplot(ax=axes[1], data=treino[treino['Cover_Type'] == b], x='Slope', lw=3, c=c[b - 1])

axes[1].set_xlim(-10, 60)
axes[1].grid(lw=0.3)
axes[1].set_xlabel('Inclinação')
axes[1].legend(['Três', 'Quatro', 'Cinco', 'Seis'], title='Espécie')

plt.show()


# ### Sombra

# #### Por área

titulos = ['1 - Rawah Wilderness Area', '2 - Neota Wilderness Area', '3 - Comanche Peak Wilderness Area',
           '4 - Cache la Poudre Wilderness Area']

fig, axes = plt.subplots(2, 2, figsize=(12, 9), sharex=True, sharey=True)

plt.rcParams.update({'font.size':14})
plt.subplots_adjust(wspace = 0.2, hspace = 0.25)
plt.suptitle('Sombra por área', fontsize=20)

b = 0
for i in range(2):
    for k in range(2):
        b += 1

        sns.kdeplot(ax=axes[i, k], data=treinoarea.query(f'Area == {b}'), x='Hillshade_9am', lw=3, color='#bf9005')  # 'xkcd:ochre'
        sns.kdeplot(ax=axes[i, k], data=treinoarea.query(f'Area == {b}'), x='Hillshade_Noon', lw=3, color='#047495')  # 'xkcd:sea blue'
        sns.kdeplot(ax=axes[i, k], data=treinoarea.query(f'Area == {b}'), x='Hillshade_3pm', lw=3, color='#658b38')  # 'xkcd:moss green'

        axes[i, k].grid(lw=0.3)
        axes[i, k].set_title(titulos[b - 1])
        axes[i, k].set_xlabel(xlabel='Sombra', labelpad=20, fontsize=18)
        axes[i, k].set_ylabel(ylabel='Frequência', labelpad=20, fontsize=18)
        axes[i, k].set_xlim(-50, 300)
        axes[i, k].set_ylim(0, 0.035)
        axes[i, k].set_xticks((0, 100, 200))
        axes[i, k].set_yticks((0.010, 0.020, 0.030))

axes[0, 1].legend(['09h', '12h', '15h'], title='Sombra', loc=[1.05, 0.30])
axes[1, 1].legend(['09h', '12h', '15h'], title='Sombra', loc=[1.05, 0.30])

plt.show()


# #### Por espécie

titulos = ['Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', '']

fig, axes = plt.subplots(2, 4, figsize=(22, 12), sharex=True, sharey=True)  # 

plt.rcParams.update({'font.size':18})
plt.subplots_adjust(wspace = 0.1, hspace = 0.15)
plt.suptitle('Sombra por espécie', fontsize=24)

b = 0
for i in range(2):
    for k in range(4):
        b += 1

        if b == 8: break
        
        sns.kdeplot(ax=axes[i, k], data=treino.query(f'Cover_Type == {b}'), x='Hillshade_9am', lw=3,
                    color='#bf9005')  # 'xkcd:ochre'
        sns.kdeplot(ax=axes[i, k], data=treino.query(f'Cover_Type == {b}'), x='Hillshade_Noon', lw=3,
                    color='#047495')  # 'xkcd:sea blue'
        sns.kdeplot(ax=axes[i, k], data=treino.query(f'Cover_Type == {b}'), x='Hillshade_3pm', lw=3,
                    color='#658b38')  # 'xkcd:moss green'
        
        axes[i, k].grid(lw=0.3)
        axes[i, k].set_title(titulos[b - 1])
        axes[i, k].set_xlabel(xlabel='Sombra', labelpad=20, fontsize=18)
        axes[i, k].set_ylabel(ylabel='Frequência', labelpad=20, fontsize=18)
        axes[i, k].set_xlim(-50, 300)
        axes[i, k].set_ylim(0, 0.035)
        axes[i, k].set_xticks((0, 100, 200))
        axes[i, k].set_yticks((0.010, 0.020, 0.030))

axes[1, 2].legend(['09h', '12h', '15h'], title='Sombra', loc=0, frameon=True)

plt.show()


# ### Elevação

titulos = ['Áreas', 'Espécies']

ca = ['blue', 'green', 'red', 'black']
ce = ['#0504aa', '#029386', '#677a04', '#bf77f6', '#d1b26f', 'brown', '#c20078']

fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True, sharex=True)

plt.subplots_adjust(wspace = 0.1)
plt.suptitle('Elevação por área e espécie', fontsize=24) 

sns.kdeplot(ax=axes[0], data=treinoarea, x=treinoarea.Elevation, hue=treinoarea.Area, lw=3, palette=ca)
axes[0].grid(axis='x')
axes[0].set_xlabel(xlabel='Elevação', labelpad=20, fontsize=18)
axes[0].set_ylabel(ylabel='Frequência', labelpad=20, fontsize=18)
axes[0].set_title(titulos[0])
axes[0].legend(['Quatro', 'Três', 'Dois', 'Um'], title='Áreas', loc=0)

sns.kdeplot(ax=axes[1], data=treino, x=treino.Elevation, hue=treino.Cover_Type, palette=ce, lw=3)
axes[1].grid(axis='x')
axes[1].set_xlabel(xlabel='Elevação', labelpad=20, fontsize=18)
axes[1].set_title(titulos[1])
axes[1].legend(['Sete', 'Seis', 'Cinco', 'Quatro', 'Três', 'Dois', 'Um'], title='Espécie', loc=[1.05, 0.15])

plt.show()


# ### Dispersão dos solos

fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

plt.suptitle('Dispersão dos solos', fontsize=24) 

# figura 1
sns.histplot(ax=axes[0], x=treinosolo.Area, y=treinosolo.Solo)
axes[0].set_xticks([1, 2, 3, 4])
axes[0].set_xlabel('Área')

# figura 2
sns.histplot(ax=axes[1], x=treinosolo.Cover_Type, y= treinosolo.Solo, color= "green")
axes[1].set_xlabel('Espécie')

plt.savefig('C:/Users/Admin/Desktop/Minhas coisas/PUCC/Primeiro Semestre/Mineração de Dados e Visualização/Projeto 3/Dispersão dos solos',
            facecolor='white', bbox_inches='tight')

plt.show()

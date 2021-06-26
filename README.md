# Visualização: exemplo de análise de dados

Este repositório tem o mesmo *dataset* [Forest Cover Type Prediction | Kaggle](https://www.kaggle.com/c/forest-cover-type-prediction) que o repositório [Algoritmo K-NN e estruturação de dados](https://github.com/brenoccosta/Algoritmo-K-NN-e-estruturacao-de-dados) como objeto, porém diferindo na abordagem: enquanto aquele foca na aplicação de uma inteligência artificial e no tratamento dos dados, este focará na análise dos atributos presentes no banco de dados. De qualquer maneira, recomenda-se a breve leitura do outro ou de sua introdução.

O *dataset* apresenta três categorias: espécie, área e solo; e uma série de outros atributos, tais como distância da fonte de água mais próxima, altitude, inclinação, sombra. Esses serão os atributos discutidos aqui.

Para fins didáticos, todas as *espécies* serão mencionadas por **numerais cardinais**, enquanto todas as *áreas/regiões*, por **numerais ordinais**. Igualmente, dentre os valores fornecidos textualmente e aqueles dispostos por tabelas ou gráficos, considerar os últimos.

## Distribuição das espécies

Cada espécie conta com 2.160 exemplares, distribuídas irregularmente dentre as quatro áreas florestais. Montou-se a **Tabela 1** como uma primeira abordagem para a compreensão das informações contidas no *dataset* e, apesar da simplicidade, algumas características marcantes podem ser notadas, que posteriormente guiarão nosso olhar:

-  **Cache la Poudre** (quarta área) :
	 - Concentra todas as amostras de **salgueiros** (espécie quatro) e três quintos das amostras de ***Pinii ponderosa*** (três) e de ***Psudotsuga menziesli*** (seis);
	 - É a segunda área mais arborizada – um terço.
 - **Pico Comanche** (terceira área):
	 - Alberga o restante das amostras das **espécies três e seis**  – dois quintos  –, bem como corresponde à mesma proporção de **abetos** (um), de ***Pinii contorta*** (dois) e da floresta, sendo a maior região;
	 - *Três quintos* dos **álamos** (cinco) e dos **krummholz** (sete) estão contidos nessa área.
- **Neota**:
	- Menor área – 03,30% do total;
	- Um terço corresponde a **abetos** (um) e metade, a **krummholz** (sete).
- **Rawah**:
	- Zona de arborização intermediária – um quinto do todo;
	- Metade dos **abetos** (um) e dos ***Pinii contorta*** (dois) estão presentes, bem como dois quintos dos **álamos** (cinco) e um quarto dos **krummholz** (sete).

###### Tabela 1
![Tabela de distribuição das espécies por área](https://github.com/brenoccosta/Visualizacao-exemplo-de-analise-de-dados/blob/a716d46fc2469bcc8128e7fb95297daa6a958b4d/Gr%C3%A1ficos/Esp%C3%A9cies%20por%20%C3%A1reas.png?raw=True)

> **Explicando a tabela** (optou-se pela versão compacta pela visualização, ao invés da maior mais intuitiva): a) *colunas*: o número indica a área; "Espécie" indica a porcentagem correspondente daquela espécie; "Área" indica a porcentagem correspondente da vegetação presente naquela área; o nome – coluna intermediária – indica o número absoluto de espécimes presentes; b) *linhas*: "Total" indica i) a porcentagem de amostras presentes em dada área, e ii) número absoluto das amostras.

Conforme o [algoritmo K-NN aplicado à matriz sem qualquer alteração](https://github.com/brenoccosta/Algoritmo-K-NN-e-estruturacao-de-dados#aplica%C3%A7%C3%A3o-imediata-do-k-nn), as espécies sete, quatro e cinco, em ordem decrescente, foram as melhor classificadas, além de um alto número de atribuições errôneas às classes mencionadas. Isso sugere características notórias de cada uma das três. Pela tabela, salta aos olhos a particularidade do **salgueiro** (quatro), presente em uma única área. Já distribuição paritária das **espécies sete e cinco** pela floresta e sua *não-confusão* indica ocuparem nichos distintos das mesmas regiões e, portanto, diferenças notáveis dentro das mesmas. Por sua vez, a alta taxa de confusão recíproca entre os **abetos** (um) e os ***Pinii contorta*** (dois), aliada também à sua distribuição paritária, denota a competição pelos mesmos espaços, contrariamente ao par anterior.

A investigação será orientada a partir de tais observações, extremamente proveitosas por se tratar de um *dataset* de 15.120 entradas, de três categorias e outros nove atributos (sobre a transformação do banco de dados, acesse [aqui](https://github.com/brenoccosta/Algoritmo-K-NN-e-estruturacao-de-dados#limpeza-e-processamento-dos-dados)).

## Distribuição dos tipos de solo

Conforme vimos na **Tabela 1**, todos os espécimes da espécie quatro e três quintos das espécies três e seis estão na quarta área. Entretanto, enquanto o *Psudotsuga menziesli* (seis) vinga em uma amplitude razoável de solos (**Figura 1**), praticamente todas as demais amostras do *Pinus ponderosa* (três) permanecem no mesmo tipo de solo, indicando uma especificidade da espécie.

O krummholz (sete) se mostra o antagônico da espécie quatro, ocupando o limite superior dos tipos de solo, tornando-o também específico. Por sua vez, o álamo (cinco) aparenta ser uma espécie intermediária, com boa ocupação de diversos terrenos, perdendo, não obstante, para o abeto (um) e para o *Pinus contorta* (dois), que reforçam a ideia de competitividade entre ambas espécies pela incrível similaridade da ocupação do solo, os mais tolerantes.

###### Figura 1
![Dispersão dos solos por área e por espécie](https://github.com/brenoccosta/Visualizacao-exemplo-de-analise-de-dados/blob/878b28aa8d86859f217e74b7618913336cb0ed8a/Gr%C3%A1ficos/Dispers%C3%A3o%20dos%20solos.png?raw=True)

### Relevo

Algumas informações concernentes ao relevo já podem ser extraídas desse gráfico.

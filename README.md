# Visualização: exemplo de análise de dados

Este repositório tem o mesmo *dataset* [Forest Cover Type Prediction | Kaggle](https://www.kaggle.com/c/forest-cover-type-prediction) que o repositório [Algoritmo K-NN e estruturação de dados](https://github.com/brenoccosta/Algoritmo-K-NN-e-estruturacao-de-dados) como objeto, porém diferindo na abordagem: enquanto aquele foca na aplicação de uma inteligência artificial e no tratamento dos dados, este focará na análise dos atributos presentes no banco de dados. De qualquer maneira, recomenda-se a breve leitura do outro ou de sua introdução.

O *dataset* apresenta três categorias: espécie, área e solo; e uma série de outros atributos, tais como distância da fonte de água mais próxima, altitude, inclinação, sombra. Esses serão os atributos discutidos aqui.

Para fins didáticos, todas as *espécies* serão mencionadas por **numerais cardinais**, enquanto todas as *áreas/regiões*, por **numerais ordinais**. Igualmente, dentre os valores fornecidos textualmente e aqueles dispostos por tabelas ou gráficos, considerar os últimos.

## Distribuição das espécies

Cada espécie conta com 2.160 exemplares, distribuídas irregularmente dentre as quatro áreas florestais. Montou-se a **Tabela 1** como uma primeira abordagem para a compreensão das informações contidas no *dataset* e, apesar da simplicidade, algumas características marcantes podem ser notadas, que posteriormente guiarão nosso olhar:

-  **Cache la Poudre** (quarta área) :
	 - Concentra todas as amostras de **salgueiros** (espécie quatro) e três quintos das amostras de ***Pinii ponderosa*** (três) e de ***Psudotsuga menziesli*** (seis);
	 - É a segunda área mais arborizada – um terço.
 - **Pico Comanche** (terceira):
	 - Alberga o restante das amostras das **espécies três e seis**  – dois quintos  –, bem como corresponde à mesma proporção de **abetos** (um), de ***Pinii contorta*** (dois) e da floresta, sendo a maior região;
	 - *Três quintos* dos **álamos** (cinco) e dos **krummholz** (sete) estão contidos nessa área.
- **Neota** (segunda):
	- Menor área – 03,30% do total;
	- Um terço corresponde a **abetos** (um) e metade, a **krummholz** (sete).
- **Rawah** (primeira):
	- Zona de arborização intermediária – um quinto do todo;
	- Metade dos **abetos** (um) e dos ***Pinii contorta*** (dois) estão presentes, bem como dois quintos dos **álamos** (cinco) e um quarto dos **krummholz** (sete).

###### Tabela 1
![Tabela de distribuição das espécies por área](https://github.com/brenoccosta/Visualizacao-exemplo-de-analise-de-dados/blob/a716d46fc2469bcc8128e7fb95297daa6a958b4d/Gr%C3%A1ficos/Esp%C3%A9cies%20por%20%C3%A1reas.png?raw=True)

> **Explicando a tabela** (optou-se pela versão compacta pela visualização, ao invés da maior mais intuitiva): a) *colunas*: o número indica a área; "Espécie" indica a porcentagem correspondente daquela espécie; "Área" indica a porcentagem correspondente da vegetação presente naquela área; o nome – coluna intermediária – indica o número absoluto de espécimes presentes; b) *linhas*: "Total" indica i) a porcentagem de amostras presentes em dada área, e ii) número absoluto das amostras.

Conforme o [algoritmo K-NN aplicado à matriz sem qualquer alteração](https://github.com/brenoccosta/Algoritmo-K-NN-e-estruturacao-de-dados#aplica%C3%A7%C3%A3o-imediata-do-k-nn), as espécies sete, quatro e cinco, em ordem decrescente, foram as melhor classificadas, além de um alto número de atribuições errôneas às classes mencionadas. Isso sugere características notórias de cada uma das três. Pela tabela, salta aos olhos a particularidade do **salgueiro** (quatro), presente em uma única área. Já distribuição paritária das **espécies sete e cinco** pela floresta e sua *não-confusão* indica ocuparem nichos distintos das mesmas regiões e, portanto, diferenças notáveis dentro das mesmas. Por sua vez, a alta taxa de confusão recíproca entre os **abetos** (um) e os ***Pinii contorta*** (dois), aliada também à sua distribuição paritária, denota a competição pelos mesmos espaços, contrariamente ao par anterior.

A investigação será orientada a partir de tais observações, extremamente proveitosas por se tratar de um *dataset* de 15.120 entradas, de três categorias e outros nove atributos (sobre a transformação do banco de dados, acesse [aqui](https://github.com/brenoccosta/Algoritmo-K-NN-e-estruturacao-de-dados#limpeza-e-processamento-dos-dados)).

## Distribuição dos tipos de solo

Conforme vimos na **Tabela 1**, todos os espécimes da **espécie quatro** e três quintos das **espécies três e seis** estão na quarta área. Entretanto, enquanto o *Psudotsuga menziesli* (seis) vinga em uma amplitude razoável de solos (**Figura 1**), praticamente todas as demais amostras do *Pinus ponderosa* (três) permanecem no mesmo tipo de solo, indicando uma especificidade da espécie.

O **krummholz** (sete) se mostra o antagônico da espécie quatro, ocupando o limite superior dos tipos de solo, tornando-o também específico. Por sua vez, o **álamo** (cinco) aparenta ser uma espécie intermediária, com boa ocupação de diversos terrenos, perdendo, não obstante, para o **abeto** (um) e para o ***Pinus contorta*** (dois), que reforçam a ideia de competitividade entre ambas espécies pela incrível similaridade da ocupação do solo, os mais tolerantes.

###### Figura 1
![Dispersão dos solos por área e por espécie](https://github.com/brenoccosta/Visualizacao-exemplo-de-analise-de-dados/blob/878b28aa8d86859f217e74b7618913336cb0ed8a/Gr%C3%A1ficos/Dispers%C3%A3o%20dos%20solos.png?raw=True)

### Relevo

Algumas informações concernentes ao relevo já podem ser extraídas desse gráfico. Tendo em vista que quão maior o número do tipo de solo, mais pedregoso e rochoso é, infere-se que a quarta região deva ser a mais baixa e, por conseguinte, com maior acúmulo de águas; que a terceira, pela sua variedade, deva ser a de maior amplitude; que a segunda, a mais alta e árida; e que a primeira, intermediária entre as duas últimas.

A quantidade de solo (idêntica à quantidade de amostras da **Tabela 1**, pois cada entrada possui um único solo) pode ser interpretada como um parâmetro que reflete a extensão de cada região, mas isso pode ser ilusório. A região **Neota** (segunda) corresponde a 03,30% da vegetação da Floresta, sendo a mais inóspita pela altitude e pelo solo rochoso. Isso não quer dizer que corresponde a 03,30% de todo o espaço ocupado pela floresta, uma vez que, naturalmente, em regiões de maior altitude e de solos menos férteis, menos árvores crescem.

## Elevação

Abaixo pode ser visto a altitude por região e por espécie, confirmando o que a distribuição do solo sugerira (**Figura 2**). A área do gráfico da seção *Áreas* corresponde à maior ou menor presença de amostras coletadas, conforme a **Tabela 1**, enquanto todas as áreas de *Espécies* são a mesma, por uma mesma quantidade de entradas relativas a cada espécie ter sido fornecida no *dataset*.

Das regiões, destaca-se a baixa altitude da **quarta área**, bem como o a repentina elevação da **terceira** entre 2.750 e 3.250 metros de altitude, com uma pequena faixa próximo a 3.000 metros. Isso implica um terreno extremamente íngreme, desfavorecendo as fixação de vegetação e ocupando pouco espaço, quando comparado à extensão das outras faixas de terra da floresta. Ainda da terceira área, nota-se que alcança o patamar dos 4.000 metros, provavelmente denotando o *pico* do **Pico Comanche**.

Das espécies, há dois grupos muito distintos: o das espécies *endêmicas* e o das *epidêmicas*. Compõem as endêmicas as **espécies quatro, cinco e sete**, notadamente as melhor classificadas pelo algoritmo K-NN. Os **salgueiros** (quatro) predominam nas regiões mais baixas de **Cache la Poudre** (quarta); os **álamos** (cinco), na região intermediária do **Pico Comanche** (terceira) e nas regiões baixas de **Rawah** (primeira); e o **krummholz** (sete), nas regiões mais elevadas de **todas** as áreas, salvo a quarta; essa distribuição pode ser verificada na **Tabela 1**.

Quanto às espécies epidêmicas, as **espécies três e seis** ocupam as terras mais baixas, e as **um e dois**, as mais altas. Os ***Pinii ponderosa*** (três) e os ***Psudotsuga menziesli*** (seis) formam a transição de **Cache la Poudre** (quarta) para o **Pico Comanche** (terceira), ocupando as regiões mais altas e baixas dessas áreas, respectivamente. Já os **abetos** (um) e os ***Pinii contorta*** (dois) são mais característicos de uma altitude pouco favorecida pela geografia do **Pico Comanche** (terceira), por isso sendo mais preponderantes em **Rawah** (primeira); tais observações também são constatadas na **Tabela 1**, embora ela por si só não forneça as informações concernentes ao padrão da distribuição.

###### Figura 2
![Elevação por área e espécie](https://github.com/brenoccosta/Visualizacao-exemplo-de-analise-de-dados/blob/28c19c4f0994c4b6fe54d3a3df490d285686648b/Gr%C3%A1ficos/Eleva%C3%A7%C3%A3o%20por%20%C3%A1rea%20e%20esp%C3%A9cie.png?raw=True)

## Conclusão

Restam ainda outros atributos para serem explorados, tais como inclinação, sombra e acesso a água. Devido à extensão da matéria, concluirei com um breve comentário acerca da importância hídrica dessas montanhas para a região.

A **Figura 3** mostra a proximidade horizontal e vertical da fonte de água mais próxima. Chamo a atenção aqui para a resiliência do **krummholz** (sete) que, no **Pico Comanche**, a partir de 750 metros horizontais, é a vegetação predominante. Contudo, na **Neota**, essa espécie está muito concentrada próximo a fontes de água. Se nos recordarmos que tal região se concentra em elevadas altitudes e é cheio de rochas, provavelmente muitas das águas das terras baixas derivam desse *habitat*, onde possivelmente essa espécie desenvolve um papel de preservação do ecossistema. A reflexo do escoamento das águas pode ser visto em **Cache la Poudre**, de todas as áreas, onde as amostras mais se aproximam. Não coincidentemente, é a região florestal mais baixa.

###### Figura 3
![Distribuição do acesso à água](https://github.com/brenoccosta/Visualizacao-exemplo-de-analise-de-dados/blob/28c19c4f0994c4b6fe54d3a3df490d285686648b/Gr%C3%A1ficos/%C3%81reas%20geogr%C3%A1ficas%20-%20proximidade%20com%20a%20%C3%A1gua.png?raw=True)

Os muitos atributos do *dataset* oferecem uma série de informações importantes acerca dos dados coletados. Uma análise detalhada de um aspecto basta para levantar questões que serão respondidas pela correlação com os demais, situando o agente no mar de dados disponíveis e permitindo-o fazer bom uso dos mesmos. Apesar de nem todas as descobertas estarem relacionadas ao objetivo inicial (como os reflexos na hidrologia), conhecer o mundo do qual provêm as amostras pode abrir caminhos inesperados, engrandecendo o trabalho, ou, no mínimo, solidificar as ações tomadas, pelo conhecimento ser melhor embasado.

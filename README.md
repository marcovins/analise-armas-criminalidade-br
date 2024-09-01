# Análise da Correlação entre Armas de Fogo Ilegais e Criminalidade no Brasil
Análise da relação entre a presença de armas de fogo ilegais e a taxa de criminalidade nas regiões do Brasil, modelando e analisando esses fatores como redes complexas, para o curso de Engenharia de Computação - IFPB.

<p align="center"> 
<h4 align="center"> Grafo para Análise de Armas e Criminalidade - Engenharia de Computação/<a href="https://www.ifpb.edu.br/">IFPB</a> (Inverno 2024) </h4>

<br>
</br>
<p align="center"> 
<a href="https://i.makeagif.com/media/8-07-2015/otpMtV.gif" target="_blank"><img src="https://i.makeagif.com/media/8-07-2015/otpMtV.gif" alt="image host" height="142px"/></a>
</p>

<h4 align="center"> | <a href="#obetivo">Objetivos</a> | <a href="#desenvolvimento">Desenvolvimento</a> | <a href="#resultados">Resultados  obtidos</a> | <a href="#descricao">Descrição dos arquivos</a> | <a href="#creditos">Créditos</a> |</h4>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="objetivo"> :brain: OBJETIVOS</h2>

<p><li><strong>Objetivo geral</strong></li></p>

<div style="text-align: justify;"> 
Explorar a relação entre a presença de armas de fogo ilegais e a taxa de criminalidade nas regiões do Brasil, modelando e analisando esses fatores como redes complexas. O desenvolvimento do projeto dar-se-á uma proposta de avaliação para a cadeira de Teoria dos Grafos, ministrada pelo professor Henrique Cunha.
</div>

<p><li><strong>Objetivos específicos</strong></li></p>
<div align="justify"> → Modelar as conexões entre diferentes tipos de crimes e a apreensão de armas de fogo ilegais em diversas Unidades Federativas (UFs) brasileiras; </div>
<div align="justify"> → Analisar padrões geográficos e temporais para identificar regiões com alta correlação entre a criminalidade e a presença de armas de fogo; </div>
<div align="justify"> → Detectar componentes conexas e analisar a centralidade de estados e crimes específicos em relação à presença de armas ilegais. </div>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="desenvolvimento"> 🖥️ DESENVOLVIMENTO</h2>

<p><li><strong>Impacto social da análise</strong></li></p>
<ul>
<div align="justify"> Este projeto pode contribuir para o desenvolvimento de políticas públicas de segurança mais eficientes, ao fornecer evidências empíricas sobre a relação entre armas ilegais e o aumento da criminalidade em determinadas regiões. </div>
</ul>

<p><li><strong>Ferramentas utilizadas</strong></li></p>
<ul>
<div align="justify"> → Bibgrafo: Para modelagem e estruturação dos dados como grafos; </div>
<div align="justify"> → Gephi: Para visualização e análise das propriedades do grafo; </div>
<div align="justify"> → NetworkX: Para análises adicionais das propriedades dos grafos, como centralidade e detecção de comunidades. </div>
</ul>

<p><li><strong>Formato dos dados</strong></li></p>
<ul>
<div align="justify"> Todos os arquivos utilizados no projeto foram extraídos em formato tabular, através da extensão .xlxs. São eles: </div>
<div align="justify"> → Ocorrências com Armas de Fogo: dados categorizados por UF, tipo de ocorrência (ex: apreensão, furto), data e características da arma; </div>
<div align="justify"> → Crimes por Estado no Brasil: dados categorizados por UF, tipo de crime, data, e quantidade de ocorrências; </div>
<div align="justify"> → População do País por Estado:  dados categorizados por UF e quantidade de habitantes. </div>
</ul>

<p><li><strong>Transformação dos dados</strong></li></p>
<ul>
<div align="justify"> → Vértices: Unidades Federativas (UFs), tipos de crimes e ocorrências de incidência de armas; </div>
<div align="justify"> → Arestas: relações entre a quantidade de habitantes em uma UF, a presença de armas ilegais e a ocorrência de determinados tipos de crimes também em uma UF; </div>
<div align="justify"> → Pesos das arestas: frequência das apreensões de armas e a quantidade de crimes em uma determinada região. </div>
</ul>

<p><li><strong>Análise das características dos dados</strong></li></p>
<ul>
<div align="justify"> → Centralidade: identificação das UFs com maior influência tanto em termos de apreensões de armas quanto de ocorrências criminais; </div>
<div align="justify"> → Componentes Conexas: detecção de regiões com alta interconexão entre crimes e apreensões; </div>
<div align="justify"> → Comunidades: identificação de grupos de estados onde a relação entre crimes e apreensões é mais forte. </div>
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="resultados"> 📈 RESULTADOS OBTIDOS</h2>

<p><li><strong>Grafo de População</strong></li></p>
<ul>
Grafo direcionado onde os nós representam as Unidades Federativas (UFs) do Brasil e as arestas representam a relação entre cada estado e sua respectiva população. Assim, o grafo conecta cada UF a um nó 'População', com o peso da aresta representando a população daquela UF. </ul>
<ul> Grafo obtido:
</ul>

<br>
</br>
<p align="center"> 
<a href="https://s4.aconvert.com/convert/p3r68-cdx67/auo53-5z1zr.jpg" target="_blank"><img src="https://s4.aconvert.com/convert/p3r68-cdx67/auo53-5z1zr.jpg" alt="image host"/></a>
</p>

<p><li><strong>Grafo de Ocorrências de Crimes Violentos</strong></li></p>
<ul>
Grafo direcionado onde os nós representam as Unidades Federativas (UFs) do Brasil e as arestas representam a relação entre cada estado e sua respectiva população. Assim, o grafo conecta cada UF a um nó 'População', com o peso da aresta representando a população daquela UF. </ul>
<ul> Grafo obtido:
</ul>

<br>
</br>
<p align="center"> 
<a href="https://s4.aconvert.com/convert/p3r68-cdx67/alsyk-4i5xr.jpg" target="_blank"><img src="https://s4.aconvert.com/convert/p3r68-cdx67/alsyk-4i5xr.jpg" alt="image host"/></a>
</p>

<p><li><strong>Grafo de Incidência de Armas Ilícitas</strong></li></p>
<ul>
Grafo direcionado onde os nós representam as Unidades Federativas (UFs) do Brasil e as arestas representam a relação entre cada estado e sua respectiva população. Assim, o grafo conecta cada UF a um nó 'População', com o peso da aresta representando a população daquela UF. </ul>
<ul> Grafo obtido:
</ul>

<br>
</br>
<p align="center"> 
<a href="https://s4.aconvert.com/convert/p3r68-cdx67/a1ekr-hwhaj.jpg" target="_blank"><img src="https://s4.aconvert.com/convert/p3r68-cdx67/a1ekr-hwhaj.jpg" alt="image host"/></a>
</p>

<p><li><strong>Grafo final</strong></li></p>
<ul>
Grafo direcionado onde os nós representam as Unidades Federativas (UFs) do Brasil e as arestas representam a relação entre cada estado e sua respectiva população. Assim, o grafo conecta cada UF a um nó 'População', com o peso da aresta representando a população daquela UF. </ul>
<ul> Grafo obtido:
</ul>

<br>
</br>
<p align="center"> 
<a href="https://s4.aconvert.com/convert/p3r68-cdx67/axln2-m0v6l.jpg" target="_blank"><img src="https://s4.aconvert.com/convert/p3r68-cdx67/axln2-m0v6l.jpg" alt="image host"/></a>
</p>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="arquivos"> :floppy_disk: DESCRIÇÃO DOS ARQUIVOS DO PROJETO</h2>

<p>Este projeto inclui arquivos executáveis e de destino, além de acesso ao diretório fonte (repositório), como a seguir:</p>
<h4>➔ Arquivos executáveis:</h4>
<ul>
<li><a href="https://github.com/marcovins/analise-armas-criminalidade-br/blob/master/src/Populacao.py"><b>Populacao.py</b></a> - Contém o código-fonte responsável pela importação do dataset de população. </li>
<li><a href="https://github.com/marcovins/analise-armas-criminalidade-br/blob/master/src/OcorrenciasViolencia.py"><b>OcorrenciasViolencia.py</b></a> - Contém o código-fonte responsável pela importação do dataset de Ocorrências de Crimes de Violentos. </li>
<li><a href="https://github.com/marcovins/analise-armas-criminalidade-br/blob/master/src/FurtosDeArmas.py"><b>FurtosDeArmas.py</b></a> - Contém o código-fonte responsável pela importação do dataset de Incidência de Armas Ilícitas. </li>
<li><a href="https://github.com/marcovins/analise-armas-criminalidade-br/blob/master/src/ModelagemGrafos/grafoPopulacao.py"><b>grafoPopulacao.py</b></a> - Este código utiliza as bibliotecas pandas e networkx para criar e manipular um grafo direcionado com base em dados populacionais das Unidades Federativas (UFs) do Brasil. O grafo é estruturado a partir de um arquivo Excel que contém as informações populacionais, e, em seguida, as arestas são adicionadas com os pesos correspondentes. </li>
<li><a href="https://github.com/marcovins/analise-armas-criminalidade-br/blob/master/src/ModelagemGrafos/grafoOcorrencias.py"><b>grafoOcorrencias.py</b></a> - Utiliza as bibliotecas pandas e networkx para criar e manipular um grafo direcionado com base em dados de ocorrências criminais nas UFs do Brasil. O grafo é gerado a partir de um arquivo CSV contendo informações detalhadas sobre as ocorrências e é estruturado para mostrar a relação entre as UFs e os tipos de ocorrências. </li>
<li><a href="https://github.com/marcovins/analise-armas-criminalidade-br/blob/master/src/ModelagemGrafos/grafoCrimes.py"><b>grafoCrimes.py</b></a> - Construção de grafo direcionado que representa a relação entre as UFs os e tipos de crimes, com base em um conjunto de dados de ocorrências criminais e permitindo a distribuição geográfica de crimes em relação a cada estado. </li>
<li><a href="https://github.com/marcovins/analise-armas-criminalidade-br/blob/master/src/ModelagemGrafos/grafoFinal.py"><b>grafoFinal.py</b></a> - Este código cria um grafo direcionado para modelar a associação entre a violência (representada por crimes) e a circulação ilícita de armas de fogo em diferentes UFs do Brasil. Ele utiliza três grafos distintos: um para crimes, outro para ocorrências envolvendo armas de fogo e um último para a população. A partir destes grafos, um grafo final é construído para analisar a relação entre esses fatores. </li>
<li><a href="https://github.com/marcovins/analise-armas-criminalidade-br/blob/master/src/visualizar.py"><b>visualizar.py</b></a> - Contém uma função chamada visualizar_grafo, que utiliza as bibliotecas matplotlib e networkx para gerar uma visualização gráfica de um grafo. A função permite que ele seja exibido com um layout de mola, o que ajuda a distribuir os nós de forma que as arestas sejam equilibradas visualmente. </li>
</ul>

<h4>➔ Bibliotecas utilizadas:</h4> 
<ul>
  <li>pandas (pd): é uma biblioteca de software de código aberto para a linguagem de programação Python, usada para manipulação e análise de dados. Em particular, ela oferece estruturas de dados e operações para manipular tabelas numéricas e séries temporais. A biblioteca é amplamente utilizada para lidar com dados estruturados e não estruturados, como CSV, Excel, SQL e muitos outros formatos. No projeto, foi utilizada para carregar e manipular dados, como um conjunto de dados de crimes ou população. </li>
  <li>networkx (nx): é uma biblioteca Python para a criação, manipulação e estudo da estrutura, dinâmica e funções de redes complexas (grafos). A biblioteca fornece ferramentas para a criação de vários tipos de grafos (direcionados, não direcionados, multigrafos) e oferece funções para análise de redes, como cálculo de centralidade, detecção de componentes conexas e muitas outras. N oprojeto, foi utilizada para criar um grafo, onde nós podem representar diferentes entidades (como estados ou tipos de crimes) e as arestas podem representar as relações entre essas entidades.</li>
  <li>matplotlib.pyplot (plt): é uma biblioteca de plotagem 2D para Python que gera gráficos de alta qualidade em uma variedade de formatos e ambientes interativos. O módulo pyplot de matplotlib fornece uma interface semelhante à do MATLAB, que simplifica a criação de gráficos simples como linhas, histogramas, gráficos de dispersão, etc. No projeto, foi utilizado por networkx para visualizar os grafos, permitindo a criação de gráficos interativos e customizados para análise. </li>
</ul>

<h4>➔ Arquivos de destino:</h4> 
<ul>
  <li><a href="https://github.com/marcovins/analise-armas-criminalidade-br/tree/master/rsc/datasets/populacao"><b>populacao</b></a> - Contém os datasets de população utilizados como uma das fontes de dados do projeto. </li>
  <li><a href="https://github.com/marcovins/analise-armas-criminalidade-br/tree/master/rsc/datasets/ocorrencias"><b>ocorrencias</b></a> - Contém os datasets de ocorrências utilizados como uma das fontes de dados do projeto. </li>
  <li><a href="https://github.com/marcovins/analise-armas-criminalidade-br/tree/master/rsc/datasets/crimes_por_estado"><b>crimes</b></a> - Contém o dataset de crimes por estado utilizado como uma das fontes de dados do projeto. </li>
  <li><a href="https://github.com/marcovins/analise-armas-criminalidade-br/tree/master/rsc/datasets/Seguranca_publica"><b>segurança</b></a> - Contém os datasets de segurança pública utilizados como uma das fontes de dados do projeto. </li>
</ul>

<h4>➔ Diretório fonte:</h4>
<ul>
  <li><a href="https://github.com/marcovins/analise-armas-criminalidade-br"><b>Análise Armas Criminalidade Br</b></a> - Inclui todos os arquivos listados acima. </li>
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="creditos"> :scroll: CRÉDITOS</h2>

<p><li><strong>Alunos</strong></li></p>
<ul> Anna Lígia Alves Nogueira </ul>
<ul> Marcos Vinícis Belo da Silva </ul>

<p><li><strong>Professor responsável</strong></li></p>
<ul> Henrique Cunha </ul>


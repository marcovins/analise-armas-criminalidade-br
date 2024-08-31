# Análise da Correlação entre Armas de Fogo Ilegais e Criminalidade no Brasil
Análise da relação entre a presença de armas de fogo ilegais e a taxa de criminalidade nas regiões do Brasil, modelando e analisando esses fatores como redes complexas, para o curso de Engenharia de Computação - IFPB.

<p align="center"> 
<h4 align="center"> Grafo para Análise de Armas e Criminalidade - Engenharia de Computação/<a href="https://www.ifpb.edu.br/">IFPB</a>(Inverno 2024) </h4>

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
Este projeto pode contribuir para o desenvolvimento de políticas públicas de segurança mais eficientes, ao fornecer evidências empíricas sobre a relação entre armas ilegais e o aumento da criminalidade em determinadas regiões.
</ul>

<p><li><strong>Ferramentas utilizadas</strong></li></p>
<div align="justify"> → Bibgrafo: Para modelagem e estruturação dos dados como grafos; </div>
<div align="justify"> → Gephi: Para visualização e análise das propriedades do grafo; </div>
<div align="justify"> → NetworkX: Para análises adicionais das propriedades dos grafos, como centralidade e detecção de comunidades. </div>

<p><li><strong>Formato dos dados</strong></li></p>
<ul>
Todos os arquivos utilizados no projeto foram extraídos em formato tabular, através da extensão .xlxs. São eles:
<div align="justify"> → Ocorrências com Armas de Fogo: dados categorizados por UF, tipo de ocorrência (ex: apreensão, furto), data e características da arma; </div>
<div align="justify"> → Crimes por Estado no Brasil: dados categorizados por UF, tipo de crime, data, e quantidade de ocorrências; </div>
<div align="justify"> → População do País por Estado:  dados categorizados por UF e quantidade de habitantes. </div>
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
  » No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/main.py"><b>main.py</b>:</a>
  <li>asyncio: sendo uma biblioteca para escrever código simultâneo, utilizamos as sintaxes async/await. Com o seu conjunto de APIs, conseguimos efetuar funções Python simultaneamente e ter domínio sobre sua execução, além de controlar subprocessos, distribuir tarefas por meio de filas e sincronizar código simultâneo. Apesar de o parâmetro ctx ser uma convenção para boa parte dos comandos, "member" também foi utilizado para uma melhor legibilidade do código.</li>
  <li>discord: esta biblioteca tem como princípio o conceito de eventos, possibilitando que as mensagens possam ser enviadas, lidas e respondidas com base em pré-definições. </li>
  <li>from discord.ext import commands:  O discord.ext é um módulo da biblioteca discord.py que oferece um framework de extensão para criar bots e aplicações utilizando a API do Discord. A sua utilização dentro do código deu-se de forma a facilitar a escrita dos comandos. </li>
</ul>
<ul>
  » No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/database.py"><b>database.py</b>:</a>
  <li>pandas: utilizamos esta biblioteca para a incorporação dos arquivos .csv, que contém as relações de alunos e professores que poderão ser vinculados ao servidor. Pandas é responsável por incorporar e verificar estes Dataframes no processo de autenticação. </li>
 </ul> 
 <ul>
  » No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/bot_functions.py"><b>bot_functions.py</b>:</a>
  <li>email.message: sendo uma biblioteca de gerenciamento, seu componente central é um “modelo de objeto” que representa mensagens de e-mail. As aplicações do código interagem com o pacote principalmente através da interface do modelo de objeto definida no submódulo "message".</li>
  <li>random: aqui, são implementados geradores de números pseudoaleatórios para várias distribuições. A biblioteca é utilizada, no código, para gerar a chave de segurança que será enviada para o endereço eletrônico do usuário no processo de autenticação. </li>
  <li>requests: esta é uma biblioteca necessária para requisições de API, foi utilizada devido às integrações com o Arxiv e Stack Overflow. No código, para ambas as funções, fizemos uso do método "get" para recuperar os dados do endpoint definido. Entretanto, para a primeira, foram utilizados métodos de busca específicos; para a segunda, por sua vez, definimos o URL da API para varredura dos dados e utilizamos o response.json() para exibir as respostas obtidas. </li>
  <li>smtplib: familiar ao protocolo HTTP, o SMTP (Simple Mail Transfrer Protocol) é utilizado para envio de e-mail; ele dita como este será formatado, criptografado e transmitido.</li>
  <li>xml.etree.ElementTree: XML se refere a "Extensible Markup Language" e possui similaridades com o HTML, sendo que sua proposta principal é guardar e transportar dados. Trata-se de uma linguagem auto-descritiva. Esta biblioteca implementa uma API simples e eficiente para analisar e criar dados XML, funcionando como uma estrutura de árvore que suporta hierarquia. Juntamente aos métodos findall() e find(), o Bot consegue fazer uma busca e retornar o resultado solicitado com base nas variáveis pré-definidas. O modúlo foi utilizado para realizar uma cópia do arquivo XML gerado por uma requisição e acessar as informações como strings. </li>
</ul>

<h4>➔ Módulos internos:</h4> 
<ul>
  » No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/main.py"><b>main.py</b>:</a> </li>
  <li>from config import *: ao buscar os dados confidenciais do config.py e importá-los no servidor, conseguimos prosseguir com os comandos necessários para o processo de autenticação do usuário. </li>
  <li>from bot_functions import *: o arquivo bot_functions é o responsável pelo processo de verificação e envio de e-mail ao usuário do servidor, bem como geração e validação da chave de autenticação. Além disso, ele importa as funções utilizadas nos comandos "!artigos" e "!duvida". O seu uso fora imprescindível tanto por questões de organização e leitura do código, quanto por maior praticidade de uso das funções. </li>
  <li>from database import *: neste arquivo, encontramos strings com dicas a serem enviadas, em um intervalo de 60 minutos, para o usuário autenticado no servidor. "From" e "import" são comandos utilizados para integrá-lo ao servidor através do main.py. </li>
</ul>
<ul>
  » No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/bot_functions.py"><b>bot_functions.py</b>:</a>
  <li>from database import *: para bot_function, são importados os dataframes a serem utilizados na função authenticate. Optamos pela importação de todo o modúlo devido à questões de praticidade. </li>
  <li>from config import *: os dados confidenciais do config.py são necessários para a normalização do funcionamento das funções do Bot. </li>
</ul>  
<h4>➔ Arquivos de destino:</h4> 
<ul>
  <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/data/alunos.csv"><b>alunos.csv</b></a> - Contém o arquivo de "alunos.csv", utilizado como banco de dados do projeto. Não é uma informação confidencial, visto que apresenta alunos matriculados em uma Instituição de Ensino Pública.</li>
  <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/data/professores.csv"><b>professores.csv</b></a> - Contém o arquivo de "professores.csv" utilizado como banco de dados do projeto. Não é uma informação confidencial, visto que apresenta professores vinculados à uma Instituição de Ensino Pública.</li>
</ul>

<h4>➔ Diretório fonte:</h4>
<ul>
  <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB"><b> Bot_Discord_IFPB</b></a> - Inclui todos os arquivos listados acima. </li>
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="ferramentas"> :books: PRINCIPAIS FERRAMENTAS UTILIZADAS </h2>

<ul>
  <li>Discord</li>
  <p> Utilizamos a plataforma <strong>Discord</strong> como alicerce do Bot, sendo esta, além de uma das principais ferramentas de comunicação dentro da comunidade de TI, detentora de funcionalidades próprias de autenticação e atribuição de cargos. </p>
</ul> 
<ul>
  <li>Python</li>
  <p> Para o desenvolvimento do projeto, utilizados como base a linguagem de programação<strong> Python</strong>, tanto por ser a ferramenta de aprendizado utilizada durante o curso de Algoritmos, quanto por ser uma linguagem de alto nível, orientada a objetos, funcional e de tipagem dinâmica e forte. </p>
</ul>  
<ul>
  <li>Pandas</li>
  <p> Utilizamos, para manipulação dos arquivos .csv, a biblioteca <strong>Pandas</strong>, visto que esta auxilia com uma melhor visualização do Dataframe e possui uma filtragem de dados melhor documentada. </p>
</ul> 
<ul>
  <li>HTML</li>
  <p> Para envio do e-mail contendo o código de verificação do usuário a ser autenticado, fizemos uso da linguagem <strong>HTML</strong> para melhor formatação e agradabilidade estética, visto que é uma linguagem de marcação utilizada na construção de páginas na Web. </p>
</ul>
<ul>
  <li>Chat GPT</li>
  <p> Para esclarecimento de dúvidas e obtenção de um melhor direcionamentos durante a escrita do código, o <strong>Chat GPT</strong> fora de grande ajuda, sendo uma ferramenta de grande relevância para o desenvolvimento deste projeto. O seu uso foi correspondente às diretrizes estabelecidas pela OpenAI, de modo que todos os trechos utilizados e gerados foram devidamente adaptados. Além disso, o Chat GPT está sendo citado como referência, conforme legislação prescrita no Art. 184 do Código Penal. </p>
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="bot">🤖 O BOT</h2>

<h4>➔ Confira alguns exemplos do funcionamento do Bot IFPB</h4>

<h4 align="center">Canais:</h4>
<p align="center"> 
<a href="" target="_blank"><img src="https://uploaddeimagens.com.br/images/004/519/173/full/Captura_de_tela_2023-06-24_183525.png?1687643464"/></a>

<h4 align="center">Envio automático de dicas acadêmicas:</h4>
<p align="center"> 
<a href="" target="_blank"><img src="https://uploaddeimagens.com.br/images/004/519/181/full/Captura_de_tela_2023-06-24_151119.png?1687643850"/></a>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="creditos"> :scroll: CRÉDITOS</h2>

<p><li><strong>Alunos</strong></li></p>
<ul> Anna Lígia Alves Nogueira </ul>
<ul> Marcos Vinícis Belo da Silva </ul>

<p><li><strong>Professor responsável</strong></li></p>
<ul> Henrique Cunha </ul>


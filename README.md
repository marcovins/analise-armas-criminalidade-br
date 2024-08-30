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

<p><li>Objetivo geral</li>
    
<div style="text-align: justify;">
Explorar a relação entre a presença de armas de fogo ilegais e a taxa de criminalidade nas regiões do Brasil, modelando e analisando esses fatores como redes complexas. O desenvolvimento do projeto dar-se-á uma proposta de avaliação para a cadeira de Teoria dos Grafos, ministrada pelo professor Henrique Cunha.
</div> </p>

<p><li>Objetivos específicos</li>
<h4 align="justify" style="font-weight: normal;"> → Modelar as conexões entre diferentes tipos de crimes e a apreensão de armas de fogo ilegais em diversas Unidades Federativas (UFs) brasileiras; </h4>
<h4 align="justify" style="font-weight: normal;"> → Analisar padrões geográficos e temporais para identificar regiões com alta correlação entre a criminalidade e a presença de armas de fogo; </h4> 
<h4 align="justify" style="font-weight: normal;"> → Detectar componentes conexas e analisar a centralidade de estados e crimes específicos em relação à presença de armas ilegais. </h4> 
</p>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="desenvolvimento"> 🖥️ DESENVOLVIMENTO</h2>

<li>Impacto social da análise:</li> 
<ul>
Este projeto pode contribuir para o desenvolvimento de políticas públicas de segurança mais eficientes, ao fornecer evidências empíricas sobre a relação entre armas ilegais e o aumento da criminalidade em determinadas regiões.
</ul>

<li>Ferramentas utilizadas</li> 
<ul>
Bibgrafo: Para modelagem e estruturação dos dados como grafos;
Gephi: Para visualização e análise das propriedades do grafo;
NetworkX: Para análises adicionais das propriedades dos grafos, como centralidade e detecção de comunidades.
</ul>

<li>Formato dos dados</li> 
<ul>
Todos os arquivos utilizados no projeto foram extraídos em formato tabular, através da extensão .xlxs. São eles:
Ocorrências com Armas de Fogo: dados categorizados por UF, tipo de ocorrência (ex: apreensão, furto), data e características da arma;
Crimes por Estado no Brasil: dados categorizados por UF, tipo de crime, data, e quantidade de ocorrências;
População do País por Estado:  dados categorizados por UF e quantidade de habitantes. 
</ul>


<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="funcionalidades">✍️ FUNCIONALIDADES ADICIONAIS</h2>

<li>Comando “!artigos” 🔍:</li> 
<ul>
Este comando pode ser utilizado dentro do servidor, em qualquer canal, para busca de artigos científicos (no idioma inglês) localizados através da palavra-chave informada. O Bot retornará 5 artigos classificados por ordem de relevância na arvix, constando: título, autor e link para download em pdf. É importante frisar que outros membros podem ter acesso à pesquisa, com exceção do chat privado com o Bot IFPB (para acessá-lo, basca clicar sobre o nome ou ícone do mascote e digitar o comando no campo “Conversar com @IFPB”).
</ul>

<li>Integração com o Stack Overflow 🗣️:</li>  
<ul>
Pertencente à Rede Stack Exchange, o Stack Overflow é um dos maiores sites de perguntas e respostas para profissionais e entusiastas na área de programação de computadores. Por isso, a funcionalidade é pertinente ao solicitar a pergunta ao usuário do servidor (através do comando “!duvida”) e respondê-lo com as soluções mais relevantes encontradas no site e seus respectivos links.
</ul>

<li>Envio de dicas acadêmicas 🎓:</li>
<ul>
Em um intervalo de 60 minutos, o servidor encaminha mensagens para suporte acadêmico aos discentes, dentre elas: dicas sobre o Campus (como se conectar ao Wi-Fi e horário dos transportes públicos, por exemplo), dicas acadêmicas/de estudo (por exemplo, revisar regularmente o conteúdo já estudado para fortalecer a memória) e dicas profissionais/da área (a exemplo desta: "Quando estiver programando, lembre-se de que um bom café pode ser o seu 'compilador' secreto!"). Algumas das orações podem conter tom humorístico, também sendo uma característica pertinente ao BOT. 
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="arquivos"> :floppy_disk: DESCRIÇÃO DOS ARQUIVOS DO PROJETO</h2>

<p>Este projeto inclui arquivos executáveis e de destino, além de acesso ao diretório fonte (repositório), como a seguir:</p>
<h4>➔ Arquivos executáveis:</h4>
<ul>
  <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/main.py"><b>main.py</b></a> - Contém o código-fonte responsável pela integração entre o Bot e o servidor do Discord. Para isso, foram utilizados procedimentos de autenticação, em que o BOT envia os comandos de solicitação de e-mail e atribui o usuário ao respectivo cargo quando a condição é cumprida. </li>
   <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/database.py"><b>database.py</b></a> - Contém os dataframes utilizados para a autenticação e strings com dicas a serem enviadas, em um intervalo de 60 minutos, para o usuário autenticado no servidor. </li>
    <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/bot_functions.py"><b>bot_functions.py</b></a> - Modúlo responsável por armazenar as funções utilizadas no main.py, estando estas devidamente documentadas no código por suas respectivas docstrings. </li>
   <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/.gitignore"><b>.gitignore</b></a> - Contém um arquivo config.py não rastreável, sendo este responsável pela informação dos dados de e-mail, token de comunicação com o Google, token do Discord e as ID's dos canais do servidor. Sendo assim, o .gitigoore é utilizado como recurso de segurança e confidencialidade das informações sensíveis do código. Caso queira testar o servidor e sua funcionamento devida, crie um arquivo "config.py" e adicione as variáveis: token, email_bot, password, pretendente_id, public_channel_id, off_topic_id e welcome_id (as variáveis de ID podem ser substituídas pelos canais de sua preferência). </li>
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

<li>Alunos</li>
<p>Anna Lígia Alves Nogueira</p>
<p>Rodrigues Matheus Lima</p></p>

<li>Professor responsável</li>
<p>Henrique Cunha</p>

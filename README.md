# BattleShip

BOARD

- A primeira coisa que comecei a fazer foi o board.

- Repare que quado o usuario escreve o nome, aparece logo acima do board dizendo o proprio nome do usuario ao inves de "Your board" por exemplo", isso deixa o jogo mais convidativo para o usuario.

- No comeco o board estava escrito de forma extenca, muito loga, como "V1=[' ~',' ~',' ~',' ~',' ~',' ~',' ~',' ~',' ~',' ~',' ~',' ~']", isso estava escrito 12 vezes e o codigo nao funcionava como deveria se eu colocasse por exemplo "V1=[' ~'*12]" ou "V1[' ~',' ~',' ~',' ~',' ~',' ~',' ~',' ~',' ~',' ~',' ~',' ~']*12", pois a linguagem interpreta isso como sendo o mesmo elemeto, o '~' deveria ser considerado como um elemento individual, mas apos algumas pesquisas eu pude mudalo para:
"V1=[]
for i in range(12):
    V1.append([' ~']*12)"
    
- e caso nao tenha ficado muito claro, os espacos no comeco do '~' sao apenas para dar uma aparencia melhor e poder colorir o fundo de um dos ' ~' pra vermelho substituindo por ' X' quando ambos os jogadores jogarem a bomba e conseguirem acertar uma parte do ship.

GETTING THE USERS COORDINATES

- Foi colocado instrucoes para o usuario poder inserir as cordenatas onde deseja inserir o ship.

- Here "letter=input('\033[0;35;48m☻ Choose a row (A-L): \033[m').capitalize()" and here "letter2=input('\033[0;35;48m☻ Another row: \033[m').capitalize()", foi nescessario transformar a letra no qual o usuario digitou em numero. Por isso foi preciso capitalizar a letra do input para poder comparar as letras de "H=['A','B','C','D','E','F','G','H','I','J','K','L']") e "transformar em numero" com for loop.

- Ha falhas como: o usuario nao pode errar as cordenadas, o codigo nao detecta o erro e nao oferece chance de tentar denovo, caso o usuario escreva todos as cordenadas de forma correta nos primeiros quatro ships e no quinto ship o usuario errar, tera que clicar run denovo e inserir os dados novamente. Teria que haver codigos para detectar quando o usuario coloca um '■' (no caso um pedaco do barco) em cima de outro '■', caso o usuario erre a linha ou coluna onde iria colocar o resto do barco, quando o usuario escreve uma letra ou numero ou qualquer tipo de outro caracter que nao existe nas opcoes do board...

- Alem dos bugs nao fica claro o suficiente como exatamente o usuario deveria colocar os barcos, o usuario deve entender que o Carrier sao seis '■' consecutivamente sem separar um '■' do outro '■', como '■ ■ ■ ■ ■ ■', deve aparentar assim no board, mas nao consegui pensar em uma maneira melhor de expressar isso sem usar outra plataforma, apenas usando python puro.

GETTING THE PC COORDINATES

- Foi usado a propriedade randint de random para escolher um numero aleatoriamente. a variavel "hv=randint(0,1)" significa que ele ira aleatoriamente escolher 0 ou 1 com a intencao de definir se o barco sera desenhado horizontalmente ou verticalmente:
■     or    ■ ■ ■ ■ ■ ■
■
■
■
■
■

- "pcrow=randint(0,11)" e "pccolumn=randint(0,11)" esta tambem aleatoriamente escolhendo um numero de 0 a 11 pois sao 12 linhas e 12 colunas (colunas representadas pela variavel "H=['A','B','C','D','E','F','G','H','I','J','K','L']").

- Logo abaixo no for loop estou substituindo o '~' que representa a agua por '■' que representa o ship. Porem caso antes de ser imprimido o programa consegue detectar caso o ship ultrapasse o board e uma parte do ship nao sera imprimido dentro da area do board. Caso isso venha a ocorrer ele ira imprimilo na direcao contraria ou seja negativamente. Este era um dos problemas iniciais desta parte, foi preciso bastante esforco para se achar uma maneira para que o ship nao fosse imprimido antes de saber se iria caber, antes disso ser resolvido o programa imprimia a parte do ship que cabia no board e escolhia outra coordenada e continuava a imprimir o resto do ship.

- Ha tambem o problema de que o programa nao detecta se os ships terao colisao (um ship ou mais serem imprimidos no mesmo lugar) isso tambem acontece com getcoordinatesUser. Tentei varias formas de corrigir isso, pois eh um problema que tambem afeta no numero de '■' dentro do board e com isso, se nao houver o numero exato de '■', nao sera possivel declarar um vencedor ou perdedor de acordo com a forma no qual eu decidi escrever meu codigo para decidir isso.

- O programa nao tem inteligencia artificial para caso ele acerte um '■' e continuar tentando na msm area ate terminar de destruir o ship inteiro por exemplo. Pode acontecer de o programa possa atingir o mesmo lugar no qual tivesse ja atingido antes. Entau issu o torna um oponente praticamente irrelevante hahaha, sendo quase impossivel que ele ganhe do usuario.

- Eu poderia tentar corrigir isso mas levaria muito tempo e meu prazo eh apenas de um mes, como apenas iniciante isso eh dificil.

WHEN USER ARE GOING TO DROP THE BOMB

- A ideia eh parecida com a de quando o usuario escolhe onde colocar o '■', nao houve muito alarde com isso. Adcionei uns comentarios para dar mais diversao ao jogador mas caso eu tivesse mais tempo poderia pensar em mais opcoes de comentarios para que o computador pudesse aleatoriamente escolher uma delas.

WHEN PC ARE GOING TO DROP THE BOMB

- Tambem sendo uma ideia mais simples de quando o PC escolhe um lugar no board aletorimente onde colocar os barcos, essa funcao escolhe um lugar aleatoriamente onde colocar o "X"  com fundo vermelho indicando que o barco foi atingido.

WHILE LOOP

- O while loop foi criado para que ele imprima e execute as funcoes acima ate o jogo finalizar com um vencedor e perdedor interropendo o loop. A maio dificuldade nesta parte foi encontrar uma maneira de contagem de '■', pois quem obter 20*'■' primeiro seria o vencedor. Tudo issu foi resolvido com a funcao variavel.find(), mas como mencionei acima, essa funcao nao funcionara caso o usuario ou o PC tenha tido colisao de ships.

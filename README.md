 
<div style="display: flex; align-items: center; justify-content: space-between;">
  <img src="https://github.com/francisquinho777/projeto_A3_Lucena/blob/533857d9b24d78d695f6eb0f8dc961af9f5d3fe0/a3voz/logofpb.png" alt="FPB Logo" width="200">

  <div style="text-align: center; width: 100%;">
    <p><strong>Wedson Francisco da Silva</strong> </p>
	  <p><strong>RA: 1362311302 </strong> </p>
   <p><strong>Curso:</strong> Ciência da computação</p>
  </div>
</div>

## A Voz da Comunidade

## Introdução
A participação ativa da população nas decisões que impactam diretamente sua comunidade é um dos pilares fundamentais para o desenvolvimento social. No entanto, muitos cidadãos ainda enfrentam dificuldades para acessar espaços democráticos ou expressar suas opiniões sobre projetos públicos. Nesse contexto, a tecnologia surge como uma ferramenta essencial para aproximar os moradores das ações do poder público e fortalecer o engajamento social.
O sistema “A Voz da Comunidade” foi idealizado com o objetivo de oferecer uma plataforma digital simples e acessível, que permita aos cidadãos votarem em propostas de melhorias para sua região. Por meio de uma interface intuitiva, o usuário pode conhecer os projetos sociais disponíveis, registrar seu voto e acompanhar os resultados, contribuindo para uma gestão mais participativa e transparente.
Além de incentivar a democracia participativa, o projeto busca coletar dados relevantes sobre as necessidades e prioridades da população, auxiliando na tomada de decisões futuras. Assim, o desenvolvimento deste sistema alia tecnologia, cidadania e inovação social, ampliando as possibilidades de envolvimento comunitário e promovendo maior inclusão no processo decisório.


## Engenharia de Requisitos
O sistema “Votação Comunitária – A Voz da Comunidade” consiste em uma aplicação web e desktop voltados para promover a participação da população em decisões relacionadas a projetos sociais da cidade. A plataforma possibilita que os moradores escolham, de forma democrática, quais iniciativas devem receber prioridade de execução.
O principal propósito do sistema é aproximar a comunidade das decisões públicas, fortalecendo o engajamento social por meio de uma interface acessível, simples de utilizar e segura para o usuário.
________________________________________
## Objetivos

•	Proporcionar uma forma democrática, transparente e segura de votação comunitária;

•	Possibilitar o cadastro e autenticação de usuários;

•	Disponibilizar categorias de ações sociais com suas respectivas descrições;

•	Registrar votos e apresentar resultados parciais e finais de forma clara;

•	Coletar dados das escolhas da população, contribuindo para análises e tomadas de decisão futuras.

## Público-Alvo
O sistema é destinado aos moradores da comunidade local, de diferentes faixas etárias, que possuam acesso à internet e interesse em participar de projetos sociais que contribuam para o desenvolvimento e melhoria da qualidade de vida da região.

## Funcionalidades Principais
Usuário Comum:
•	Realizar cadastro e login;


•	Recuperar senha;


•	Visualizar as categorias de ações sociais disponíveis;


•	Registrar voto na opção desejada;


•	Acompanhar o resultado parcial ou final das votações.


Administrador:


•	Gerenciar cadastros de usuários;


•	Cadastrar, editar e remover opções de votação;


•	Acompanhar relatórios, métricas e estatísticas da plataforma;


•	Encerrar votações e divulgar seus resultados.


## Funcionalidades Implementadas no MVP

O MVP foi construído com base nas etapas essenciais de interação entre o usuário e o sistema.
Nessa versão inicial, é possível realizar cadastro, login, navegação e votação simulada nas categorias disponíveis.


| Funcionalidade                             | Descrição                                                                              | Status                |
| ------------------------------------------ | -------------------------------------------------------------------------------------- | --------------------- |
| **Página inicial (index.html)**         | Exibe as categorias de projetos sociais e informações introdutórias.                          | ✅ Concluído           |
| **Sistema de Login**         | Interface simples de autenticação para simular o acesso de usuários.                          | 🔄 Planejado          |
| **Páginas temáticas (saúde, limpeza, educação, esporte, cidadania)**         | Mostram as propostas de ação social disponíveis para votação.                          | ✅ Concluído           |
| **Tela de Votação (votacao.html)**         | Permite que o usuário selecione uma categoria e envie o voto.                          | ✅ Concluído           |
| **Integração com backend (PHP ou Python)** | O sistema envia o voto e recebe uma resposta simulada (“Voto registrado com sucesso”). | 🟡 Em desenvolvimento |
| **Confirmação visual do voto**             | Exibe mensagem de sucesso após o envio da votação.                                     | ✅ Concluído           |
| **Banco de Dados (MySQL)**                 | Estrutura planejada para armazenar usuários e votos.                                   | 🔄 Planejado          |


## Categorias de Votação
1.	Saúde e Bem-Estar:

	Atendimento médico e dentista (clínico geral, pediatria, geriatria).

2.	Limpeza e Melhorias:

Mutirão de limpeza de ruas e terrenos baldios.

3.	Educação e Cultura:

Aulas rápidas (informática básica, leitura, escrita, artesanato).

4.	Esporte e Lazer:

Torneios esportivos (futebol, queimada, corrida de rua, artes marciais).

5.	Ação Social e Cidadania:

Doação de roupas e alimentos, cadastro e atualização de documentos.


## Requisitos Funcionais 

| Descrição                                                        | Prioridade |
| ---------------------------------------------------------------- | :--------: |
| O sistema deve permitir o cadastro e login do usuário.           |   🔥 Alta  |
| O sistema deve exibir as opções de projetos sociais disponíveis. |   🔥 Alta  |
| O usuário deve poder votar em apenas um projeto.                 |   🔥 Alta  |
| O sistema deve registrar o voto no banco de dados.               |   🔥 Alta  |
| O administrador pode ver os resultados das votações.             |  ⚠️ Média  |

| O sistema deve permitir o redirecionamento após o voto.             |  ⚠️ Média  |


## Requisitos Não Funcionais (RNF)

O sistema deve ser responsivo e fácil de usar.

O sistema deve manter a segurança das informações de login.

O tempo de resposta de cada ação deve ser inferior a 3 segundos.

O código deve seguir boas práticas de HTML, CSS, PHP e JavaScript.

O sistema deve estar preparado para integração com banco de dados MySQL.

## Documentação Técnica

O sistema foi desenvolvido com foco na simplicidade, acessibilidade e usabilidade, possibilitando que qualquer cidadão, mesmo com pouca familiaridade com tecnologia, consiga navegar e registrar seu voto com facilidade.
________________________________________

## Arquitetura e Tecnologias Utilizadas

O projeto adota uma arquitetura em três camadas, garantindo melhor organização do código, facilidade de manutenção e escalabilidade.

| Camada                                    | Descrição                                                       | Tecnologias             |
| ----------------------------------------- | --------------------------------------------------------------- | ----------------------- |
| **Apresentação (Frontend)**               | Responsável pela interface gráfica acessada pelo usuário final. | HTML5, CSS3, JavaScript |
| **Lógica de Negócio (Backend)**           | Processa as requisições, regras de voto e respostas ao cliente. | PHP e Python            |
| **Banco de Dados *(em desenvolvimento)*** | Armazena os dados de usuários, votos e opções de votação.       | MySQL                   |

## Outras ferramentas utilizadas:
•	Visual Studio Code (IDE)

•	Navegadores Web (Google Chrome)

•	Servidor Local: XAMPP ou WAMP

•	CustomTkinter (protótipo desktop para login em Python)
________________________________________
## Configuração do Ambiente (Ambiente Local)

Para executar o sistema localmente, devem ser seguidos os seguintes passos:
1.	Instalar o servidor XAMPP (ou equivalente contendo PHP e MySQL).
2.	Copiar a pasta do projeto para o diretório:
C:\xampp\htdocs\VotacaoComunitaria
3.	Iniciar o servidor Apache (e MySQL, se necessário) no XAMPP Control Panel.
4.	Acessar o sistema pelo navegador, utilizando o endereço:
http://localhost/VotacaoComunitaria/index.html
________________________________________

## Lógica de Funcionamento do Sistema
•	O usuário acessa a página principal do sistema e visualiza as categorias de votação disponíveis;


•	Ao selecionar uma opção e clicar em “Votar”, um script em JavaScript envia o registro ao backend utilizando fetch();


•	O backend em PHP processa a solicitação e registra o voto no sistema;


•	Após o processamento, o servidor retorna uma resposta em formato JSON, confirmando o sucesso da operação;

•	O frontend exibe ao usuário uma mensagem de confirmação como:
“Voto registrado com sucesso!”

## Possíveis Erros e Soluções

A tabela a seguir apresenta problemas comuns que podem ocorrer durante a execução do sistema, bem como suas possíveis causas e soluções recomendadas:

| Erro                                   | Causa Provável                                                      | Solução             |
| ----------------------------------------- | --------------------------------------------------------------- | ----------------------- |
| **Página em branco**               | Servidor local não iniciado | Verificar se o Apache está ativo no XAMPP e recarregar a página
| **PHP não executa**               | Arquivo fora da pasta htdocs| Mover o projeto para dentro do diretório C:\xampp\htdocs\
| **Tela de Login não abre**               |Ausência do Python instalado na máquina | Instalar Python 3.10 ou versão superior e configurar corretamente

## Guia do Usuário

O sistema foi projetado para ser simples, acessível e de fácil utilização, incentivando a participação ativa da população em decisões relacionadas a projetos sociais da comunidade. Para acessar o sistema, o usuário deve realizar login utilizando e-mail e senha previamente cadastrados.
________________________________________
## Como Votar

1.	Realize login com suas credenciais de acesso;

2.	Escolha uma categoria de ação social (ex.: Saúde, Limpeza Urbana, Educação, etc.);

3.	Leia atentamente a descrição da proposta selecionada;

4.	Clique no botão “Votar”;

5.	Aguarde a confirmação exibida na tela com a mensagem:
“Voto registrado com sucesso!”

Após a confirmação, o voto será computado automaticamente no sistema.

## Modelagem
**Diagrama de Casos de Uso**

![image alt](https://github.com/francisquinho777/projeto_A3_Lucena/blob/7d8293197287c2c93218f14f2c9787da0bb74a76/a3voz/diagrama1.png)

## Casos de uso principais:
![image alt](https://github.com/francisquinho777/projeto_A3_Lucena/blob/c74d3117bed5c36d2ca05ee4edde17ee0e88aa0c/a3voz/diagrama2.png)

## Estrutura de Banco (planejado)

| Tabela                               | Campos                                                     | Descrição             |
| ----------------------------------------- | --------------------------------------------------------------- | ----------------------- |
| **users**               | id, nome, email, senha| Armazena informações dos usuários
| **votacoes**               | id, categoria, descricao| Guarda as opções de votação
| **votos**               | id, user_id, votacao_id| Registra os votos de cada usuário

## Arquitetura do Sistema 
A aplicação adota uma arquitetura em camadas, garantindo organização lógica, melhor manutenção e evolução do projeto. As camadas responsáveis por cada parte do sistema são descritas a seguir:


•	Frontend (HTML, CSS e JavaScript): Responsável pela interface gráfica e pela interação com o usuário. Também realiza chamadas ao backend utilizando a função fetch() para envio e recebimento de dados.


•	Backend (PHP e Python): Executa as regras de negócio do sistema, como autenticação de usuários e registro de votos. (Atualmente em desenvolvimento e aprimoramento).


•	Banco de Dados (MySQL): Armazena informações relativas aos usuários cadastrados, categorias e votos registrados. (Estrutura em construção e teste.)

## Fluxo de Navegação do Sistema

O fluxo básico de utilização da plataforma pode ser representado da seguinte forma:
index.html  
      ↓
Escolha de uma categoria de votação  
      ↓
saude.html / limpeza.html / outras categorias  
      ↓
votacao.html  
      ↓
Envio do voto  
      ↓
Servidor (PHP/Python) processa e registra o voto
Esse fluxo visa proporcionar simplicidade e objetividade no processo de votação, reduzindo etapas desnecessárias para o usuário final.

## Prototipagem
O protótipo do sistema foi desenvolvido utilizando HTML, CSS e JavaScript, com o objetivo de demonstrar de maneira interativa o funcionamento da plataforma, permitindo ao usuário navegar entre as telas, realizar cadastro, efetuar login e registrar seu voto em projetos sociais.
As principais telas desenvolvidas até o momento são:

•	Tela Inicial (index.html):
Apresenta o propósito do sistema e lista as categorias de ações sociais disponíveis para votação.

•	Tela de Detalhes (saude.html, limpeza.html, entre outras):
Exibe informações detalhadas sobre cada projeto social selecionado pelo usuário.

•	Tela de Votação (votacao.html):
Disponibiliza a interface onde o cidadão pode escolher uma opção e registrar seu voto de forma simples e rápida.

•	Tela de Login (logado.py):
Protótipo de autenticação de usuários e administradores, desenvolvido em Python com o objetivo de simular o controle de acesso ao sistema.

## Tela inicial (index):
![image alt](https://github.com/francisquinho777/projeto_A3_Lucena/blob/c74d3117bed5c36d2ca05ee4edde17ee0e88aa0c/a3voz/index1.png)
![image alt](https://github.com/francisquinho777/projeto_A3_Lucena/blob/c74d3117bed5c36d2ca05ee4edde17ee0e88aa0c/a3voz/index2.png)


## Tela de Detalhes: 
![image alt](https://github.com/francisquinho777/projeto_A3_Lucena/blob/c74d3117bed5c36d2ca05ee4edde17ee0e88aa0c/a3voz/info_saude.png)
![image alt](https://github.com/francisquinho777/projeto_A3_Lucena/blob/c74d3117bed5c36d2ca05ee4edde17ee0e88aa0c/a3voz/info_lim.png)
![image alt](https://github.com/francisquinho777/projeto_A3_Lucena/blob/c74d3117bed5c36d2ca05ee4edde17ee0e88aa0c/a3voz/info_edu.png)
![image alt](https://github.com/francisquinho777/projeto_A3_Lucena/blob/c74d3117bed5c36d2ca05ee4edde17ee0e88aa0c/a3voz/inf_esport.png)
![image alt](https://github.com/francisquinho777/projeto_A3_Lucena/blob/c74d3117bed5c36d2ca05ee4edde17ee0e88aa0c/a3voz/info_brecho.png)

## Tela de Sistema de Votação:

![image alt](https://github.com/francisquinho777/projeto_A3_Lucena/blob/c74d3117bed5c36d2ca05ee4edde17ee0e88aa0c/a3voz/votacao.png)

## Tela de Login:

![image alt](https://github.com/francisquinho777/projeto_A3_Lucena/blob/c74d3117bed5c36d2ca05ee4edde17ee0e88aa0c/a3voz/login.png)


## Padrões de Projeto 

Durante o desenvolvimento do sistema, foram aplicados conceitos essenciais de organização estrutural e boas práticas de programação, tais como:

•	Modularização:
Cada página do sistema representa um módulo funcional específico, facilitando a manutenção e evolução do projeto.
•	Arquitetura MVC (em planejamento):

Estruturação do sistema com separação entre:

o	Modelo (MySQL): gerenciamento e persistência dos dados;

o	Visão (HTML/CSS): apresentação e interação com o usuário;

o	Controle (JavaScript/PHP): lógica e fluxo das funcionalidades do sistema.

Esse modelo visa proporcionar melhor escalabilidade e clareza na implementação.
•	Validação:

Tratamento básico de erros em funcionalidades como login e registro de votos, evitando ações indevidas e garantindo maior confiabilidade ao sistema.

## Integração Contínua (Planejada)
Está prevista a utilização de um repositório no GitHub, onde serão aplicadas práticas de versionamento e testes, incluindo:

•	Controle de versões do código utilizando Git;

•	Execução e validação do sistema em ambiente local, via servidor XAMPP, para testes de comunicação entre frontend e backend.

Essas práticas têm como objetivo garantir organização do desenvolvimento, rastreabilidade de mudanças e redução de falhas nas futuras versões do sistema.

## Conclusão

O desenvolvimento do sistema “A Voz da Comunidade” demonstra como soluções tecnológicas podem contribuir de maneira significativa para o fortalecimento da participação popular nas decisões relacionadas às necessidades sociais da comunidade. A plataforma foi projetada para ser acessível, intuitiva e funcional, permitindo que cidadãos de diferentes perfis possam registrar suas opiniões e acompanhar os resultados de votações de forma clara e transparente.
Embora ainda esteja em processo de expansão e aperfeiçoamentos técnicos, o sistema já apresenta funcionalidades essenciais para o engajamento comunitário, como o registro de votos, gerenciamento de usuários e prototipação de interfaces. Com a implementação contínua de práticas como integração e versionamento de código, espera-se que o projeto se torne cada vez mais robusto, seguro e preparado para uso em situações reais.
Portanto, este trabalho evidencia a importância de iniciativas que aproximem a população das decisões públicas, utilizando a tecnologia como meio para promover inclusão social e incentivar o exercício da cidadania. A perspectiva futura é ampliar as funcionalidades do sistema, aprimorar a segurança das informações e possibilitar que a plataforma se torne uma ferramenta efetiva de transformação social.





## Referencias:
Durante o desenvolvimento textual deste trabalho, utilizou-se o ChatGPT como ferramenta de apoio para revisão, organização e aprimoramento da escrita, não sendo considerado como fonte bibliográfica.



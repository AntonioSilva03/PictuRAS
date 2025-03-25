# Trabalho desenvolvido para RAS(Requisitos e Arquiteturas de Software)

​PictuRAS é uma aplicação web desenvolvida como parte da cadeira de RAS durante o ano letivo de 2024/2025, no âmbito do Mestrado em Engenharia Informática. O objetivo principal é fornecer uma plataforma de edição de imagens poderosa e intuitiva, com suporte para edição em massa, recursos avançados alimentados por IA e contas de utilizador com diferentes níveis de subscrição.

## Funcionalidades

- **Edição de Imagens em Massa**: Permite a aplicação de alterações a múltiplas imagens simultaneamente, otimizando o fluxo de trabalho.​

- **Funcionalidades Avançadas com IA**: Utiliza inteligência artificial para oferecer ferramentas de edição sofisticadas, melhorando a qualidade e eficiência das edições, utilizando bibliotecas Python.​

- **Gestão de Projetos**: Organize as suas imagens em projetos, facilitando o acesso e a gestão dos seus trabalhos.​

- **Contas de Utilizador com Níveis de Subscrição**: Oferece diferentes planos de subscrição, adaptados às necessidades de cada utilizador, desde funcionalidades básicas a premium.

## Arquitetura

- O projeto adota uma arquitetura de microserviços, com serviços dedicados à gestão de projetos, gestão de utilizadores/sessões, ferramentas e um gateway, através do qual o frontend comunica.​

## Desenvolvimento

- Para iniciar o ambiente de desenvolvimento, execute o seguinte comando no diretório raiz do repositório:

`docker-compose up --build -d`

O frontend estará disponível na porta 3000

## Tecnologias utilizadas

- **Frontend**: Desenvolvido com Vue.js, proporcionando uma interface de utilizador reativa e dinâmica.​

- **Backend**: Implementado em Python, garantindo robustez e flexibilidade no processamento de dados.​

- **Docker**: Utilizado para containerização dos serviços, assegurando consistência entre os ambientes de desenvolvimento e produção.

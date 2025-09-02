# Documento de Requisitos de Software (DRS)
# Projeto: Mapa Astral AI

**Versão:** 1.0

**Data:** 02 de Setembro de 2025

**Autores:** Breno Silva de Abreu

---

## 1. Introdução

### 1.1. Propósito

Este documento tem como propósito definir e detalhar os requisitos funcionais, não-funcionais e de interface para o desenvolvimento do sistema "Mapa Astral AI". Ele servirá como guia para as equipes de design, desenvolvimento e testes, garantindo que o produto final atenda às expectativas e objetivos estabelecidos.

### 1.2. Escopo do Projeto

O projeto "Mapa Astral AI" consiste na criação de uma aplicação web que permite aos usuários gerar um horóscopo personalizado e um mapa astral detalhado a partir de seus dados de nascimento (data, hora e local). O sistema se diferenciará por integrar uma "Astróloga AI", um assistente virtual baseado em um Modelo de Linguagem de Grande Escala (LLM), para fornecer interpretações textuais do mapa e interagir com o usuário através de um chat para responder a dúvidas específicas.

### 1.3. Público-Alvo

*   **Usuário Final:** Pessoas interessadas em astrologia, desde leigos a entusiastas, que buscam uma análise personalizada e interativa de seu mapa astral.
*   **Stakeholders Acadêmicos:** Professores e alunos da disciplina de "Qualidade de Software" e do curso de "Gestão de Tecnologia da Informação", para os quais este documento serve como material de estudo e exemplo prático.
*   **Equipe de Desenvolvimento:** Desenvolvedores, designers e testadores que utilizarão este documento como fonte primária de informação durante o ciclo de vida do projeto.

### 1.4. Definições, Acrônimos e Abreviações

| Termo | Descrição |
| :--- | :--- |
| **DRS** | Documento de Requisitos de Software. |
| **IA** | Inteligência Artificial. |
| **LLM** | Large Language Model (Modelo de Linguagem de Grande Escala). |
| **API** | Application Programming Interface (Interface de Programação de Aplicações). |
| **Mapa Astral** | Diagrama que representa as posições dos planetas, signos e casas astrológicas no momento exato do nascimento de um indivíduo. |
| **Geocodificação** | Processo de converter um endereço textual (ex: "São Paulo, Brasil") em coordenadas geográficas (latitude e longitude). |
| **RF** | Requisito Funcional. |
| **RNF** | Requisito Não-Funcional. |

### 1.5. Referências

*   `roadmap.md` - Documento de planejamento e fases do projeto.

### 1.6. Visão Geral do Documento

Este documento está organizado da seguinte forma: a Seção 2 fornece uma descrição geral do produto, seu contexto e restrições. A Seção 3 detalha os requisitos específicos, divididos em funcionais, não-funcionais e de interface.

---

## 2. Descrição Geral

### 2.1. Perspectiva do Produto

O "Mapa Astral AI" será uma aplicação web autônoma, acessível através de navegadores modernos em desktops e dispositivos móveis. Ele dependerá de serviços externos para funcionalidades chave, como cálculos de efemérides, geocodificação e processamento de linguagem natural.

### 2.2. Funções do Produto

As principais funcionalidades do sistema incluem:
*   Coleta de dados de nascimento do usuário.
*   Cálculo do signo solar e apresentação de um horóscopo diário.
*   Geração completa de um mapa astral (planetas, casas, aspectos).
*   Visualização gráfica do mapa astral.
*   Geração de interpretações textuais personalizadas via IA.
*   Interface de chat para interação e aprofundamento na análise do mapa.

### 2.3. Características dos Usuários

Os usuários finais não necessitam de conhecimento técnico avançado. A interface deve ser intuitiva para guiar tanto usuários novatos em astrologia quanto aqueles que já possuem familiaridade com o tema.

### 2.4. Restrições Gerais

*   **Tecnologia:** O backend será desenvolvido em Python utilizando o framework Django.
*   **Banco de Dados:** SQLite será utilizado para o ambiente de desenvolvimento e PostgreSQL para o ambiente de produção.
*   **Segurança de Dados:** O tratamento de dados pessoais (nome, data de nascimento) deve estar em conformidade com a Lei Geral de Proteção de Dados (LGPD).
*   **Dependências Externas:** O sistema dependerá da disponibilidade e dos termos de serviço das APIs de geocodificação e do LLM escolhido.

### 2.5. Suposições e Dependências

*   Assume-se que os usuários fornecerão informações de nascimento precisas para garantir a acurácia dos cálculos.
*   O projeto depende da existência e acesso a uma biblioteca Python robusta para cálculos de efemérides (ex: `kerykeion`).
*   A qualidade das interpretações da IA está diretamente ligada à qualidade do LLM e à engenharia de prompt desenvolvida.

---

## 3. Requisitos Específicos

### 3.1. Requisitos Funcionais

| ID | Requisito | Descrição | Prioridade | Rastreabilidade (Roadmap) |
| :--- | :--- | :--- | :--- | :--- |
| **RF-001** | Entrada de Dados do Usuário | O sistema deve apresentar um formulário para que o usuário possa inserir seu nome, data de nascimento, horário de nascimento e local de nascimento (cidade, país). | Alta | Tarefa 1.1 |
| **RF-002** | Cálculo de Signo Solar | Com base na data de nascimento, o sistema deve calcular e identificar o signo solar do usuário. | Alta | Tarefa 1.2 |
| **RF-003** | Exibição de Horóscopo do Dia | O sistema deve exibir um texto de horóscopo genérico correspondente ao signo solar do usuário. | Alta | Tarefa 1.2 |
| **RF-004** | Geocodificação de Local | O sistema deve converter o local de nascimento textual em coordenadas geográficas (latitude, longitude) através de uma API externa. | Alta | Tarefa 2.2 |
| **RF-005** | Cálculo Completo do Mapa Astral | Utilizando os dados de nascimento e as coordenadas geográficas, o sistema deve calcular: a) Posição dos planetas nos signos; b) Posição das 12 casas astrológicas; c) Principais aspectos entre os planetas. | Alta | Tarefa 2.3 |
| **RF-006** | Armazenamento de Dados do Mapa | O sistema deve persistir os dados calculados do mapa astral em um banco de dados, associando-os ao perfil do usuário/sessão. | Média | Tarefa 2.4 |
| **RF-007** | Geração de Gráfico do Mapa | O sistema deve gerar uma representação visual (gráfico/imagem) do mapa astral calculado. | Alta | Tarefa 3.1 |
| **RF-008** | Apresentação de Resultados | A página de resultados deve exibir o gráfico do mapa astral e uma tabela/lista detalhada com as posições dos planetas e casas. | Alta | Tarefa 3.2 |
| **RF-009** | Geração de Interpretação por IA | O sistema deve enviar os dados estruturados do mapa para uma API de LLM e obter uma interpretação textual, seguindo um prompt que define a persona "Astróloga AI". | Alta | Tarefa 4.2 |
| **RF-010** | Exibição da Interpretação da IA | O sistema deve formatar e exibir a interpretação gerada pela IA na página de resultados. | Alta | Tarefa 4.3 |
| **RF-011** | Cache de Interpretação | O sistema deve implementar um mecanismo de cache para armazenar as interpretações da IA, evitando chamadas repetidas à API para os mesmos dados de entrada. | Média | Tarefa 4.3 |
| **RF-012** | Chat Interativo com a IA | O sistema deve fornecer uma interface de chat para que o usuário possa fazer perguntas sobre seu mapa. Cada pergunta deve ser enviada à IA com o contexto do mapa para garantir respostas relevantes. | Média | Fase 5 |
| **RF-013** | Autenticação de Usuário | O sistema deve permitir que os usuários criem uma conta e façam login para salvar e acessar seus mapas astrais posteriormente. | Baixa (Pós-MVP) | Fase 6 |

### 3.2. Requisitos Não-Funcionais

| ID | Requisito | Descrição |
| :--- | :--- | :--- |
| **RNF-001** | Desempenho | O tempo de carregamento da página de resultados, incluindo o cálculo do mapa e a primeira interpretação da IA, não deve exceder 10 segundos. As respostas subsequentes no chat devem ser retornadas em menos de 5 segundos. |
| **RNF-002** | Segurança | As chaves de API e outras credenciais devem ser gerenciadas através de variáveis de ambiente e nunca devem ser expostas no código-fonte. O sistema deve empregar as proteções nativas do Django contra ataques comuns (XSS, CSRF, SQL Injection). |
| **RNF-003** | Usabilidade | A interface do usuário deve ser limpa, intuitiva e responsiva, proporcionando uma boa experiência em navegadores de desktop e dispositivos móveis. |
| **RNF-004** | Confiabilidade | O sistema deve ter uma disponibilidade (uptime) de 99.5%. Deve haver tratamento de erros para falhas de comunicação com APIs externas, informando o usuário de maneira clara. |
| **RNF-005** | Precisão | Os cálculos astrológicos devem ser baseados em uma biblioteca de efemérides de alta precisão (ex: Swiss Ephemeris) para garantir a exatidão dos dados do mapa. |
| **RNF-006** | Manutenibilidade | O código-fonte deve ser modular, bem documentado e seguir as convenções de estilo do Python (PEP 8) e as melhores práticas do Django para facilitar futuras manutenções e evoluções. |
| **RNF-007** | Escalabilidade | A arquitetura deve ser projetada para suportar um aumento gradual no número de usuários simultâneos sem degradação significativa do desempenho. |

### 3.3. Requisitos de Interface Externa

#### 3.3.1. Interfaces de Usuário (UI)

O sistema apresentará, no mínimo, as seguintes interfaces:
1.  **Página Inicial:** Contém o formulário de entrada de dados (RF-001).
2.  **Página de Resultados:** Exibe de forma integrada o gráfico do mapa (RF-007), os dados tabulados (RF-008), a interpretação da IA (RF-010) e a interface de chat (RF-012).

#### 3.3.2. Interfaces de Hardware

Não há requisitos específicos de hardware, além da necessidade de um dispositivo cliente (computador, tablet, smartphone) com acesso à internet e um navegador web moderno.

#### 3.3.3. Interfaces de Software (APIs)

1.  **Biblioteca Astrológica (ex: `kerykeion`):** Será utilizada para realizar todos os cálculos de posições de planetas, casas e aspectos. A interface será via chamada de funções/métodos Python.
2.  **API de Geocodificação (ex: Nominatim via `geopy`):** Será utilizada para a tarefa de geocodificação (RF-004). A interface será via requisição HTTP para a API do serviço.
3.  **API do LLM (ex: Gemini, OpenAI):** Será utilizada para gerar as interpretações (RF-009) e responder no chat (RF-012). A interface será via requisição HTTP para a API do provedor.

# Roadmap do Projeto: Mapa Astral AI

Este documento descreve as fases de desenvolvimento para a criação de um sistema de horóscopo e mapa astral com uma assistente de astrologia baseada em IA.

---

## Fase 0: Configuração e Planejamento

O objetivo desta fase é preparar o ambiente de desenvolvimento e definir a arquitetura inicial do projeto.

- **Tarefa 0.1: Configuração do Ambiente**
  - [x] Inicializar o repositório Git.
  - [x] Configurar ambiente virtual Python.
  - [x] Instalar o Django e dependências iniciais.
  - [x] Criar o projeto Django e a primeira `app` (ex: `core` ou `astrologia`).

- **Tarefa 0.2: Definição da Arquitetura e Modelos**
  - [x] Desenhar o Diagrama Entidade-Relacionamento (DER) inicial.
  - [x] Criar o modelo `Pessoa` ou `Cliente` para armazenar os dados de nascimento (nome, data, hora, local).
  - [x] Configurar o banco de dados (SQLite para desenvolvimento, PostgreSQL para produção).
  - [x] Configurar o painel de administração do Django.

---

## Fase 1: MVP - Cálculo de Signo e Horóscopo do Dia

O objetivo é entregar a funcionalidade mais simples e central: permitir que o usuário insira seus dados e descubra seu signo solar, recebendo um horóscopo genérico.

- **Tarefa 1.1: Formulário de Entrada**
  - [x] Criar um `forms.Form` ou `forms.ModelForm` para coletar data, hora e local de nascimento.
  - [x] Desenvolver a `view` principal que renderiza o formulário.
  - [x] Criar o template HTML para a página inicial com o formulário.

- **Tarefa 1.2: Lógica de Astrologia Básica**
  - [x] Implementar uma função ou classe de serviço para determinar o signo solar com base na data de nascimento.
  - [ ] Criar um sistema simples para fornecer um "horóscopo do dia" (pode ser um texto estático por signo, atualizado manualmente ou via uma fonte externa simples).

- **Tarefa 1.3: Página de Resultados**
  - [x] Criar a `view` que processa o formulário, calcula o signo e exibe os resultados.
  - [x] Desenvolver o template HTML para mostrar o signo do usuário e o horóscopo do dia.

---

## Fase 2: Geração do Mapa Astral (Cálculos)

Esta é a fase mais complexa do ponto de vista astrológico. O objetivo é calcular todas as posições planetárias, casas e aspectos do mapa astral do usuário.

- **Tarefa 2.1: Integração com Biblioteca Astrológica**
  - [ ] Pesquisar e escolher uma biblioteca Python para cálculos de efemérides (ex: `kerykeion`, `pyswisseph`).
  - [ ] Adicionar a biblioteca escolhida ao `requirements.txt`.

- **Tarefa 2.2: Serviço de Geocodificação**
  - [ ] Integrar uma biblioteca como `geopy` para converter o local de nascimento (cidade/país) em coordenadas (latitude/longitude).

- **Tarefa 2.3: Serviço de Cálculo do Mapa Astral**
  - [ ] Criar uma classe de serviço que recebe os dados de nascimento (data, hora, lat/lon).
  - [ ] Implementar a função para calcular as posições dos planetas nos signos.
  - [ ] Implementar a função para calcular as cúspides das casas astrológicas (ex: Placidus).
  - [ ] Implementar a função para calcular os principais aspectos (conjunção, oposição, trígono, etc.) entre os planetas.

- **Tarefa 2.4: Armazenamento dos Dados**
  - [ ] Expandir os modelos do Django para armazenar os dados calculados do mapa astral (posições, casas, aspectos) de forma estruturada, associando-os ao `Cliente`.

---

## Fase 3: Visualização do Mapa Astral

O objetivo é criar uma representação gráfica do mapa astral para o usuário.

- **Tarefa 3.1: Geração do Gráfico**
  - [ ] Pesquisar e escolher um método de visualização (ex: `matplotlib` para gerar uma imagem estática, ou uma biblioteca JS como `D3.js` para um gráfico interativo).
  - [ ] Criar um endpoint na API ou uma `view` que gere e sirva a imagem/dados do gráfico do mapa astral.

- **Tarefa 3.2: Integração no Frontend**
  - [ ] Atualizar a página de resultados para exibir o gráfico do mapa astral gerado.
  - [ ] Adicionar uma tabela ou lista com as posições detalhadas (ex: Sol em Áries na Casa 5, Lua em Touro na Casa 7).

---

## Fase 4: Integração com a "Astróloga AI" (Apresentação)

O objetivo é usar um modelo de linguagem (LLM) para gerar uma interpretação textual do mapa astral, atuando como a "Astróloga AI".

- **Tarefa 4.1: Configuração da API da IA**
  - [ ] Escolher um provedor de LLM (Gemini, OpenAI, etc.).
  - [ ] Configurar as chaves de API de forma segura (variáveis de ambiente).
  - [ ] Criar um serviço em Python para se comunicar com a API do LLM.

- **Tarefa 4.2: Engenharia de Prompt**
  - [ ] Desenvolver um prompt detalhado que envie os dados estruturados do mapa astral para a IA.
  - [ ] Instruir a IA no prompt a agir como uma "Astróloga AI", fornecendo uma interpretação clara, positiva e didática sobre os principais pontos do mapa (Sol, Lua, Ascendente, etc.).

- **Tarefa 4.3: Exibição da Interpretação**
  - [ ] Na `view` de resultados, chamar o serviço da IA com os dados do mapa do usuário.
  - [ ] Exibir a interpretação gerada pela IA na página de resultados.
  - [ ] Implementar um sistema de cache para as respostas da IA, evitando chamadas repetidas e custos desnecessários para mapas idênticos.

---

## Fase 5: Interação com a "Astróloga AI" (Chat)

O objetivo é permitir que o usuário "converse" com a Astróloga AI para tirar dúvidas sobre seu mapa.

- **Tarefa 5.1: Interface de Chat**
  - [ ] Desenvolver um componente de chat no frontend (pode usar HTML, CSS e JavaScript simples inicialmente).
  - [ ] Criar um endpoint de API no Django para receber as mensagens do usuário e retornar as respostas da IA.

- **Tarefa 5.2: Lógica de Conversação com Contexto**
  - [ ] Adaptar o serviço da IA para que cada pergunta do usuário seja enviada para o LLM juntamente com o contexto completo do seu mapa astral.
  - [ ] Gerenciar o histórico da conversa na sessão para permitir perguntas de acompanhamento.
  - [ ] Usar AJAX ou WebSockets para uma experiência de chat fluida, sem a necessidade de recarregar a página.

---

## Fase 6: Refinamento e Produção

- [ ] Implementar autenticação de usuários para que possam salvar seus mapas.
- [ ] Escrever testes unitários e de integração.
- [ ] Otimizar a performance e a segurança.
- [ ] Configurar o ambiente de produção (Gunicorn, Nginx, etc.).
- [ ] Realizar o deploy do projeto.
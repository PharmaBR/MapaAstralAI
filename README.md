# Mapa Astral AI

Este é um projeto de aplicação web desenvolvido com Django para gerar horóscopos e mapas astrais personalizados, utilizando uma "Astróloga AI" para interpretações.

## Pré-requisitos

- Python 3.10+
- Gerenciador de pacotes `pip`
- Um ambiente virtual (recomendado)

## Configuração do Ambiente

Siga os passos abaixo para configurar e executar o projeto localmente.

1.  **Clone o repositório** (se aplicável)
    ```bash
    git clone <url-do-repositorio>
    cd mapa_astral
    ```

2.  **Crie e ative um ambiente virtual**
    ```bash
    # No macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # No Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados**
    ```bash
    python manage.py migrate
    ```

5.  **Instale as dependências do Tailwind CSS**
    ```bash
    python manage.py tailwind install
    ```

## Executando a Aplicação com Honcho

Para iniciar o servidor de desenvolvimento e o compilador do Tailwind simultaneamente, execute o seguinte comando no seu terminal:

```bash
honcho start
```

### Acesso à Aplicação

- **Localmente:** Abra seu navegador e acesse `http://127.0.0.1:8000`
- **Na sua rede (LAN):** Encontre o endereço IP da sua máquina (ex: `192.168.1.10`) e acesse `http://<SEU_IP_LOCAL>:8000` de outro dispositivo na mesma rede.

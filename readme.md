# SimpleAgent API


## 📌 Descrição
O **SimpleAgent** é uma API baseada em agentes que utilizam OpenAI e LangChain para processar solicitações de maneira inteligente, direcionando-as para agentes especializados conforme o contexto.

## 🚀 Funcionalidades
- Classifica automaticamente se uma solicitação é de **consulta de CEP** ou **Operações simples**.
- Extrai automaticamente o ID da solicitação sem o uso de expressões regulares.
- Encaminha a solicitação para o agente adequado para processamento.
- Utiliza OpenAI ou Ollama para processamento de linguagem natural.

## 🛠️ Tecnologias Utilizadas
- **Python** (3.12)
- **LangChain**
- **OpenAI API**
- **FastAPI** (caso esteja sendo usado para expor a API)

## 📦 Instalação
Clone o repositório:
```sh
$ git clone https://github.com/edugobatti/simpleAgent.git
$ cd simpleAgent
```

Instale as dependências:
```sh
$ pip install -r requirements.txt
```

## 🚀 Uso
Para iniciar a API, execute:
```sh
$ python main.py
```

A documentação interativa estará disponível em:
```
http://localhost:5000/docs
```

## 📡 Endpoints Principais

### 🔹 Classificação e Encaminhamento
```http
POST /llm
```
**Exemplo de Request:**
```json
{
  "query:":"Quanto é 5+5",
  "llm_model": "ollama"
}
```
**Exemplo de Response:**
```json
{
  "content": "O resultado de 5+5 é 10.",
}
```

## 🛠️ Configuração
Defina suas credenciais da OpenAI no arquivo `.env`:
```env
OPENAI_API_KEY=your_openai_api_key
```


## 📬 Contato
Criado por **Eduardo Faria Gobatti** - [LinkedIn](https://www.linkedin.com/in/eduardo-gobatti-5b8a18188/)


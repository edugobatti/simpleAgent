import os
from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.schema import SystemMessage
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory


#Agents
from src.tools.cep_tool import consultaCEP
from src.tools.operation_tool import ferramenta_generica



class LangChainAgentOllama:
    def __init__(self):
        # Configuração do modelo Ollama
        self.chat = ChatOllama(model=os.environ["OLLAMA_MODEL"], temperature=0, base_url="http://localhost:11434")

        # Definição do prompt
        self.prompt = ChatPromptTemplate(
            messages=[
                SystemMessage(content=(
                    "Você é um sistema de múltiplas tools.\n"
                    "Não deve responder nada fora das suas tools."
                )),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad")
            ]
        )

        # Configuração da memória
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        # Definição das ferramentas disponíveis
        self.tools = [consultaCEP, ferramenta_generica]

        # Criação do agente usando Ollama
        self.agent_executor = initialize_agent(
            tools=self.tools,
            llm=self.chat,
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,  # Agente compatível com Ollama
            verbose=True,
            memory=self.memory
        )

    def run_query(self, query: str):
        """
        Executa uma consulta no agente LangChain e retorna a resposta.
        :param query: A consulta do usuário (string).
        :return: A resposta gerada pelo agente.
        """
        try:
            response = self.agent_executor.invoke({"input": query})
            return response["output"]
        except Exception as e:
            raise RuntimeError(f"Erro ao processar a consulta: {str(e)}")

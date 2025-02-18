import os
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from langchain.memory import ConversationBufferMemory

# Importação das tools personalizadas
from src.tools.cep_tool import tool_cep
from src.tools.operation_tool import tool_calculo

# Agent simples do langchain usando servidor local openai
class LangChainAgentOpenai:
    def __init__(self):
        # Configuração do modelo OpenAI
        self.chat = ChatOpenAI(
            model=os.environ["MODEL_OPENAI"], # precisa substituir no .env
            temperature=0,
            openai_api_key=os.environ["OPENAI_API_KEY"] # precisa substituir no .env
        )

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
        self.tools = [
            tool_calculo,
            tool_cep
        ]

        # Criação do agente usando OpenAIFunctionsAgent
        self.agent = OpenAIFunctionsAgent(
            llm=self.chat,
            prompt=self.prompt,
            tools=self.tools
        )

        # Executor do agente
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            verbose=True,
            tools=self.tools,
            memory=self.memory
        )

    def run_query(self, query: str):
        """
        Executa uma consulta no agente LangChain e retorna a resposta.
        :param query: A consulta do usuário (string).
        :return: A resposta gerada pelo agente.
        """
        try:
            response = self.agent_executor.run(input=query)
            return response
        except Exception as e:
            raise RuntimeError(f"Erro ao processar a consulta: {str(e)}")
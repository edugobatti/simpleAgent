# Função genérica para realizar operações
from langchain.tools import StructuredTool
from pydantic import BaseModel, Field
from src.workers.operation import operacao_generica

# Definição do esquema de argumentos para a ferramenta genérica
class OperacaoArgsSchema(BaseModel):
    operacao: str = Field(..., description="Operação a ser realizada (ex.: soma, subtracao, multiplicacao, divisao)")
    num1: float = Field(..., description="Primeiro número")
    num2: float = Field(..., description="Segundo número")

# Tools de calculo basico de CEP 
tool_calculo = StructuredTool.from_function(
    name="Ferramenta Genérica",
    description="Você é uma ferramenta responsável por realizar operações matemáticas básicas.",
    func=operacao_generica,
    args_schema=OperacaoArgsSchema
)

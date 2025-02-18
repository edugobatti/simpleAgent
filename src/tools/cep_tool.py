from langchain.tools import StructuredTool
from pydantic import BaseModel
from src.workers.consulta_cep import consulta_cep


class ConsultaArgsSchema(BaseModel):
    cep: str


consultaCEP = StructuredTool.from_function(
    name="Consulta base",
    description="Voce é um agent de consulta de CEP o usuario irá passar um conjunto numerico de 8 digitos, o mesmo tem que estar no formato 00000000",
    func=consulta_cep,
    args_schema=ConsultaArgsSchema
)

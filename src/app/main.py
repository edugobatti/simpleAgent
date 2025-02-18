import os
import sys
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import threading

from src.agents.agent_ollama import LangChainAgentOllama
from src.agents.agent_openai import LangChainAgentOpenai
# Instancia a classe
agentOllama = LangChainAgentOllama()
agentOpenai = LangChainAgentOpenai()

app = FastAPI()


@app.get("/")
async def service():
    return "live"


class SolicitationRequest(BaseModel):
    query: str
    llm_model: str


@app.post("/llm")
async def generate(request: SolicitationRequest):
    try:
        if request.llm_model == "ollama":
            response_llm = agentOllama.run_query(request.query)
        elif request.llm_model == "openai":
            response_llm = agentOpenai.run_query(request.query)

        return {'content': response_llm}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Função para iniciar o Streamlit
def start_streamlit():
    streamlit_command = ["streamlit", "run", "./src/playground/playground.py"]
    subprocess.Popen(streamlit_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# Iniciar a API e o Streamlit
if __name__ == "__main__":
    # Inicia o Streamlit em uma thread separada
    streamlit_thread = threading.Thread(target=start_streamlit, daemon=True)
    streamlit_thread.start()

    # Inicia a API FastAPI
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
import json
import re

# Node Receptor: receives the question and checks if it's mathematical
class Receptor:
    def __init__(self):
        self.professor = ProfessorVirtual()

    def receber_pergunta(self, pergunta):
        if self._eh_pergunta_matematica(pergunta):
            mensagem = json.dumps({"tipo": "pergunta", "conteudo": pergunta})
            return self.professor.responder_pergunta(mensagem)
        else:
            return json.dumps({"erro": "Pergunta inválida. Envie uma questão matemática."}, indent=4, ensure_ascii=False)

    def _eh_pergunta_matematica(self, pergunta):
        return bool(re.search(r"\d+[\+\-\*/]\d+", pergunta))  # Looks for expressions like "2+2"

# Node Professor Virtual: processes the question and responds
class ProfessorVirtual:
    def responder_pergunta(self, mensagem_json):
        mensagem = json.loads(mensagem_json)
        if mensagem["tipo"] == "pergunta":
            try:
                resposta = eval(mensagem["conteudo"])  # Evaluates the mathematical expression
                return json.dumps({"resposta": resposta})
            except Exception:
                return json.dumps({"erro": "Erro ao processar a pergunta."})
        return json.dumps({"erro": "Mensagem inválida."})

# Testing the system
if __name__ == "__main__":
    receptor = Receptor()

    # Test with a mathematical question
    pergunta1 = "5+3"
    resposta1 = receptor.receber_pergunta(pergunta1)
    print("Pergunta:", pergunta1)
    print("Resposta:", resposta1)

    # Test with an invalid question
    pergunta2 = "Qual é a capital do Brasil?"
    resposta2 = receptor.receber_pergunta(pergunta2)
    print("\nPergunta:", pergunta2)
    print("Resposta:", resposta2)

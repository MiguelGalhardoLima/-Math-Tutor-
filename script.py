import json
import re

# Receiver Node: receives the question and checks if it's mathematical
class Receptor:
    def __init__(self):
        self.professor = ProfessorVirtual()

    def receber_pergunta(self, pergunta):
        # Checks if the question is mathematical
        if self._eh_pergunta_matematica(pergunta):
            # Sends the valid question to the Virtual Professor
            mensagem = json.dumps({"tipo": "pergunta", "conteudo": pergunta})
            return self.professor.responder_pergunta(mensagem)
        else:
            # Returns an error message if the question is not mathematical
            return json.dumps({"erro": "Pergunta inválida. Envie uma questão matemática."}, indent=4, ensure_ascii=False)

    def _eh_pergunta_matematica(self, pergunta):
        # Looks for mathematical expressions like "2+2"
        return bool(re.search(r"\d+[\+\-\*/]\d+", pergunta))

# Virtual Professor Node: processes the question and provides an answer
class ProfessorVirtual:
    def responder_pergunta(self, mensagem_json):
        # Loads the question from JSON format
        mensagem = json.loads(mensagem_json)
        
        if mensagem["tipo"] == "pergunta":
            try:
                # Tries to evaluate the mathematical expression
                resposta = eval(mensagem["conteudo"])
                return json.dumps({"resposta": resposta})
            except Exception:
                # If there's an error in processing, returns an error message
                return json.dumps({"erro": "Erro ao processar a pergunta."})
        
        # If the message is invalid, return an error
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

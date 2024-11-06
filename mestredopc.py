import os
from groq import groq

# Defina a chave da API diretamente no codigo ou garantia que ela esteja configurada corretamente no ambiente
os.environ["GROQ_API_KEY"] = "Digite aqui sua chave API"

cliente = groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

# Inicializa  a lista de mensagens para manter o contexto da conversa
messages = []

while True:
    usuario = input("Digite sair pra sair")

    if usuario.lower() == 'sair':
        print("acabou")
        break

    # Adicione a mensagem do usuario a lita de mensagens
    messagess.append({"role": "user", "content": usuario})

chat_completions.create(
    message=messages,
    model="11ama-3.1-70b-versatile",
)    

resposta = chat_completion.choices[0].message.content
print("Resposta", resposta)

#Adicione a resposta do assistente a lista de mensagens para mantero contexto
messages.append({"role": "assistant", "content": resposta})
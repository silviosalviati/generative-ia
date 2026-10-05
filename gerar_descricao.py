import sys
from pathlib import Path
from llama_cpp import Llama

# Procura o modelo GGUF local reconstruído
LOCAL_MODEL = Path("modelo_gguf") / "qwen2.5-1.5b-instruct-q4_k_m.gguf"

if not LOCAL_MODEL.exists():
    print(f"Erro: Modelo não encontrado em '{LOCAL_MODEL}'.")
    print("Execute primeiro: python reconstruir_gguf.py")
    sys.exit(1)

nome_app = input("Nome do aplicativo: ") if len(sys.argv) < 2 else sys.argv[1]
detalhes = input("Explique brevemente o que o app faz: ") if len(sys.argv) < 3 else sys.argv[2]

print("\nCarregando modelo Qwen 2.5 1.5B (GGUF Quantizado)...")
llm = Llama(
    model_path=str(LOCAL_MODEL),
    n_ctx=2048,
    verbose=False,
)

messages = [
    {"role": "system", "content": "Você é um redator de produto. Responda sempre em português do Brasil."},
    {
        "role": "user",
        "content": (
            f"Aplicativo: {nome_app}\nDetalhes: {detalhes}\n\n"
            "Escreva uma 'Descrição' (2 a 3 parágrafos) e um 'Objetivo' (1 parágrafo) para este aplicativo."
        ),
    },
]

print("Gerando texto...\n")
response = llm.create_chat_completion(
    messages=messages,
    max_tokens=512,
    temperature=0.7,
    top_p=0.9,
)

print(response["choices"][0]["message"]["content"])


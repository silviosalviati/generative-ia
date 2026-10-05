# 🚀 Generative IA - Gerador Offline de Descrição e Objetivos (Qwen 2.5 1.5B GGUF)

Este projeto executa uma LLM (**Qwen 2.5 1.5B Instruct**) de forma **100% local e offline**, ideal para ambientes corporativos com restrições de rede (*air-gapped*), garantindo privacidade total dos dados.

---

## 📋 Passo a Passo para Executar no Trabalho

### 0. Clonar o Repositório e Entrar na Pasta

Abra o terminal (PowerShell ou Prompt de Comando) e execute:

```powershell
git clone https://github.com/silviosalviati/generative-ia.git
cd generative-ia
```

---

### 1. Criar e Ativar o Ambiente Virtual Python

Abra o terminal (PowerShell ou Prompt de Comando) na pasta do projeto e rode:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

> **Dica:** Se o PowerShell bloquear a ativação de scripts, use:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```

---

### 2. Instalar as Dependências

Com o ambiente virtual ativado:

```powershell
pip install -r requirements.txt
```

*(Instala o `llama-cpp-python` pré-compilado para CPU e utilitários sem precisar de compilador C++).*

---

### 3. Reconstruir o Modelo LLM

Como os arquivos de IA são pesados, os pesos foram fatiados em partes de ~85 MB para transitar pelo Git.  
Para juntar as partes e recriar o arquivo `.gguf` original (~1 GB), execute:

```powershell
python reconstruir_gguf.py
```

> ⏱️ Esse processo leva menos de 5 segundos e criará a pasta `modelo_gguf/` com o modelo consolidado.

---

### 4. Gerar Descrição e Objetivo do Aplicativo

Agora é só rodar o gerador! Você pode usar de duas formas:

#### Opção A: Passando os argumentos direto na linha de comando
```powershell
python gerar_descricao.py "NomeDoApp" "Breve explicação do que o app faz"
```

*Exemplo:*
```powershell
python gerar_descricao.py "Roadmap Estratégico" "Painel web que centraliza as principais iniciativas da diretoria financeira."
```

#### Opção B: Modo interativo
```powershell
python gerar_descricao.py
```
*(O script perguntará o nome do app e a explicação interativamente no terminal).*

---

## 🔒 Privacidade e Segurança dos Dados
- **Sem tráfego de rede:** O script não faz nenhuma requisição externa durante a inferência.
- **On-Premises / Local:** Os dados que você digitar nunca saem da memória RAM da sua máquina.
- **Conformidade:** Totalmente aderente às políticas de segurança corporativa e LGPD.

from pathlib import Path
from huggingface_hub import hf_hub_download

REPO_ID = "Qwen/Qwen2.5-1.5B-Instruct-GGUF"
FILENAME = "qwen2.5-1.5b-instruct-q4_k_m.gguf"
PARTS_DIR = Path("modelo_gguf_partes")
CHUNK_SIZE_MB = 85
CHUNK_SIZE_BYTES = CHUNK_SIZE_MB * 1024 * 1024

print("=== 1. Baixando/localizando o arquivo GGUF (apenas ~986 MB) ===")
cached_path = hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
source_file = Path(cached_path)
total_size_mb = source_file.stat().st_size / (1024 * 1024)
print(f"Arquivo de origem: {source_file.name} ({total_size_mb:.1f} MB)")

PARTS_DIR.mkdir(exist_ok=True)

# Limpa partes antigas caso existam
for f in PARTS_DIR.glob(f"{FILENAME}.part*"):
    f.unlink()

print(f"\n=== 2. Fatiando em blocos de {CHUNK_SIZE_MB} MB para o GitHub ===")
part_num = 0
with open(source_file, "rb") as f_in:
    while True:
        chunk = f_in.read(CHUNK_SIZE_BYTES)
        if not chunk:
            break
        part_file = PARTS_DIR / f"{FILENAME}.part{part_num:03d}"
        with open(part_file, "wb") as f_out:
            f_out.write(chunk)
        print(f"  -> Criada parte: {part_file.name} ({len(chunk) / (1024 * 1024):.1f} MB)")
        part_num += 1

print(f"\nPronto! Foram geradas {part_num} partes (total ~986 MB).")
print(f"Arquivos salvos em: '{PARTS_DIR.resolve()}' prontos para o Git.")

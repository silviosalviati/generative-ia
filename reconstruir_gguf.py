import shutil
from pathlib import Path

PARTS_DIR = Path("modelo_gguf_partes")
OUTPUT_DIR = Path("modelo_gguf")
FILENAME = "qwen2.5-1.5b-instruct-q4_k_m.gguf"

def reconstruir():
    if not PARTS_DIR.exists():
        print(f"Erro: Pasta '{PARTS_DIR}' nao encontrada.")
        return

    OUTPUT_DIR.mkdir(exist_ok=True)
    target_file = OUTPUT_DIR / FILENAME

    parts = sorted(PARTS_DIR.glob(f"{FILENAME}.part*"))
    if not parts:
        print(f"Erro: Nenhuma parte encontrada em '{PARTS_DIR}'.")
        return

    print(f"=== Reconstruindo '{FILENAME}' a partir de {len(parts)} partes ===")
    with open(target_file, "wb") as f_out:
        for p in parts:
            print(f"  Anexando {p.name}...")
            with open(p, "rb") as f_in:
                shutil.copyfileobj(f_in, f_out)

    size_mb = target_file.stat().st_size / (1024 * 1024)
    print(f"\nSucesso! Modelo reconstruido em: {target_file.resolve()} ({size_mb:.1f} MB)")

if __name__ == "__main__":
    reconstruir()

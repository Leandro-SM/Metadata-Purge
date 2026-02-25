import os
import sys
import hashlib
from PIL import Image

# ================== CORES ==================
GREEN = "\033[92m"
PURPLE = "\033[95m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

ASCII = f"""{PURPLE}
███╗   ███╗███████╗████████╗ █████╗ ██████╗ ██╗   ██╗██████╗  ██████╗ ███████╗
████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║   ██║██╔══██╗██╔════╝ ██╔════╝
██╔████╔██║█████╗     ██║   ███████║██████╔╝██║   ██║██████╔╝██║  ███╗█████╗
██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██╔═══╝ ██║   ██║██╔══██╗██║   ██║██╔══╝
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
{GREEN}              Exclusão de Metadados em Lote - Termux Edition
{CYAN}                     Desenvolvido por: @leandro-sm
{RESET}
"""

# Funções

def clear():
    os.system("clear")

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def remove_metadata(image_path):
    try:
        original_hash = sha256_file(image_path)

        img = Image.open(image_path)
        data = list(img.getdata())

        clean_img = Image.new(img.mode, img.size)
        clean_img.putdata(data)

        clean_img.save(image_path)

        new_hash = sha256_file(image_path)

        print(f"{GREEN}[✔] Sanitizado:{RESET} {image_path}")
        print(f"{CYAN}    Hash Antes:{RESET} {original_hash}")
        print(f"{CYAN}    Hash Depois:{RESET} {new_hash}\n")

        return True

    except Exception as e:
        print(f"{RED}[!] Erro em {image_path}: {e}{RESET}")
        return False

def process_directory(path, recursive):
    total = 0
    success = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.bmp')):
                total += 1
                full_path = os.path.join(root, file)
                if remove_metadata(full_path):
                    success += 1

        if not recursive:
            break

    print(f"\n{PURPLE}Resumo:{RESET}")
    print(f"{GREEN}Arquivos encontrados: {total}")
    print(f"Arquivos sanitizados: {success}{RESET}\n")

# Menu

def menu():
    while True:
        print(GREEN + "Escolha uma opção:\n" + RESET)
        print("[1] Limpar uma pasta específica")
        print("[2] Limpar Metadados de todas as Subpastas")
        print("[3] Limpar armazenamento Android (Exclui todos os metadados))\n")
        print(RED + "[4] Sair\n")

        choice = input(PURPLE + ">>> " + RESET)

        if choice == "1":
            path = input(GREEN + "Digite o caminho da pasta: " + RESET)
            if os.path.isdir(path):
                process_directory(path, recursive=False)
            else:
                print(RED + "Caminho inválido.\n" + RESET)

        elif choice == "2":
            path = input(GREEN + "Digite o caminho da pasta: " + RESET)
            if os.path.isdir(path):
                process_directory(path, recursive=True)
            else:
                print(RED + "Caminho inválido.\n" + RESET)

        elif choice == "3":
            android_path = "/storage/emulated/0/"
            if os.path.isdir(android_path):
                print(RED + "⚠ Isso pode processar milhares de arquivos!\n" + RESET)
                confirm = input("Deseja continuar? (s/n): ")
                if confirm.lower() == "s":
                    process_directory(android_path, recursive=True)
            else:
                print(RED + "Armazenamento não acessível.\n" + RESET)

        elif choice == "4":
            print(PURPLE + "Encerrando...\n" + RESET)
            sys.exit()

        else:
            print(RED + "Opção inválida.\n" + RESET)

# Main

if __name__ == "__main__":
    clear()
    print(ASCII)
    menu()
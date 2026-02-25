<img width="683" height="457" alt="image" src="https://github.com/user-attachments/assets/06bf4ffb-9349-488d-9815-adddf9ee2e97" />

# Exclusão de Metadados em Lote - Termux (Android)

## Modo de Uso | How to Install

```bash
git clone https://github.com/leandro-sm/metapurge.git 
cd metapurge
pkg install python
pip install -r requirements.txt
python metapurge.py
```

# Acessando arquivos do Armazenamento Interno

Execute:
```bash
termux-setup-storage
```
Permita o acesso do Termux ao seu armazenamento.

### Pasta "Storage" é criada na Home
Ela te dá acesso via Termux ao Shared (Pasta 'Local')
Através dela você tem acesso às pastas comuns do seu armazenamento interno Android. (Android, DCIM, Download, etc.)

Utilize **~/storage/shared/...** para indicar o caminho das pastas e arquvos.

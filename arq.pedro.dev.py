# =========================
# MODOS DE ARQUIVOS EM PYTHON
# x | w | a | r
# =========================

print("=== SISTEMA DE ARQUIVOS ===")

# -------------------------
# MODO X -> cria arquivo novo
# -------------------------

print("\n[1] Criando arquivo com modo X")

arq = open("pedro.txt", "x")

arq.write("Primeira linha do arquivo.\n")

arq.close()

print("Arquivo criado com sucesso!")

# -------------------------
# MODO W -> sobrescreve
# -------------------------

print("\n[2] Escrevendo com modo W")

arq = open("pedro.txt", "w")

arq.write("Texto novo usando W.\n")

arq.close()

print("Texto escrito!")

# -------------------------
# MODO A -> adiciona conteúdo
# -------------------------

print("\n[3] Adicionando texto com modo A")

arq = open("pedro.txt", "a")

arq.write("Nova linha adicionada com A.\n")

arq.close()

print("Texto adicionado!")

# -------------------------
# MODO R -> ler arquivo
# -------------------------

print("\n[4] Lendo arquivo com modo R")

arq = open("pedro.txt", "r")

conteudo = arq.read()

print("\nCONTEÚDO DO ARQUIVO:")
print(conteudo)

arq.close()

print("\nSistema finalizado!")

senha = input("Digite a senha: ")

if senha == "1234":

    arq = open("pedro.txt", "r")

    print(arq.read())

    arq.close()

else:
    print("Senha incorreta!")
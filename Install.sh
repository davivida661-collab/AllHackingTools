#!/bin/bash

# --- Cores Padronizadas (usando \033 por ser mais universal em scripts bash) ---
# A ideia é ter um conjunto único e bem definido
GREEN="\033[1;32m"
RED="\033[1;31m"
BLUE="\033[1;34m"
YELLOW="\033[1;33m"
ORANGE="\033[38;5;208m" # Um laranja mais vibrante
RESET="\033[0m"

clear
sleep 1.5
echo -e "$RESET" # Garante que o terminal comece com cores padrão

echo -e "${GREEN}Iniciando configuração do ambiente AllHackingTools...${RESET}"

# --- Instalação de Pacotes Essenciais ---
install_package() {
    PACKAGE=$1
    echo -e "${YELLOW}Verificando e instalando $PACKAGE...${RESET}"
    if ! dpkg -s "$PACKAGE" >/dev/null 2>&1; then
        sudo apt update >/dev/null 2>&1 && sudo apt install -y "$PACKAGE"
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}$PACKAGE instalado com sucesso!${RESET}"
        else
            echo -e "${RED}Falha ao instalar $PACKAGE. Por favor, verifique sua conexão ou repositórios.${RESET}"
            exit 1
        fi
    else
        echo -e "${BLUE}$PACKAGE já está instalado.${RESET}"
    fi
}

install_python_dependency() {
    PYTHON_EXEC=$1 # python3 ou python2
    PACKAGE=$2
    echo -e "${YELLOW}Verificando e instalando dependência Python ($PACKAGE para $PYTHON_EXEC)...${RESET}"
    if ! $PYTHON_EXEC -c "import $PACKAGE" >/dev/null 2>&1; then
        $PYTHON_EXEC -m pip install "$PACKAGE"
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}$PACKAGE ($PYTHON_EXEC) instalado com sucesso!${RESET}"
        else
            echo -e "${RED}Falha ao instalar $PACKAGE ($PYTHON_EXEC).${RESET}"
            exit 1
        fi
    else
        echo -e "${BLUE}$PACKAGE ($PYTHON_EXEC) já está instalado.${RESET}"
    fi
}

# Foca em Python 3 para o MainMenu, mas mantém Python 2 se os scripts internos ainda precisarem
install_package "python3"
install_package "python3-pip"
install_package "python2" # Mantém por enquanto, se os sub-scripts ainda forem Python 2
install_package "python-is-python2" # Garante que 'python' aponte para python2, se necessário

# Instalação das dependências Python
install_python_dependency "python3" "requests"
install_python_dependency "python2" "requests" # Para scripts antigos que ainda rodam em python2

# Navega para o diretório correto
TARGET_DIR="$HOME/AllHackingTools"
echo -e "${YELLOW}Navegando para o diretório: $TARGET_DIR${RESET}"
if [ ! -d "$TARGET_DIR" ]; then
    echo -e "${RED}Diretório $TARGET_DIR não encontrado. Por favor, clone o repositório primeiro.${RESET}"
    exit 1
fi
cd "$TARGET_DIR" || exit 1

echo -e "${GREEN}Ambiente AllHackingTools configurado!${RESET}"
echo -e "${BLUE}Iniciando InstallMenu (ainda em Python 2, para compatibilidade inicial)...${RESET}"

# Executa o InstallMenu.py (considerando que ele ainda é Python 2 e pode ter sua própria lógica de instalação)
python2 src/InstallMenu.py

echo -e "${GREEN}Pronto para executar o MainMenu.py modernizado (em Python 3)!${RESET}"
# Aqui você chamaria o seu MainMenu.py já em Python 3
# python3 MainMenu.py

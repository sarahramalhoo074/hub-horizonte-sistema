
# Funções auxiliares para formatação e processamento de dados

import re

def limpar_numero(texto):
    """Remove caracteres não numéricos"""
    if not texto:
        return ""
    return re.sub(r'\D', '', str(texto))

def formatar_cnpj(cnpj):
    """Configuração de CNPJ: XX.XXX.XXX/XXXX-XX"""
    n = limpar_numero(cnpj)
    if len(n) == 14:
        return f"{n[:2]}.{n[2:5]}.{n[5:8]}/{n[8:12]}-{n[12:14]}"
    return cnpj if cnpj else "Não informado"

def formatar_cpf(cpf):
    """Configuração de CPF: XXX.XXX.XXX-XX"""
    n = limpar_numero(cpf)
    if len(n) == 11:
        return f"{n[:3]}.{n[3:6]}.{n[6:9]}-{n[9:11]}"
    return cpf if cpf else "Não informado"

def formatar_telefone(tel):
    """Configuração de telefone"""
    n = limpar_numero(tel)
    if len(n) == 11:  # Telemóvel com 9
        return f"({n[:2]}) {n[2:7]}-{n[7:]}"
    elif len(n) == 10:  # Fixo
        return f"({n[:2]}) {n[2:6]}-{n[6:]}"
    return tel if tel else "Não informado"

def formatar_moeda(valor):
    """Formatação do padrão monetário R$."""
    if not valor:
        return "R$ 0,00"
    num = re.sub(r'[^\d,]', '', str(valor))
    if ',' not in num:
        num += ",00"
    return f"R$ {num}"
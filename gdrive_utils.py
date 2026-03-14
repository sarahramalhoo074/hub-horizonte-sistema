# gdrive_utils.py
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import streamlit as st
from Perguntas import GDRIVE_CONFIG

def get_gdrive_service( ):
    """Autentica e retorna o serviço do Google Drive."""
    creds = None
    # O arquivo token.pickle armazena o login para não precisar logar toda hora
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                GDRIVE_CONFIG['client_secret.json'], 
                [
                    'https://www.googleapis.com/auth/drive',
                    'https://www.googleapis.com/auth/spreadsheets',
                    'https://www.googleapis.com/auth/calendar'
                ]
            )
            creds = flow.run_local_server(port=0)
        
        # Salva as credenciais para a próxima vez
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
            
    return build('drive', 'v3', credentials=creds)

def gerir_pasta_empresa(nome_empresa, cnpj, id_mae):
    """Cria ou localiza a pasta da empresa (Nome - CNPJ) no Drive."""
    service = get_gdrive_service()
    nome_pasta = f"{nome_empresa} - {cnpj}"
    
    # Procura se a pasta já existe
    query = f"name = '{nome_pasta}' and '{id_mae}' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    
    try:
        resultado = service.files().list(q=query).execute()
        pastas = resultado.get('files', [])
        
        if pastas:
            return pastas[0]['id']
        else:
            # Se não existir, cria a pasta
            file_metadata = {
                'name': nome_pasta, 
                'parents': [id_mae], 
                'mimeType': 'application/vnd.google-apps.folder'
            }
            nova_pasta = service.files().create(body=file_metadata, fields='id').execute()
            return nova_pasta.get('id')
    except Exception as e:
        st.error(f"Erro ao acessar o Google Drive: {e}")
        return None

def upload_arquivo(caminho_arquivo, id_destino):
    """Faz o upload de um arquivo para uma pasta específica do Drive."""
    service = get_gdrive_service()
    nome_arquivo = os.path.basename(caminho_arquivo)
    
    file_metadata = {'name': nome_arquivo, 'parents': [id_destino]}
    media = MediaFileUpload(caminho_arquivo, mimetype='application/pdf')
    
    try:
        service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return True
    except Exception as e:
        st.error(f"Erro no upload: {e}")
        return False

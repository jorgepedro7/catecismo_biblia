import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase
import streamlit as st
import os
from dotenv import load_dotenv

# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializando o Firebase Admin SDK com as credenciais do arquivo JSON
if not firebase_admin._apps:
    # Obtenha a chave privada e converta os caracteres escapados para linhas reais
    private_key = os.getenv("FIREBASE_PRIVATE_KEY")

    # Construa o dicionário de credenciais
    firebase_credentials = {
        "type": "service_account",
        "project_id": os.getenv("FIREBASE_PROJECT_ID"),
        "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
        "private_key": private_key.replace("\\n", "\n"),
        "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
        "client_id": os.getenv("FIREBASE_CLIENT_ID"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-a7xzn%40leitura-catecismo-biblia.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }
cred = credentials.Certificate(firebase_credentials)
firebase_admin.initialize_app(cred)

# Inicializando o Firestore para manipular o banco de dados
db = firestore.client()

# Configuração do Pyrebase para autenticação
firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL")
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

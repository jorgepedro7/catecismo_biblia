import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase
import streamlit as st
import os
from dotenv import load_dotenv

# Verifica o ambiente: local ou Streamlit Cloud
if os.getenv("STREAMLIT_CLOUD") is None:
    # Ambiente local: carrega variáveis do .env
    load_dotenv()
    get_env = os.getenv
else:
    # Ambiente no Streamlit Cloud: usa st.secrets
    get_env = lambda key: st.secrets["firebase"][key]

# Inicializando o Firebase Admin SDK com as credenciais do arquivo JSON
if not firebase_admin._apps:
    # Obtenha a chave privada e converta os caracteres escapados para linhas reais
    private_key = get_env("FIREBASE_PRIVATE_KEY").replace("\\n", "\n")

    # Construa o dicionário de credenciais
    firebase_credentials = {
        "type": "service_account",
        "project_id": get_env("FIREBASE_PROJECT_ID"),
        "private_key_id": get_env("FIREBASE_PRIVATE_KEY_ID"),
        "private_key": private_key,
        "client_email": get_env("FIREBASE_CLIENT_EMAIL"),
        "client_id": get_env("FIREBASE_CLIENT_ID"),
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
    "apiKey": get_env("FIREBASE_API_KEY"),
    "authDomain": get_env("FIREBASE_AUTH_DOMAIN"),
    "projectId": get_env("FIREBASE_PROJECT_ID"),
    "storageBucket": get_env("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": get_env("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": get_env("FIREBASE_APP_ID"),
    "databaseURL": get_env("FIREBASE_DATABASE_URL")
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

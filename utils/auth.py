import pyrebase
from firebase_config import firebase_config

# Inicializando o Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def autenticar_usuario(email, senha):
    """
    Autentica o usuário com o Firebase Authentication.
    """
    try:
        user = auth.sign_in_with_email_and_password(email, senha)
        return user
    except Exception as e:
        print(f"Erro ao autenticar: {e}")
        return None

def criar_usuario(email, senha):
    """
    Cria um novo usuário no Firebase Authentication.
    """
    try:
        user = auth.create_user_with_email_and_password(email, senha)
        return user
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        return None

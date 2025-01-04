from firebase_config import db
import json

COLECAO_PROGRESSO = "progresso"

def carregar_leituras():
    try:
        with open('data/leitura.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def carregar_progresso(usuario_id):
    doc_ref = db.collection(COLECAO_PROGRESSO).document(usuario_id)
    try:
        doc = doc_ref.get()
        return doc.to_dict() if doc.exists else {"dias_lidos": []}
    except Exception as e:
        print(f"Erro ao carregar progresso: {e}")
        return {"dias_lidos": []}

def salvar_progresso(usuario_id, progresso):
    try:
        db.collection(COLECAO_PROGRESSO).document(usuario_id).set(progresso)
    except Exception as e:
        print(f"Erro ao salvar progresso: {e}")

def marcar_dia_lido(usuario_id, dia):
    progresso = carregar_progresso(usuario_id)
    if dia not in progresso["dias_lidos"]:
        progresso["dias_lidos"].append(dia)
        salvar_progresso(usuario_id, progresso)

def resetar_progresso(usuario_id):
    try:
        db.collection(COLECAO_PROGRESSO).document(usuario_id).set({"dias_lidos": []})
        return True
    except Exception as e:
        print(f"Erro ao resetar progresso: {e}")
        return False

def buscar_leitura(dia):
    leituras = carregar_leituras()
    return next((l for l in leituras if l['Data'] == dia), None)

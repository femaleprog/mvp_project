import json

def load_data(uploaded_file):
    data = json.load(uploaded_file)
    return data
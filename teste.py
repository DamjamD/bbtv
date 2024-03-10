import pandas as pd

def normalize_and_save(data, filename):
    
    df = pd.DataFrame(data)
    
    
    df.to_csv(filename, index=False)

# Dados de exemplo
data = {'City': ['Fredericton'],
        'State': ['New Brunswick'],
        'Latitude': [45.9635895],
        'Longitude': [-66.6431153]}


filename = 'localizacao.csv'


print(data) #normalize_and_save(data, filename)

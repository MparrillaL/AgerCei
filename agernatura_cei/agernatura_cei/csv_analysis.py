import os
import pandas as pd
import matplotlib.pyplot as plt

script_directory = os.path.dirname(os.path.abspath(__file__))
csv_file = "medidas.csv"
path_file = os.path.join(script_directory, csv_file)
df = pd.read_csv(csv_file)

df["activity"] = df["activity"].replace("LIGERA", "poco activo")
df["activity"] = df["activity"].replace("MODERADA", "activo con moderacion")

dfs_by_name = {}
for name, group in df.groupby('name'):
    if len(group['date']) > 1:
        dfs_by_name[name] = group


image_directory = "/Images"
os.makedirs(image_directory, exist_ok=True)

for name, person_df in dfs_by_name.items():
    plt.figure(figsize=(10, 6))
    plt.plot(person_df['date'], person_df['weight'], marker='o', linestyle='-', label=f'Peso de {name}')
    plt.title(f'Evolución del Peso para {name}')
    plt.xlabel('Fecha')
    plt.ylabel('Peso')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    name_graph = f"{name}_evolucion_peso.png"
    path_graph = os.path.join(image_directory, name_graph)
    plt.savefig(path_graph)
    print(f"Guardado gráfico para la evolución del peso de {name} como {name_graph} en {image_directory}")

    plt.show()

df.to_csv(path_file, index=False)
print(f"Cambios guardados en {csv_file}")

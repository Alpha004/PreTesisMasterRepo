import pandas as pd

datasets = []
for i in range(1, 16):
    name_index = f'00{i}' if i<10 else f'0{i}'
    datasets.append(pd.read_csv(f'{name_index}_dataset.csv'))

# Combinar los DataFrames
combined_df = pd.concat(datasets, ignore_index=True)

# Guardar en un archivo CSV
combined_df.to_csv('main_dataset.csv', index=False)
print('Combinacion finalizada!')
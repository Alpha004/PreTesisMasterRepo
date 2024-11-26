import pandas as pd

datasets = []
for i in range(1, 16):
    name_index = f'00{i}' if i<10 else f'0{i}'
    datasets.append(pd.read_csv(f'{name_index}_dataset.csv'))

# Combinar los DataFrames
combined_df = pd.concat(datasets, ignore_index=True)
# Retiramos las columnas de glucosa -- COMENTAR ESTA LINEA EN CASO SE QUIERA VALIDAR EL VALOR REAL DE GLUCOSA
combined_df = combined_df.drop(columns=['glucose','glucose_24h_mean'])
# Guardar en un archivo CSV
combined_df.to_csv('main_dataset_without_glucose.csv', index=False)
# combined_df.to_csv('main_dataset.csv', index=False)
print('Combinacion finalizada!')
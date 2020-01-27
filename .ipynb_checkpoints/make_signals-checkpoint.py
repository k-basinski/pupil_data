import numpy as np
import pandas as pd
import sys

# tu powinieneś sprawdzić argumenty - [1] to nazwa pliku, [2] to sub_id

# przeczytaj
tdf = pd.read_csv(sys.argv[1])

# wyciągnij dobre kolumny
df = tdf.loc[:, ['pupil_timestamp', 'diameter', 'confidence', 'eye_id']]

# dorzuć sub_id 
df.loc[:, 'sub_id'] = sys.argv[2]

# dołóż dobry czas
start_time = df['pupil_timestamp'][0]
df.loc[:, 'time'] = df['pupil_timestamp'] - start_time

# określ warunki
df['condition'] = 'recovery'
df.loc[df['time'] < 4*60, 'condition'] = 'test'
df.loc[df['time'] < 2*60, 'condition'] = 'baseline'

# zapisz do pliku
nazwa_pliku = 'signal_sub_' + sys.argv[2] + '.csv'
df.to_csv(nazwa_pliku, sep=',', index=False)
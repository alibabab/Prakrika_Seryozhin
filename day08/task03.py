import pandas as pd
temps = pd.Series([15, 18, 12], index=["Пн", "Вт", "Ср"])
print(temps["Вт"])
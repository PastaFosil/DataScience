import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('penguins')

sns.displot(df["body_mass_g"])
plt.show()
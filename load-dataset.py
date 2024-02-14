# === [Load libraries] ===
from pandas import read_csv
from matplotlib import pyplot as plts

# === [Load the dataset] ===
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# === [Look at the dataset] ===
# shape
print(dataset.shape)

# head
print(dataset.head(20))

# descriptions = statistical summary
print(dataset.describe())

# class distribution
print(dataset.groupby('class').size())

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()


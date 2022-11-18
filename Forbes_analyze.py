import pandas as pd

df = pd.read_csv("forbes_2022_billionaires.csv")
df.head()

#Data preprocessing

#The understanding stage is where we attempt to explore the data.
# Let's take a look at the shape of dataset with the shape attribute.

df.shape

#As you can see, the dataset has 2668 rows and 22 columns. Let me show you the type of columns with the dtypes attribute.

df.dtypes

#The dataset contained both numerical and categorical values. Let's select the columns I'm going to use in this data analysis with the loc method.

df = df.loc[:,["rank","personName","age","finalWorth","category","country","gender"]]
df.head()

df = df.set_index("rank")
df.head()

df.isnull().sum()

#As you can see, there are missing data in the age, country, and gender columns.
# Since there are not many missing data in these columns, let's remove these missing data with the dropna method.

df.dropna(inplace=True)

#Let's take a look at the general information in the dataset with the info method.

df.info()


#As you can see, the dataset consists of 2568 rows and 6 columns and there is no missing data in the dataset.


#Gender analysis

#Let's examine the gender of billionaires with the value_counts method.

df["gender"].value_counts()

##Most billionaires are men. Let's look at the percentage of men and women
# with the normalize =True parameter.

df["gender"].value_counts(normalize=True)


#As you can see, 89 percent of billionaires are men and 11 percent are women.
# Let's look at the mean ages according to gender. To do this, I'm going to use the groupby method.

df_gender = df.groupby(["gender"])

#Let's calculate the mean ages with the mean method.

df_gender["age"].mean()

#As can be seen, the average age of men is 64, and the average age of women is 63.
# Let's draw a bar plot for the male and female averages. First, let me specify a seaborn theme.

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
sns.set(rc = {"figure.figsize":(12,8), "figure.dpi":300})

#I'm going to use the warnings package to avoid seeing the warning messages.

import warnings
warnings.filterwarnings("ignore")

#Let's draw the bar plot with the plot method.

df_gender.size().plot(kind = "bar")
plt.title('Average ages of men and women', fontsize = 20)
plt.show()

#Top 10 richest

#To see top 10 richest in the world, let me use the barplot method in seaborn.

sns.barplot(y=df["personName"][:10], x = df["finalWorth"][:10])
plt.title('Top 10 richest', fontsize = 20)
plt.show()


#The richest person in the world, Elon Musk, then Jeff Bezos.


#Top 10 countries

#Let's take a look at countries with the most billionaries.
# First, let me calculate how many unique countries there are with the len method.

len(df["country"].unique())

#There are 73 countries in the list. To draw a bar plot of the first ten countries that have the most billionaires, let's group the dataset according to the country column with the groupby method.

df_country = df.groupby("country")

#Let's calculate the number of billionaires by country with the size method,
# and then sort the countries with the most billionaires with sort_values and transform
# this data into a dataframe with the DataFrame method.

df_country_count = pd.DataFrame(
    df_country.size().sort_values(ascending=False), columns=["Count"])
df_country_count.head()

#Now let's draw a bar plot for the first ten countries.

sns.barplot(df_country_count["Count"][:10], df_country_count.index[:10])
plt.title('Top 10 countries', fontsize = 20)
plt.show()

#As you can see, the first country with the most billionaires is the United States,
# followed by China, etc.

#Let me look at unique categories with the unique method.

df["category"].unique()

#Let me remove spaces from the columns and replace & with _ with the replace method.

df["category"]=df["category"].apply(lambda x:x.replace(" ","")).apply(lambda x:x.replace("&","_"))

#Let's look at unique categories with the unique method again.


df["category"].unique()

#Let's find the number of categories. To do this, I'm going to first use the groupby method and then the size method.

df_category = df.groupby("category").size()
df_category.head()

#Let me convert this data into a dataframe.

df_category = df_category.to_frame()
df_category.head()


#Let's name the first column with the rename method and sort the values by the number of categories with the sort_values method.

df_category=df_category.rename(columns = {0:"Count"}).sort_values(by = "Count", ascending=False)
df_category.head()

#Let's draw a bar plot of the first ten columns.

sns.barplot(df_category["Count"][:10], df_category.index[:10])
plt.title('Top 10 categories', fontsize = 20)
plt.show()

#The category that have the most billioneires is finance investments, followed by technology, etc.


#The relationship between money and age

#Let's look at the relationship between money and age with scatterplot method.

sns.scatterplot(df["age"], df["finalWorth"])
plt.title('The relationship between money and age', fontsize = 20)
plt.show()

#As you can see, there is no relationship between age and money.


#The distribution of age

#Let's take a look at the distribution of the age column.

sns.histplot(df["age"])
plt.title('The distribution of age', fontsize = 20)
plt.show()
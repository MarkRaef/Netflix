import pandas as pd
import matplotlib.pyplot as plt
fig = plt.figure()
df = pd.read_csv(r"datasets\color_data.csv",index_col=0)

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

movie_dict = {"years": years, "durations": durations}

print(movie_dict)

durations_df = pd.DataFrame(movie_dict)
print(durations_df)


plt.plot(years, durations)
plt.title("Netflix Movie Durations 2011-2020")
plt.show()

# Read in the CSV as a DataFrame
netflix_df = pd.read_csv(r"datasets\netflix_data.csv",index_col=0)
print(netflix_df.head())

# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]

# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[["title", "country", "genre", "release_year", "duration"]]
print(netflix_movies_col_subset.head())



fig = plt.figure(figsize=(12, 8))
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"])
plt.title("Movie Duration by Year of Release")
plt.show()

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60]
print(short_movies.head(20))

# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for lab, row in netflix_movies_col_subset.iterrows():
    if row['genre'] == "Children":
        colors.append("red")
    elif row['genre'] == "Documentaries":
        colors.append("blue")
    elif row['genre'] == "Stand-Up":
        colors.append('green')
    else:
        colors.append('black')

print(colors[0:10])

plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12, 8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset['duration'], netflix_movies_col_subset['release_year'], c=colors)
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie duration by year of release")
plt.show()
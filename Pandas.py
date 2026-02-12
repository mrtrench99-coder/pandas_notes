import pandas as pd

#DATA FRAMES are 2D labeled data structures with columns of potentially different types.
# Table=pd.DataFrame({'Names' : ['Alice', 'Bob', 'Charlie', 'David'],
#                       'Scores': [85, 92, 78, 90]},index=['A', 'B', 'C', 'D'])
# print(Table)


#SERIES are one-dimensional labeled arrays capable of holding any data type.
# series=pd.Series([10,20,30,30],index=['A','B','C','D'],Name='Numbers')
# print(series)


#Reading data from a CSV file into a DataFrame
# We use CSV files to store tabular data in plain text format, where each line represents 
# a row and columns are separated by commas.
# hence the name Comma Separated Values (CSV).


#BASIC FUNCTIONS FOR DATA FRAMES
# to read a file   wine_reviews = pd.read_csv('filename.csv')
# to check how large the DataFrame is print(wine_reviews.shape)
# to check the first few rows of the DataFrame print(wine_reviews.head())
# to check the last few rows of the DataFrame print(wine_reviews.tail())
# to remove the index column while reading the file wine_reviews = pd.read_csv('filename.csv',index_col=0)
# wine_reviews.head()
# to get a concise summary of the DataFrame print(wine_reviews.info())
# to save a dataframe to a CSV file wine_reviews.to_csv('new_filename.csv')


#ILOC AND LOC 
# to select the first row of the DataFrame print(wine_reviews.iloc[0])
# to get a columns we use wine_reviews.iloc[:, 0]
# to only selct the first 3 rows of the first column we use wine_reviews.iloc[:3, 0]
# difference between loc and iloc is that loc uses labels to select data while iloc uses integer-based indexing.
# example reviews.loc[:,['country','points','price']]
# differnces between the range of loc and iloc is that loc includes the end index while iloc excludes it.


#MANIPULATING DATA FRAMES
# reviews.country=='Italy'  # to filter rows where the country is Italy
# reviews.loc[reviews.country == 'Italy' ]# to get the points for wines from Italy
# reviews.loc[reviews.country == 'Italy', 'points'] # to get the points for wines from Italy

#CONDITIONAL SELECTION
# reviwes.loc[(reviews.country == 'Italy) & ()reviwes.points>=90)] # to get the points for wines from Italy with points
# greater than or equal to 90
# we use | for OR condition and & for AND condition in pandas when filtering data frames.
# we use isin() method to filter rows based on multiple values in a column. For example, reviwes.loc[reviwes.country.isin(['Italy','France])] will return rows where the country is either Italy or France.
# to filter rows, we use reviwes.loc[reviwes.price.notnull()] for non-missing values and reviwes.loc[reviwes.price.isnull()] for missing values


#ASSIGNING NEW COLUMNS
# we can assign by reviwes['critic'] ='everyone' to create a new column called critic with the value 'everyone' for all rows. 
# reviwes['index_backwards'] = range(len(reviwes), 0, -1) to create a new column called index_backwards with a range of numbers counting backwards from the length of the DataFrame to 1.



# reviwes.point.describe() and changes based on the type of date in the coulmn.
# reviwes.points.mean() 
# reviwes.taster_name.unique()
# reviwes.taster_name.value_counts() gives the count of each unique value

#review_points_mean = reviwes.points.mean()
#or
#reviews.points.map(lambda p: p-review_points_mean)
#or
#reviews.points - reviews.points.mean()

# reviews.country + '-' + reviews.region_1
#def remean_points(row):
#     row.points = row.points - review_points_mean
#     return row

# reviews.apply(remean_points, axis='columns')

# def get_stars(row):
#     if row.country == "Canada":
#         return 3
#     elif row.points >= 95:
#         return 3
#     elif row.points >= 85:
#         return 2
#     else:
#         return 1

# star_ratings = reviews.apply(get_stars, axis="columns")

# reviews.groupby('country').points.count() # to count the number of reviews for each country
# reviews.groupby('country').points.min() # to get the minimum points for each country
# reviews.groupby('country').apply(lambda df: df.title.iloc[0]) # to get the title of the first review for each country
# reviews.groupby('[]country','province']).apply(df: df.title.loc[df.points.idxmax()])

# reviews.groupby(['country']).price.agg([len,min,  max]) # agg lets you apply multiple functions at once.
# reviews.reset_index()
# reviews.sort_values(by='len', ascending=False)
# reviews.sort_index()
# reviews.sort_values(by=['country','points'], ascending=[True,False]) # to sort by country in ascending order and points in descending order

#reviews.price.dtype
#reviews.dtypes
#reviews.points.astype('float64')  to convert points from integer to float
#reviews.index.dtype
#reviews[pd.isnull(reviwes.country)] to provide the rows where the country is missing (null values)
#reviews.region_2.fillna("Unknown") to fill out the missing values in the region_2 coulmn with "Unknown"
#reviews.taster_twitter_handle.replace("Mango","Orange") to replace all instances of "Mango" with "Orange" in the taster_twitter_handle column
# to get a count of something.. we can use len or if we want count of true values then we can use sum.

#reviews.rename(columns={'points':'score'}) 
#reviews.rename(index={0 : 'first_review', 1 : 'second_review', 2 : 'third_review'})
#reviews.rename_axis("wines",axis='rows').rename_axis("attributes",axis="columns") to rename the index and columns axis labels.

# canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
#british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")
#pd.concat([canadian_youtube,british_youtube]) to concatenate the two DataFrames vertically (stacking rows)

#left=canadain_youtube.set_index(['title',trending_date'])
#right=britsh_youtube.set_index(['title','trending_date'])
#left.join(right,lsuffix='_CAN',rsuffix='_UK') to join the two DataFrames on the title and trending_date columns, adding suffixes to distinguish between the columns from each DataFrame.
renamed = reviews.rename(columns={'region_1':'region','region_2':'locale'})
reindexed = reviews.rename(index={0: 'wines'})
combined_products = pd.concat([gaming_products,movie_products])

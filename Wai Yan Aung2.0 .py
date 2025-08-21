import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    'month': ['January','February','March','April','May','June','July','August',
              'September','October','November','December'],
    'news_sold': [4174, 4507, 1860, 2294, 2130, 2095, 4772, 4092, 2638, 3169, 1466, 2238]
}

df = pd.DataFrame(data)

# 1. Plot a line graph
plt.figure(figsize=(10,6))
plt.plot(df['month'], df['news_sold'], marker='o', linestyle='-', color='b')
plt.title('News Sold per Month')
plt.xlabel('Month')
plt.ylabel('News Sold')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 2. Add sales_category column
df['sales_category'] = df['news_sold'].apply(lambda x: 'High' if x > 3000 else 'Low')

# 3. Sort DataFrame in descending order of news_sold
sorted_df = df.sort_values(by='news_sold', ascending=False)
print("\nSorted DataFrame:\n", sorted_df)

# 4. Calculate average number of news sold
average_sales = df['news_sold'].mean()
print("\nAverage number of news sold:", average_sales)

# 5. Find month(s) with maximum news sold
max_sales = df['news_sold'].max()
max_months = df[df['news_sold'] == max_sales]['month'].tolist()
print("\nMonth(s) with maximum sales:", max_months)

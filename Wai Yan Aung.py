import pandas as pd
import matplotlib.pyplot as plt

# Example dataset
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'news_sold': [2500, 2700, 3200, 3100, 4000, 4200,
                  3900, 2800, 3600, 3300, 4100, 4500]
}

# Create DataFrame
df = pd.DataFrame(data)

# 1. Plot line graph of news sold per month
plt.plot(df['month'], df['news_sold'], marker='o')
plt.title('Monthly News Sales')
plt.xlabel('Month')
plt.ylabel('News Sold')
plt.grid(True)
plt.show()

# 2. Add sales_category column
df['sales_category'] = df['news_sold'].apply(lambda x: 'High' if x > 3000 else 'Low')

# 3. Sort DataFrame in descending order of news_sold
sorted_df = df.sort_values(by='news_sold', ascending=False)
print("\nSorted DataFrame (Descending order of news_sold):")
print(sorted_df)

# 4. Calculate and print average news sold
average_sales = df['news_sold'].mean()
print("\nAverage news sold across all months:", average_sales)

# 5. Find and display month(s) with maximum news sold
max_sales = df['news_sold'].max()
max_months = df[df['news_sold'] == max_sales]['month'].tolist()
print("\nMonth(s) with maximum news sold:", max_months)

import pandas as pd

# Load dataset
df = pd.read_csv('DataCoSupplyChainDataset.csv', encoding='latin-1')

# Create delay flag (1 = delayed, 0 = on time)
df['delay_flag'] = (df['Days for shipping (real)'] > df['Days for shipment (scheduled)']).astype(int)

# Overall delay rate
total = len(df)
delayed = df['delay_flag'].sum()
print(f"Total Orders: {total}")
print(f"Delayed Orders: {delayed}")
print(f"Overall Delay Rate: {round(delayed/total*100, 2)}%")

# Delay rate by Shipping Mode
print("\nDelay Rate by Shipping Mode:")
print(df.groupby('Shipping Mode')['delay_flag'].mean().mul(100).round(2).astype(str) + '%')

# Delay rate by Market/Region
print("\nDelay Rate by Market/Region:")
print(df.groupby('Market')['delay_flag'].mean().mul(100).round(2).astype(str) + '%')
print("\nDelay Rate by Product Category:")
print(df.groupby('Category Name')['delay_flag'].mean().mul(100).round(2).sort_values(ascending=False).astype(str)+'%')
# Save results for Power BI
delay_by_shipping = df.groupby('Shipping Mode')['delay_flag'].mean().mul(100).round(2).reset_index()
delay_by_region = df.groupby('Market')['delay_flag'].mean().mul(100).round(2).reset_index()
delay_by_category = df.groupby('Category Name')['delay_flag'].mean().mul(100).round(2).reset_index()

delay_by_shipping.to_csv('delay_by_shipping.csv', index=False)
delay_by_region.to_csv('delay_by_region.csv', index=False)
delay_by_category.to_csv('delay_by_category.csv', index=False)

print("\nCSV files saved successfully!")
# Average delay days by shipping mode
df['delay_days'] = df['Days for shipping (real)'] - df['Days for shipment (scheduled)']
delayed_only = df[df['delay_flag'] == 1]

print("\nAverage Delay Days by Shipping Mode (delayed orders only):")
print(delayed_only.groupby('Shipping Mode')['delay_days'].mean().round(2))
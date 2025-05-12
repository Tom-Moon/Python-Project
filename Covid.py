# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
covid_data = pd.read_csv(url)

# Data Cleaning and Preprocessing
columns = ['location', 'date', 'total_cases', 'total_deaths', 'total_vaccinations', 'new_cases', 'new_deaths']
covid_data = covid_data[columns]
covid_data['date'] = pd.to_datetime(covid_data['date'])
covid_data.fillna(0, inplace=True)

# Global Trends Visualization
global_trends = covid_data.groupby('date').sum()
plt.figure(figsize=(12, 6))
plt.plot(global_trends.index, global_trends['total_cases'], label='Total Cases')
plt.plot(global_trends.index, global_trends['total_deaths'], label='Total Deaths')
plt.title('Global COVID-19 Trends')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.show()

# Country-Specific Trends
country = 'United States'
country_data = covid_data[covid_data['location'] == country]
plt.figure(figsize=(12, 6))
plt.bar(country_data['date'], country_data['new_cases'], color='blue', alpha=0.7)
plt.title(f'Daily New Cases in {country}')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.show()

# Interactive Visualization
fig = px.line(covid_data[covid_data['location'] == 'India'], x='date', y='total_vaccinations', title='Total Vaccinations in India')
fig.show()

# Comparative Analysis
countries = ['United States', 'India', 'Brazil']
filtered_data = covid_data[covid_data['location'].isin(countries)]
fig = px.line(filtered_data, x='date', y='total_cases', color='location', title='Total Cases Across Selected Countries')
fig.show()

# Export Summary
summary = covid_data.groupby('location')[['total_cases', 'total_deaths', 'total_vaccinations']].max()
summary = summary.sort_values(by='total_cases', ascending=False)
summary.to_csv('covid_summary.csv')
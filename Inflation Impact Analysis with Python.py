#!/usr/bin/env python
# coding: utf-8

# # Inflation 
# Inflation is the rate at which the general level of prices for goods and services rises over time, which leads to a decrease in the purchasing power of money. It indicates how much more expensive a set of goods and services has become over a certain period. If you want to learn about Inflation and how to analyze its impact on an economy, this article is for you. In this article, I’ll take you through the task of Inflation impact analysis with

# Inflation occurs when there is a sustained increase in the general price level of goods and services in an economy over time. It impacts various aspects of the economy, including purchasing power, consumer behaviour, savings, and investment. Moderate inflation is typically a sign of a healthy, growing economy, as it encourages spending and investment. However, high or unpredictable inflation can erode the value of money, disrupt financial planning, and lead to economic uncertainty.
# 
# To analyze the impact of inflation, we need to compare it with other economic indicators. So, to analyze the impact of inflation on the economy, we will compare it with the exchange rates over time. This comparison is important because exchange rates are influenced by inflation differentials between countries, such that higher inflation in a country generally leads to a weaker currency relative to countries with lower inflation.
# 
# We will analyse inflation in India and the United States with the exchange rates over time.

# Problem
# The objective of this analysis is to determine the extent to which inflation rates in India and the United States influence the INR/USD exchange rate over time. Specifically, the task is to:
# 
# *Identify the correlation between inflation rates and the exchange rate, considering potential lag effects.
# *Analyze whether the Purchasing Power Parity (PPP) theory holds by comparing the actual exchange rate with the expected   exchange rate based on inflation differentials.
# *Explore any deviations from the expected PPP-based exchange rate to uncover other economic factors that may contribute to exchange rate fluctuations.

# In[1]:


import pandas as pd 
import plotly.express as px 
import plotly.graph_objs as go 

inflation_data = pd.read_csv(r"Inflation_Rates_Transformed-1.csv")
exchange_rate_data = pd.read_csv(r"USD_INR_Exchange_Rates_1980_2024.csv")

exchange_rate_data.head()


# In[2]:


inflation_data.head()


# Merge these datasets to analyze the impact of inflation on exchange rates

# In[3]:


# filter the inflation data for India and the United States
inflation_filtered_df = inflation_data[inflation_data['Country'].isin(['India', 'United States'])]

# pivot the inflation data to have separate columns for India and the United States inflation rates
inflation_pivot_df = inflation_filtered_df.pivot(index='Year', columns='Country', values='Inflation Rate').reset_index()

# merge the exchange rates data with inflation data
merged_df = pd.merge(exchange_rate_data, inflation_pivot_df, on = 'Year')

# renaming columns 
merged_df.columns = ['Year', 'Exchange Rate (INR/USD)', 'Inflation Rate (India)', 'Inflation Rate (United States)']

merged_df.head()


# Let’s start by analyzing the trend of inflation rates for both India and the United States alongside the exchange rate:

# In[4]:


import plotly.graph_objs as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=3, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.1,
                    subplot_titles=("Trend of Exchange Rate (INR/USD)",
                                    "Trend of Inflation Rate (India)",
                                    "Trend of Inflation Rate (United States)"))

fig.add_trace(go.Scatter(x=merged_df['Year'],
                         y=merged_df['Exchange Rate (INR/USD)'],
                         mode='lines+markers',
                         marker=dict(color='blue'),
                         name='Exchange Rate (INR/USD)'),
              row=1, col=1)

fig.add_trace(go.Scatter(x=merged_df['Year'],
                         y=merged_df['Inflation Rate (India)'],
                         mode='lines+markers',
                         marker=dict(color='orange'),
                         name='Inflation Rate (India)'),
              row=2, col=1)

fig.add_trace(go.Scatter(x=merged_df['Year'],
                         y=merged_df['Inflation Rate (United States)'],
                         mode='lines+markers',
                         marker=dict(color='green'),
                         name='Inflation Rate (United States)'),
              row=3, col=1)

fig.update_layout(height=800,
                  width=900,
                  showlegend=False,
                  title_text="Trends of Exchange Rate and Inflation Rates",
                  xaxis3_title="Year",
                  template='plotly_white')

fig.update_yaxes(title_text="Exchange Rate (INR/USD)", row=1, col=1)
fig.update_yaxes(title_text="Inflation Rate (%)", row=2, col=1)
fig.update_yaxes(title_text="Inflation Rate (%)", row=3, col=1)

fig.show()




# The exchange rate shows a general upward trend over the years, which indicates a depreciation of the Indian Rupee against the US Dollar. However, there are periods of both sharp increases and relative stability.
# 
# India’s inflation rate has fluctuated significantly over the years, with periods of high inflation (e.g., early 2000s) and more stable inflation in recent years. The United States has generally experienced lower and more stable inflation rates compared to India, with fewer extreme fluctuations.
# 
# Next, let’s perform a correlation analysis to explore the relationship between the inflation rates and the exchange rates:

# In[5]:


correlation_matrix = merged_df[['Exchange Rate (INR/USD)',
                                'Inflation Rate (India)',
                                'Inflation Rate (United States)']].corr()

correlation_matrix


# Findings from the correlation analysis:
# 
# Exchange Rate vs. Inflation Rate (India): The correlation coefficient is approximately -0.34, which indicates a weak negative relationship. It suggests that as inflation in India increases, the INR tends to depreciate against the USD, though the relationship is not very strong.
# Exchange Rate vs. Inflation Rate (United States): The correlation coefficient is approximately 0.24, which indicates a weak positive relationship. It suggests that higher inflation in the United States might be associated with a depreciation of the USD against the INR, but again, the relationship is not strong.
# Inflation Rate (India) vs. Inflation Rate (United States): The correlation between the inflation rates of India and the United States is very weak and negative (-0.12), which indicates that the inflation rates in these two countries do not move together.
# Next, we’ll perform a comparative analysis to highlight periods of significant divergence or convergence between the inflation rates and the exchange rates:

# In[6]:


fig = go.Figure()

fig.add_trace(go.Scatter(x=merged_df['Year'],
                         y=merged_df['Exchange Rate (INR/USD)'],
                         mode='lines+markers',
                         name='Exchange Rate (INR/USD)',
                         line=dict(color='blue')))

fig.add_trace(go.Scatter(x=merged_df['Year'],
                         y=merged_df['Inflation Rate (India)'],
                         mode='lines+markers',
                         name='Inflation Rate (India)',
                         line=dict(color='orange')))

fig.add_trace(go.Scatter(x=merged_df['Year'],
                         y=merged_df['Inflation Rate (United States)'],
                         mode='lines+markers',
                         name='Inflation Rate (United States)',
                         line=dict(color='green')))

fig.update_layout(title='Comparative Analysis: Exchange Rate vs Inflation Rates (India & US)',
                  xaxis_title='Year',
                  yaxis_title='Value',
                  legend_title_text='Indicators',
                  template='plotly_white',
                  height=600,
                  width=1000)

fig.show()


# Findings from the comparative analysis:
# 
# Early 2000s: A period of high inflation in India coincides with a period of relative stability in the exchange rate. It suggests that factors other than inflation may have been driving the exchange rate during this time.
# Late 2000s to Early 2010s: The period shows some alignment between rising inflation in India and a weakening INR, which indicates that inflation could be contributing to exchange rate movements.
# 2015 Onwards: The exchange rate continues to rise, while both India’s and the United States’ inflation rates remain relatively low. This divergence suggests that the exchange rate is influenced by additional factors beyond inflation, such as economic growth, monetary policy, and international trade dynamics.
# Analyzing Inflation based on the Purchasing Power Parity (PPP)
# Purchasing Power Parity (PPP) is an economic theory that suggests that in the long term, exchange rates between two countries should adjust so that a basket of goods costs the same in both countries when priced in a common currency. PPP is used as a method to compare the economic productivity and standards of living between different countries. If one country’s inflation rate is higher than another’s, its currency should depreciate accordingly to maintain parity in purchasing power to ensure that the same goods cost the same in both locations.
# 
# We will now analyze whether the Purchasing Power Parity theory holds by comparing the relative inflation rates and exchange rate movements over time. It will provide a deeper understanding of whether the exchange rate aligns with the theoretical value based on inflation differentials.
# 
# To test whether PPP holds for India and the United States, we can:
# 
# Calculate the Expected Exchange Rate Based on PPP
# Compare the Actual Exchange Rate with the PPP-Based Expected Exchange Rate
# The formula for PPP-based exchange rate prediction is:
# 
# Expected Exchange Rate = Initial Exchange Rate × ( 1 + Inflation Rate in India / 1 + Inflation Rate in the US)
# 
# Let’s calculate and visualize the PPP-based expected exchange rate versus the actual exchange rate:

# In[7]:


initial_exchange_rate = merged_df['Exchange Rate (INR/USD)'].iloc[0]

# calculate expected exchange rate based on PPP
merged_df['Expected Exchange Rate (PPP)'] = initial_exchange_rate * (
    (1 + merged_df['Inflation Rate (India)'] / 100) / (1 + merged_df['Inflation Rate (United States)'] / 100)
).cumprod()

fig = go.Figure()

# plot actual exchange rate
fig.add_trace(go.Scatter(x=merged_df['Year'],
                         y=merged_df['Exchange Rate (INR/USD)'],
                         mode='lines+markers',
                         name='Actual Exchange Rate (INR/USD)',
                         line=dict(color='blue')))

# plot PPP-based expected exchange rate
fig.add_trace(go.Scatter(x=merged_df['Year'],
                         y=merged_df['Expected Exchange Rate (PPP)'],
                         mode='lines+markers',
                         name='Expected Exchange Rate (PPP)',
                         line=dict(color='orange', dash='dash')))

fig.update_layout(title='Actual vs. Expected Exchange Rate (PPP)',
                  xaxis_title='Year',
                  yaxis_title='Exchange Rate (INR/USD)',
                  legend_title_text='Exchange Rates',
                  template='plotly_white',
                  height=600,
                  width=1000)

fig.show()


# The blue line represents the actual exchange rate (INR/USD) over time, while the orange dashed line represents the expected exchange rate based on PPP. In some periods, the actual exchange rate closely follows the expected PPP-based rate, which suggests that PPP holds. However, in other periods, there are significant deviations between the two.
# 
# The PPP-based expected exchange rate shows a more rapid increase compared to the actual exchange rate. It suggests that, according to PPP, the INR should have depreciated more than it actually did. However, the actual exchange rate was consistently lower than the PPP-based expected rate, which indicates that factors other than inflation are at play.

# In[ ]:


#Conclusion
#Our analysis revealed that inflation in India and the United States influences the exchange rate between INR and USD. Higher inflation in India generally leads to a depreciation of the INR relative to the USD, while lower inflation in the United States contributes to a stronger USD. While inflation affects the exchange rate between INR and USD, it is only one of many factors.


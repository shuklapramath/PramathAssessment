from preswald import connect
import pandas as pd
import preswald
from preswald import query
from preswald import table, text

#connect()  # Initialize connection to preswald.toml data sources
df = pd.read_csv('data/Thyroid_Diff.csv')  # Load data
table(df.head())

sql = "SELECT * FROM df WHERE Age > 30"
filtered_df = query(sql, df)
text("# My Data Analysis App")
table(filtered_df)

# Summary stats
text("## Summary Statistics")
summary_stats = df.describe()
table(summary_stats)

# Risk Level Distribution
text("## Risk Level Distribution")
risk_counts = df['Risk'].value_counts()
table(risk_counts)

# Response Analysis by Risk Level
text("## Response Analysis by Risk Level")
response_by_risk = pd.crosstab(df['Risk'], df['Response'])
table(response_by_risk)

# Age Distribution by Gender
text("## Age Distribution by Gender")
age_by_gender = df.groupby('Gender')['Age'].agg(['mean', 'median', 'min', 'max'])
table(age_by_gender)

# Pathology Distribution
text("## Pathology Distribution")
pathology_counts = df['Pathology'].value_counts()
table(pathology_counts)

from preswald import plotly
import plotly.express as px

# Scatter plot of Age vs Risk, colored by Gender
fig = px.scatter(df, x="Age", y="Risk", color="Gender", title="Age vs Risk Level by Gender")
plotly(fig)

# Create a pie chart for Risk Distribution
fig2 = px.pie(df, names='Risk', title='Distribution of Risk Levels')
plotly(fig2)

# Create a bar chart for Response Analysis
fig3 = px.bar(response_by_risk, title='Response Analysis by Risk Level', barmode='group')
plotly(fig3)

# Create a box plot for Age Distribution by Gender
fig4 = px.box(df, x='Gender', y='Age', title='Age Distribution by Gender')
plotly(fig4)
# Daily Challenge: Interactive Data Visualization with Matplotlib and Seaborn

Notebook: `interactive_data_visualization.ipynb`

In this notebook I clean the US Superstore data (9,994 orders, 2014–2017) and make:
- an interactive Matplotlib line chart of monthly sales, where I pick the year from a dropdown,
- an interactive map of sales by US state (the data has only one country, the United States),
- Seaborn charts of the top 10 products by sales and of profit vs discount,
- a comparison of Matplotlib and Seaborn.

## Key insights
- Sales grew from $470K (2015) to $733K (2017), and profit grew every year from $50K (2014) to $93K (2017). September, November and December are the peak months.
- Most sales come from the coasts: California ($458K) and New York ($311K) lead.
- The top product, the Canon imageCLASS 2200 Advanced Copier ($61,600), sells more than double the 2nd product.
- Discounts hurt profit: from a 30% discount up, the average profit is negative (correlation −0.22).
- I found Seaborn quicker for clean statistical charts, and Matplotlib better for full control and interactivity.

## Data and how to run
The exercise gives the data as `US Superstore data.xls`. The same data (same 9,994 rows and 21 columns) is on Kaggle as a CSV, which I already had, so I use `Superstore Dataset (vivek468).zip`. I open the notebook in Google Colab, choose that zip in the upload cell, and run all cells.

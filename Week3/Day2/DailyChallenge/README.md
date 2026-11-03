# Global Power Plant Analysis

In this daily challenge I analyzed the Global Power Plant Database (World Resources Institute) with NumPy, Pandas, Matplotlib and Seaborn. The notebook is `global_power_plant_analysis.ipynb`.

## Key insights
- The dataset has 34,936 plants in 167 countries. The USA has the most (9,833), then China (4,235) and the UK (2,751).
- Most plants are small. The median capacity is 16.7 MW, but the mean is 163.4 MW because a few huge plants pull it up.
- Solar has the most plants (10,665), but they are tiny (17.7 MW on average). Nuclear (2,092 MW) and Coal (844 MW) have the biggest plants, and Coal has the largest total capacity.
- ANOVA across fuels and a Coal vs Solar t-test both gave p ≈ 0, so the mean capacity really differs by fuel type.
- Hydro dropped from about 47% of new capacity in the 1950s to 12% in the 2010s. Wind grew from 0% to about 9%, and Coal stayed the biggest share (about 50%).
- The numeric attributes are only weakly related. The strongest link is capacity vs renewable (-0.32), and all eigenvalues of the correlation matrix are close to 1.

## Dataset
I downloaded `globalpowerplantdatabasev130.zip` and used `global_power_plant_database.csv` from inside it. The zip is not in this repo.

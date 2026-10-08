# NERIS Carroll County Analysis
## Overview
The National Emergency Response Information System (NERIS) offers a 60-day-lagged dataset of incidents reported by fire departments for free on their website (https://www.usfa.fema.gov/neris/public/). I wanted to explore the dataset to see what it contained, as well as to identify any high-level trends of incidents we may be able to make for Carroll County (CC), MD, USA.

## Key Findings
- The overwhelming majority of incidents in CC were coded as Medical (n = 1512) for the primary incident type, with the remaining 5 incident types combined adding up to 727.
- Mondays (n = 337) showed the highest occurrence of incidents, though all days of the week were within a reasonable range with Wednesdays showing the lowest occurrence (n = 296).
- Mornings (6a-12p; n = 772) and afternoons (12p-6p; n = 756) had the highest incident volumes, with evenings (6p-12a; n = 256) having the least.
- 1822 of the 2239 incidents had 1 unit that responded.
- Incidents tended to cluster into higher volume areas that seem to correspond with Westminster, Taneytown, and Eldersburg.

## How to Run
### Install dependencies
```bash
python3 -m pip install -r requirements.txt --upgrade
```

### Get dataset 
- Use https://neris.fsri.org/public for your specific county and date range (current dataset was Carroll County YTD to 8/2/2026)
- rename the .csv file neris.csv so it will work in exploration notebook

### Explore the dataset w/ Jupyter
```bash
jupyter notebook notebooks/01_exploration.ipynb
```

### Clean the dataset for analysis w/ a script
```bash
python3 scripts/clean_data.py
```

### Analyze high-level trends w/ Jupyter
```bash
jupyter notebook notebooks/02_analysis.ipynb
```

## Skills Used
pandas, matplotlib, data cleaning, data analysis, data visualization, Jupyter, git

## Challenges
When trying to extract the 1st tag from the type_1 column, I was attempting to parse on a double pipe like this, ||, because that's what was shown. This did not work, and after some diagnoses, the single pipe, |, worked as a parser. This made little sense to me, and the only thing Claude Code could come up with was that pandas interpreted the double pipe as regex. This was proven correct, as I changed regex=False and it worked perfectly again.
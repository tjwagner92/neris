# This script is used for cleaning the data from the NERIS
# dataset after conducting an exploration in notebook 01

#Imports
import pandas as pd

#Data loading/check
data = pd.read_csv('data/neris_FD24013403_2026-08-02.csv')
data.info()

#Changing the call_create to datetime
data['call_create'] = pd.to_datetime(data['call_create'], utc=True)
print(data['call_create'].dtype)

#Convert from UTC to local time (Eastern)
data['call_create_eastern'] = data['call_create'].dt.tz_convert('US/Eastern')
print(data['call_create_eastern'].dtype)

#Make some 'timing' variables'
data['day_of_week'] = data['call_create_eastern'].dt.day_name()
print(data['day_of_week'].unique())

data['hour'] = data['call_create_eastern'].dt.hour
print(sorted(data['hour'].unique()))

#Make function to define time of day based on hour
def get_time_period(hour):
    """
    Bins time of day into listing below.
        Hour 0 (midnight): 0 <= 0 < 6 → overnight
        Hour 6 (6am): 6 <= 6 < 12 → morning
        Hour 12 (noon): 12 <= 12 < 18 → afternoon
        Hour 18 (6pm): else → evening 
        Hour 23 (11pm): else → evening 
    
    Args:
        hour: hour of day
    
    Returns:
        time of day converted to categorical nomenclature
    """
    if 0 <= hour < 6:        # includes 0, 1, 2, 3, 4, 5
        return 'overnight'
    elif 6 <= hour < 12:     # includes 6, 7, 8, 9, 10, 11
        return 'morning'
    elif 12 <= hour < 18:    # includes 12, 13, 14, 15, 16, 17
        return 'afternoon'
    else:                    # includes 18, 19, 20, 21, 22, 23
        return 'evening'

#Call the function
data['time_period'] = data['hour'].apply(get_time_period)
print(data['time_period'].unique())

#Extract just the 1st tag from the Type 1 column
data['type_1_main'] = data['type_1'].astype(str).str.split('||', regex=False).str[0]
print(data['type_1_main'].value_counts())

#take forward only the relevant columns for analysis
keep_cols = [
    'neris_id_incident',
    'department_name',
    'type_1_main',
    'call_create_eastern',
    'hour',
    'day_of_week',
    'time_period',
    'unit_response_count',
    'x', 'y'
]

data = data[keep_cols]

#save cleaned dataset
data.to_csv('data/neris_cleaned.csv', index=False)
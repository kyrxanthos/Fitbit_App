import os
import pandas as pd
import json
import altair as alt

def get_dataframes():
    path_to_json = '../data/Physical Activity'
    # json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.startswith('steps-')]

    dataframes = []
    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            json_text = json.load(json_file)
            df = pd.json_normalize(json_text)
            df['dateTime'] = pd.to_datetime(df['dateTime'], format='%m/%d/%y %H:%M:%S')
            dataframes.append(df)

    df = pd.concat(dataframes)
    df['value'] = df['value'].astype(int)
    df = df.groupby(df['dateTime'].dt.date).sum()
    df = df.reset_index()
    df['dateTime'] = pd.to_datetime(df['dateTime'])
    # create a new column with the week number
    df['week'] = df['dateTime'].dt.isocalendar().week
    # group the data by week and calculate the mean for each week
    df_weekly = df.groupby('week').mean().reset_index()
    return df, df_weekly

import datetime
import pandas as pd
import datetime
import os 
from tqdm import tqdm

tqdm.pandas(desc='Data Processing')

def timepoint_convert(time_point):
    time = datetime.datetime.strptime(time_point, '%Y-%m-%d %H:%M:%S').time()
    date = datetime.date(1900,1,1)
    return datetime.datetime.combine(date, time)


all_trip_path = "./opendriver/"


for path in tqdm(os.listdir(all_trip_path)[:]):
    try:
        name = path[-4:]
            
        csv_path = os.path.join(all_trip_path,path,name+'_axis.csv')
        ecg_csv_path = os.path.join(all_trip_path,path,name+'_ecg.csv')
        eda_csv_path = os.path.join(all_trip_path,path,name+'_eda.csv')
        trip_id = name

        axis_df = pd.read_csv(csv_path)
        axis_df['time_point'] = axis_df['time_point'].apply(timepoint_convert)
        ecg_df = pd.read_csv(ecg_csv_path)
        ecg_df['time_point'] = ecg_df['time_point'].apply(timepoint_convert)
        
        eda_df = pd.read_csv(eda_csv_path)
        eda_df['time_point'] = eda_df['time_point'].apply(timepoint_convert)


    except:
        print("{} empty".format(name))
        continue

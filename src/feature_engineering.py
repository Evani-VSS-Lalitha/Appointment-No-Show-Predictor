import pandas as pd

def preprocess(df):
    df['No-show'] = df['No-show'].map({'Yes': 1, 'No': 0})
    df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
    df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])
    df['LeadTime'] = (df['AppointmentDay'] - df['ScheduledDay']).dt.days
    df = df.drop(['PatientId', 'AppointmentID', 'ScheduledDay', 'AppointmentDay', 'Neighbourhood'], axis=1)
    df = pd.get_dummies(df, columns=['Gender'], drop_first=True)
    return df

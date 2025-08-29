import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
L1 = pd.read_csv('Stress_Dataset.csv')
L2 = pd.read_csv('StressLevelDataset.csv')

'''
# Alias : Question

Q01 : Have you recently experienced stress in your life?
Q02 : Have you noticed a rapid heartbeat or palpitations?
Q03 : Have you been dealing with anxiety or tension recently?
Q04 : Do you face any sleep problems or difficulties falling asleep?
Q05 : Have you been getting headaches more often than usual?
Q06 : Do you get irritated easily?
Q07 : Do you have trouble concentrating on your academic tasks?
Q08 : Have you been feeling sadness or low mood?
Q09 : Have you been experiencing any illness or health issues?
Q10 : Do you often feel lonely or isolated?
Q11 : Do you feel overwhelmed with your academic workload?
Q12 : Are you in competition with your peers, and does it affect you?
Q13 : Do you find that your relationship often causes you stress?
Q14 : Are you facing any difficulties with your professors or instructors?
Q15 : Is your working environment unpleasant or stressful?
Q16 : Do you struggle to find time for relaxation and leisure activities?
Q17 : Is your hostel or home environment causing you difficulties?
Q18 : Do you lack confidence in your academic performance?
Q19 : Do you lack confidence in your choice of academic subjects?
Q20 : Academic and extracurricular activities conflicting for you?
Q21 : Do you attend classes regularly?,Have you gained/lost weight?
Q22 : Which type of stress do you primarily experience?
'''
#Drop the voided column since it was a duplicate 
L1.drop('voided', axis=1, inplace=True)

#Create a function to rename
def rename_columns(df):
    for col in range(2,len(df.columns) - 1):
        current_column = df.columns[col]
        df.rename(columns = {current_column: f'Q{col}'}, inplace=True)
    return df

#Function for old graph so the whole block does not needed to be commented
def graph_data(df, graph_set):
    L2_Beta = (df['mental_health_history'], df['depression']/6, df['headache'], df['blood_pressure'], df['sleep_quality'], df['breathing_problem'], df['noise_level'], df['living_conditions'], df['safety'], df['basic_needs'], df['academic_performance'], df['study_load'], df['teacher_student_relationship'], df['future_career_concerns'], df['social_support'], df['peer_pressure'], df['extracurricular_activities'], df['bullying'], df['stress_level'])
    graphSet = graph_set
    match graphSet:
        case 1: # Only shows self-reported values rated between 0 and 5
            plt.plot(L2_Beta)
            return  plt.show()
        case 2: # Standardizes 0-30 to 0-5 scale by dividing anxiety_level and self_esteem by 6 (W.I.P.)
             plt.plot(L2['anxiety_level']/6, L2['self_esteem']/6, L2_Beta)
             return  plt.show()
        case 3: # Shows all raw data
             plt.plot(L2['anxiety_level'], L2['self_esteem'], L2_Beta)
             return  plt.show()
   


#next I want to learn how to make this data into a histogram


'''
plt.plot(L1['Q01'], L1['Q02'], L1['Q03'], L1['Q04'], L1['Q05'], L1['Q06'], L1['Q07'], L1['Q08'], L1['Q09'], L1['Q10'], L1['Q11'], L1['Q12'], L1['Q13'], L1['Q14'], L1['Q15'], L1['Q16'], L1['Q17'], L1['Q18'], L1['Q19'], L1['Q20'], L1['Q21'], L1['Q22'], L1['Q23'])
#plt.show()
#print(L1[['Q01']])
'''

#print(L2['stress_level'].max())

#Test Please work 
#Another line of comment
#Work Oml
L1 = rename_columns(L1)
print(L1.head())
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.linear_model import LinearRegression

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

#Noeal Stuff

L2_Beta = np.array((L2['headache'], L2['blood_pressure'], L2['sleep_quality'], L2['breathing_problem'], L2['noise_level'], L2['living_conditions'], L2['safety'], L2['basic_needs'], L2['academic_performance'], L2['study_load'], L2['teacher_student_relationship'], L2['future_career_concerns'], L2['social_support'], L2['peer_pressure'], L2['extracurricular_activities'], L2['bullying']))
L2_Beta2 = L2['headache', 'blood_pressure', 'sleep_quality', 'breathing_problem', 'noise_level', 'living_conditions', 'safety', 'basic_needs', 'academic_performance', 'study_load', 'teacher_student_relationship', 'future_career_concerns', 'social_support', 'peer_pressure', 'extracurricular_activities', 'bullying']
print(L2_Beta2.head)

####Noael Stuff
'''
means, maxs, mins, modes = [], [], [], []


#print(L2['stress_level'].max())
#print(L2['stress_level'].min())

for col in L2.columns:
    print(L2[col])

'''
#Scatterplot function to see relation ship between X's and Y's

y_axis = ['stress_level']

x_axis = [ 'mental_health_history',
       'headache', 'blood_pressure', 'sleep_quality', 'breathing_problem',
       'noise_level', 'living_conditions', 'safety', 'basic_needs',
       'academic_performance', 'study_load', 'teacher_student_relationship',
       'future_career_concerns', 'social_support', 'peer_pressure',
       'extracurricular_activities', 'bullying']

def scatter_graphs(df,x_col,y_col):
             
             df_x = df[x_col]
             df_y = df[y_col]
            
             for col in range(df_x.shape[1]):
                   plt.scatter(df_x.iloc[:,col],df_y)
             
             plt.xlabel('Independent Variable')
             plt.ylabel('Stress_Levels(Dependent Variable)')
             plt.show()
def gradient_descent(predictors):
    '''
    # normalize our vehicle weight values 'X'
    L2_Beta_mean = L2_Beta.mean()
    L2_Beta_std = L2_Beta.std()
    L2_Beta_norm = (L2_Beta - L2_Beta_mean) / L2_Beta_std

    #pred_y = .predict(predictors_norm.to_frame()) # get predictions for mpg
    
    ### In a video I watched for multivariable gradient descent he made a vector for L2_Beta's values
    ### and for multivariate you can make a vector of Y as well

    # Import LinearRegression from sklearn
    '''
    x = pd.DataFrame(predictors).T  # Convert tuple of Series to DataFrame and transpose
    y = L2['stress_level']

    # Normalize X for gradient descent
    x_norm = (x - x.mean()) / x.std()
    print(x.mean())
    print(x.std())

    # Fit linear regression model
    model = LinearRegression()
    model.fit(x_norm, y)

    # Predict stress levels using the trained model
    y_pred = model.predict(x_norm)

    # Plot actual vs predicted stress levels
    plt.scatter(y, y_pred, color='blue', label='Predicted vs Actual')
    plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', label='Ideal Fit')
    plt.title('Linear Regression using Gradient Descent (sklearn)')
    plt.xlabel("Actual Stress Level")
    plt.ylabel("Predicted Stress Level")

    plt.legend()
    plt.show()

graphSet = 0
match graphSet:
    case 0:
        pass
    case 1: # Only shows self-reported values rated between 0 and 5
        sb.histplot(L2_Beta, bins=5, kde=True)
    case 2:
        scatter_graphs(L2, x_axis, y_axis)
    case 3:
        gradient_descent(L2_Beta)
plt.show()
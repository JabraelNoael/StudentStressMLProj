import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sb
from sklearn.linear_model import LinearRegression
import seaborn as sb
import scipy.stats as stats
from scipy.stats import spearmanr
from statsmodels.stats.outliers_influence import variance_inflation_factor

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

L2_Beta = (L2['headache'], L2['blood_pressure'], L2['sleep_quality'], L2['breathing_problem'], L2['noise_level'], L2['living_conditions'], L2['safety'], L2['basic_needs'], L2['academic_performance'], L2['study_load'], L2['teacher_student_relationship'], L2['future_career_concerns'], L2['social_support'], L2['peer_pressure'], L2['extracurricular_activities'], L2['bullying'])

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

#Removed predictors, also removed social support and blood pressure since theor scale is 0-3
#Removed predictors breathing_problems,living_conditions,student_teacher_relationship,study_load,peer_pressure for p <.7
#Might add back Study load and peer preasure because logicly they make sense to keep

x_axis = ['headache', 'blood_pressure', 'sleep_quality', 'breathing_problem', 'noise_level', 'living_conditions', 
          'safety', 'basic_needs', 'academic_performance', 'study_load', 'teacher_student_relationship', 
          'future_career_concerns', 'social_support', 'peer_pressure', 'extracurricular_activities', 'bullying']
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

def scatter_graphs(df,x_col,y_col):
             
             df_x = df[x_col]
             df_y = df[y_col]
            
             for col in range(df_x.shape[1]):
                   plt.scatter(df_x.iloc[:,col],df_y)
             
             plt.xlabel('Independent Variable')
             plt.ylabel('Stress_Levels(Dependent Variable)')
             plt.show()

x_and_y =  y_axis + x_axis 

def scatter_graphs(df, x_col, y_col):
    df_x = df[x_col]
    df_y = df[y_col]

    plt.figure(figsize=(10, 6))
    markers = ['o', 's', '^', 'D', 'v', 'p', '*', 'X', '<', '>', 'h', '8', 'P', 'H', 'd', '|', '_']
    for col in range(df_x.shape[1]):
        sizes = np.random.randint(200, 500)
        marker = markers[col % len(markers)]
        plt.plot(df_x.iloc[:, col], df_y.values.flatten(), s=sizes, alpha=0.3, label=x_col[col], marker=marker)

    plt.xlabel('Independent Variables')
    plt.ylabel('Stress_Levels (Dependent Variable)')
    plt.legend(loc='best')
    plt.show()

#scatter_graphs(L2, x_axis, y_axis)

#Correlation HeatMap Using Spearman
def plot_correlation_heatmap(df):
    correlation = df.corr(method='spearman')
    # Get absolute correlations with the target (assume first column is target)
    target_col = df.columns[0]
    abs_corr = correlation[target_col].abs().sort_values(ascending=False)
    # Reorder the correlation matrix rows/columns by sorted absolute correlation
    sorted_cols = abs_corr.index.tolist()
    correlation = correlation.loc[sorted_cols, sorted_cols]
    plt.figure(figsize=(12, 8))
    correlmapType = 2
    match correlmapType:
        case 0:
            correlmap = LinearSegmentedColormap.from_list("red_purple_blue_purple_red", ["red", "purple", "blue", "purple", "red"])
        case 1:
            correlmap = LinearSegmentedColormap.from_list("green_orange_red_orange_green", ["green", "orange", "red", "orange", "green"])
        case 2:
            correlmap = LinearSegmentedColormap.from_list("exaggerated_orange_mid", ["darkgreen","green","darkorange","orange","red","orange","darkorange","green","darkgreen"])
    sb.heatmap(correlation, annot=True, cmap=correlmap, fmt=".2f", vmin=-1, vmax=1, center=0)

#Check which is signifcant based of alpha = 0.05
def spearman_significance(x_col, y_col, alpha=0.05):

    significant_predictors = []

    for col in range(x_col.shape[1]):
        rho, p = spearmanr(x_col.iloc[:, col], y_col)
        
        if p < alpha:
            significant_predictors.append(x_col.columns[col])

    return significant_predictors




significant_predictors = spearman_significance(L2[x_axis], L2[y_axis])
#print("Significant predictors:", significant_predictors)

#Calculate VIF
def calculate_vif(dataset):
    vif = pd.DataFrame()
    vif['features'] = dataset.columns
    vif['VIF_Value'] = [variance_inflation_factor(dataset.values,i) for i in range(dataset.shape[1])]
    
    return(vif)

#predictors = L2.copy()
#predictors = predictors[x_axis]
#print(calculate_vif(predictors))
#print("Significant predictors:", significant_predictors)
#print(L2.columns)

graphSet = 4
match graphSet:
    case 0:
        pass
    case 1: # Only shows self-reported values rated between 0 and 5
        sb.histplot(L2_Beta, bins=5, kde=True)
    case 2:
        scatter_graphs(L2, x_axis, y_axis)
    case 3:
        gradient_descent(L2_Beta)
    case 4:
        plot_correlation_heatmap(L2[x_and_y])
plt.show()
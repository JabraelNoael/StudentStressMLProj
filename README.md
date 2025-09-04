# StudentStressMLPro

Data Source: [Kaggle](https://www.kaggle.com/datasets/mdsultanulislamovi/student-stress-monitoring-datasets?resource=download&SSORegistrationToken=CfDJ8BfigAjZUoJHuOjXpienVtDbGExeMzM5KlyH9fiZoi8LRsQEEePfUw8yadlGTGQwleoOxpJ27NNVLIWhxS2zBa4TFz01S1QcMkIhK9Uujcu4CR7MDdsH9jkem9jlzBfufOqe7lDX-sgBBh9dk5vDVfgEYvfCrR_KeZQC2iUsMQgJccih-EX1eiWzSxeFZgqjxsjB2QRpHSDnVdQZss7dVDAHH2gjc5hQLumoGuAke4sTYBoHwNcUAIQRyKJOAG_T9crxArU7c5Gh8i7Y7cU_-2Y-hlZn13WyaHKjtgYDjSZ6uJoi-WOapITklkyvoWhvZ_Qx5hb57zb8eTCzarmtrgcnNFyV&DisplayName=Noael%20Jabrael)

---
## StressLevelDataset (Legend)

### Dependent Variables (Y)
- **mental_health_history** = {(0 : false), (1 : true)}
- **anxiety_level** = (int 0-30)
- **self_esteem** = (int 0-30)
- **depression** = (int 0-30)
- **stress_level** = {(0 : low stress), (1 : moderate stress), (2 : high stress)}
### Predictors (Coefficients)
> *The following predictors are self-reported from a scale of 0-5. Sadly the exact original questionnaire is not provided in the dataset, however, questions similar to these appear on the Perceived Stress Scale (PSS) and the Student Stress Inventory (SSI). We faithfully found similar questions from those questionaires to here but cannot gurantee their correctness.*

> * The following predictors were chosen based of the standard spearmans correlation scale for Pscyhology. Each predictor was less than 0.05 alpha, which shows that they are statistically significant. The moderate significance for correlation in a Pyschological setting is > |.3| spearmans p. Each predictor that were chosen was > |.3| spearmans p.
 
 Predictors:

- **headache**: "*How often do you experience headaches?*" (0 = Never, 5 = Very Often)
- **blood_pressure**: "*How often do you notice changes in your blood pressure?*" (0 = Never, 3 = Very Often)
- **sleep_quality**: "*How would you rate your sleep quality?*" (0 = Very Poor, 5 = Excellent)
- **breathing_problem**: "*How often do you experience breathing problems?*" (0 = Never, 5 = Very Often)
- **noise_level**: "*How would you describe the noise level in your environment?*" (0 = Very Quiet, 5 = Very Noisy)
- **living_conditions**: "*How would you rate your living conditions?*" (0 = Very Poor, 5 = Excellent)
- **safety**: "*How safe do you feel in your current environment?*" (0 = Not Safe at All, 5 = Very Safe)
- **basic_needs**: "*Are your basic needs (food, shelter, etc.) being met?*" (0 = Not Met at All, 5 = Fully Met)
- **academic_performance**: "*How satisfied are you with your academic performance?*" (0 = Not Satisfied at All, 5 = Very Satisfied)
- **study_load**: "*How would you rate your current study load?*" (0 = Very Light, 5 = Very Heavy)
- **teacher_student_relationship**: "*How would you describe your relationship with your teachers?*" (0 = Very Poor, 5 = Excellent)
- **future_career_concerns**: "*How concerned are you about your future career?*" (0 = Not Concerned at All, 5 = Extremely Concerned)
- **social_support**: "*How would you rate your level of social support?*" (0 = No Support, 3 = Excellent Support)
- **peer_pressure**: "*How often do you feel peer pressure?*" (0 = Never, 5 = Very Often)
- **extracurricular_activities**: "*How involved are you in extracurricular activities?*" (0 = Not Involved, 5 = Very Involved)
- **bullying**: "*How often do you experience bullying?*" (0 = Never, 5 = Very Often)

> Similar Questionaires
- [Perceived Stress Scale (PSS)](https://www.mindgarden.com/132-perceived-stress-scale)
- [Student Stress Inventory (SSI)](https://www.researchgate.net/publication/340251765_Student_Stress_Inventory_SSI)

---

## Stress_Dataset (W.I.P.)
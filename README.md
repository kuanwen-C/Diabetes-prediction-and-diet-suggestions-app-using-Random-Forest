# Diabetes-prediction-and-diet-suggestions-app
This app harnesses machine learning to predict  the presence or absence of diabetes. The app takes it a step  further by  offering customized diet suggestions tailored to  the user's health status, desired diet goals, daily activity  volume, and diabetes prediction outcome.

demo video: https://youtu.be/5oK51loKqIQ

----------
# Abstract

This app harnesses machine learning to predict diabetes and provide personalized diet 
recommendations. Using a Random Forest model, it analyzes user-provided data 
such as age, gender, family history, blood pressure, height, weight, and glucose levels 
to accurately predict the presence or absence of diabetes. The app takes it a step 
further by calculating the user's Total Daily Energy Expenditure (TDEE) based on 
their BMI, which is derived from their height and weight, as well as their activity 
level. Utilizing this information, the app offers customized diet suggestions tailored to 
the user's health status, desired diet goals (cutting, bulking, or standard), daily activity 
volume, and diabetes prediction outcome. These suggestions consider macronutrient 
distribution, portion sizes, empowering users to make informed decisions about their 
dietary habits. With its ability to predict diabetes and provide tailored diet plans, this 
app serves as a valuable tool for individuals, particularly those with diabetes, in 
organizing their meals and managing their health effectively.

-----------------------------------------------------------------------------------------------------
# Purpose & Objectives

Diabetes is a common chronic disease in modern society, and it can have severe
consequences on the body, especially in old age. This is particularly crucial for
individuals already diagnosed with diabetes, as having correct dietary concepts,
nutrient proportions, and portion control is vital in managing the progression of the
disease. Unfortunately, due to the inconvenience of medical check-ups, many
individuals neglect assessing their current risk of developing diseases.
Therefore, a system that can quickly utilize certain test data without requiring
individuals to visit hospitals would enable them to assess their own risk of disease
from the comfort of their homes. This would be extremely important for early
treatment and prevention.
For many people, there is a lack of understanding regarding nutrient concepts in their
diet planning. Often, they consume excessive carbohydrates, inappropriate nutrient
proportions, or improper portions, which can greatly contribute to the development of
diabetes.

Additionally, for individuals without diabetes, the daily intake of nutrients in proper
proportions and quantities is also highly important. Depending on their activity levels,
dietary goals, and individual physical condition, the daily nutrient requirements vary
among individuals. There is no fixed value, as it is tailored to each person's needs. A
well-planned diet can help prevent chronic diseases such as diabetes. Furthermore,
correct, and appropriate dietary planning is indispensable for those who aim to build
muscle or lose weight.
However, busy modern individuals often lack the time and knowledge to extensively
study dietary concepts. The prevalence of eating out among the population further
contributes to neglecting the content of their meals. Therefore, a user-friendly tool
that simplifies the process would allow both diabetic patients and the public to
quickly determine how to arrange their diets. Such a tool could potentially play a
significant role in overall chronic disease prevention and disease management.

-----------------------------------
# Method 

Part1. 

The diabetes prediction model:

Diabetes Prediction Model
Using the random forest algorithm, I constructed decision trees based on several
features (Pregnancies, glucose, blood pressure, skin thickness, insulin, diabetes
prediction function, age). The individual decision trees were then combined, and the
results were averaged to obtain an overall analysis of whether a person is likely to
have diabetes based on the values.

By combining the data from these trees, we ensure obtaining the most accurate
predictions. While individual decision trees can provide a result and a narrow range of
groups, a forest improves the accuracy of the results through multiple groups and
decision processes. It adds randomness to the model by finding the best features
within random subsets of features.

For model training, I utilized the random forest algorithm from the scikit-learn library.
I used a dataset from Kaggle, consisting of 768 records of body data along with
information on the presence or absence of diabetes. This dataset served as the training
dataset for the model.

![image](https://github.com/kuanwen-C/Diabetes-prediction-and-diet-suggestions-app-using-Random-Forest/assets/128893625/ce748961-c406-4bbf-b273-73c2a6778d41)

![image](https://github.com/kuanwen-C/Diabetes-prediction-and-diet-suggestions-app-using-Random-Forest/assets/128893625/10cebc88-512b-4b0f-af85-e492fb852304)


The above figures are the data analysis of the dataset used reveals that most of the
data tends to be concentrated within a specific range but also exhibits a continuous
distribution. This distribution will serve as a reference for future design
considerations.

For example, in the case of the "Diabetes Prediction Function," which relates to
family medical history, we can observe that the majority of the data falls below
0.6263, with an average of 0.4719. Therefore, when designing the user interface for
the Diabetes Prediction Function dropdown, we can consider the distribution of this
data and create options that align with the data patterns.



Part2.

Dietary Planning system:

Based on the user's input of height and weight, the following steps can be taken to
calculate the user's Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure
(TDEE). This information, along with the diabetes prediction result, can further guide
appropriate dietary recommendations.
For males: BMR = 66 + (bodyweight * 13.7) + (5 * height) - (6.8 * age)
For females: BMR = 655 + (bodyweight * 9.6) + (1.8 * height) - (4.7 * age)
Next, the user can select their activity level from a menu, categorized as low,
moderate, or high:

Low: Almost no exercise and not involved in labor-intensive work.
Moderate: Regular exercise two to three times a week.
High: Labor-intensive work, athlete, or exercising more than four times a week.

Based on this activity level categorization, the TDEE can be calculated as follows:
Low activity level: TDEE = BMR * 1.2
Moderate activity level: TDEE = BMR * 1.55
High activity level: TDEE = BMR * 1.9

Next, in conjunction with the diabetes prediction result from Part 1.
If the prediction indicates a potential risk of diabetes, the system will allocate the
user's daily calorie intake directly to the most suitable one for a diabetes patient.
The recommended distribution, according to Taiwan's Ministry of Health and Welfare,
is to allocate the user's daily calories as follows: protein and fat each account for
25%, and carbohydrates account for 50%.

For users who are predicted to be healthy, they can select their dietary goal (e.g.,
muscle gain, fat loss, or maintenance). The system will then provide the
recommended daily calorie intake based on their goal:

For fat loss: TDEE - 300 kcal
For muscle gain: TDEE + 400 kcal
For weight maintenance: Intake should be based on TDEE

Once the calorie intake for each nutrient is determined, the corresponding portions of
each nutrient can be calculated based on the energy density of each nutrient
(carbohydrates: 4 kcal/g, protein: 4 kcal/g, fat: 9 kcal/g).

--------------------------------
# Process:

![image](https://github.com/kuanwen-C/Diabetes-prediction-and-diet-suggestions-app-using-Random-Forest/assets/128893625/b06d6f5a-876b-40e6-86a5-65f5b958415f)



![image](https://github.com/kuanwen-C/Diabetes-prediction-and-diet-suggestions-app-using-Random-Forest/assets/128893625/f1f0990e-1a73-434a-a548-20a378319c9b)


------------------------------------
# Note

1. The image folder and .csv file should be put under the same folder as the code file.
2. The ML training dataset comes from   https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset

---------------------------------------------------------------------------------------------------------------------------------------------

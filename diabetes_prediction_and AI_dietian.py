#!/usr/bin/env python
# coding: utf-8

# Imprt modules needed

# In[56]:


import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier     #we'll use random forest as the ML alogortihm to form the ensemble model
from sklearn.model_selection import train_test_split
import flet as ft


# Machine Learning to predict Diabetes 1 -read the training dataset
# 

# In[57]:


df=pd.read_csv(r'diabetes.csv')  #read the training dataset (it supposed to be under the same folder as the code,the dataset is download from kaggle)
#df  #show the csv to check it


# In[58]:


#df.groupby('Outcome').hist(figsize=(9,9))


# Machine Learning to predict Diabetes 2-arrange the data
# 

# In[59]:


x=df.drop(['Outcome'],axis=1)        #x is the one, with  the coloumn named "Outcome" of csv removed
y=df.iloc[:,-1]         #y is the list of the values of every row in the last coloumn

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0) #set training and test dataset

#train
rf  = RandomForestClassifier()
rf.fit(x_train, y_train)


# In[60]:


#used to check x (pandas dataframe  with the original  coloumn named "Outcome" removed)
#x  


# In[61]:


#used to check y (which is the outcome coloumn)
#y


# In[62]:



def bmi_calculate(height,weight):             #bmi calculate
    bmi=weight/(height**2)
    return bmi


# In[63]:


def ML_predict(input_data):
    result=rf.predict(input_data)
    accuracy=accuracy_score(y_test,rf.predict(x_test))
    return result[0],accuracy     #if it return 0-> diabetes ; return 1->healthy;accuracy is the accuracy of the model


'''used to test the ML model
user__data_dir = {
            'Pregnancies':0,
            'Glucose':170,
            'BloodPressure':100,
            'SkinThickness':91,
            'Insulin':85,
            'BMI':21,
            'DiabetesPedigreeFunction':0.37,
            'Age':31
                         }
user_data = pd.DataFrame(user__data_dir, index=[0])
user_result,accuracy=ML_predict(user_data)
print(user_result,"  ",accuracy)
'''


# In[64]:


def calculate_desire_TDEE(activity,bodyweight,sex,age,height):
    BMR=0.0
    TDEE=0.0

    #use Harris-Benedict equation to calculate BMR
    if sex==0 :       #female
        BMR=655+(bodyweight*9.6)+(1.8*height)-(4.7*age)
    else:             #male
        BMR=66+(bodyweight*13.7)+(5*height)-(6.8*age)
    
    #Get TDEE with respect to different daily activity 
    if activity==0 : #low
        TDEE=BMR*1.2
    elif activity==1 : #medium
        TDEE=BMR*1.55
    else:  #high
        TDEE=BMR*1.9

    return TDEE


# In[65]:


def desired_nutrition(goal,TDEE):

    #Get daily energy required due to different purpose
    if goal==0 :   #cutting
        energy=TDEE-300
    elif goal==1 : #standard
        energy=TDEE
    else  :  #Bulking
        energy=TDEE+400

    #according to Taiwan Ministry of Health and Welfare ,
    #carbonhydrate(4 cal/gram) should account for 50% ,protein(4cal/gram) 25%,fat(9cal/gram) 25% 
    c=(energy*0.5)/4
    p=(energy*0.25)/4
    f=(energy*0.25)/9  

    return energy,c,p,f


''' used to check the function
e,c,p,f=desired_nutrition(1,2100)
print(e,c,p,f)
'''
        


# GUI

# In[66]:


def main(page: ft.Page):

    page.window_width=1320
    page.window_height=880        #set the GUI page size
    page.window_resizable=False
    page.bgcolor=ft.colors.BLUE_GREY_300    #set page color

    global user_result                 #initialize
    user_result=0
    global index
    index = 0
    
    
    def page_next(e):                   #used to switch pages(page up )
        global index
        index=index+1

        Intro_title.visible=True if index==0 else False
        blank_intropage.visible=True if index==0 else False
        blank_intropage1.visible=True if index==0 else False
        page_intro.visible=True if index==0 else False
        title.visible=False if index==0 else True
        blank.visible=False if index==0 else True

        P2_data.visible= True if index==1 else False
        
        P3_data.visible=True if index==2 else False
        
        P4_select.visible=True if index ==3 else False
        goal.visible=True if  user_result==1 else False
        t_energy.visible=True if user_result==1 else False
        goal_diabetes.visible=False if user_result==1 else True
        t_energy_diabetes.visible=False if user_result==1 else True

        next_page_button.visible=False if index==3 else True # index=3  -->last page ,there's no more pages to go(no more page to go forward)
        last_page_button.visible=False if index==0 else True # index=0  -->first page ,there's no more pages to go(no more page to go backward)

        page.update()
    
    def page_last(e):                    #used to switch pages(page down )
        global index
        index=index-1

        Intro_title.visible=True if index==0 else False
        blank_intropage.visible=True if index==0 else False
        blank_intropage1.visible=True if index==0 else False
        page_intro.visible=True if index==0 else False
        title.visible=False if index==0 else True
        blank.visible=False if index==0 else True

        P2_data.visible= True if index==1 else False
        
        P3_data.visible=True if index==2 else False
        
        P4_select.visible=True if index ==3 else False
        goal.visible=True if  user_result==1 else False
        t_energy.visible=True if user_result==1 else False
        goal_diabetes.visible=False if user_result==1 else True
        t_energy_diabetes.visible=False if user_result==1 else True

        next_page_button.visible=False if index==3 else True # index=3  -->last page ,there's no more pages to go(no more page to go forward)
        last_page_button.visible=False if index==0 else True # index=0  -->first page ,there's no more pages to go(no more page to go backward)

        page.update()
    
    def Bmi_calculate(e):                                   #used to calculate the BMI and the function of BMI calculate button
        global bmi,weight_value,height_value
        height_value=float(height.value)
        weight_value=float(weight.value)
        bmi=bmi_calculate(height_value,weight_value)   
        t_bmi.value=f"Your BMI: {bmi}"
        page.update()


    def get_ML_result(e):
        global user_result
        global accuracy,age_value
        pregnancies_value=float(pregnancies.value)
        glucose_value=float(glucose.value)
        bloodpressure_value=float(bloodpressure.value)
        skinthick_value=float(skinthick.value)
        insulin_value=float(insulin.value)
        dpf_value=float(dpf.value)
        age_value=float(age.value)

        user__data_dir = {                             #store the user inputs into a dictionary
            'Pregnancies':pregnancies_value,
            'Glucose':glucose_value,
            'BloodPressure':bloodpressure_value,
            'SkinThickness':skinthick_value,
            'Insulin':insulin_value,
            'BMI':bmi,
            'DiabetesPedigreeFunction':dpf_value,
            'Age':age_value
                         }
        user_data = pd.DataFrame(user__data_dir, index=[0])                            #arrange
        user_result,accuracy=ML_predict(user_data)                                     #call the ML prediction function
        accuracy=accuracy*100                                                          #get the accuracy
        if user_result==0:
            t_ML.value=f"You might have Diabetes! (prediction with accuracy of {accuracy}%)"
            t_ML.bgcolor=ft.colors.RED_300
        else:
            t_ML.value=f"You are healthy! (prediction with accuracy of {accuracy}%)"
            t_ML.bgcolor=ft.colors.GREEN_300
    
        page.update()


    
    def nutrition(e):
        global protein,carbon,fat,desired_energy,tdee
        global activity_index,sex_index,goal_index

        if activity.value=="Low" :                     #set these indexs of the function 
            activity_index=0
        elif activity.value=="Medium":
            activity_index=1
        else:
            activity_index=2

        if gender.value=="Female":
            sex_index=0
        else:
            sex_index=1

        if user_result==1:
            if goal.value=="Cutting":
                goal_index=0
            elif goal.value=="Standard":
                goal_index=1
            else:
                goal_index=2
        else:
            goal_index=1

        tdee=calculate_desire_TDEE(activity_index,weight_value,sex_index,age_value,height_value)          #Get TDEE
        desired_energy,carbon,protein,fat=desired_nutrition(goal_index,tdee)                             #Get the energy needed,and the portions of each nutritions

        t_TDEE.value=f"Accodring to your activity volume {activity.value}, yout TDEE is {tdee} kcal"
        t_energy.value=f"For {goal.value} goal, you should have {desired_energy} kcal per day"
        t_energy_diabetes.value=f"To control your diabetes,it's sugguested to have {desired_energy} kcal per day"
        t_protein.value=f"| Protein: {protein}  grams | "
        t_carb.value=f"| Carbonhydrate: {carbon} grams |"
        t_fat.value=f"Fat: {fat} grams"
        page.update()




        


    img=ft.Image(src="./image/AI_doctor.png",width=480,height=480)     #import the images
    img_diet=ft.Image(src="./image/diet.png",width=550,height=550)
    
    height = ft.TextField(label="Enter height (unit:meter)")                         #the input sections
    weight = ft.TextField(label="Enter weight (unit:Kg)")
    pregnancies = ft.TextField(label="Enter Pregnancies (If no, please input 0)")
    glucose = ft.TextField(label="Enter glucose (0~200)")
    bloodpressure = ft.TextField(label="Enter avgerage blood pressure(unit:mmHg)")
    skinthick=ft.TextField(label="Enter the current skin thickness (0~100)")
    insulin=ft.TextField(label="Enter the current insulin value (0~846)")
    age=ft.TextField(label="Enter the Age")

    dpf=ft.Dropdown(label="Diabetes Predict Function",                                        #dropdowns
                    hint_text="selcet a most approach Diabetes Predict Function (0.0~2.4)",
                    options=[
                        ft.dropdown.Option("0.0"),
                        ft.dropdown.Option("0.05"),
                        ft.dropdown.Option("0.1"),
                        ft.dropdown.Option("0.33"),
                        ft.dropdown.Option("0.38"),
                        ft.dropdown.Option("0.47"),
                        ft.dropdown.Option("0.626"),
                        ft.dropdown.Option("1.0"),
                        ft.dropdown.Option("1.5"),
                        ft.dropdown.Option("2.0"),
                        ft.dropdown.Option("2.4"),
                            ],
                        autofocus=True,
                        
                    )
    activity=ft.Dropdown(label="Your daily activity",
                    
                    options=[
                        ft.dropdown.Option("Low"),
                        ft.dropdown.Option("Medium"),
                        ft.dropdown.Option("High")
                            ],
                        autofocus=True,
                        width=400
        
                    )
    goal=ft.Dropdown(label="Diet Goal ",
                    hint_text="selcet your expected diet goal ",
                    options=[
                        ft.dropdown.Option("Cutting"),
                        ft.dropdown.Option("Standard"),
                        ft.dropdown.Option("Bulking"),
                            ],
                        autofocus=True,
                        width=400,
                        visible=False
                    )
    goal_diabetes=ft.Dropdown(label="Diet Goal (You might have diabetes, so this option is set to Standard option)",       #when the user has diabetes，lock this dropdown
                        autofocus=True,
                        width=400
            
                    )
    gender=ft.Dropdown(label="Sex ",
                  
                    options=[
                        ft.dropdown.Option("Male"),
                        ft.dropdown.Option("Female"),
                        
                            ],
                        autofocus=True,
                        width=400
            
                    )
   
    bmi_button=ft.FilledButton(text="Enter (Please make sure to enter,or prediction can't be done correctly)", width=490, on_click=Bmi_calculate)        #buttons
    ML_button=ft.FilledButton(text="Start ML prediction", width=200, on_click=get_ML_result)
    next_page_button=ft.FilledButton(text="Next page", width=150,on_click=page_next)
    last_page_button=ft.FilledButton(text="Last page", width=150,on_click=page_last,visible=False) #initial index=0(first page,so there's no page to go backward)
    nutrition_button=ft.FilledButton(text="Enter ",width=150,on_click=nutrition)

    title=ft.Text("       Diabetes Prediction ML and nutrition suggest system ",style=ft.TextThemeStyle.DISPLAY_MEDIUM,visible=False)
    t_ML=ft.Text(size=25)
    t_bmi=ft.Text(size=40)
    blank_intropage=ft.Text("  ",style=ft.TextThemeStyle.DISPLAY_LARGE)        #empty block is used to make the page more readable
    blank_intropage1=ft.Text("  ",style=ft.TextThemeStyle.DISPLAY_LARGE)
    blank=ft.Text("  ",style=ft.TextThemeStyle.DISPLAY_SMALL,visible=False)
    blank1=ft.Text("  ",style=ft.TextThemeStyle.DISPLAY_SMALL)
    t_intro=ft.Text("This is a Diabetes prediction and nutrition suggest system.The system will calculate your BMI first .T you might be required to input some informations about your body.The system will based on the result,and give you some suggests. ",size=20,width=700)
    Intro_title=ft.Text("              Diabetes Prediction ML and nutrition suggest system ",size=40)
    t_nutrition_title=ft.Text("       Nutrition suggests: ",size=30)
    t_p4_blank0=ft.Text("<------------------------------------------------------>",size=30)
    t_TDEE=ft.Text(size=20)
    t_energy=ft.Text(size=20,visible=False)
    t_energy_diabetes=ft.Text(size=20)
    t_protein=ft.Text(size=20)
    t_carb=ft.Text(size=20)
    t_fat=ft.Text(size=20)


    #stores the features of the same page into a list(easier to manage) 
    intro_list=[t_intro,img] 
    page_intro=ft.Row(intro_list,alignment=ft.MainAxisAlignment.CENTER)
    
    page_change_list=[last_page_button,next_page_button]                            #arrange the page change button
    page_change=ft.Row(page_change_list,alignment=ft.MainAxisAlignment.END)

    P2_list=[height,weight,bmi_button,t_bmi]                                        #used to manage all items in Page 2
    P2_data=ft.Column(P2_list,alignment=ft.MainAxisAlignment.CENTER,visible=False)

    P3_list=[pregnancies,glucose, bloodpressure,skinthick,insulin,dpf,age,ML_button,t_ML]   #used to managed all items in page3
    P3_data=ft.Column(P3_list,alignment=ft.MainAxisAlignment.CENTER,visible=False)

    P4_select_list_left=[t_nutrition_title,activity,goal,goal_diabetes,gender,nutrition_button,t_p4_blank0,t_TDEE,t_energy,t_energy_diabetes,t_protein,t_carb,t_fat]
    diet_select_left=ft.Column(P4_select_list_left,alignment=ft.MainAxisAlignment.CENTER)
    P4_select_list=[diet_select_left,img_diet]
    P4_select=ft.Row(P4_select_list,alignment=ft.MainAxisAlignment.CENTER,visible=False)

    page.add(blank_intropage1,Intro_title,blank_intropage,page_intro)
    page.add(title,blank)
    page.add(P2_data)
    page.add(P3_data)
    page.add(P4_select)
    page.add(blank1,page_change)



ft.app(target=main)


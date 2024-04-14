from tkinter import  *
Screen=Tk()
Screen.title("BMI Calculator")
Screen.minsize(400,400)

user_weight=Entry()
user_weight.place(x=140,y=125)
user_weight_text=Label(text="Enter your weight (kg)")
user_weight_text.place(x=150,y=100)
user_height=Entry()
user_height.place(x=140,y=175)
user_height_text=Label(text="Enter your weight (cm)")
user_height_text.place(x=150,y=150)


def BMI():
    try:
        weight = float(user_weight.get())
        height = float(user_height.get()) / 100
        bmi = weight / (height ** 2)

        if bmi <= 18.5:
            print("Zayıf")
        elif bmi <= 24.9:
            print("Normal")
        elif bmi <= 29.9:
            print("Kilolus")
        elif bmi <= 34.9:
            print("1.dereceden Obez")
        elif bmi <= 39.9:
            print("2.Dereceden obez")
        else:
            print("3.Dereceden obez")


    except:
         print("Enter a valid number!")

calculate_button=Button(text="Calculate",command=BMI)
calculate_button.place(x=175,y=225)
Screen.mainloop()
import tkinter as tk  
import pandas as pd
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


name = input("Please Enter Your Name: \n ")
age = int(input("Please Enter Your Age: \n "))
gender = input("Please Enter Your Gender: \n ")

window = tk.Tk()
window.title('COVID 19 - Investigation Process')
window.geometry('800x600')

l = tk.Label(window, bg='light blue', width=65, text='',pady=20,padx=10,borderwidth=4)

l.pack()


Fever=tk.DoubleVar()
DryCough=tk.DoubleVar()
Tiredness=tk.DoubleVar()
losstastesmell=tk.DoubleVar()
MostCommonSymptoms=tk.DoubleVar()
LessCommonSymptoms = tk.DoubleVar()
AchesPains= tk.DoubleVar()
SoreThroat=tk.DoubleVar()
Diarrhoea=tk.DoubleVar()
headache=tk.DoubleVar()
Conjunctivitis=tk.DoubleVar()
SeriousSymptoms=tk.DoubleVar()
DifficultyBreathing=tk.DoubleVar()
ChestPain=tk.DoubleVar()  
LossofSpeech=tk.DoubleVar()


def print_selection():
    df = pd.DataFrame(columns=['Symtoms','Response','Prob'])
    df['Symtoms'] = ["Fever", "DryCough", "Tiredness", "losstastesmell","AchesPains", "SoreThroat", "Diarrhoea", "Conjunctivitis","headache", "DifficultyBreathing", "ChestPain", "LossofSpeech"]
    
    if (var1.get() == 1):
        Fever =0.05
    else:
        Fever =0
        
    if (var2.get() == 1):
        DryCough=0.05
    else:
        DryCough=0
        
    if (var3.get() == 1):
        Tiredness=0.05
    else:
        Tiredness=0
        
    if (var4.get() == 1):
        losstastesmell=0.05
    else:
        losstastesmell=0
    if (var11.get() == 1):
        AchesPains =0.07
    else:
        AchesPains =0
    if (var12.get() == 1):
        SoreThroat=0.07
    else:
        SoreThroat=0
    if (var13.get() == 1):
        Diarrhoea=0.07
    else:
        Diarrhoea=0
    if (var14.get() == 1):
        Conjunctivitis=0.07
    else:
        Conjunctivitis=0
    if (var15.get() == 1):
        headache=0.07
    else:
        headache=0
    if (var21.get() == 1):
        DifficultyBreathing =0.15
    else:
        DifficultyBreathing =0
    if (var22.get() == 1):
        ChestPain=0.15
    else:
        ChestPain=0
    if (var23.get() == 1):
        LossofSpeech=0.15
    else:
        LossofSpeech=0
    df['Response'] = [var1.get(),var2.get(),var3.get(),var4.get(),var11.get(),var12.get(),var13.get(),var14.get(),var15.get(),var21.get(),var22.get(),var23.get()]
    df['Prob'] = [Fever,DryCough,Tiredness,losstastesmell,AchesPains,SoreThroat,Diarrhoea,Conjunctivitis,headache,DifficultyBreathing,ChestPain,LossofSpeech]
    return df

def final_selection():
    x=print_selection()
    final_value=round(x['Prob'].sum(),3)     
    return final_value


## Assign the value from the Checkbox to Variable for Most Common Symptoms
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()

tk.Label(window, 
         text="1. Most Common Symptoms:",
         fg = "light green",
         bg = "dark green",
         font = "Helvetica 16 bold italic").pack()

c1 = tk.Checkbutton(window, text='1.Fever',variable=var1, onvalue=1, offvalue=0, command=final_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='2.Dry Cough',variable=var2, onvalue=1, offvalue=0, command=final_selection)
c2.pack()
c3 = tk.Checkbutton(window, text='3.Tiredness',variable=var3, onvalue=1, offvalue=0, command=final_selection)
c3.pack()
c4 = tk.Checkbutton(window, text='4.Loss of Taste/Smell ',variable=var4, onvalue=1, offvalue=0, command=final_selection)
c4.pack()

## Assign the value from the Checkbox to Variable for Less Common Symptoms
var11 = tk.IntVar()
var12 = tk.IntVar()
var13 = tk.IntVar()
var14 = tk.IntVar()
var15 = tk.IntVar()

tk.Label(window, 
         text="2. Less Common Symptoms:",
         fg = "light green",
         bg = "dark green",
         font = "Helvetica 16 bold italic").pack()

c11 = tk.Checkbutton(window, text='1.Aches and Pains',variable=var11, onvalue=1, offvalue=0, command=final_selection)
c11.pack()
c12 = tk.Checkbutton(window, text='2.Sore Throat',variable=var12, onvalue=1, offvalue=0, command=final_selection)
c12.pack()
c13 = tk.Checkbutton(window, text='3.Diarrhoea',variable=var13, onvalue=1, offvalue=0, command=final_selection)
c13.pack()
c14 = tk.Checkbutton(window, text='4.Conjunctivitis',variable=var14, onvalue=1, offvalue=0, command=final_selection)
c14.pack()
c15 = tk.Checkbutton(window, text='5.Headache',variable=var15, onvalue=1, offvalue=0, command=final_selection)
c15.pack()

## Assign the value from the Checkbox to Variable for Serious Symptoms
var21 = tk.IntVar()
var22 = tk.IntVar()
var23 = tk.IntVar()

tk.Label(window, 
         text="3. Serious Symptoms:",
         fg = "light green",
         bg = "dark green",
         font = "Helvetica 16 bold italic").pack()

c21 = tk.Checkbutton(window, text='1.Difficulty in Breathing',variable=var21, onvalue=1, offvalue=0, command=final_selection)
c21.pack()
c22 = tk.Checkbutton(window, text='2.Chest Pain or Pressure',variable=var22, onvalue=1, offvalue=0, command=final_selection)
c22.pack()
c23 = tk.Checkbutton(window, text='3.Loss of Speech or Movement',variable=var23, onvalue=1, offvalue=0, command=final_selection)
c23.pack()

def covid_logic():
    covid=final_selection()
    if (covid <= 0.30):
        message= 'You do not have COVID-19. Take rest'
    elif(covid > 0.30 and covid <=0.60):
        message= 'Less likely of having COVID-19. Please go for a checkup'
    elif(covid > 0.60):
        message= 'High chances of having COVID-19'
    
    l.config(text=message+', Probability is '+str(covid))
    message1=message+' with chances '+str(covid)
    return message1

def plot_pdf():
        
    with PdfPages(r'covid_report.pdf') as export_pdf:
        
        df1 = print_selection()
        plt.figure(figsize=(16, 8))
        plt.text(0.40,0.9,'COVID REPORT', size=24,color='blue') 
        plt.text(0.03,0.7,'Patient Name : '+name, size=20 ) 
        plt.text(0.03,0.6,'Patient Age : '+str(age), size=20 ) 
        plt.text(0.03,0.5,'Patient Gender : '+gender, size=20) 
        message = covid_logic()
        plt.text(0.03,0.3,message, size=24,color='red')
        export_pdf.savefig()
        plt.close()
        
        plt.figure(figsize=(16, 8))
        plt.bar(df1['Symtoms'], df1['Response'], color='blue')
        plt.title('SYMPTOMS Vs RESPONSE', fontsize=10)
        xlabel('SYMPTOMS', fontsize=8 )
        ylabel('RESPONSE', fontsize=8)
        plt.grid(True)
        export_pdf.savefig()
        plt.close()
    
        df2 = print_selection()
        plt.figure(figsize=(16, 8))
        plt.bar(df2['Symtoms'], df2['Prob'], color='red')
        plt.title('SYMPTOMS Vs PROBABILTY', fontsize=10)
        xlabel('SYMPTOMS', fontsize=8 )
        ylabel('PROBABILTY', fontsize=8)
        plt.grid(True)
        export_pdf.savefig()
        plt.close()


c31=tk.Button(window, text='GENERATE REPORT', fg="red", command=covid_logic)
c31.pack(side=tk.LEFT)
c32=tk.Button(window, text='EXPORT COVID RESULT TO PDF', fg="red", command=plot_pdf)
c32.pack(side=tk.RIGHT)
window.mainloop()






# importing every object from tkinter module
from cmath import e
from textwrap import fill
from tkinter import *
from turtle import back

# creating module
class App:
    def __init__(self):
        # creating Tk windows
        root = Tk()

        # specs of tk windows
        root.title("Loan Calculator")

        # unreasizable windows
        root.resizable(height=False, width=False)

        # setting back-ground color to windows
        root.configure(background = "light green")        

        # creating labels
        Label(root, font="Helvetica 12 bold", bg="light green", text="Annual Interest Rate").grid(row=1, column=1, sticky=W)
        Label(root, font="Helvetica 12 bold", bg="light green", text="NUmber of Years").grid(row=2, column=1, sticky=W)
        Label(root, font="Helvetica 12 bold", bg="light green", text="Loan Amount").grid(row=3, column=1, sticky=W)
        Label(root, font="Helvetica 12 bold", bg="light green", text="Monthly Payment").grid(row=4, column=1, sticky=W)
        Label(root, font="Helvetica 12 bold", bg="light green", text="Total Payment").grid(row=5, column=1, sticky=W)

        # accepting inputs for labels from user
        self.annualInterestRateVar = StringVar()
        Entry(root, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1, column=2)
        self.numberofYearsVar = StringVar()
        Entry(root, textvariable=self.numberofYearsVar, justify=RIGHT).grid(row=2, column=2)
        self.loanAmountVar = StringVar()
        Entry(root, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)

        # labels for montly and total payment
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(root, textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)

        self.totalPaymentVar = StringVar()
        lblTotalPaymentVar = Label(root, textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)

        # compute payment
        btComputePayment = Button(root, text="Compute Payment", bg="red", fg="white", font="Helvetica 14 bold", command=self.computePayment).grid(row=6, column=2, sticky=E)

        # clear button
        btClear = Button(root, text="Clear", bg="blue", fg="white", font="Helvetica 14 bold", command=self.delete_all).grid(row=6, column=8, padx=20, pady=20, sticky=E)

        root.mainloop()

    # compute 
    def computePayment(self):
        # setting parameters for getMontlyPayment function
        montlyPayment = self.getMontlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberofYearsVar.get()))

        # setting montlyPaymetvar label, result
        self.monthlyPaymentVar.set(format(montlyPayment, "10.2f"))

        #print(montlyPayment)
        totalPayment = float(montlyPayment * 12 \
            * int(self.numberofYearsVar.get()))

        # setting totalPaymentVar label, result
        self.totalPaymentVar.set(format(totalPayment, "10.2f"))
    
    # calculating montly payment
    def getMontlyPayment(self, loanAmount, montlyInterestRate, numberofYears):
        montlyPayment = loanAmount * montlyInterestRate / (1-1/(1 + montlyInterestRate) ** (numberofYears * 12))
        return montlyPayment

    # deleting all information to calculate new
    def delete_all(self):
        self.monthlyPaymentVar.set("")
        self.loanAmountVar.set("")
        self.annualInterestRateVar.set("")
        self.numberofYearsVar.set("")
        self.totalPaymentVar.set("")
        

# calling class
App()
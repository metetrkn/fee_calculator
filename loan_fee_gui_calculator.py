from tkinter import *

# Creating the Loan Calculator class
class App:
    def __init__(self):
        # Creating the Tkinter window
        root = Tk()

        # Setting window title and making it unresizable
        root.title("Loan Calculator")
        root.resizable(height=False, width=False)

        # Setting background color for the window
        root.configure(background="light green")

        # Creating labels for input fields
        Label(root, font="Helvetica 12 bold", bg="light green", text="Annual Interest Rate").grid(row=1, column=1, sticky=W)
        Label(root, font="Helvetica 12 bold", bg="light green", text="Number of Years").grid(row=2, column=1, sticky=W)
        Label(root, font="Helvetica 12 bold", bg="light green", text="Loan Amount").grid(row=3, column=1, sticky=W)
        Label(root, font="Helvetica 12 bold", bg="light green", text="Monthly Payment").grid(row=4, column=1, sticky=W)
        Label(root, font="Helvetica 12 bold", bg="light green", text="Total Payment").grid(row=5, column=1, sticky=W)

        # Creating input fields for the labels
        self.annualInterestRateVar = StringVar()
        Entry(root, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1, column=2)
        self.numberofYearsVar = StringVar()
        Entry(root, textvariable=self.numberofYearsVar, justify=RIGHT).grid(row=2, column=2)
        self.loanAmountVar = StringVar()
        Entry(root, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)

        # Labels for displaying monthly and total payment
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(root, textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)

        self.totalPaymentVar = StringVar()
        lblTotalPaymentVar = Label(root, textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)

        # Compute Payment button
        btComputePayment = Button(root, text="Compute Payment", bg="red", fg="white", font="Helvetica 14 bold", command=self.computePayment).grid(row=6, column=2, sticky=E)

        # Clear button
        btClear = Button(root, text="Clear", bg="blue", fg="white", font="Helvetica 14 bold", command=self.delete_all).grid(row=6, column=8, padx=20, pady=20, sticky=E)

        root.mainloop()

    # Function to compute the payment
    def computePayment(self):
        # Calculate the monthly payment using the input values
        montlyPayment = self.getMontlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberofYearsVar.get()))

        # Update the monthly payment label with the calculated value
        self.monthlyPaymentVar.set(format(montlyPayment, "10.2f"))

        # Calculate the total payment
        totalPayment = float(montlyPayment * 12 * int(self.numberofYearsVar.get()))

        # Update the total payment label with the calculated value
        self.totalPaymentVar.set(format(totalPayment, "10.2f"))


    # Function to calculate the monthly payment
    def getMontlyPayment(self, loanAmount, montlyInterestRate, numberofYears):
        # Calculate the monthly payment using the given formula
        montlyPayment = loanAmount * montlyInterestRate / (1-1/(1 + montlyInterestRate) ** (numberofYears * 12))
        return montlyPayment

    # Function to clear all input fields and payment labels
    def delete_all(self):
        self.monthlyPaymentVar.set("")
        self.loanAmountVar.set("")
        self.annualInterestRateVar.set("")
        self.numberofYearsVar.set("")
        self.totalPaymentVar.set("")

# Instantiate the Loan Calculator class
App()


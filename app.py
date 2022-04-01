from flask import Flask, request, render_template
import pickle
model = pickle.load(open('loan.pkl', 'rb'))


app=Flask(__name__)

@app.route('/predict', methods=['GET','POST'])
def input():
    if request.method=="POST":
        details=request.form
        gender=details['gender']
        md=details['married']
        dpdents=details['dependents']
        edu=details['education']
        selemp=details['selfemployed']
        applincome=details['applicantIncome']
        coapplincome=details['coapplicantIncome']
        loanmt=details['loanAmount']
        loanterm=details['loanterm']
        cdhistory=details['credit history']
        proparea=details['propertyarea']
        
        pred=model.predict([[gender,md,dpdents,edu,selemp,applincome,coapplincome,loanmt,loanterm,cdhistory,proparea]])
        
        if (pred[0] > 0.5):
            return render_template('Loan_App_Template.html', msg='RESULTS:  Loan Approved')

        else:
            return render_template('Loan_App_Template.html', msg='RESULTS:  Loan Rejected')
@app.route('/')
def submit():
    return render_template('Loan_App_Template.html')

if __name__ == '__main__':
    app.run(debug=True)

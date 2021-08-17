# Decision Tree Classifications
This Exercise involved looking at old data from a lending service. The idea was to create a decision tree model for looking at potential customers who paid off their loans in full. This involved doing exploratory data analysis and creating a machine learning model of the not fully paid information to see did people usualyy tend to pay out their loans.

the first plot created was used to look at how the fico score of individuals compared to the companys credit policy compared together. Graph shows a tipping point around 660 fico score of people passing the credit policy check and being able to apply for a loan. Red color shows individual fico scores that were rejected and blue color the ones that were qualified for a loan.

![The data file itself](https://github.com/viltsu123/basic_python_practice/blob/master/data_analysis_learning/DecisionTreeExercise/ExpDataAnalysisOne.png)

The next plot generated was used to look at the interest rates applied to different fico scores and to see how they correlated. The blunt interpretation is that the higher the fico score, the lower the interest rate tended to be.

![The data file should be here](https://github.com/viltsu123/basic_python_practice/blob/master/data_analysis_learning/DecisionTreeExercise/ficotinterest.png)

Third we looked at the loan purposes and if they had been fully paid back. This would show some categorical information about the loans and whether people were paying it back. Graph shows how debt management was the main purposes for loans taken out and that type of loan had the highest return rate on the loans being paid back.

![The data plot](https://github.com/viltsu123/basic_python_practice/blob/master/data_analysis_learning/DecisionTreeExercise/LoanPurposeCount.png)

Finally we looked at the interest rate and fico scores on loans that were paid back and not paid back and if they passed the credit policy of the company. It is visible that people who passed the credit policy and had higher fico scores tended to have lower interest rates and were able to pay back their loans in full.

![The data plot should be here](https://github.com/viltsu123/basic_python_practice/blob/master/data_analysis_learning/DecisionTreeExercise/ficointcredpol.png)

Then we preceded to create a decision tree classifier model that predicted if loans were going to be paid back in full. We used a Decision Tree Classifier and a Random Forest Classifier model to see if predictions and confusion matrix results would differ and to see which performed better on this instance. End result seemed to favor the Decision Tree Classifier model as classification reports showed higher accuracy on recall and f1-score values. Also the confusion matrix showed better predictions of loans being paid with the Decision Tree Classifier model.:robot:

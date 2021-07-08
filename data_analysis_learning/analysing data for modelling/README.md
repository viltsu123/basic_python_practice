# Data analysis
We have a task: you are a serious data analyzer that has been employed by a poor store owner. The owner wants to see if he/she/they can improve their stores revenue by looking at some relevant data. The tools in use are python (numpy, pandas, matplotlib and seaborn) and finally scikit_learn. First you got to get the data and make some sense of it, what is it telling you about the customers and so on. Then you have to see if there is something you can do with machine learning (linear regression) to help make clear to the owner what he/she/they/it can do to save their business!

So lets look at some graphs to make sense of this data:

![The data file itself](https://github.com/viltsu123/basic_python_practice/blob/master/data_analysis_learning/analysing%20data%20for%20modelling/Ecommerce%20Customers)

That is a readable file and pandas will read it as a csv so no worries about the file type :smile:

So next we have to make some sense of this, so that we can help our poor store owner.

Time on Website vs Yearly Amount Spent:
![The photo would go here](https://github.com/viltsu123/basic_python_practice/blob/master/data_analysis_learning/analysing%20data%20for%20modelling/TimeWbVsSpent.png)

Looking at this photo we can see that around 37 minutes (x axis) seems to be the sweet spot for maximum spending (y axis) on customers visiting the stores website. Lets see if the same carries over to people using the stores phone application.

Time on App vs Yearly Amount Spent:
![The photo here please](https://github.com/viltsu123/basic_python_practice/blob/master/data_analysis_learning/analysing%20data%20for%20modelling/AppvsSpending.png)
So this tells us that shorter time is needed for same kind of spending from customers. The application is providing the same level of revenue in a shorter time so looking good, lets see if the customers using the app are new members or established ones.

Length of Memebership vs Time on App:
![Photo please](https://github.com/viltsu123/basic_python_practice/blob/master/data_analysis_learning/analysing%20data%20for%20modelling/MembersVsApp.png)
Somewhat established members are the main users on the app, lets take a look at how these values correlate to each other:

Comprehensive plot:
![Photo would be nice](https://github.com/viltsu123/basic_python_practice/blob/master/data_analysis_learning/analysing%20data%20for%20modelling/pairplotWholeSet.png)

interesting stuff, something about the Length of Memebership and Yearly amount spent that have a more correlated line.... Lets see if these two sit well on a linearmodel plot!

Yearly amount spent vs Length of Membership:
![Wheres the photo](https://github.com/viltsu123/basic_python_practice/blob/master/data_analysis_learning/analysing%20data%20for%20modelling/linearplot.png)

Well it looks like the more experienced members tend to spend more on a yearly level, of course the bulk of the stores revenue seems to be coming from the customers who have been a member for a couple of months/years/weeks (not sure what the kind is for the Length of Membership :smile:).

After some nifty machine guessing we are able to produce an output that looks like this:
![What, no photo](https://github.com/viltsu123/basic_python_practice/blob/master/data_analysis_learning/analysing%20data%20for%20modelling/Screenshot%202021-07-08%20at%2014.46.39.png)
The lines we would be interested in are the coefficient lines. values that went into the making of the coefficient dataframe are the training materials gotten from the origianl dataframe that carries info about the store. Yearly amount spent is put in the dataframe that will be handled as the "real values" and then info about the customers behaviour is put in the dataframe we used to calculate predictions.

The coefficient dataframe reads so that a one unit increase in the Length of Membership would equate to a 61,28$ return. And this is true for the other values as well. We were looking for ways to make the store revenues go up, and looking at the numbers here, an investment into the mobile app development and the membership promotion (to get more members) would be a step in the right direction. Of course we could look at this from the perspective of making the Web app better so as to catch up with the mobile app revenues. More comparing can be done on that front before a decision is reached :smile:

So this was a first example of using some dataframe magic and great machine learning library together to produce viable results in improving ones revenue stream :feelsgood: stay tuned for more! :cowboy_hat_face:

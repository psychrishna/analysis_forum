# analysis_forum
Analysis forum, or better known as “Perception”, is used to visualise data and analyse it. 
When the user uploads a dataset, the backend process the data on the go and provides suitable options to plot the data for analysis. 
The webApp provides six types of visualisations, viz: bar chart, pie chart, polar area, scatter plot, line chart and linear regression. 
This aids the user in detecting patterns, trends, and outliers in groups of data. 
Linear regression is used to model selective features from the dataset. 
The line of best fit is plotted and the user can supply X values to predict Y values.

Frameworks:
  Frontend:
    jQuery
    AngularJS
    Bootstrap
  Backend:
		Django
    
Libraries : 
  numpy
  pandas
  sklearn
  jQuery
  chartJS

Languages: 
  HTML
  CSS
  JavaScript
  Python
	
Techniques Implemented:
1.Predictive Fetch:
	When user selects the x-axis and y-axis to chart a graph, the user is likely to try out other combinations as well. The first request is sent for the selected columns as well as for 2 other similar columns. Similar in the sense that the columns have same data types/similar values. These values are then stored in the Local Storage. To plot the next graph, server need not be contacted! 
2. Multi-Stage Download:
	The training for linear regression takes up a fair bit of time in most cases. To show that the browser is responsive, a loading gif is made use of while awaiting the response from the server.
3.Rest API :
	The webApp makes use of the Rest API to contact the server. Each functionality has a unique URL that triggers the respective functions on the server. The server does not maintain any ‘state’ information. Cookies are used in order to verify identity of the client.

Intelligent Functionality:
  The entire Web App makes use of intelligence to handle data on the fly. The user is allowed to upload a csv without any restrictions on the number of columns or type of data present in it. The backend being built on Django enables the use of Python in a wholesome manner. Using pythons pandas library we are able to extract useful columns from the database and send it back to client so that data visualization can be done. 
  We have built a sample neural net in the backend using the scikit learn library which is been trained is order to perform linear regression(ie) learning the slope and intercept of the given set of points. This trained model is then used to predicted the dependant variable when independent variable is queried. So based on the selected columns the model is trained and used for prediction.   

Testing Code to be added soon
	

# Movie-Recommender-System1
A Content Based Movie Recommender System using Machine Learning
First of all What is a Recommender System?
Recommender systems are the systems that are designed to recommend things to the user based on many different factors. These systems predict the most likely product that the users are most likely to purchase and are of interest to.We all have used services like Netflix, Amazon, and Youtube. These services use very sophisticated systems to recommend the best items to their users to make their experiences great.

Theory of the Recommender system:
The purpose of a recommender system is to suggest relevant items to users. To achieve this task, there exist two major categories of methods:
1.collaborative filtering methods
2.content based methods

In this project we will work with the content based recommender system

A Content based recommender system works with data that the user provides, either explicitly (rating) or implicitly (clicking on a link). Based on that data, a user profile is generated, which is then used to make suggestions to the user. As the user provides more inputs or takes actions on the recommendations, the engine becomes more and more accurate.

I have taken the tmdb dataset from the kaggle,the main aim of this project is to recommend the best 5 recommended movies related to the movie which is inputted by the user and after that make a website on it using Python streamlit server and also deploying the model in any cloud platform(I have uploaded it in Heroku)

You can go through this link to check the webapp I made for this recommeder system-https://movie-recommender-system12.herokuapp.com/

step-1: Select any movie of your choice
![image](https://user-images.githubusercontent.com/71590118/135730734-bd7cd91e-32b0-4036-8591-b933d6ced612.png)

step-2: Type on the Related Searches button to see the movies which is recommended by the model(After clicking on the button You will see 5 recommended movies predicted by the model)
![image](https://user-images.githubusercontent.com/71590118/135730807-91518d7c-0906-45a3-b980-506feb9d720f.png)

So from the above You can see that the model predicts exactly the movies which are related to what the user has searched.

You can go through the jupyter notebook that I have uploaded the code is readable and I have added comments all around and explained each steps so that a beginner who wants to learn about recommender system can understand without any problem or hesitation

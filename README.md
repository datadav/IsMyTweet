# ITC Hackathon - IsMyTweet



*Authors : Alexis AMSELLEM, David BLOCH, David Jacob COHEN, David COHEN*

This repository is the Hackathon ITC 2018 app we created.  
IsMyTweet is an app that allows influencer twitter to be folow and detect whether the content of new message tweeted comply to the usual style of the influencer.
For now the app isn't still deployed, but you can use it in local by running the app Flask.  
 

### Installation   
InIsMytTweet uses an "intelligent" algorithm containing  Machine Learning and Natural Language Processing to detect the most suspicous tweets.  
See requirements.txt for the list of all the required packages.  
Creating a virtual environment is recommanded, then you can install all the requirements  
```
pip install git+https://github.com/erikavaris/tokenizer.git  
pip install -r requirements.txt
```  
Then you can run the flask APP : 
```
export FLASK_APP=app.py
flask run
```  
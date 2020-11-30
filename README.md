# Lawyers_Twitter_Turnover
## 1. Introduction
In the management world, it is important to not only satisfy your customers, but to satisfy your hardworking employees. How well your finance and accounting group is good at keeping balance sheet intact, if your employees are not satisfied with your company, you will lose your smartest minds in your company. Therefore, it is important to analyze what makes employees lose faith on their workplace and to analyze what makes them to move from one company to another. In this project, we will touch on how use of social media affect workers to change their workplace.
## 2. About each files
### 1) Find-a-twitter-account-of-a-lawyer-just-by-name
This program uses Python library "tweepy", "xlsxwriter", "xlrd", and "time".</br>
</br>
From existing xlsx file(Schnader_lawfirm_scrapping_sample_excel.xlsx), the code gets names of lawyers that we have previously collected. In this example code, the names of lawyers that we have collected in advance were from lawfirm called Schwabe, Williamson & Wyatt. Then, we will search the name of each lawyers using Twitter API. If there are certain words(i.e. "schwabe", "law", "litigation", "practice", "partner", "legal") that seems like the person is a lawyer, we will print "######### A Lawyer found #########" on the console and write the account id of the lawyer in newly made xlsx file.</br>
</br>
For each lawfirms, the xlsx file filled with collected account id will be saved and we can organize them and use them to collect Twitter activity info of each lawyers.

### 2) Lawfirm_follower_following_account_gathering
This program uses Python library "tweepy", "xlsxwriter", "xlrd", and "time".</br>
</br>
This program is for gathering Twitter account id for lawyers just like program "Find-a-twitter-account-of-a-lawyer-just-by-name". Although the purpose is exactly same this program as very different approach with program "Find-a-twitter-account-of-a-lawyer-just-by-name".</br>
</br>
Before using this code, we need Twitter account id for our targeted lawfirms. As this was not what we could automate, we manually collected about 300 lawfirms' Twitter account ids in a single column of a xlsx file.</br>
</br>
When the Twitter account ids of lawfirms are ready, we will then use Twitter API and Python library "tweepy" to gather Twitter account ids of followers of the lawfirm and Twitter account ids of followings of the lawfirm. Then, for each followers and followings, we will check whether the account seems to be a Twitter account of a lawyer. Also, if there is any mention of the lawfirm from the bio description of the account, then we will identify the account as highly likely account to be a lawyer's account. After running this program, we will get xlsx files that has rows of Twiiter account ids for each lawfirm.

### 3) Gather-tweets-that-each-lawyer-have-tweeted
This program uses Python library "tweepy", "xlsxwriter", "xlrd", and "time".</br>
</br>
This program is for collecting tweet data using Twitter account ids that we have gathered through programs such as "Find-a-twitter-account-of-a-lawyer-just-by-name", "Lawfirm_follower_following_account_gathering".</br> 
Once you have an excel file that has a column of account ids of lawyers, we can use Twitter API and Python library "Tweepy" to get tweets that each lawyers have done. We will use for loop to cover every single Twitter ids that we have gathered and get tweets of them in each single newly made xlsx file. For each loop, we will first get a single Twitter account id. We will get tweets as a single lump using code "tweet_data = tweepy.Cursor(api.user_timeline, id=twitter_account).items()". Then we will organize the single lump of data with for loop to write twitter account id, tweet date, and actual text of each tweet. After running this Python program, we can see all of the tweet data collected in each single xlsx file for each lawyer in a well arraged manner.
 
### 4) Scrapping-lawyers-data-from-lawfirm-Schnader

# Lawyers_Twitter_Turnover
## 1. Introduction
In the management world, it is important to not only satisfy your customers, but to satisfy your hardworking employees. How well your finance and accounting group is good at keeping balance sheet intact, if your employees are not satisfied with your company, you will lose your smartest minds in your company. Therefore, it is important to analyze what makes employees lose faith on their workplace and to analyze what makes them to move from one company to another. In this project, we will touch on how use of social media affect workers to change their workplace.
## 2. About each files
### 1) Scrapping-lawyers-data-from-lawfirm-Schnader
This program uses Python library "requests", "xlsxwriter", "xlrd", and "BeautifulSoup".</br>
</br>
This program is a web-scrapping program that gathers lawyers' information such as name, title, area of practice, location, bachelors degree, and j.d. degree.</br>
</br>
You need to have some background in HTML to handle this code.</br>
</br>
The Python libraries "requests" and "BeautifulSoup" is core web-scrapping program that allows us to get full html code of a single webpage.</br>
</br>
When you think of a webpage that has hundreds of people's bio, you can think of about 20 people's bio in each webpage with multiple pages. Most of such webpages have multiple pages that you can select from page 1, page 2, to the end page. For each webpages that shows about 20 people's short description on their bio, you can click the short description if you want to expand it and see the full bio in a whole new webpage. We will need to consider such rules that most webpages with hundreds of people's bio have.</br>
</br>
The code uses such rules and web-scrap data from lawfirms' webpages. Through some for loops program will loop each bios in lawfirms' bio webpage. Then the code will scrap bio infp such as title, practice, location, bachelors, and jd degrees. The most important part of code that you need to understand is code that resembles "soup.find('span', {'class': "location"}).text.strip()" which is on the 83rd line of the code. The "soup" is entire HTML code that you have scrapped from webpage that you assigned on lawyer_link. Once you have gotten HTML code for the webpage you need, you can use find() to specify exact part of HTML code that you have received. In this case, you are trying to take specific HTML code line that has HTML tag 'span" with HTML class value of 'location'. Then you should make it as a text data in order to save it in xlsx file as text value. You can eliminate any blank spaces on the front and back of your output through strip().</br>
</br>
After repeating this, you can get bio info of hundreds of lawyers from hundreds of lawfirms.</br>
</br>
Limitation for this code is that you have to manually find each HTML tags for each info for every lawfirm which is very time consuming.

### 2) Find-a-twitter-account-of-a-lawyer-just-by-name
This program uses Python library "tweepy", "xlsxwriter", "xlrd", and "time".</br>
</br>
From existing xlsx file(Schnader_lawfirm_scrapping_sample_excel.xlsx), the code gets names of lawyers that we have previously collected. In this example code, the names of lawyers that we have collected in advance were from lawfirm called Schwabe, Williamson & Wyatt. Then, we will search the name of each lawyers using Twitter API. If there are certain words(i.e. "schwabe", "law", "litigation", "practice", "partner", "legal") that seems like the person is a lawyer, we will print "######### A Lawyer found #########" on the console and write the account id of the lawyer in newly made xlsx file.</br>
</br>
For each lawfirms, the xlsx file filled with collected account id will be saved and we can organize them and use them to collect Twitter activity info of each lawyers.

### 3) Lawfirm_follower_following_account_gathering
This program uses Python library "tweepy", "xlsxwriter", "xlrd", and "time".</br>
</br>
This program is for gathering Twitter account id for lawyers just like program "Find-a-twitter-account-of-a-lawyer-just-by-name". Although the purpose is exactly same this program as very different approach with program "Find-a-twitter-account-of-a-lawyer-just-by-name".</br>
</br>
Before using this code, we need Twitter account id for our targeted lawfirms. As this was not what we could automate, we manually collected about 300 lawfirms' Twitter account ids in a single column of a xlsx file.</br>
</br>
When the Twitter account ids of lawfirms are ready, we will then use Twitter API and Python library "tweepy" to gather Twitter account ids of followers of the lawfirm and Twitter account ids of followings of the lawfirm. Then, for each followers and followings, we will check whether the account seems to be a Twitter account of a lawyer. Also, if there is any mention of the lawfirm from the bio description of the account, then we will identify the account as highly likely account to be a lawyer's account. After running this program, we will get xlsx files that has rows of Twiiter account ids for each lawfirm.

### 4) Gather-tweets-that-each-lawyer-have-tweeted
This program uses Python library "tweepy", "xlsxwriter", "xlrd", and "time".</br>
</br>
This program is for collecting tweet data using Twitter account ids that we have gathered through programs such as "Find-a-twitter-account-of-a-lawyer-just-by-name", "Lawfirm_follower_following_account_gathering".</br> 
Once you have an excel file that has a column of account ids of lawyers, we can use Twitter API and Python library "Tweepy" to get tweets that each lawyers have done. We will use for loop to cover every single Twitter ids that we have gathered and get tweets of them in each single newly made xlsx file. For each loop, we will first get a single Twitter account id. We will get tweets as a single lump using code "tweet_data = tweepy.Cursor(api.user_timeline, id=twitter_account).items()". Then we will organize the single lump of data with for loop to write twitter account id, tweet date, and actual text of each tweet. After running this Python program, we can see all of the tweet data collected in each single xlsx file for each lawyer in a well arraged manner.
 

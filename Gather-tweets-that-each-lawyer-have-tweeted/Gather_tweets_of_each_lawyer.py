import tweepy
import time

# Twitter API authentication
auth = tweepy.OAuthHandler('You can find this in Twitter developer account', 'You can find this in Twitter developer account')
auth.set_access_token('You can find this in Twitter developer account',
                      'You can find this in Twitter developer account')
api = tweepy.API(auth)

twitter_account_list = []

wb = xlrd.open_workbook("lawfirm_final.xlsx")
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

for rows_in_excel in range(sheet.nrows):
    twitter_account_list.append(sheet.cell_value(rows_in_excel, 21).split("@")[1])
    print(sheet.cell_value(rows_in_excel, 21))
    exit()

for twitter_account in twitter_account_list:
    print(twitter_account)
    outWorkbook = xlsxwriter.Workbook(str(twitter_account) + "_tweet_history.xlsx")
    outSheet = outWorkbook.add_worksheet()

    outSheet.write("A1", "twitter_account")
    outSheet.write("B1", "tweet_date")
    outSheet.write("C1", "tweet_text")

    tweet_data = tweepy.Cursor(api.user_timeline, id=twitter_account).items()

    #num_of_tweets = sum(1 for _ in tweet_data)

    tweet_index = 0

    for tweets in tweet_data:
        tweet_text = tweets.text
        tweet_date = tweets.created_at
        outSheet.write("A{}".format(tweet_index + 2), twitter_account)
        outSheet.write("B{}".format(tweet_index + 2), tweet_date)
        outSheet.write("C{}".format(tweet_index + 2), tweet_text)
        tweet_index += 1
        time.sleep(1)
        print(tweet_index, tweet_date, tweet_text)

    print("Twitter data gathering for " + str(twitter_account) + " is done.")
    outWorkbook.close()
print("Every twitter data gathering done.")

import xlsxwriter
import xlrd
from collections import OrderedDict
import tweepy
import xlsxwriter
import datetime
import time

# Twitter API authentication
auth = tweepy.OAuthHandler('N9jwAo7s7bHrH1NVYwz48kYJd', 'a4x07AlrYNxWZ8pgaKQkcEQ6cvjnOrhrjv3FksA4b8UVrnhzId')
auth.set_access_token('1034523492488830978-y6eufhKywWxaJ3DTVehO0Ee2UVe7y4',
                      'GzBlOyfhhVs6w0WHZezTtCggePjaTw6HQT0U1dmM6jZRj')
api = tweepy.API(auth)

lawfirm_names = []
url_core = []
twitter_account_list = []

wb = xlrd.open_workbook("firm_name.xlsx")  # 수정: 위에 function에서 만들었던 xlsx file과 같은 이름으로 수정해주세요
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

for rows_in_excel in range(sheet.nrows):
    if (rows_in_excel >= 200) and (rows_in_excel < 270):
        try:
            twitter_account_list.append(sheet.cell_value(rows_in_excel, 3).split('@')[1])
            lawfirm_names.append(sheet.cell_value(rows_in_excel, 1))
            url_core.append(sheet.cell_value(rows_in_excel, 2))
        except AttributeError:
            continue

for twitter_account in twitter_account_list:
    print(twitter_account)
    outWorkbook = xlsxwriter.Workbook(str(twitter_account) + "_lawfirm_follower_following.xlsx")
    outSheet = outWorkbook.add_worksheet()

    outSheet.write("A1", "lawfirm_twitter_account")
    outSheet.write("B1", "follower_following_account")

    follower_ids = []
    following_ids = []

    for page in tweepy.Cursor(api.followers_ids, screen_name=str(twitter_account)).pages():
        follower_ids.extend(page)
    time.sleep(60*15)
    print("Lawfirm follower gathering done.")

    for page in tweepy.Cursor(api.friends_ids, screen_name=str(twitter_account)).pages():
        following_ids.extend(page)
    time.sleep(60*15)
    print("Lawfirm following gathering done.")

    print("Follower and Following accounts gathering done.")

    all_ids = follower_ids + following_ids

    ids_index = 0
    just_index = 0

    for follwer_followings in all_ids:
        print(just_index)
        try:
            user_data = api.get_user(follwer_followings)
            time.sleep(1)

            if lawfirm_names[twitter_account_list.index(twitter_account)].lower() in str(user_data.description).lower():
                outSheet.write("A{}".format(ids_index + 2), twitter_account)
                outSheet.write("B{}".format(ids_index + 2), user_data.screen_name)
                print("######### A Lawyer found #########", user_data.name, user_data.screen_name)
                ids_index += 1
            elif ("@" + twitter_account) in str(user_data.description).lower():
                outSheet.write("A{}".format(ids_index + 2), twitter_account)
                outSheet.write("B{}".format(ids_index + 2), user_data.screen_name)
                print("######### A Lawyer found #########", user_data.name, user_data.screen_name)
                ids_index += 1
            elif url_core[twitter_account_list.index(twitter_account)] in str(user_data.entities['url']['urls'][0]['expanded_url']).lower():
                outSheet.write("A{}".format(ids_index + 2), twitter_account)
                outSheet.write("B{}".format(ids_index + 2), user_data.screen_name)
                print("######### A Lawyer found #########", user_data.name, user_data.screen_name)
                ids_index += 1
        except Exception:
            continue
        just_index += 1

    outWorkbook.close()

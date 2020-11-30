import tweepy
import time


def twitter_name_search():
    # Twitter API authentication
    auth = tweepy.OAuthHandler('This can be found in Twitter developer account', 'This can be found in Twitter developer account')
    auth.set_access_token('This can be found in Twitter developer account',
                          'This can be found in Twitter developer account')
    api = tweepy.API(auth)

    # List for storing lawyers' name
    lawyer_names = []
    # Opening existing file "lawfirm_n.xlsx" which has names of lawyers we are targeting
    # You can make it on your own
    # Make sure to make a column of names of lawyers you are targeting
    wb = xlrd.open_workbook("lawfirm_n.xlsx")
    
    # No need to change next two lines
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    # Gather lawyers' names from "lawfirm_n.xlsx" file and append into list "lawyer_names"
    for rows_in_excel in range(sheet.nrows):
        if rows_in_excel != 0:
            lawyer_names.append(sheet.cell_value(rows_in_excel, 1))

    # Create file (workbook) and worksheet
    outWorkbook = xlsxwriter.Workbook("twitter_name_search_for_lawfirm_n.xlsx")
    outSheet = outWorkbook.add_worksheet()

    # Write column headers
    outSheet.write("A1", "LawFirm")
    outSheet.write("B1", "Name")
    outSheet.write("C1", "TwitterID")

    # Search the name of lawyers, search on Twitter and see if we can find accounts that seem to be the lawyer we are looking for
    for names in lawyer_names:
        print(lawyer_names.index(names))
        outSheet.write("A{}".format(lawyer_names.index(names) + 2), "Schwabe, Williamson & Wyatt")
        outSheet.write("B{}".format(lawyer_names.index(names) + 2), names)
        try:
            results = api.search_users(q=names, rpp=20)
            for results_names in results:
                if "schwabe" in str(results_names.entities['url']['urls'][0]['expanded_url']): 
                    outSheet.write("C{}".format(lawyer_names.index(names) + 2), ('@' + results_names.screen_name))
                    print("######### A Lawyer found #########", results_names.name, results_names.screen_name)
                elif "law" in str(results_names.description).lower():
                    outSheet.write("C{}".format(lawyer_names.index(names) + 2), ('@' + results_names.screen_name))
                    print("######### A Lawyer found #########", results_names.name, results_names.screen_name)
                elif "litigation" in str(results_names.description).lower():
                    outSheet.write("C{}".format(lawyer_names.index(names) + 2), ('@' + results_names.screen_name))
                    print("######### A Lawyer found #########", results_names.name, results_names.screen_name)
                elif "practice" in str(results_names.description).lower():
                    outSheet.write("C{}".format(lawyer_names.index(names) + 2), ('@' + results_names.screen_name))
                    print("######### A Lawyer found #########", results_names.name, results_names.screen_name)
                elif "partner" in str(results_names.description).lower():
                    outSheet.write("C{}".format(lawyer_names.index(names) + 2), ('@' + results_names.screen_name))
                    print("######### A Lawyer found #########", results_names.name, results_names.screen_name)
                elif "legal" in str(results_names.description).lower():
                    outSheet.write("C{}".format(lawyer_names.index(names) + 2), ('@' + results_names.screen_name))
                    print("######### A Lawyer found #########", results_names.name, results_names.screen_name)
        except Exception:
            continue

        if (results.__len__()) == 0:
            outSheet.write("C{}".format(lawyer_names.index(names) + 2), "N/A")


    outWorkbook.close()

    print('Web scrapping done for Twitter')

    
twitter_name_search()

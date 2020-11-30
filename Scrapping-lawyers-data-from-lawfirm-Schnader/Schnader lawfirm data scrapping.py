import requests # For web scrapping
import xlsxwriter # For writing new xlsx files
import xlrd # For reading xlsx files
from bs4 import BeautifulSoup # Main web scrapping package for this project
from collections import OrderedDict


def lawfirm_final():
    # Read any file that had links for bio pages for each lawyers
    # In this case, the file name that I was using is "lawfirm_final.xlsx" excel file
    wb = xlrd.open_workbook("lawfirm_final.xlsx")
    # No need to change next two lines
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    # We will gather links of lawyers' web pages
    # This list will be used to store such links in strings
    lawyer_link = []

    # This is a for loop that gathers links of lawyers' web pages from already written excel file (in this case, "lawfirm_final.xlsx"
    for rows_in_excel in range(sheet.nrows):
        # In here you can replace numbers 2912 and 2930 to row number in your excel file
        if (rows_in_excel >= 2912) and (rows_in_excel <= 2930):
            # Add urls from xlsx file into list "lawyer_link"
            lawyer_link.append(sheet.cell_value(rows_in_excel, 2))

    # Create file (workbook) and worksheet
    outWorkbook = xlsxwriter.Workbook("lawfirm_final_info.xlsx")
    outSheet = outWorkbook.add_worksheet()

    # Write column headers
    outSheet.write("D1", "title")
    outSheet.write("E1", "practice")
    outSheet.write("F1", "location")
    outSheet.write("G1", "bachelors")
    outSheet.write("H1", "jd_degree")

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

    for lawyer_links in lawyer_link:
        if lawyer_links != 'N/A':
            print(lawyer_links)
            request = requests.get(lawyer_links, headers=header)
            html = request.text
            # Variable 'soup' stores html code
            soup = BeautifulSoup(html, 'html.parser')

            lawyer_name = soup.find('div', {'class': "basic-info-section"}).text.strip()

            try:
                lawyer_title = soup.find('span', {'class': "position"}).text.strip()
            except AttributeError:
                lawyer_title = 'N/A'

            lawyer_practice = ""

            try:
                lawyer_practice = soup.find('aside', {'class': 'sidebar'}).text.strip().split('Service Areas')[1].split('Bar Admissions')[0]

                """
                for practices in lawyer_practice_temp:
                    if lawyer_practice_temp.index(practices) == len(lawyer_practice_temp) - 1:
                        lawyer_practice += practices.text.strip()
                    else:
                        lawyer_practice += practices.text.strip() + ", "
                """
            except AttributeError:
                lawyer_practice = 'N/A'
            except IndexError:
                lawyer_practice = 'N/A'

            """
            lawyer_practice = ''
    
            for practices in lawyer_practice_temp:
                if lawyer_practice_temp.index(practices) == (len(lawyer_practice_temp) - 1):
                    lawyer_practice += practices
                else:
                    lawyer_practice += practices
                    lawyer_practice += ', '
            """
            lawyer_location = soup.find('span', {'class': "location"}).text.strip()
            """
            lawyer_location_temp = soup.findAll('a', {'class': "PositionOffices__office_0"})
            for locations in lawyer_location_temp:
                if lawyer_location_temp.index(locations) == len(lawyer_location_temp) - 1:
                    lawyer_location += locations.text.strip()
                else:
                    lawyer_location += locations.text.strip() + ", "
            """
            try:
                lawyer_bachelors = soup.find('aside', {'class': 'sidebar'}).text.strip().split('Education')[1]
            except AttributeError:
                lawyer_bachelors = 'N/A'
            except IndexError:
                lawyer_bachelors = 'N/A'
            try:
                lawyer_jd_temp = 'N/A'
                lawyer_jd = soup.find('aside', {'class': 'sidebar'}).text.strip().split('Education')[1]

                """
                for jds in lawyer_jd_temp:
                    if 'J.D.' in jds:
                        lawyer_jd = jds
                """


            except AttributeError:
                lawyer_jd = 'N/A'
            except IndexError:
                lawyer_jd = 'N/A'

            outSheet.write("B{}".format(lawyer_link.index(lawyer_links) + 2), lawyer_name)
            outSheet.write("D{}".format(lawyer_link.index(lawyer_links) + 2), lawyer_title)
            outSheet.write("E{}".format(lawyer_link.index(lawyer_links) + 2), lawyer_practice)
            outSheet.write("F{}".format(lawyer_link.index(lawyer_links) + 2), lawyer_location)
            outSheet.write("G{}".format(lawyer_link.index(lawyer_links) + 2), lawyer_bachelors)
            outSheet.write("H{}".format(lawyer_link.index(lawyer_links) + 2), lawyer_jd)

    print('Web scrapping done for lawfirm webpage.')

    outWorkbook.close()
    
lawfirm_final()

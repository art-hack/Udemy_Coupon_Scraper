import csv
from bs4 import BeautifulSoup
import requests


# function to scrape smartybro
def smartybro(string):
    page_response = requests.get(string, timeout=15)
    if page_response.status_code == 200:
        page_content = BeautifulSoup(page_response.content, "html.parser")
        header = page_content.find_all('h3', class_="sing-tit")
        linker = page_content.find_all('a', attrs={'class': 'fasc-button fasc-size-xlarge fasc-type-flat'})
        for row in header:
            header = row.text
        # prices_clean = prices["href"]
        for a in linker:
            linker = a['href']
        # prices= prices.url
        u1 = requests.get(linker, timeout=5)
        # linker = u1.url
        # with open('output.csv', 'wb') as file:
        #     for line1 in header:
        #         file.write(line1)
        #         file.write(',')
        #     for line2 in linker:
        #         file.write(line2)
        #         file.write('\n')
        # RESULT = [header, linker]
        header = str(header).encode('utf-8')
        linker = str(linker).encode('utf-8')
        listFile2 = open('output.csv', 'a')
        writer2 = csv.writer(listFile2)
        writer2.writerow([header] + [linker] + [u1.url])
        # print u1.url
        print header
        print u1.url
    else:
        print "Error Fetching the Data"


# Code to scrape Anycouponcode.com
def anycode(check):
    page_response = requests.get(check, timeout=15)
    if page_response.status_code == 200:
        page_content = BeautifulSoup(page_response.content, "html.parser")
        header = page_content.find('h2', class_="alt")
        linker = page_content.find_all('a', attrs={'target': '_blank', 'rel': 'noopener'})
        header = header.text
        header = header.encode('ascii', 'ignore')
        for a in linker:
            linker = a['href']
        # u1 = requests.get(linker, timeout=5)
        header = str(header).encode('utf-8')
        linker = str(linker).encode('utf-8')
        listFile2 = open('output.csv', 'a')
        writer2 = csv.writer(listFile2)
        writer2.writerow([header] + [linker])
        print header
        print linker
    else:
        print "Error Fetching the Data"


# function to scrape BuzzUdemy.com
def bu(check):
    page_response = requests.get(check, timeout=5)
    if page_response.status_code == 200:
        page_content = BeautifulSoup(page_response.content, "html.parser")
        header = page_content.find_all('h2', class_="title front-view-title")
        linker = page_content.find_all('a', class_="deal-button show-coupon-button activate-button activate-modal")
        for row in header:
            header = row.text
        for a in linker:
            linker = a['href']
        header = str(header).encode('utf-8')
        linker = str(linker).encode('utf-8')
        listFile2 = open('output.csv', 'a')
        writer2 = csv.writer(listFile2)
        writer2.writerow([header] + [linker])
        print header
        print linker
    else:
        print "Error Fetching the Data"


# function to scrape Comidoc.com
def comidoc(check):
    page_response = requests.get(check, timeout=5)
    if page_response.status_code == 200:
        page_content = BeautifulSoup(page_response.content, "html.parser")
        header = page_content.find_all('h1', class_="header-post-title-class")
        linker = page_content.find_all('a', class_="maxbutton-3 maxbutton maxbutton-enroll-lt")
        for row in header:
            header = row.text
        for a in linker:
            linker = a['href']
        listFile2 = open('output.csv', 'a')
        writer2 = csv.writer(listFile2)
        writer2.writerow([header] + [linker])
        print header
        print linker
    else:
        print 'Error Fetching the Data'


# function to scrape coupontry.com
def coupontry(check):
    page_response = requests.get(check, timeout=5)
    if page_response.status_code == 200:
        page_content = BeautifulSoup(page_response.content, "html.parser")
        header = page_content.find_all('h1', class_="entry-title")
        linker = page_content.find_all('a', attrs={'title': 'Click to open site'})
        for row in header:
            header = row.text
        for a in linker:
            linker = a['href']
        listFile2 = open('output.csv', 'a')
        writer2 = csv.writer(listFile2)
        writer2.writerow([header] + [linker])
        print header
        print linker
    else:
        print "Error Fetching the Data"


# function to scrape udemycoupon.learnviral
def learnviral(check):
    page_response = requests.get(check, timeout=5)
    if page_response.status_code == 200:
        page_content = BeautifulSoup(page_response.content, "html.parser")
        header = page_content.find_all('h1', class_='entry-title')
        linker = page_content.find_all('a', attrs={'title': 'Click to open site'})
        for row in header:
            header = row.text
        for a in linker:
            linker = a['href']
        listFile2 = open('output.csv', 'a')
        writer2 = csv.writer(listFile2)
        writer2.writerow([header] + [linker])
        print header
        print linker
    else:
        print "Error Fetching the Data"


# function to scrape Udemycoupon.club
def ucc(check):
    page_response = requests.get(check, timeout=5)
    if page_response.status_code == 200:
        page_content = BeautifulSoup(page_response.content, "html.parser")
        header = page_content.find_all('h1', class_="post-title entry-title")
        linker = page_content.find_all('blockquote')
        linker = linker[0].find('a')
        for row in header:
            header = row.text
        for a in linker:
            linker = a
        header = header[1:-1]
        listFile2 = open('output.csv', 'a')
        writer2 = csv.writer(listFile2)
        writer2.writerow([header] + [linker])
        print header
        print linker
    else:
        print "Error Fetching the Data"


# function that sorts the function to be used
def checker(check):
    if 'smartybro' in check:
        try:
            smartybro(check)
        except Exception:
            pass
    elif 'anycouponcode' in check:
        try:
            anycode(check)
        except Exception:
            pass
    elif 'buzzudemy' in check:
        try:
            bu(check)
        except Exception:
            pass
    elif 'comidoc' in check:
        try:
            comidoc(check)
        except Exception:
            pass
    elif 'coupontry' in check:
        try:
            coupontry(check)
        except Exception:
            pass
    elif 'udemycoupon.learnviral' in check:
        try:
            learnviral(check)
        except Exception:
            pass
    elif 'udemycoupon.club' in check:
        try:
            ucc(check)
        except Exception:
            pass


# Main driver Program
listFile2 = open('output.csv', 'w')
listFile2.close()
with open('input.txt') as openfileobject:
    for line in openfileobject:
        page_link = line
        checker(page_link)

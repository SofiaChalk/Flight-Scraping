from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

one_way = False
email = True
sms = True

# Flight details
from_airport = 'LON'  # Country Code
to_airport = 'ATH'  # Country Code
departure_date = '2020-07-05'  # Format needed: yyyy-mm-dd
return_date = '2020-08-21'

# Email details
from_email = 'your email'
from_email_password = 'your_email_pass'
to_email = 'to email'

# SMS details
to_sms = 'phone number'  # Format: Include country code with +, eg:+xx xxxxxxxxxx

# User agent
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
# Headers for user-agent
headers = {'User-Agent': user_agent}


def scrape_flights(url, headers, from_airport, to_airport, departure_date, return_date, one_way):
    global df
    # Get response from url using requests
    response = requests.get(url, headers=headers)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    # Get departure time
    soup_dep_time = soup.find_all('span', class_='depart-time base-time')
    # Get arrival time
    soup_arr_time = soup.find_all('span', class_='arrival-time base-time')
    # Get the price
    regex = re.compile('Common-Booking-MultiBookProvider (.*)multi-row Theme-featured-large(.*)')
    soup_price = soup.find_all('div', class_= regex)

    # Put findings in lists
    dep_time = []
    for div in soup_dep_time:
        dep_time.append(div.getText())

    arr_time = []
    for div in soup_arr_time:
        arr_time.append((div.getText()))

    price = []
    currency = []
    for div in soup_price:
        currency.append(div.getText().split('\n')[3][0:1])
        price.append(div.getText().split('\n')[3][1:])

    # Create df from the results
    if one_way == False and url == arr_url:
        df = pd.DataFrame({'Origin': to_airport,
                           'Destination': from_airport,
                           'Date': return_date,
                           'Departure Time': dep_time,
                           'Arrival Time': arr_time,
                           'Price': price,
                           'Currency': currency})
    else:
        df = pd.DataFrame({'Origin': from_airport,
                           'Destination': to_airport,
                           'Date': departure_date,
                           'Departure Time': dep_time,
                           'Arrival Time': arr_time,
                           'Price': price,
                           'Currency': currency})
    # Sort price from low to high
    df['Price'] = df['Price'].astype(int)
    df['Price'] = df['Price'].sort_values(ascending=True)


def send_sms(final_dict, to_sms, sms):
    # If final_dict is not empty send an sms with the results
    if sms == True and len(final_dict) > 0:
        account_sid = 'twilio_account_sid'
        auth_token = 'twilio_auth_token'
        client = Client(account_sid, auth_token)

        message_text = 'Flight Info:\n{}'.format("\n".join(str(v)[1:-1] for v in final_dict))

        client.messages \
            .create(
            body=message_text,
            from_='+12029310937',
            to=to_sms)


def send_email(final_df, email, from_email, from_email_password, to_email):
    if email == True:

        # final_df to html table
        message_text = MIMEMultipart()
        message_text['Subject'] = 'Flight Info'
        html = """\
        <html>
          <head></head>
          <body>
            {0}
          </body>
        </html>
        """.format(final_df.to_html())
        html_msg = MIMEText(html, 'html')
        message_text.attach(html_msg)

        # Email settings
        mail = smtplib.SMTP('smtp.office365.com', 587)
        mail.starttls()
        mail.login(from_email, from_email_password)
        mail.sendmail(from_email, to_email, message_text.as_string())
        mail.close()


# Url
dep_url = 'https://www.kayak.co.uk/flights/' + from_airport + '-' + to_airport + '/' + departure_date + '?sort=bestflight_a&fs=stops=0'
arr_url = 'https://www.kayak.co.uk/flights/' + to_airport + '-' + from_airport + '/' + return_date + '?sort=bestflight_a&fs=stops=0'


# If one_way= True then run the function only once otherwise, run it again and change the info
if one_way == True:
    scrape_flights(url=dep_url, headers=headers, from_airport=from_airport, to_airport=to_airport,
                   departure_date=departure_date, return_date=return_date, one_way=True)
    final_df = df.copy()
else:
    scrape_flights(url=dep_url, headers=headers, from_airport=from_airport, to_airport=to_airport,
                   departure_date=departure_date, return_date=return_date, one_way=False)
    dep_df = df.copy()
    scrape_flights(url=arr_url, headers=headers, from_airport=from_airport, to_airport=to_airport,
                   departure_date=departure_date, return_date=return_date, one_way=False)
    arr_df = df.copy()
    final_df = dep_df.append(arr_df)

# Put df in a dictionary to print it in a message later
final_dict = final_df.to_dict('r')

# Run sms function
send_sms(final_dict=final_df, sms=sms, to_sms=to_sms)

# Run email function
send_email(final_df=final_df, email=email, from_email=from_email, to_email=to_email,
           from_email_password=from_email_password)

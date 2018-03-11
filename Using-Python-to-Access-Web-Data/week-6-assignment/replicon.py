import requests
import json

url = 'https://na1.replicon.com/GreatestGood/RemoteApi/RemoteApi.ashx/8.29.78/testmode'

username = 'jcaracotsios'
password = 'thedug1!'

header = {'X-Replicon-Security-Context': 'User',
          'Content-Type': 'application/json'}

begin_session = '''[   {     "Action": "BeginSession"   } ]'''
end_session = '''[   {     "Action": "EndSession"   } ]'''


# Input start/end dates for query
start_date = '2015-12-17'
start_date = start_date.split('-')

end_date = '2015-12-17'
end_date = end_date.split('-')

time_off = json.dumps([
  {
    "Action": "Query",
    "QueryType": "TimeOffBookingByDateRange",
    "DomainType": "Replicon.TimeOff.Domain.TimeOffBooking",
    "Args": [
      {
        "__type": "Date",
        "Year": start_date[0],
        "Month": start_date[1],
        "Day": start_date[2]
      },
      {
        "__type": "Date",
        "Year": end_date[0],
        "Month": end_date[1],
        "Day": end_date[2]
      }
    ]
  }
])

# Begin session
requests.post(url, data=begin_session, auth=(username, password), headers=header)

# Get all people who are gone
req = requests.post(url, data=str(time_off), auth=(username, password), headers=header)

data = json.loads(req.content)

# data['Value'] is a list containing all the time off requests for the given range of days
# Its elements correspond to individual TGG employees' requests

for time_off_booking in data['Value']:
    user_id = time_off_booking['Properties']['CreatedByUserId']

    name_query = json.dumps([
      {
        "Action": "Query",
        "QueryType": "UserById",
        "DomainType": "Replicon.Domain.User",
        "Args": [
          [
            user_id
          ]
        ]
      }
    ])

    name_req = requests.post(url, data=str(name_query), auth=(username, password), headers=header)

    name_data = json.loads(name_req.content)

    first_name = name_data['Value'][0]['Properties']['FirstName']
    last_name = name_data['Value'][0]['Properties']['LastName']

    time_off_start = data['Value'][0]['Properties']['StartDate']
    start_string = str(time_off_start['Day']) + "-" + str(time_off_start['Month']) + "-" + str(time_off_start['Year'])

    time_off_end = data['Value'][0]['Properties']['EndDate']
    end_string = str(time_off_end['Day']) + "-" + str(time_off_end['Month']) + "-" + str(time_off_end['Year'])

    print(first_name + last_name + " is gone from " + start_string + " until " + end_string)


# End session
requests.post(url, data=end_session, auth=(username, password), headers=header)


# from twilio.rest import Client

# account_sid = 'ACa0bfb37ce89b2182189b6482e7614b71'
# auth_token = '35d76a0aad56ad20bd586947f7ead690'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               body='Hey chan How are you',
#                               from_='+19093652996',
#                               to='+95 9 966 565693'
#                           )

# print(message.sid)

import pip

installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)
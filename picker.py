import smtplib, ssl
import random
import copy

# add names here
names = ['<Name>']

# add emails here
emails = {'<Name>':'<email>'}

# add names and corresponding spouse's name here so spouses do not get one another
spouses = {'<Name>':'<Spouse's Name>'}

def name_algo():

  shuffled = copy.deepcopy(names)
  random.shuffle(shuffled)

  for i in range(0, len(shuffled)):
    current_giver = names[i]
    current_recipient = shuffled[i]

    if current_giver == current_recipient or current_recipient == spouses[current_giver]: 
      
      return False, shuffled

  return True, shuffled

def send_email(giver, recipient):
  
  # add sending email and password here
  sender_email = '<sender_email>'
  password = '<password>'

  port = 465  # For SSL

  # Create a secure SSL context
  context = ssl.create_default_context()

  subject ="Secret Santa Name"

  message_text = "Hi " + giver + ',\n\nFor Christmas you will be getting a gift for ' + recipient + '.'

  message = 'Subject: {}\n\n{}'.format(subject, message_text)

  recipient = emails[giver]

  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
          server.login(sender_email, password)
          server.sendmail(sender_email, recipient, message)
          print('email sent')

is_good = False
shuffled = []

while not is_good:
  print('sorting names...')
  is_good, shuffled = name_algo()

checking_names = True

for i in range(0, len(names)):

  if names[i] == shuffled[i] or shuffled[i] == spouses[names[i]]:
    checking_names = False
  
  print('Sending email to ' + names[i] + '...')
  # send_email(names[i], shuffled[i]) # comment this out in order to actually send the email

print('If this isn\'t True then you screwed up')
print(checking_names)
  


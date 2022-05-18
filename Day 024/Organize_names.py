chat = """
Prahlad Rao to Everyone (8:03 PM)
Prahlad Rao
Prakash Udupa to Everyone (8:03 PM)
Medha Udupa
Swathi to Everyone (8:04 PM)
Swathi
Guurumoorthy to Everyone (8:04 PM)
Gurumoorthy R
Maanya to Everyone (8:04 PM)
Maanya H
Aadhya to Everyone (8:04 PM)
Aadhya Anand
Niyati to Everyone (8:05 PM)
Niyati Makkithaya
Siddharth Poyapakkam to Everyone (8:05 PM)
Siddharth Poyapakkam
Rashmi to Everyone (8:05 PM)
Rashmi H
Niha Udipi to Everyone (8:05 PM)
Niha Udipi
Inchara Aithal to Everyone (8:05 PM)
Inchara Aithal
Ranjana rao to Everyone (8:05 PM)
Ranjana Rao
Medha Udupa to Everyone (8:05 PM)
Medha Udupa
Prahlad Rao to Everyone (8:05 PM)
Prahlad Rao
"""

messages = chat.strip().splitlines()

attendence = []

for message in messages:
    if " to Everyone " not in message:
        attendence.append(message.capitalize())

for name in sorted(attendence):
    print(name)





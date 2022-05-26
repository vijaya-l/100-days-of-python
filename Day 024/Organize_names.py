from pyexpat.errors import messages


chat = """
Prahlad Rao
Guurumoorthy to Everyone (8:01 PM)
Gurumoorthy R
Siddharth Poyapakkam to Everyone (8:01 PM)
Siddharth Poyapakkam
Niyati to Everyone (8:01 PM)
niyati
no
Aadhya to Everyone (8:03 PM)
Aadhya Anand
Aditi Adiga to Everyone (8:03 PM)
Aditi Adiga
Hamsa Vinod to Everyone (8:04 PM)
Hamsa V
Aarush Goli to Everyone (8:04 PM)
Aarush
Ranjana Rao
"""

messages = chat.strip().splitlines()
print(messages)
attendence = []

for message in messages:
    if " to Everyone " not in message:
        attendence.append(message.capitalize())

for name in sorted(attendence):
    print(name)

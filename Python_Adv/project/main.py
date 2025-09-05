from chats_1 import Login

def LoginSystem(mobile, password):
    lg = Login(mobileno=mobile, password=password)
    print(lg)
    return lg.log

ls = LoginSystem(mobile=9820646838, password="suresh123")
if ls:
    print('Hi, I am Small Chat System!')
else:
    print('Validation & Verification is Failed, Due To Some Resion!')
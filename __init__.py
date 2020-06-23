class User():
    username,fname,lname = '','',''
    email = ''
    def __init__(self, username, fname, lname, *args, **kwargs):
        self.username = username
        self.fname, self.lname = fname, lname

    @classmethod
    def setEmail(cls, email):
        cls.email = f'{email}@g.net'

        return cls.email
    def setFullName(self):
        return f'{self.fname} {self.lname}'

    def __str__(self):
        return f'Hi {self.username}\nEmail:{self.setEmail(self.username)}\nFull Name:{self.setFullName()}'
        
usr = User(username='jdoea', fname='John', lname='Doe')
setmail = usr.setEmail(email='John')
print(usr)
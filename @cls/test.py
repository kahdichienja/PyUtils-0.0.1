from utility import Utils
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
        
        
usr = User(username='jdoea', fname='John', lname='@Doe')
setmail = usr.setEmail(email='John')

assert Utils.remove_punctuation(usr.setEmail('john')) == 'johngnet'
assert Utils.remove_dollar_white_space(",12") == 12.0
assert Utils.remove_dollar_white_space("$123") == 123.0
assert Utils.remove_comma_and_spaces(" , ,1234") == 1234.0
my_str = "Hello!!!, he said ---and went."
assert Utils.remove_punctuation(my_str) == "Hello he said and went"

print('Assertion Test Complete')
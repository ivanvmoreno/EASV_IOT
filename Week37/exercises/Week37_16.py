import random

class Password_Generator:
    SETS = {
        'uppercase': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'lowercase': 'abcdefghijklmnopqrstuvwxyz',
        'symbols': '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~/?>',
        'numbers': '0123456789',
        'keywords': ['testing', 'home', 'bird', 'cat', 'human', 'wizard']
    }

    SETTINGS = {
        'stronger': {
            'length': 40,
            'sets': ['uppercase', 'lowercase', 'symbols', 'numbers']
        },
        'memorizable': {
            'length': 30,
            'sets': ['keywords'],
            'separator': '-'
        },
        'default': {
            'length': 25,
            'sets': ['uppercase', 'lowercase', 'symbols', 'numbers']
        }
    }

    def get_random(self, set):
        set = self.SETS[set]
        return set[(random.randint(0, len(set) - 1))]

    def generate(self, mode):
        settings = self.SETTINGS.get(mode, self.SETTINGS['default'])
        password = ''
        if not settings.get('separator'):
            while (len(password) < settings['length']):
                password += self.get_random(self, random.choice(settings['sets']))
        else:
            while (len(password) < settings['length']):
                password += '%s-' % self.get_random(self, random.choice(settings['sets']))
            password = password[:-1]
        return password
            

def main():
    print('Choose password strength:')
    print('1) Stronger – 60 characters, uppercase, lowercase, numbers, symbols')
    print('2) Memorizable – 30 characters, concatenation of words')
    print('3) Default – 25 characters, uppercase, lowercase, numbers, symbols')
    mode = input()
    mode = 'stronger' if mode == '1' else ('memorizable' if mode == '2' else 'default')
    password = Password_Generator.generate(Password_Generator, mode)
    print('Generated password (%s mode):' % mode)
    print(password)

if __name__ == '__main__': 
    main()
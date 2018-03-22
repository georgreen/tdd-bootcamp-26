import cmd
import os

from docopt import DocoptExit, docopt
from termcolor import colored

# symboles
unicode_tick = u'\u2713'
unicode_cross = u'\u274c'
unicode_warning = u'\u26A0'
unicode_stop = u'\u26d4'

# emojies
unicode_winkface = u"\U0001F609"
unicode_coolface = u"\U0001F60E"
unicode_sadface = u"\u2639"
unicode_luckyface = u"\U0001F61B"

# fancy UI things
def dynamic_promt(color='green', symbole=unicode_luckyface):
    prompt = colored("INPUT ", color) + symbole + "  "
    return prompt

def print_message(msg, status="", symbole="", color='green'):
    padding = 80
    msg_len = 10
    if type(msg) == str:
        msg_len = padding - len(msg)
    print(' ' * 5, colored(msg, color), " " * msg_len, end=' ')
    print(colored(status, color), colored(symbole, color))

def print_error(msg, status='Error', c='red'):
    print_message(msg, status=status, symbole=unicode_stop, color=c)

# main App things
class App(cmd.Cmd):
    prompt = dynamic_promt()

    def argument_parser(fn):
        '''
        input fn -> function
        return -> a fuction that can parse commandline args using docopt.
        '''
        def get_args(self, args):
            try:
                opt = docopt(fn.__doc__, args)
                App.prompt = dynamic_promt()
                return fn(self, opt)
            except DocoptExit as e:
                print_error(e, status="Malformed Command")
                App.prompt = dynamic_promt(color='red',
                                                symbole=unicode_sadface)
        return get_args

    def default(self, args):
        invalid_command = args.split(' ')[0]
        print_error(invalid_command, status='Command Does Not exist')
        prompt = dynamic_promt(color='red',
                                        symbole=unicode_sadface)
    
    @argument_parser
    def do_add_contact(self, person_information):
        """
            Usage:
                add_contact <firtname> <secondname> <phone_number>
        """
        #TODO
        pass

if __name__ == '__main__':
    app = App()
    app.cmdloop()
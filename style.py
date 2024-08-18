def easy_escape_char(espace_char, how_many):
    """
    your code will look cleaner
    :param espace_char: it takes escape characters like "/n"
    :param how_many: how many "/n"s do you want
    :return: e.g. easy_escape_char(/n, 5) --> /n/n/n/n/n
    """
    return espace_char * how_many

new_line = easy_escape_char("\n", 4)
new_line_short = easy_escape_char("\n", 2)
space = easy_escape_char("  ", 33)
multiple_stars = easy_escape_char("*", 15)
multi_dots = easy_escape_char(".", 3)

ASCII = {"klasik": """
 _  _ __     __   ___ ____ _  _ 
( )/ |  )   /__\ / __|_  _| )/ )
 )  ( )(__ /(__)\\__ \_)(_ )  ( 
(_)\_|____|__)(__|___(____|_)\_)
""",
         "karma" : """
 _  _   __   ____ __  __   __   
( )/ ) /__\ (  _ (  \/  ) /__\  
 )  ( /(__)\ )   /)    ( /(__)\ 
(_)\_|__)(__|_)\_|_/\/\_|__)(__)

         """,
         "kahin" : """    
 _  _   __   _   _ ____ _  _ 
( )/ ) /__\ ( )_( |_  _| \( )
 )  ( /(__)\ ) _ ( _)(_ )  ( 
(_)\_|__)(__|_) (_|____|_)\_)
"""}

ascii_rock_scissors_paper = {
    'taş': '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    'kağıt': '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
    'makas': '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}

writing_rock_scissors_paper = {'rock_paper_scissors_ascii': '''
██████████████████████████
█▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄███
██─▄─▄█─██─█─███▀██─▄▀████
▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
█████████████████████████████████
█▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀███
██─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
██████████████████████████████████████████████
█─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀█─▄▄▄▄█
█▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
'''}
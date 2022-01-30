#if else and elif
print('''
                                 ,ood8888booo,
                              ,od8           8bo,
                           ,od                   bo,
                         ,d8                       8b,
                        ,o                           o,    ,a8b
                       ,8                             8,,od8  8
                       8'                             d8'     8b
                       8                           d8'ba     aP'
                       Y,                       o8'         aP'
                        Y8,                      YaaaP'    ba
                         Y8o                   Y8'         88
                          `Y8               ,8"           `P
                            Y8o        ,d8P'              ba
                       ooood8888888P"""'                  P'
                    ,od                                  8
                 ,dP     o88o                           o'
                ,dP          8                          8
               ,d'   oo       8                       ,8
               $    d$"8      8           Y    Y  o   8
              d    d  d8    od  ""boooooooob   d"" 8   8
              $    8  d   ood' ,   8        b  8   '8  b
              $   $  8  8     d  d8        `b  d    '8  b
               $  $ 8   b    Y  d8          8 ,P     '8  b
               `$$  Yb  b     8b 8b         8 8,      '8  o,
                    `Y  b      8o  $$o      d  b        b   $o
                     8   '$     8$,,$"      $   $o      '$o$$
                      $o$$P"                 $$o$
    ''')



print("Welcome to find the wolf game")
user_input=input("Were do you want to search for the wolf ? Forest  , Mountain or at Home ?\n")
if user_input.lower()=="forest":
    user_input=input("In whtch part of the forst you whant to search for ? North , West , East or south\n")
    if user_input.lower()=="north":
        print("You found the wolf good job")

        print('''
              /^\      /^\
              |  \    /  |
              ||\ \../ /||
              )'        `(
             ,;`w,    ,w';,
             ;,  ) __ (  ,;
              ;  \(\/)/  ;;
             ;|  |vwwv|    ``-...
              ;  `lwwl'   ;      ```''-.
             ;| ; `""' ; ;              `.
              ;         ,   ,          , |
              '  ;      ;   l    .     | |
              ;    ,  ,    |,-,._|      \;
               ;  ; `' ;   '    \ `\     \;
               |  |    |  |     |   |    |;
               |  ;    ;  |      \   \   (;
               | |      | l       | | \  |
               | |      | |  pb   | |  ) |
               | |      | ;       | |  | |
               ; ,      : ,      ,_.'  | |
              :__'      | |           ,_.'
                       `--'
              ''')
    else:
        print("Game Over")

elif user_input.lower()=="mountain":
    print("Game Over")

elif user_input.lower()=="home":
    print("Game Over")

else:
    print("Invalid input please try again next time")



























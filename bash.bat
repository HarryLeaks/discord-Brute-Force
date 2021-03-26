@prompt $g$s &setlocal &set /a n=0
:loop
  python .\Bruteforce.py
  for /F "tokens=*" %%A in (tokens.txt) do python .\connecter.py %%A
goto loop
:exitloop
pause
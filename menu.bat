:MENU_START
@echo off
cls
set INPUT=false
set "MENU_OPTION="
set "OPTION1_INPUT="
set "OPTION2_INPUT="
echo +================================================+
echo . SIMPLE PROGRAMMABLE GAMES -PORTFOLIO OF THRIBHU.
echo +================================================+
echo .                                                .
echo .  1) Magic 8-Ball                               .
echo .  2) Rock Paper Scissors                        .
echo .  3) Tetris                                     .
echo .  4) Chess                                     .
echo .  5) EXIT                                       .
echo .                                                .
echo +================================================+
set /p MENU_OPTION="OPTION: "

IF %MENU_OPTION%==1 GOTO OPTION1
IF %MENU_OPTION%==2 GOTO OPTION2
IF %MENU_OPTION%==3 GOTO OPTION3
IF %MENU_OPTION%==4 GOTO OPTION4
IF %MENU_OPTION%==5 GOTO EXIT
IF %INPUT%==false GOTO DEFAULT

:OPTION1
timeout 2 > NUL
python.exe .\Magic8Ball\magic8ball.py
timeout 2 > NUL
exit /b

:OPTION2
timeout 2 > NUL
python.exe .\RockPaperScissors\rps.py

:OPTION3
timeout 2 > NUL
python.exe .\Tetris\tetris.py

:OPTION4
timeout 2 > NUL
python.exe .\Chess\chess.py

:EXIT
set INPUT=true
timeout 2 > NUL
exit /b

:DEFAULT
echo Option not available, try again.
timeout 2 > NUL
GOTO MENU_START
@echo off
start cmd /k "python main.py --logic VanBot --email=vanson@gmail.com --name=vanson --password=654321 --team etimo --host http://20.243.68.103:8082/api/ --board=2"
start cmd /c "python main.py --logic EdBot --email=edbert@email.com --name=edbert --password=123456 --team etimo --host http://20.243.68.103:8082/api/ --board=2"
start cmd /c "python main.py --logic FDL --email=test@email.com --name=stima --password=123456 --team etimo --host http://20.243.68.103:8082/api/ --board=2"
start cmd /c "python main.py --logic VanBot --email=test1@email.com --name=stima1 --password=123456 --team etimo --host http://20.243.68.103:8082/api/ --board=2"
@REM start cmd /c "python main.py --logic Random --email=test2@email.com --name=stima2 --password=123456 --team etimo"
@REM start cmd /c "python main.py --logic Random --email=test3@email.com --name=stima3 --password=123456 --team etimo"


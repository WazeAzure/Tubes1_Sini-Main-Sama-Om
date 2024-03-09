@echo off
start cmd /k "python main.py --logic DenBot --email=denbot@email.com --name=denbot --password=123456 --team etimo --host http://20.243.68.103:8082/api/ --board=2"
start cmd /c "python main.py --logic EdBot --email=edbot@email.com --name=edbot --password=123456 --team etimo --host http://20.243.68.103:8082/api/ --board=2"
start cmd /c "python main.py --logic FDL --email=fdl@email.com --name=fdl --password=123456 --team etimo --host http://20.243.68.103:8082/api/ --board=2"
start cmd /c "python main.py --logic VanBot --email=vanbot@email.com --name=vanbot --password=123456 --team etimo --host http://20.243.68.103:8082/api/ --board=2"
@REM start cmd /c "python main.py --logic Random --email=test2@email.com --name=stima2 --password=123456 --team etimo"
@REM start cmd /c "python main.py --logic Random --email=test3@email.com --name=stima3 --password=123456 --team etimo"
@REM start cmd /k "python main.py --logic OptBot --email=optbot@email.com --name=optbot --password=123456 --team etimo --host http://20.243.68.103:8082/api/ --board=2"
@echo off
start cmd /k "python main.py --logic OptBot --email=optbot1@email.com --name=optbot1 --password=123456 --team etimo"
start cmd /c "python main.py --logic OptBot --email=optbot2@email.com --name=optbot2 --password=123456 --team etimo"
start cmd /c "python main.py --logic AstLog --email=astlog1@email.com --name=astlog1 --password=123456 --team etimo"
start cmd /c "python main.py --logic AstLog --email=astlog2@email.com --name=astlog2 --password=123456 --team etimo"
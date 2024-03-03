1. Run this before starting the python environment
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
1a. If imports are not happening
 VSCode, Ctrl + Shift + P -> Type and select 'Python: Select Interpreter' - PICK THE GLOBAL ONE

1b. Create docker image from requirements.txt and docker-compose.yml
docker-compose build --no-cache
docker-compose up


2. Microservice directory (PS C:\VSCode\Learning\MicroService\microserviceenv> Scripts\activate) type: 
Scripts\activate
3. to deactivate the virtual environment run
Scripts\deactivate.bat
pip list
pip install djangorestframework 
pip install django
pip list
4. Runs server -- windows uses python, unix macos have python3
Might need to start previous docker images that were stopped.
python manage.py runserver 
5. Find docker containers running
docker PS

6. Connect to container with a shell command
docker exec -it 30e8988fcb9e bash
7. check folder structure and instlaled components
pip list
ls 

6. Connect to container by service name
docker-compose exec backend sh




59 mins https://www.youtube.com/watch?v=0iB5IPoTDts&t=2112s




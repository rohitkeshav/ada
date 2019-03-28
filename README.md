Another Django App

__Rent management platform.__
__Built using Django on the frontend and React on the frontend__

## Getting Started (Unix environment)

Must be a python 3.6.x environment. 3.5 has breaking changes

1. Install pipenv -
    ```
        sudo apt-get install pipenv
    ```
2. Clone repo -
    ```
        https://github.com/rohitkeshav/ada.git
    ```
3. Install all dependencies -
    ```
        pipenv install
4. Activate pipenv shell (similar to activating virtual environment) -
    ```
        pipenv shell
    ```
5. Make migrations -
    ```
        python manage.py makemigrations rent
        python manage.py migrate
    ```
6. Setup the frontend -
    ```
        cd frontend/
        npm install && cd ..
    ```
7. Run project locally -
    ```
        python manage.py runserver
    ```

__Open 127.0.0.1:8000 on your browser to see the rendered React App with the Django backend__

# Instructions for configuring and launching the project

 Щоб встановити та запустити проект, виконайте наступні кроки:

1. Clone the repository:

    ```bash
    git clone https://github.com/Hant0-0/test_for_Solidway.git
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Perform migrations to create a database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Go to the `core` directory:

    ```bash
    cd core
    ```

6. Load the test data into the database:

    ```bash
    python manage.py loaddata test_list/fixtures/dogs_data.json
    ```

Now your project should be ready to use!

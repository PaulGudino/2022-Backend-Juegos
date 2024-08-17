# Installation Manual

## Introduction
This manual provides step-by-step instructions for setting up the project's local environment. Follow these instructions carefully to ensure a successful installation.

## Prerequisites
Before starting the installation process, make sure you have the following software installed on your system:
- Python 3.10.0
- Node.js
- MySQL Workbench
- Microsoft Visual C++ 14.0
- Source code editor (of your choice)
- asgiref==3.5.2
- cached-property==1.5.2
- Django==4.1.1
- django-cors-headers==3.13.0
- django-filter==22.1
- django-simple-history==3.0.0
- djangorestframework==3.13.1
- djangorestframework-simplejwt==5.2.0
- enum-compat==0.0.3
- mysqlclient==2.1.1
- Pillow==9.2.0
- PyJWT==2.4.0
- pytz==2022.2.1
- six==1.16.0
- sqlparse==0.4.2
- tzdata==2022.2


## System Requirements
Ensure that your system meets the following minimum requirements:
- **Operating System:** Windows, macOS, or Linux
- **Processor:** Dual-core processor or higher
- **Memory:** 8 GB of RAM or more
- **Storage:** 20 GB or more of available disk space

## Installation Summary
This section provides an overview of the installation steps:
1. Configure the database.
2. Clone and set up the frontend and backend repositories.
3. Configure the environment.
4. Run the application.
5. Access the admin interface and manage the assets.

## Step 1: Database Configuration
To configure the MySQL database, follow these steps:
1. Open MySQL Workbench.
2. Run the following queries to set up the database:
    ```sql
    DROP DATABASE juegos;
    CREATE DATABASE juegos;
    USE juegos;
    CREATE USER 'admin'@'localhost' IDENTIFIED BY 'Root@123';
    GRANT ALL PRIVILEGES ON juegos.* TO 'admin'@'localhost';
    FLUSH PRIVILEGES;
    ```

## Step 2: Repository Cloning and Setup
To start working on the project, clone the necessary repositories (frontend and backend) and follow the steps below:

### Backend Setup
1. Clone the backend repository.
   ```bash
    git clone https://github.com/RobertoEncalada/T2-Backend-Kiosco-Touch
    ```
3. Navigate to the backend directory.
   ```bash
    git checkout local
    ```
5. Activate the virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
6. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
7. Apply the database migrations and start the server:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

### Frontend Setup (Optional)
1. Clone the frontend repository.
2. Navigate to the frontend directory.
3. Install the necessary packages:
    ```bash
    npm install
    ```
4. Start the development server:
    ```bash
    npm start
    ```

## Step 3: Environment Configuration
After setting up the backend and frontend, ensure that all environment variables are properly configured. This includes setting up the database connection, API keys, and other necessary configurations. Refer to the `.env.example` file in each repository for guidance.

## Step 4: Running the Application
Once everything is set up, you can run the application by following these steps:
1. Ensure that the backend server is running.
2. Start the frontend server (if applicable).
3. Access the application at:
    ```url
    http://localhost:8000
    ```

## Step 5: Creating a Superuser
To access the Django admin interface, create a superuser by running:
    ```bash
    python manage.py createsuperuser
    ```
Recommended settings:
- **Username:** root
- **Email:** root@example.com
- **Password:** root

## Step 6: Accessing the Admin Interface
Once the server is running, you can access the admin interface by navigating to:
    ```url
    127.0.0.1:8000/admin
    ```

## Asset Upload and Game Management
1. Navigate to the styles section and upload the necessary assets.
2. In the games section, add the games to the database.

## Troubleshooting
If you encounter any issues during installation, consider the following:
- **Database Connection Errors:** Ensure that MySQL is running and that the connection credentials in the environment variables are correct.
- **Server Not Starting:** Ensure that all dependencies are installed and that the virtual environment is activated.
- **Access Issues:** Verify the superuser credentials and ensure that the migrations have been applied correctly.

## Completion of Configuration
To finish setting up the project, access the admin view and upload the missing styles for each game by navigating to:
    ```url
    localhost:4200/#/login
    ```
To play, access:
    ```url
    localhost:4200/#/juego
    ```

## Uninstallation
To uninstall the application, follow these steps:
1. Deactivate the virtual environment:
    ```bash
    deactivate
    ```
2. Delete the cloned repositories and any associated files.
3. Delete the database by running:
    ```sql
    DROP DATABASE juegos;
    ```
## Participants
- Roberto Encalada
- Jefferson Eras
- Irving Macías
- Nick Arévalo

## Appendix
### Communications folder
- [Acceptance letter](https://github.com/RobertoEncalada/T2-Backend-Kiosco-Touch/tree/local/Communications/Acceptance%20letter): client acceptance card
- [Images](https://github.com/RobertoEncalada/T2-Backend-Kiosco-Touch/tree/local/Communications/Images): face-to-face meetings we had
- [Messages](https://github.com/RobertoEncalada/T2-Backend-Kiosco-Touch/tree/local/Communications/Messages): Whatsapp group chats between us and the client

   
### Additional Resources
- **Documentation:** Refer to the official project documentation for more detailed instructions and advanced configuration options.



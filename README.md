# Python Licensing System

![License](https://img.shields.io/badge/license-MIT-blue.svg)

Welcome to the Python Licensing System repository! This open-source project provides a comprehensive licensing solution 
for your software applications. It consists of two main components: a server application built with Flask and a client 
library using curses. Together, they enable you to manage licenses for your applications effortlessly.

## Features

- **Flexible Licensing:** Easily integrate our licensing library into your Python applications, enabling you to control 
access and usage.
- **Database Integration:** The server application connects to a database to store and manage license information, 
including software details, expiration dates, and user data.
- **Curses-based Interface:** The client library offers a user-friendly, text-based interface using curses, making it 
accessible across various platforms.
- **RESTful API:** Manage licenses and interact with the licensing system through a RESTful API provided by the server 
application.
- **Secure and Scalable:** Built with security in mind, our system ensures that your software's licensing is robust and 
scalable as your user base grows.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Pipenv for managing dependencies (install using `pip install pipenv`)

### Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/your-username/python-licensing-system.git

2. Navigate to the project directory:

   ```shell
   cd python-licensing-system

3. Install the required dependencies using Pipenv:

    ```shell
   pipenv install

## Usage
### Server Application

1. Configure your database settings in server/config.py.

2. Initialize the database:
     ```shell
    pipenv run python server/init_db.py

3. Start the server:
    ```shell
   pipenv run python server/app.py

4. Your server is now running at http://localhost:5000. You can interact with it through the RESTful API.

### Client Library

1. Import the licensing module into your Python application:
   ```shell
   from licensing import LicensingClient
2. Create an instance of LicensingClient and use its methods to manage licenses in your application.

For detailed usage examples, check the documentation.

## Contributing

We welcome contributions from the community! If you'd like to improve the Python Licensing System or report issues, 
please check our [contribution guidelines]().

## License

This project is licensed under the MIT License - see the [LICENSE]() file for details.
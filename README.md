# Python Calculator Project

This project demonstrates the integration of a complete CI/CD pipeline using GitHub Actions. The pipeline includes stages for linting, testing, code coverage, Dockerization, and automated deployment to a remote server.

## Features

- **Linting**: Analyzes Python code using `pylint` to ensure adherence to coding standards and best practices.
- **Testing**: Executes unit tests with `pytest` and generates a code coverage report to verify the correctness and quality of the code.
- **Code Coverage**: Uploads the test coverage report as an artifact for further analysis and quality assurance.
- **Dockerization**: Builds a Docker image of the application and pushes it to Docker Hub, providing a consistent deployment environment.
- **Deployment**: Automates deployment by connecting to a remote server via SSH to pull and run the latest Docker image, ensuring the application is always up-to-date.

## CI/CD Pipeline

The CI/CD pipeline is defined using GitHub Actions and includes the following jobs:

1. **Lint**
   - **Runs-on**: `ubuntu-latest`
   - **Steps**:
     - Checkout the code.
     - Set up Python environment.
     - Install `pylint`.
     - Run `pylint` on the `calculator.py` file.

2. **Test**
   - **Runs-on**: `ubuntu-latest`
   - **Needs**: `lint`
   - **Steps**:
     - Checkout the code.
     - Set up Python environment.
     - Install dependencies from `requirements.txt`.
     - Run `pytest` and generate a code coverage report.
     - Upload the coverage report as an artifact.

3. **Build and Push Docker Image**
   - **Runs-on**: `ubuntu-latest`
   - **Needs**: `test`
   - **Steps**:
     - Checkout the code.
     - Set up Docker Buildx.
     - Log in to Docker Hub.
     - Build and tag the Docker image.
     - Push the Docker image to Docker Hub.

4. **Deploy**
   - **Runs-on**: `ubuntu-latest`
   - **Needs**: `build-and-push`
   - **Steps**:
     - Set up SSH.
     - Deploy to server via SSH:
       - Pull the latest Docker image from Docker Hub.
       - Stop and remove any existing containers.
       - Run the new Docker container.

## Getting Started

### Prerequisites

- **Python**: Ensure Python 3.12.4 is installed for development.
- **Docker**: Ensure Docker is installed and running on the target deployment server.
- **GitHub Secrets**: Set up the following secrets in your GitHub repository:
  - `DOCKER_USERNAME`: Your Docker Hub username.
  - `DOCKER_TOKEN`: Your Docker Hub access token or password.
  - `SSH_PRIVATE_KEY`: Your private SSH key for server access.
  - `SERVER_USER`: The username for SSH access to the server.
  - `SERVER_HOST`: The IP address or hostname of the deployment server.

### Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/python-calculator.git
   cd python-calculator

pipeline {
    agent any
    
    stages {
        stage('Set Up Python and Install Dependencies') {
            steps {
                script {
                    // Set up Python
                    sh 'python -m pip install --upgrade pip'
                    // Install dependencies
                    sh 'pip install -r ./src/requirements.txt'
                }
            }
        }
        
        stage('Start Services with Docker Compose') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }
        
        stage('Add .env file') {
            steps {
                script {
                    sh "echo '${{ secrets.ENV_FILE }}' > .env"
                }
            }
        }
        
        stage('Wait') {
            steps {
                script {
                    sh 'sleep 20'
                }
            }
        }
        
        stage('Run Pytest') {
            steps {
                script {
                    sh 'pytest'
                }
            }
        }
        
        stage('Remove .env file') {
            steps {
                script {
                    sh 'rm .env'
                }
            }
        }
        
        stage('Shutdown Docker Compose') {
            steps {
                script {
                    sh 'docker-compose down'
                }
            }
        }
        
        stage('Configure AWS Credentials') {
            steps {
                script {
                    // Configure AWS Credentials
                }
            }
        }
        
        stage('Login to Amazon ECR') {
            steps {
                script {
                    // Login to Amazon ECR
                }
            }
        }
        
        stage('Build, tag, and push image to Amazon ECR') {
            steps {
                script {
                    // Build, tag, and push image to Amazon ECR
                }
            }
        }
    }
}

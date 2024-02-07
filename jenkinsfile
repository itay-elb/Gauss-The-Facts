pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'project:latest'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/itay-elb/project.git'
            }
        }
        
        stage('Build') {
            steps {
                script {
                    docker.build DOCKER_IMAGE
                }
            }
        }
        
        stage('Set Up Python and Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r ./src/requirements.txt'
            }
        }
        
        stage('Start Services with Docker Compose') {
            steps {
                sh 'docker-compose -f docker-compose.yml up -d'
            }
        }
        
        stage('Run Pytest') {
            steps {
                sh 'pytest'
            }
        }
        
        stage('Shutdown Docker Compose') {
            steps {
                sh 'docker-compose -f docker-compose.yml down'
            }
        }
    }
    
    post {
        always {
            // Clean up docker resources
            sh 'docker-compose -f docker-compose.yml down -v --remove-orphans'
        }
        success {
            emailext subject: 'Build Successful',
                      body: 'Your build was successful. Congratulations!',
                      to: 'lioramar8991@gmail.com'
        }
        failure {
            emailext subject: 'Build Failed',
                      body: 'Your build has failed. Please investigate and take appropriate actions.',
                      to: 'lioramar8991@gmail.com'
        }
    }
}

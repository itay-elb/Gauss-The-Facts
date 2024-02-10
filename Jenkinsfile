pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/itay-elb/project.git'
            }
        }
        
        stage('Set Up Python') {
            steps {
                script {
                    sh 'python -m pip install --upgrade pip'
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r ./src/requirements.txt'
            }
        }
        
        stage('Start Services with Docker Compose') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        
        stage('Add .env file') {
            steps {
                script {
                    // Define your environment variable here
                    def envFileContent = env.ENV_FILE
                    sh "echo '${envFileContent}' > .env"
                }
            }
        }
        
        // Add other stages as needed
        
        stage('Remove .env file') {
            steps {
                sh 'rm .env'
            }
        }
        
        stage('Shutdown Docker Compose') {
            steps {
                sh 'docker-compose down'
            }
        }
    }
    
    post {
        always {
            // Clean up docker resources
            sh 'docker-compose down -v --remove-orphans'
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

pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from GitHub
                git 'https://github.com/itay-elb/project.git'
            }
        }
        
        stage('Build and Test') {
            steps {
                // Set up Python environment and install dependencies
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r ./src/requirements.txt'
                
                // Run tests using pytest
                sh 'pytest'
            }
        }
    }
    
    post {
        always {
            // Clean up resources if needed
        }
        success {
            // Send success notification via email
            emailext subject: 'Build Successful',
                      body: 'Your build was successful. Congratulations!',
                      to: 'lioramar8991@gmail.com'
        }
        failure {
            // Send failure notification via email
            emailext subject: 'Build Failed',
                      body: 'Your build has failed. Please investigate and take appropriate actions.',
                      to: 'lioramar8991@gmail.com'
        }
    }
}

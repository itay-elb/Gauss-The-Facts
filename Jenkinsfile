pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Checkout code from repository
                checkout scm
                
                // Set up Python
                script {
                    sh 'python -m pip install --upgrade pip'
                }
                
                // Install dependencies
                script {
                    sh 'pip install -r src/requirements.txt'
                }
                
                // Start services with Docker Compose
                script {
                    sh 'docker-compose up -d'
                }
                
                // Add .env file
                script {
                    withCredentials([string(credentialsId: 'ENV_FILE', variable: 'ENV_FILE')]) {
                        sh "echo '\${ENV_FILE}' > .env"
                    }
                }
                
                // Wait
                script {
                    sh 'sleep 20'
                }
                
                // Run Pytest
                script {
                    sh 'pytest'
                }
                
                // Remove .env file
                script {
                    sh 'rm .env'
                }
                
                // Shutdown Docker Compose
                script {
                    sh 'docker-compose down'
                }
                
                // Configure AWS Credentials
                script {
                    withCredentials([awsAccessKey(credentialsId: 'AWS_ACCESS_KEY_ID', accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                        sh 'aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID'
                        sh 'aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY'
                        sh 'aws configure set region us-east-1'
                    }
                }
                
                // Login to Amazon ECR
                script {
                    sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ECR_REGISTRY'
                }
                
                // Build, tag, and push image to Amazon ECR
                script {
                    sh 'docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_DB_TAG ./db/'
                    sh 'docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_DB_TAG'
                    sh 'docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_APP_TAG ./src/'
                    sh 'docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_APP_TAG'
                }
            }
        }
    }
}

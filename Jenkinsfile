pipeline {  
    agent any  

    environment {  
        // Define the Docker image name and tag  
        IMAGE_NAME = '2350_ISA2'  
        IMAGE_TAG = 'latest'  
    }  

    stages {  
        stage('Clone Repository') {  
            steps {  
                // Checkout the repository containing the Dockerfile  
                git branch: 'main', url: 'https://github.com/USERNAME/REPOSITORY_NAME.git'  
            }  
        }  

        stage('Build Docker Image') {  
            steps {  
                script {  
                    // Build the Docker image  
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."  
                }  
            }  
        }    
    }  

    post {  
        always {  
            // Clean up workspace  
            cleanWs()  
        }  
        success {  
            echo "Docker image ${IMAGE_NAME}:${IMAGE_TAG} built and pushed successfully."  
        }  
        failure {  
            echo "There was an error building the Docker image."  
        }  
    }  
}

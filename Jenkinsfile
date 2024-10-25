pipeline {  
    agent any  


    stages {  
        stage('Clone Repository') {  
            steps {  
                // Checkout the repository containing the Dockerfile  
                git branch: 'main', url: 'https://github.com/AnkurFalari/2350_ISA2.git'  
            }  
        }  

        stage('Build Docker Image') {  
            steps {  
                script {  
                    // Build the Docker image  
                    bat "docker build -t ankurmca/2350_isa2 ." 
                }  
            }
        }

        stage('Build & run docker container') {
        steps {
            script {
                bat "docker rm -f 2350 || exit 0"
                    
                bat "docker run -d --2350 ankurmca/2350_isa2"
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
            echo "Docker image built successfully."  
        }  
        failure {  
            echo "There was an error building the Docker image."  
        }  
    }  
}
}

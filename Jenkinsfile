pipeline {  
    agent any  

    stages {  
        stage('Clone Repository') {  
            steps {  
                // Clone the repository from GitHub  
                git branch: 'main', url: 'https://github.com/USERNAME/REPOSITORY_NAME.git'  
                // If the repository is private, use credentials  
                // git credentialsId: 'your-credentials-id', branch: 'main', url: 'https://github.com/USERNAME/REPOSITORY_NAME.git'  
            }  
        }  
    }  

    post {  
        always {  
            // Archive the workspace or perform other post-build actions  
            echo 'Finished cloning the repository.'  
        }  
    }  
}

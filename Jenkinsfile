pipeline {
   agent any
   stages {
    stage('Checkout') {
      steps {
        script {
           // The below will clone your repo and will be checked out to master branch by default.
           git credentialsId: 'AnkurFalari', url: 'https://github.com/AnkurFalari/2350_ISA2.git'
           // Do a ls -lart to view all the files are cloned. It will be clonned. This is just for you to be sure about it.
           sh "ls -lart ./*" 
           // List all branches in your repo. 
           sh "git branch -a"
           // Checkout to a specific branch in your repo.
           sh "git checkout main"
          }
       }
    }

  
    stage('Build docker image') {
        steps {
            scripts {
                bat "docker build -t ankurmca/2350_ISA2 ."
                }
            }
        }
	
	stage('Build & run docker container') {
        steps {
            scripts {
                bat "docker rm -f my-app-container || exit 0"
                    
                bat "docker run -d --name my-app-container ankurmca/2350_ISA2"
                }
          }
      }
		
		

   }	
}

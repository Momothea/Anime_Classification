pipeline {
    agent any
    environment{
        DOCKERHUB_CREDENTIALS = credentials('momotheID')
        GITHUB_CREDENTIALS = credentials('privateKey1')
    }
    

    stages {

        stage('version') {
            steps {
                sh'python --version'
                sh'pwd'
            }
        }
        stage('Creanting staging branch') {
            steps { 
                sshagent(credentials: ['privateKey1']) {
                    sh'git branch --delete staging'
                    sh'git checkout -b staging remotes/origin/dev2'
                    sh'git checkout staging'
                    sh'git branch --all'
                    }
            }
        }
        
        stage('Installing requirements') {
            steps {
                
                sh'pip install -r flask_web_application/requirements.txt'
                sh'pip install -r Model/requirements.txt'
            }
        }

        stage('testing the app') {
            steps {
                sh'python -m unittest'
            }
        }

        stage('build  Docker images') {
            steps {
                sh'docker build -t momothe/flask:flaskweb_latest ./flask_web_application'
                sh'docker build -t momothe/flask:model_latest ./Model'
                
            }
        }

        stage('launch application the app') {
            steps {
                sh'docker compose up -d'
            }
        }


        stage('sign in dockerhub'){
            steps {
                sh'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }

        stage('Push in dockerhub'){
            steps {
                sh'docker push momothe/flask:flaskweb_latest'
                sh'docker push momothe/flask:model_latest'
            }
        }

        stage('Merge with master'){
            steps {
                sshagent(credentials: ['privateKey1']) {
                    sh'git pull'
                    sh'git checkout staging'
                    sh'git checkout master'
                    sh'git merge staging' 
                    sh'git push -f origin master'
                    
                    }
            }
        }    
    }
    
    post{
        always{
            sh'docker logout'
        }
    }
}

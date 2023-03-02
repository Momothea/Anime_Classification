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
                sh'cd  flask_web_application'
                sh'pwd'
                sh'docker build -t momothe/flask:flaskweb_latest .'
                sh'cd ..'
                sh'cd  Model'
                sh'pwd'
                sh'docker build -t momothe/flask:model_latest .'
                sh'cd ..'
            }
        }

        stage('launch application the app') {
            steps {
                sh'docker compose up'
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

        stage('Merge with dev3'){
            steps {
                sshagent(credentials: ['privateKey1']) {
                    sh'git pull'
                    sh'git checkout staging'
                    sh'git checkout dev3'
                    sh'git merge staging' 
                    sh'git push -f origin dev3'
                    
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

pipeline {
   agent any
   
    stages {
        stage('Checkout') {
            steps {
                 git url: 'https://github.com/Humphrey-nyaga/devops.git/', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                script {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '. venv/bin/activate && python3 -m pytest'
                }
            }
        }
    }
}


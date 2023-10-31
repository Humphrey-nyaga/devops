pipeline {
    agent any // You can specify a specific agent label if needed
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

pipeline {
    agent any

    stages {

        stage('Hello') {
            steps {
                echo 'Bonjour depuis Jenkins'
            }
        }

        stage('Infos environnement') {
            steps {
                echo "Nom du noeud Jenkins: ${env.NODE_NAME}"
                echo "Workspace: ${env.WORKSPACE}"
            }
        }

        stage('Installation des dependances') {
            steps {
                bat '"C:/Users/GIGABYTE/AppData/Local/Microsoft/WindowsApps/python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Execution des tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }
    }
}


pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Bonjour ! Mon pipeline a été modifié.'
            }
        }

        stage('Infos environnement') {
            steps {
                echo "Nom du noeud Jenkins: ${env.NODE_NAME}"
                echo "Workspace: ${env.WORKSPACE}"
            }
        }
    }
}

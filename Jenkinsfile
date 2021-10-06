pipeline {

  agent any

  stages {

    stage('Prepare Agent') {
      steps {
        sh 'sudo su'
        sh 'apt-get update && apt-get install -y apt-transport-https \
               ca-certificates curl gnupg2 \
               software-properties-common'
        sh 'curl -L \
          "https://github.com/docker/compose/releases/download/1.25.3/docker-compose-$(uname -s)-$(uname -m)" \
          -o /usr/local/bin/docker-compose \
          && sudo chmod +x /usr/local/bin/docker-compose'
      }
    }
    stage('Build Docker Image'){
      steps {
        sh 'docker build .'
        sh 'docker version'
        sh 'docker-compose version'
    }
  }
    stage('test') {

      steps {
        sh 'docker-compose run app sh -c "python manage.py test && flake8"'
      }
    }

    stage('deploy') {
      steps {
        sh 'echo Deployed sucessfully!'
      }
    }

  }

}

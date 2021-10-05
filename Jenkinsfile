pipeline {

  agent any

  stages {

    stage('Build Docker Image'){
      steps {
      sh 'docker build .'
      sh 'sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
      sh 'sudo chmod +x /usr/local/bin/docker-compose'
      sh 'docker-compose build'
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

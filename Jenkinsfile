pipeline {

  agent any

  stages {

    stage('Build Docker Image'){
      steps {
      sh 'docker version'
      sh 'docker compose version'
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

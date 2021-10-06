pipeline {

  agent any

  stages {

    stage('Build Docker Image'){
      steps {
        sh 'docker build .'
        sh 'docker-compose build'
    }
  }
    stage('test') {

      steps {
        sh 'docker-compose run app sh -c "python manage.py test"'
      }
    }

    stage('deploy') {
      steps {
        sh 'echo Deployed sucessfully!'
      }
    }

  }

}

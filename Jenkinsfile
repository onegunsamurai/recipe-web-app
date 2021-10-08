pipeline {

  agent any

  stages {

    stage('Build Docker Image'){
      steps {
        sh 'export uid=${uid} && export gid=${gid}'
        sh 'docker build .'
        sh 'docker-compose build'
    }
  }
    stage('test') {

      steps {
        sh 'docker-compose up app sh -c "python manage.py wait_for_db"'
        sh 'docker-compose up app sh -c "python manage.py test"'
      }
    }

    stage('deploy') {
      steps {
        sh 'echo Deployed sucessfully!'
      }
    }

  }

}

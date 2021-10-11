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
        sh "docker-compose run app sh -c 'python manage.py migrate'"
        sh 'docker-compose run app sh -c "python manage.py test"'
      }
    }

    stage('Stop Postgres') {
      steps {
        sh 'sudo kill -9 $(ps ax | grep postgres | awk "{print $1}")'
      }
    }

  }

}

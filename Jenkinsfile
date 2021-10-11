def DB_HOST
def DB_NAME
def DB_USER
def DB_PASS

pipeline {

  agent any

  environment {
    DB_HOST = credentials('db-host')
    DB_NAME = credentials('db-name')
    DB_USER = credentials('db-user')
    DB_PASS = credentials('db-password')
  }

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
        sh 'echo Deployed sucessfully!'
        sh 'docker system prune -a -f'
        sh 'sudo kill -9 $(ps -ax | grep postgres | awk "{print $1}" )'
      }
    }

  }

}

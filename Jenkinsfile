def DB_HOST
def DB_NAME
def DB_USER
def DB_PASS

pipeline {

  agent any

  environment {
    DB_HOST = "credentials('DB_HOST')"
    DB_NAME = "credentials('DB_NAME')"
    DB_USER = "credentials('DB_CREDS_USR')"
    DB_PASS = "credentials('DB_CREDS_PS')"

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
      }
    }

  }

}

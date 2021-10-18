pipeline {

  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '3'))
  }
  environment {
    DB_HOST = 'db'
    DB_NAME = credentials('db-name')
    DB_USER = credentials('db-user')
    DB_PASS = credentials('db-password')
    registry = 'onegunsamurai/ogs-django-web-app'
    DOCKERHUB_CREDENTIALS = credentials('docker-id')
    PRIV_KEY = credentials('SSH-SERV-CREDS')
  }

  stages {

    stage('Build Docker Image'){
      steps {
        script {
        sh "docker build -t $registry ."
        sh "docker-compose build"
      }
    }
  }
    stage('Run Unit Tests') {

      steps {
        sh "docker-compose run app sh -c 'python manage.py migrate'"
        sh 'docker-compose run app sh -c "python manage.py test"'
      }
    }

    stage('Push To DockerHub') {
      steps {
          script {
            sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            sh "docker push $registry"
          }
        }
      }


    stage('Publish Over SSH') {
      steps {
        sh 'echo Deployed sucessfully!'
        sh 'ssh -T ubuntu@34.233.80.169 -i $PRIV_KEY_PSW'
        sh 'cd project'
        sh 'git clone git@github.com:onegunsamurai/recipe-web-app.git'
        sh 'docker-compose up'
        sh 'exit'
      }
    }

  }

  post {
    always {
      sh 'docker logout'
      sh "docker rmi $registry"
    }
  }

}

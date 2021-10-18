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
        sshPublisher(publishers: [sshPublisherDesc(configName: 'Main', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: """
        cd recipe-web-app
        """, execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
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

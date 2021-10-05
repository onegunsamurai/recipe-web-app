pipeline {

  agent any

  stages {
    stage('build') {

      steps {
        sh 'apt-get install docker-compose -y'
        sh 'docker build .'
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

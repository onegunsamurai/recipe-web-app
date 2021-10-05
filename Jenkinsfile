pipeline {

  agent {
    docker { image 'python:3.7-apline' }
   }

  stages {
    stage('build') {

      steps {
        sh 'pip install -r docker-compose'
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

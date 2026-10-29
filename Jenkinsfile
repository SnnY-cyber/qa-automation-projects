pipeline {
  agent any
  options { timestamps() }
  stages {
    stage('Selenium + Python') {
      steps {
        sh 'python3 -m pip install -r python-selenium/requirements.txt'
        sh 'pytest -q python-selenium/tests'
      }
      post {
        always {
          archiveArtifacts artifacts: 'python-selenium/artifacts/**/*.png', allowEmptyArchive: true
        }
      }
    }
    stage('Postman + Newman') {
      steps {
        sh 'npm install --global newman@6'
        sh 'newman run postman/QA-API-Checks.postman_collection.json --reporters cli,junit --reporter-junit-export postman/newman-report.xml'
      }
      post {
        always {
          junit testResults: 'postman/newman-report.xml', allowEmptyResults: true
        }
      }
    }
  }
}

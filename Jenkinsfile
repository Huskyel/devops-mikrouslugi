pipeline {
    agent any
    environment {
        APP_NAME = "moja-aplikacja"
        APP_VERSION = "1.0.${BUILD_NUMBER}"
    }
    stages {
        stage('Pobranie kodu') {
            steps {
                checkout scm
            }
        }
        stage('Testy') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }
        stage('Budowanie obrazu') {
            steps {
                sh "docker build --build-arg APP_VERSION=${APP_VERSION} -t ${APP_NAME}:${APP_VERSION} -t ${APP_NAME}:latest ."
            }
        }
        stage('Wdrozenie Compose') {
            steps {
                sh "docker-compose up -d --build"
            }
        }
        stage('Wdrozenie Staging') {
            steps {
                sh "docker rm -f app-staging || true"
                sh "docker run -d --name app-staging -p 5001:5000 -e APP_VERSION=${APP_VERSION} ${APP_NAME}:${APP_VERSION}"
            }
        }
        stage('Wdrozenie Production') {
            steps {
                sh "docker rm -f app-prod-env || true"
                sh "docker run -d --name app-prod-env -p 5002:5000 -e APP_VERSION=${APP_VERSION} ${APP_NAME}:${APP_VERSION}"
            }
        }
    }
    post {
        failure {
            sh "docker-compose stop web || true"
        }
    }
}

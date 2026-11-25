pipeline {
    agent any
    environment {
        APP_NAME = "moja-aplikacja"
        CONTAINER_NAME = "aplikacja-prod"
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
        stage('Wdrozenie') {
            steps {
                sh "docker tag ${APP_NAME}:${APP_VERSION} ${APP_NAME}:previous || true"
                sh "docker rm -f ${CONTAINER_NAME} || true"
                sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${APP_NAME}:${APP_VERSION}"
            }
        }
    }
    post {
        failure {
            sh "docker rm -f ${CONTAINER_NAME} || true"
            sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${APP_NAME}:previous || true"
        }
    }
}

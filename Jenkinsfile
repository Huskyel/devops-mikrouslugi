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
                sh "docker compose up -d --build"
            }
        }
    }
    post {
        failure {
            sh "docker compose stop web || true"
        }
    }
}

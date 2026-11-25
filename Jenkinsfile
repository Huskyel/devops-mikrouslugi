pipeline {
    agent any
    stages {
        stage('Pobranie kodu') {
            steps {
                checkout scm
            }
        }
        stage('Budowanie obrazu Docker') {
            steps {
                sh 'docker build -t moja-aplikacja:${BUILD_NUMBER} .'
            }
        }
        stage('Weryfikacja obrazu') {
            steps {

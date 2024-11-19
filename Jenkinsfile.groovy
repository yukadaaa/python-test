pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Скачивание кода из репозитория
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // Установка зависимостей
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Запуск тестов
                sh 'pytest --junitxml=report.xml'
            }
        }
    }
    post {
        always {
            // Сохранение отчета о тестах
            junit 'report.xml'
        }
    }
}

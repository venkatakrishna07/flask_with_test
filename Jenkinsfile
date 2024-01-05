pipeline{
    agent { docker {image 'python:latest'}}
    stages{
        stage('build'){
            steps{
                sh 'pip install flask'
            }
        }
        stage('test'){
            steps{
                sh 'pytest test_file.py'
            }
        }
    }
}
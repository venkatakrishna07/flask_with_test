pipeline{
    agent { docker {image 'python:3.10.7'}}
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
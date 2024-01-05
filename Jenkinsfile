// pipeline{
//     agent { docker {image 'python:latest'}}
//     stages{
//         stage('build'){
//             steps{
//                 sh 'pip install flask'
//             }
//         }
//         stage('test'){
//             steps{
//                 sh 'pytest test_file.py'
//             }
//         }
//     }
// }

pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-v ${PWD}:/workspace'
        }
    }
    stages {
        stage('build') {
            steps {
                script {
                    def workspacePath = '/workspace'
                    dir(workspacePath) {
                        sh 'pip install flask'
                    }
                }
            }
        }
        stage('test') {
            steps {
                script {
                    def workspacePath = '/workspace'
                    dir(workspacePath) {
                        sh 'pytest test_file.py'
                    }
                }
            }
        }
    }
}

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
        }
    }
    environment {
        WORKSPACE = "/workspace"
    }
    stages {
        stage('build') {
            steps {
                dir("${WORKSPACE}") {
                    sh 'pip install flask'
                }
            }
        }
        stage('test') {
            steps {
                dir("${WORKSPACE}") {
                    sh 'pytest test_file.py'
                }
            }
        }
    }
}

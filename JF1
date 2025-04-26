pipeline {
    agent none
    stages {
        stage('Build web') {
            agent {
                dockerfile {
                    additionalBuildArgs '-t web'
                }
            }
            steps {
                sh 'echo web container was built'
            }
        }
        stage('Build Test Env') {
            agent {
                dockerfile {
                    dir 'tests'
                    additionalBuildArgs '-t test_env'
                }
            }
            steps {
                sh 'echo test env container was built'
            }
        }
        stage('Create network') {
            agent any
            steps {
                sh 'sh ./create_network.sh'
            }
        }
        stage('Test') {
            agent any
            steps {
                sh 'docker run --rm --network net -p 6379:6379 --name redis -d redis'
                sh 'echo Redis started!'
                sh 'docker run --rm --network net -p 80:80 --name web -d web'
                sh 'echo Web started!'
                sh 'docker run --network net test_env'
            }
            post {
                always {
                    sh 'docker kill web 2>/dev/null || true'
                    sh 'docker kill redis 2>/dev/null || true'
                }
            }
        }
    }
}


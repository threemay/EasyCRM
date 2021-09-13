pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                // checkout([$class: 'GitSCM', branches: [[name: '*/master']],
                // userRemoteConfigs: [[url: 'git@github.com:threemay/EasyCRM.git']]])
                git(
                    url: 'git@github.com:threemay/EasyCRM.git',
                    credentialsId: '1',
                    branch: "master"
                    )
                echo 'Hello World'
            }
        }


        // stage('Hello1') {
        //     steps {
        //         echo 'Hello World'
        //     }
        // }



        // stage('Hello2') {
        //     steps {
        //         echo 'Hello World'
        //     }
        // }
    }
}
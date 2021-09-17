pipeline {
    agent any


     environment {
                     GIT_REPO_URL = 'git@github.com:threemay/EasyCRM.git'
                     GIT_REPO_BRANCH = 'staging'
                     GIT_CREDENTIALS_ID = '1'
                     BUILD_USER_EMAIL = '254363807@qq.com'
                     BUILD_USER_ID = 'threemay'
                 }

    stages {

            stage('checkout from github') {

                steps {
                    echo '------------checkout from git------------'
                    git url: "${GIT_REPO_URL}",
                        credentialsId: "${GIT_CREDENTIALS_ID}",
                        branch: "${GIT_REPO_BRANCH}"
                    echo '------------checkout ./ ------------'
                }

            }


            stage('build') {

                steps {
                    echo '------------build------------'
                    sh'''
                        docker build -t easycrm .
                    '''
                    echo '------------build ./ ------------'
                }

            }

            stage('unit_test') {
                parallel {
                    stage('test_core'){
                        steps {
                            echo '------------test_core------------'
                            sh'''
                                docker container prune -f
                                docker run --name easycrm -d easycrm
                                docker exec easycrm sh -c "cp ./tests/test_core.py ./ && python -m unittest -v"
                            '''
                            echo '------------test_core ./------------'
                        }
                    }
                    
                    stage('test_auth'){
                        steps {
                            echo '------------test_auth------------'
                            sh'''
                                docker exec easycrm sh -c "cp ./tests/test_auth.py ./ && python -m unittest test_auth.py -v"
                            '''
                            echo '------------test_auth ./------------'
                        }
                    }
                }

            }

            stage('clean_up') {

                steps {
                    echo '------------clean_up------------'
                    sh'''
                    docker stop easycrm
                    docker rm easycrm
                    '''
                    echo '------------clean_up ./ ------------'
                }

            }

        //     stage('master -> staging') {
        //     steps {
                
        //         git url: "${GIT_REPO_URL}",
        //             credentialsId: "${GIT_CREDENTIALS_ID}",
        //             branch: "${GIT_REPO_BRANCH}"

                
        //         sshagent(["${GIT_CREDENTIALS_ID}"]) {
		// 		sh """
		// 			git config user.email "${BUILD_USER_EMAIL}"
		// 			git config user.name "${BUILD_USER_ID}"
		// 			git checkout "${GIT_REPO_BRANCH}"
        //             git pull origin master
        //             git branch
		// 			git rebase master
        //             git push origin staging
		// 		"""
		// 	    }

        //         echo 'Hello World'
        //     }
        // }


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
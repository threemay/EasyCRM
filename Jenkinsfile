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

            stage('checkout from git') {

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
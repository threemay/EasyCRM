pipeline {
    agent any


     environment {
                     GIT_REPO_URL = 'git@github.com:threemay/EasyCRM.git'
                     GIT_REPO_BRANCH = 'master'
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
                    ///add docker build -t easycrm . to next 3rd line
                    ///docker build -t easycrm . 
                    sh'''
                        docker run --name easycrm -d easycrm
                    '''
                }

            }

        //     stage('test_core'){
        //         steps {
        //             sh'''
        //                 docker container prune -f
        //                 docker exec easycrm sh -c "cp ./tests/test_core.py ./ && python -m unittest -v"
        //             '''
        //             }
        //     }

        //     stage('test_auth'){
        //         steps {
        //             sh'''
        //                 docker exec easycrm sh -c "cp ./tests/test_auth.py ./ && python -m unittest test_auth.py -v"
        //             '''
        //         }
        //     }
                    
        //     stage('integration test'){
        //         steps {
        //             sh'''
        //                 docker exec easycrm sh -c "curl http://0.0.0.0:8090/login/"
        //                 docker exec easycrm sh -c "curl -c cookies.txt -d 'username=test@gmail.com&password=shh' -X POST http://0.0.0.0:8090/login/"
        //                 docker exec easycrm sh -c "curl -b cookies.txt http://0.0.0.0:8090/"
        //                 docker exec easycrm sh -c "curl -b cookies.txt --request POST http://0.0.0.0:8090/organisation/create --form 'name="JiangRen"' --form 'type="other"' --form 'address="Wynyard"'"

        //             '''
        //         }
        //     }

        //     stage('load_test'){
        //                 steps {
        //                     sh'''
        //                         docker exec easycrm sh -c "locust -f load_test_easy_crm.py -u 1 -r 1 --host http://0.0.0.0:8090 --headless -t 3s"
        //                     '''
        //                 }
        //             }

        //     stage('webdriver_test'){
        //                 steps {
        //                     sh'''
        //                         python webdriver_easy_crm.py
        //                     '''
        //                 }
        //             }

        //     stage('clean_up') {

        //         steps {
        //             sh'''
        //             docker stop easycrm
        //             docker rm easycrm
        //             '''
        //         }

        //     }

        // //     stage('master -> staging') {
        // //     steps {
                
        // //         git url: "${GIT_REPO_URL}",
        // //             credentialsId: "${GIT_CREDENTIALS_ID}",
        // //             branch: "${GIT_REPO_BRANCH}"

                
        // //         sshagent(["${GIT_CREDENTIALS_ID}"]) {
		// // 		sh """
		// // 			git config user.email "${BUILD_USER_EMAIL}"
		// // 			git config user.name "${BUILD_USER_ID}"
		// // 			git checkout "${GIT_REPO_BRANCH}"
        // //             git pull origin master
        // //             git branch
		// // 			git rebase master
        // //             git push origin staging
		// // 		"""
		// // 	    }

        // //     }
        // // }


        stage('Hello1') {
            steps {
                echo 'Hello World'
                sh """
                    docker exec easycrm sh -c "chmod +x webdriver_test.sh"
                    docker exec easycrm sh -c "./webdriver_test.sh"
                """
            }
        }



        // stage('Hello2') {
        //     steps {
        //         echo 'Hello World'
        //     }
        // }
    }
}
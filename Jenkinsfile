pipeline{
	agent any

	stages {
	  stage('checkout code') {
	    steps {
	      // One or more steps need to be included within the steps block.
	      echo "checkout.."
	      checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'GitHub_SSH', url: 'git@github.com:HarmanSmith/TAE_Practice_API.git']]])
	    }
	  }

    stage('Build') {
        steps {
	    whoami
	    hostname
	    echo $PATH
	    python -V
            sh 'python --version'
            sh 'pip install --upgrade pip'
            sh 'pip install --no-cache-dir -r requirements.txt'
            }
    }

	  stage('test') {
	    steps {
	      // One or more steps need to be included within the steps block.
	      echo "testing.."
	      sh '''
                                set +e | python -m pytest -p no:cacheprovider -v -s --durations=50
             '''
	      echo "done."
	    }
	  }

	}


}
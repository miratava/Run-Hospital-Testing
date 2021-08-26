pipeline {
  
  agent any
  
  stages {
  
    stage("build") {
    
      steps {
        
        echo "biulding the application"
        
        script{
          
          def test = 2 + 2 > 3 ? "true" : "false"
          echo test
        
        }
      }
      
    }
    
    stage("test") {
    
      steps {
        
        echo "testing the application"
      
      }
    }
 
    stage("deploy") {
      
      steps {
        echo "deploying the application"
      }
    }
  }
}

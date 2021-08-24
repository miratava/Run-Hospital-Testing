# Run-Hospital-Testing
In order to execute tests you have to find test_hospital.py file and to run it from the console with pytest. You need to use the parametr --browser and to put appropriate value:
      --browser=firefox
        or
      --browser=chrome 
 
 If you want to collect test reports with hellping allure, you have to run test with a one more parametr --alluredir and point out the folder, where reports will save for example:
      --alluredir=allure_report
      which is in this repository or any others
      
If you need to change some data in the tests, you need to open test_hospital.py and change the parameters of  methods . 

# DevOps-Pipeline-Monitoring-System
AWS Based Build Monitoring System using S3 and Lambda
# DevOps Pipeline Monitoring System

## AWS-Based Build Monitoring System

### 1. Project Overview
The DevOps Pipeline Monitoring System is a Python-based automated build monitoring application integrated with AWS services. It executes automated unit tests and displays the build result through a web dashboard using LED indicators.

### 2. Objectives
- Automate application testing.
- Identify successful and failed builds.
- Integrate Python with AWS Lambda.
- Display real-time build status through a web dashboard.

### 3. Technologies Used
- **Programming Language:** Python
- **Cloud Platform:** Amazon Web Services (AWS)
- **AWS Services:** Amazon S3, AWS Lambda
- **Frontend:** HTML, CSS, JavaScript
- **Testing:** Python Unittest
- **Version Control:** GitHub

### 4. Project Features
- Automated execution of Python unit tests.
- Automatic detection of build success or failure.
- AWS Lambda integration.
- Green LED indicator for successful builds.
- Red LED indicator for failed builds.
- Web-based build monitoring dashboard.
- Manual success and failure testing buttons.

### 5. Project Structure

```text
DevOps-Pipeline-Monitoring-System/
├── application/
│   ├── app.py
│   └── test_app.py
├── build.py
├── index.html
└── README.md
```

### 6. System Workflow
1. The Python build script starts the application testing process.
2. Automated unit tests are executed.
3. The test result is identified as SUCCESS or FAILED.
4. The result is sent to AWS Lambda.
5. Lambda processes the build status.
6. The S3-hosted dashboard displays the corresponding LED indicator.

### 7. How to Run the Project

1. Clone the repository.
2. Open the project folder in VS Code.
3. Ensure Python is installed.
4. Run the following command:

```bash
py build.py
```

5. View the dashboard to check the build status.

### 8. Expected Output
- **GREEN LED:** Build Successful.
- **RED LED:** Build Failed.

### 9. Conclusion
This project demonstrates automated software testing and cloud-based build monitoring using Python and AWS services. It provides a simple visual approach to identifying application build results.

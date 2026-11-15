
import subprocess
import json
import urllib.request
import webbrowser

LAMBDA_URL = "https://7mbj4k6l32t6e5sdqbtuwumliy0tkrhi.lambda-url.us-east-1.on.aws/"

DASHBOARD_URL = "http://devops-indicator-the-achievers-2026.s3-website-us-east-1.amazonaws.com"

print("Starting application build...")

# Run automated tests
result = subprocess.run([
    "py", "-m", "unittest",
    "discover", "-s", "application",
    "-p", "test_*.py"
])

# Identify build status
if result.returncode == 0:
    status = "SUCCESS"
else:
    status = "FAILED"

print("\nBuild result:", status)
print("Sending result to AWS Lambda...")

# Send result to Lambda
data = json.dumps({"status": status}).encode("utf-8")

request = urllib.request.Request(
    LAMBDA_URL,
    data=data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

try:
    with urllib.request.urlopen(request) as response:
        output = json.loads(response.read().decode("utf-8"))

        print("\nAWS Lambda response:")
        print(json.dumps(output, indent=4))

        # Open dashboard with actual build status
        dashboard_link = DASHBOARD_URL + "?status=" + status

        print("\nOpening dashboard...")
        webbrowser.open(dashboard_link)

except Exception as error:
    print("\nUnable to contact AWS Lambda:", error)

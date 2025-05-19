# Savings Progress Microservice (Microservice A)
This microservice calculates the user's progress toward a savings goal and returns the result in a JSON format. It is designed to be used by the main dashboard to create a progress bar.
----
## Communication Contract
This microservice is accessed via an HTTP GET request. It does **not** rely on shared files or direct function calls.
## How to run the microservice:
1. Enter python app.py in your terminal. Confirm you see: Running on http://127.0.0.1:5056
2. Run your main program in a seperate terminal
3. Receive a JSON response containing savings goal data
   
## How to request data:
Send a GET request to the endpoint: 
Example code (javascript):
<img width="613" alt="Screenshot 2025-05-19 at 1 47 20 PM" src="https://github.com/user-attachments/assets/b1241b8f-2329-47b8-a385-2de8b481c874" />

---

## How to Receive Data
The microservice responds with a **JSON object** containing:
- the `goalName`
- the calculated `progressPercentage` as a number between 0 and 100
Example code (javascript):
<img width="489" alt="Screenshot 2025-05-19 at 1 47 41 PM" src="https://github.com/user-attachments/assets/8572ace2-547c-47f1-bc0f-ca5e44a800d3" />
---

UML Diagram:  

<img width="600" alt="Untitled" src="https://github.com/user-attachments/assets/a7f67dc5-190c-4820-849c-5882d27bb42b" />

Notes:
- This microservice calculates progress based only on the provided query parameters
- For best results, ensure your main dashboard handles the JSON response and renders the progress bar accordingly

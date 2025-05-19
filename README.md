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
'''javascript
async function requestAllProgressData() {
        const userId = "user123"; // or get dynamically if needed
        const response = await fetch(`http://127.0.0.1:5056/api/progress/${userId}`);
        const allGoalsData = await response.json();
        return allGoalsData;
      }
      
---

## How to Receive Data
The microservice responds with a **JSON object** containing:
- the `goalName`
- the calculated `progressPercentage` as a number between 0 and 100
Example code (javascript):
'''javascript
async function receiveAllProgressData() {
        try {
          const data = await requestAllProgressData();
          data.forEach(goal => {
            console.log("Goal:", goal.goal_name);
            console.log("Progress:", goal.progress + "%");
          });
        } catch (error) {
          console.error("Progress Microservice Error:", error.message);
        }
      }

<img width="600" alt="Untitled" src="https://github.com/user-attachments/assets/a7f67dc5-190c-4820-849c-5882d27bb42b" />

Notes & Best Practices
- This microservice calculates progress based only on the provided query parameters.
- For best results, ensure your main dashboard handles the JSON response and renders the progress bar accordingly

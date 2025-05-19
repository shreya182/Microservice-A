Savings Progress Microservice (Microservice A)
This microservice calculates the user's progress toward a savings goal and returns the result in a JSON format. It is designed to be used by the main dashboard to create a progress bar.
----
Communication Contract
This microservice is accessed via an HTTP GET request. It does **not** rely on shared files or direct function calls.
#### How to run the microservice:
1. Enter "python app.py" in your terminal. Confirm that it says Running on http://127.0.0.1:5056
2. Run your main program in a seperate terminal
3. Receive a JSON response containing savings goal data
   
#### How to request data:
Send a **GET request** to the following endpoint:
  /api/progress?goalName=<goalName>&currentAmount=<currentAmount>&goalAmount=<goalAmount>
Example request: 
  /api/progress?goalName=Vacation&currentAmount=500&goalAmount=1000

**Query Parameters:**
- `goalName` (string): the name of the savings goal
- `currentAmount` (number): how much has already been saved
- `goalAmount` (number): the total savings goal

---

### How to Receive Data

The microservice responds with a **JSON object** containing:
- the `goalName`
- the calculated `progressPercentage` as a number between 0 and 100

#### Example Response
```json
{
  "goalName": "Vacation",
  "progressPercentage": 50
}

UML Diagram
<img width="1218" alt="Untitled" src="https://github.com/user-attachments/assets/a7f67dc5-190c-4820-849c-5882d27bb42b" />


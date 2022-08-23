# 2022-COHERE-HACKATHON-TEAM-TURING
## Instructions
### Prerequisites
 - Python 3.10
 - Pipenv
### Installation
1. install prerequisites
2. Navigate to project folder in your terminal and execute `pipenv install`

### Running
 1. No dotenv has been setup for this project so please add your Co:here API key to `./ChatApp/main.py` (line 25)
 2. `pipenv shell` -> to enter configured python environment 
 3. `uvicorn ChatApp.main:app --reload` -> to run the application
 4. navigate to `127.0.0.1:8000/customer-chat` for the customer view and `127.0.0.1:8000/customer-support` for the customer support view
 5. Have fun :)
 
## Example prompts as customer
 - Hey can you help me with my cold frame I purchased from you guys?
 - What is the height at the back in cm for the Standard Cold Frame?
 - What is the height at the back in cm for the Standard Cold Frame with Toughened Glass?
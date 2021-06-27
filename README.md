# Cost_Api
A flask-driven restful API for Cost_Computation.
The API will take as input items ordered, delivery distance, and offer applied. 
The response is the total order value

## Input Format:

```json
{
  "order_items": [
    {
      "name": "bread",
      "quantity": 2,
      "price": 2200
    },
    {
      "name": "butter",
      "quantity": 1,
      "price": 5900
    }
  ],
  "distance": 1200,
  "offer": {
    "offer_type": "FLAT",
    "offer_val": 1000
  }
}
```
## Output Format:

```json
{
    "order_total":14300
}
```

## Technologies used
* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Flask](flask.pocoo.org/)** - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* Minor dependencies can be found in the requirements.txt file on the root folder.

## Concepts used
* Object Oriented Programming design to implement each request data as Order instance.
* Test Driven methodology for validation module.

## Assumptions and Technical Decisions:
    * Range Values:
        * Permissible length for name of an order item : 4-20 (both inclusive).
        * Permissible values for quantity for an order item : 1-20 (both inclusive).
        * Permissible values for price for an order item : 1-10000 (both inclusive).

    * Data Structure:
        * Data Structure used for Delivery_Cost values: Hash-map implementation using dictionary.


## Installation / Usage
* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python3 [here](https://www.python.org).

* Git clone this repo to your PC
    ```
        git clone git@github.com:gitgik/flask-rest-api.git
    ```


* #### Environment
    1. Cd into your the cloned repo as such:
        ```
        > cd COST_API
        ```

    2. Create and fire up your virtual environment:
        ```
        > virtualenv env  
        > env\Scripts\activate
        ```

* #### Install your requirements
    ```
    (env)> pip install -r requirements.txt
    ```


* #### Running It
    On your terminal, run the server using this one simple command:
    ```
    > python app.py
    ```
    You can now test the app using Postman
   ```
    http://localhost:5000/api/v1.0/OrderValue
    ```
    

## Outputs:

*   ![Case 1]
    (https://github.com/raghav1010/Cost_Api/blob/main/case_1.png  "Case 1")
    
*   ![Case 2]
    (https://github.com/raghav1010/Cost_Api/blob/main/case_2.png "Case 2")

*   ![Case 3]
    (https://github.com/raghav1010/Cost_Api/blob/main/Output3.png "Case 3")
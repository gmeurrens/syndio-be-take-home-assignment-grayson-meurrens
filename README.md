# Syndio Backend App

## Instructions
Start server with `PORT={PORT} python3 src/app.py` or specify the PORT number as an env variable in a `.env` file

REST endpoint `localhost:$PORT/pvalue`

Can test with curl by running `curl "http://localhost:$PORT/pvalue"`

Can specify an optional query parameter `department` by appending `?department={department}` to filter employees by a specific department. If no value is specified, then all employees are considered.

If there are no employees that much the `department` value, then 0 is returned.

## Notes
- Utlized the statsmodels.api library to perform the OLS regression modeling

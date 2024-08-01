/submit/expense/
  POST, returns a json
  input: date (optional), text, amount, token
  output: status:ok

/submit/income/
  POST, returns a json
  input: date (optional), text, amount, token
  output: result:ok

/accounts/login/
  POST, returns a json
  input: username, password
  output: status:ok & token
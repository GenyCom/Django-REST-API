REST API en utilisant le framework django rest framework

objectif : 
récuperer la liste des books/

Exec powershell : 
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/books/" -Headers @{Authorization="Api-Key your_key"}

Exec shell
curl -H "Authorization: Api-Key your_api_key_here" http://localhost:8000/api/books/ 

# command to sign up
curl -X POST http://127.0.0.1:8000/api/auth/signup/ \
     -H "Content-Type: application/json" \
     -d '{"username":"admin1","password":"pass123","email":"admin1@example.com"}'

# command to  signin
curl -X POST http://127.0.0.1:8000/api/auth/signin/ \
     -H "Content-Type: application/json" \
     -d '{"username":"admin1","password":"pass123"}'

# command to create Employee (requires JWT token)
curl -X POST http://127.0.0.1:8000/api/employees/ \
     -H "Authorization: Bearer ":\
     -H "Content-Type: application/json" \
     -d '{
         "full_name": "Ndegwadavid",
         "email": "ndegwadavid@example.com",
         "phone_number": "0797342380",
         "position": "Developer",
         "department": "IT"
     }'
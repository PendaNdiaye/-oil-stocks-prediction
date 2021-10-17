curl http://localhost:5000/score \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"pages": [1, 7]}'
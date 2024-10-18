from urllib.parse import urlencode

# Your dictionary
data = {
    "key": "key_val",
    "q": "q_val",
    "dt": "dt_val"
}

# Create the query string
# query_string = urlencode(data)
query_string = "&".join([f"{k}={v}" for k, v in data.items()])

print(query_string)

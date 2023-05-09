import httpx

response = httpx.delete("https://httpbin.org/delete") # POST request

print(response.status_code)
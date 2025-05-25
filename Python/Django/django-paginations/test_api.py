import time

import requests

endpoint = "http://127.0.0.1:8000/articles/"

parameters: list[dict[str, str | int]] = [
    {"page": 1},
    {"limit": 10},
    {
        "cursor": "",
        "ordering": "created_at",
    },
]

res: list[list[float]] = [list() for _ in range(3)]

for _ in range(10):
    for idx, param in enumerate(parameters):
        _endpoint = (
            endpoint
            + "?"
            + "&".join([f"{key}={value}" for key, value in param.items()])
        )
        response = requests.get(_endpoint).json()

        st = time.time()

        for _ in range(1000):
            response = requests.get(response["next"]).json()

        end = time.time()

        print(f"Time taken for {param}: {end - st:.2f} seconds")
        res[idx].append(end - st)

        time.sleep(1)

print(res)

print("Average time taken for each parameter:")
for idx, param in enumerate(parameters):
    print(f"{param}: {sum(res[idx]) / len(res[idx]):.2f} seconds")

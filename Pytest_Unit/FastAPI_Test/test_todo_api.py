# https://todo.pixegami.io/docs#/
import requests

ENDPOINT = "https://todo.pixegami.io"

response = requests.get(ENDPOINT)
data = response.json()
print(data)

status_code = response.status_code
print(status_code)


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    pass

def test_can_create_task():
    """ 
    run cmd for to see test case + return data in console:
    python -m pytest -v -s
    """
    payload = {
        "content" : "my testing 1",
        "user_id" : "test_user",
        "is_done" : False
    }
    response = requests.put(ENDPOINT + '/create-task', json=payload)
    assert response.status_code == 200

    data = response.json()
    # print(data)

    # get data from created task
    task_id = data["task"]["task_id"]
    response_get_detail = requests.get(ENDPOINT + f'/get-task/{task_id}')
    detail_data = response_get_detail.json()
    assert detail_data['content'] == payload['content']
    assert detail_data['user_id'] == payload['user_id']
    print()
    print(detail_data)
    update_item_helper(task_id=task_id, user_id=detail_data['user_id'])

def update_item_helper(task_id, user_id):
    payload = {
        "user_id": user_id,
        "task_id": task_id,
        "content": "my testing 2",
        "is_done": True,
    }
    response = requests.put(ENDPOINT + f'/update-task', json=payload)
    data = response.json()
    print("Update response:", data)
    assert response.status_code == 200

    # Ab updated detail fetch karo
    response_get_detail = requests.get(ENDPOINT + f'/get-task/{task_id}')
    detail_data = response_get_detail.json()
    assert detail_data["content"] == "my testing 2"
    assert detail_data["is_done"] is True
    print()
    print(detail_data)
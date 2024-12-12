@app.route('/guest_token/', methods=['GET'])
get_guest_token():

    @login_required # (optional)

    # --- Get access_token --- #
    auth_url = "https://api.app.preset.io/v1/auth/"

    payload = json.dumps({
        "name": token_name, # passed as variable for security purposes
        "secret": token_secret # passed as variable for security purposes
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", auth_url, headers=headers, data=payload)

    data = response.json()
    access_token = data['payload']['access_token']
    
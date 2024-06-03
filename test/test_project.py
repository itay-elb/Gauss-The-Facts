def test_home(client, db):
    response = client.get("/")
    assert b"<title>Guss The Facts</title>" in response.data

def test_add(client, db):
    response = client.get("/add")
    assert b"<title>Add Facts</title>" in response.data

def test_submit_only_one_fact_add(client, app, db):
    response = client.post("/submit_fact", data={"fact": "check"})
    with app.app_context():
        cursor = db.cursor()
        sql = "SELECT * FROM project.fansfacts WHERE fact = %s"
        params = ('check',)
        cursor.execute(sql, params)
        result = cursor.fetchall()
        cursor.close()

        assert result == []

def test_submit_only_two_fact_add(client, app, db):
    response = client.post("/submit_fact", data={"fact": "check", "question": "if?"})
    with app.app_context():
        cursor = db.cursor()
        sql = "SELECT * FROM project.fansfacts WHERE fact = %s"
        params = ('check',)
        cursor.execute(sql, params)
        result = cursor.fetchall()
        cursor.close()

        assert result == []

def test_submit_only_three_fact_add(client, app, db):
    response = client.post("/submit_fact", data={"fact": "check", "question": "if?", "true_option": "yes"})
    with app.app_context():
        cursor = db.cursor()
        sql = "SELECT * FROM project.fansfacts WHERE fact = %s"
        params = ('check',)
        cursor.execute(sql, params)
        result = cursor.fetchall()
        cursor.close()

        assert result == []

def test_submit_only_four_fact_add(client, app, db):
    response = client.post("/submit_fact", data={
        "fact": "good",
        "question": "try?",
        "true_option": "yes",
        "false_option": "no"
    })
    assert response.status_code == 302  # Check for successful redirect

    with app.app_context():
        cursor = db.cursor()
        sql = "SELECT * FROM fansfacts WHERE fact = %s"
        params = ('good',)
        cursor.execute(sql, params)
        result = cursor.fetchall()
        cursor.close()

        assert len(result) > 0  # Ensure the row exists
        assert result[0][1] == 'good'  # Verify the 'fact' column value


def test_restart(client, app, db):
    response = client.post("/delete")
    assert response.status_code == 200  # Check for successful response

    with app.app_context():
        cursor = db.cursor()
        sql = "SELECT * FROM project.fansfacts WHERE fact = %s"
        params = ('good',)
        cursor.execute(sql, params)
        result = cursor.fetchall()
        cursor.close()

        assert result == []

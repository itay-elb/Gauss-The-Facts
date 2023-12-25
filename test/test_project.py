def test_home(client):
    response=client.get("/")
    assert b"<title>Guss The Facts</title>" in response.data

def test_add(client):
    response=client.get("/add")
    assert b"<title>Add Facts</title>" in response.data

def test_submit_only_one_fact_add(client,app):
    response = client.post("/submit_fact", data={"fact":"check"})
    with (app.app_context()):
        from project.src.app import mydb
        mycursor = mydb.cursor()
        sql="SELECT * FROM project.fansfacts where fact = 'check'"
        mycursor.execute(sql)
        if (mycursor.fetchall() == []):
            assert True
        else:
            assert False

def test_submit_only_two_fact_add(client,app):
    response = client.post("/submit_fact", data={"fact":"check","qutsion":"if?"})
    with (app.app_context()):
        from project.src.app import mydb
        mycursor = mydb.cursor()
        sql="SELECT * FROM project.fansfacts where fact = 'check'"
        mycursor.execute(sql)
        if (mycursor.fetchall() == []):
            assert True
        else:
            assert False

def test_submit_only_three_fact_add(client, app):
    response = client.post("/submit_fact",data={"fact": "check", "qutsion": "if?", "true_option": "yes"})
    with (app.app_context()):
        from project.src.app import mydb
        mycursor = mydb.cursor()
        sql = "SELECT * FROM project.fansfacts where fact = 'check'"
        mycursor.execute(sql)
        if (mycursor.fetchall() == []):
            assert True
        else:
            assert False

def test_submit_only_four_fact_add(client,app):
    response = client.post("/submit_fact", data={"fact":"good","qutsion":"try?","true_option":"yes","false_option":"no"})
    with (app.app_context()):
        from project.src.app import mydb
        mycursor = mydb.cursor()
        sql="SELECT * FROM project.fansfacts where fact = 'good'"
        mycursor.execute(sql)
        if(mycursor.fetchall() != []):
            assert True
        else:
            assert False

def test_restart(client,app):
    response=client.post("/delete")
    with (app.app_context()):
        from project.src.app import mydb
        mycursor = mydb.cursor()
        sql="delete from project.fansfacts where fact = 'good'"
        mycursor.execute(sql)
        assert True








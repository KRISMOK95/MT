from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/form")
async def form_get():
    content = """
        <html>
          <head>
            <title>Sum Calculator</title>
          </head>
          <body>
            <h1>Sum Calculator</h1>
            <form action="/sum" method="post">
              <label for="var1">Variable 1:</label>
              <input type="number" id="var1" name="var1"><br><br>
              <label for="var2">Variable 2:</label>
              <input type="number" id="var2" name="var2"><br><br>
              <input type="submit" value="Calculate Sum">
            </form>
          </body>
        </html>
    """
    return HTMLResponse(content=content)

@app.post("/sum")
async def sum_post(var1: int = Form(...), var2: int = Form(...)):
    total = var1 + var2
    return {"sum": total}
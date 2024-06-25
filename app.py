from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from public.Gale_Shapley import gale_shapley, women_dictionary, men_dictionary , women_list, man_list # Import the gale_shapley function from the public folder

from lp import *

app = FastAPI()
templates = Jinja2Templates(directory="public")
app.mount("/public", StaticFiles(directory="public"), name="public")

userInfo = None
@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    # Endpoint for the main page, e.g., the registration form
    return templates.TemplateResponse("RegisterForm.html", {"request": request})

@app.get('/matches', response_class=HTMLResponse)
async def matches(request: Request):
    # Endpoint for the cart page where the matches will be displayed
    if userInfo is None:
        return RedirectResponse(url='/')

    # Apply the matchmaking algorithm to get engagements
    engagements = gale_shapley(women_dictionary, men_dictionary, women_list, man_list)

    return templates.TemplateResponse("match.html", {"request": request, "userInfo": userInfo, "engagements": engagements})

@app.post('/api/info')
async def info(request: Request):
    # Endpoint to receive the user information from the registration form
    data = await request.json()
    global userInfo
    userInfo = data
    return RedirectResponse(url='/matches')

# Define other necessary endpoints here...


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('app:app', reload=True, port=5000)


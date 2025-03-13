import json
import requests
import os

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from controllers.agent import run_agent

router = APIRouter()


class InvokeRequest(BaseModel):
    message: str


class AuthRequest(BaseModel):
    status: bool
    clientId: str


@router.post("/save-auth")
def save_auth(request: AuthRequest):
    auth_file_path = os.path.join(
        os.path.dirname(__file__), "..", "resources", "auth.json"
    )
    with open(auth_file_path, "w") as f:
        json.dump({"auth": request.status, "clientId": request.clientId}, f)
    return {"message": "Auth status saved"}


class InvokeResponse:
    response: str


@router.post("/invoke")
def invoke_agent(message: dict):
    return run_agent(message)


@router.get("/authorize", response_class=HTMLResponse)
def authorize():
    return """
    <style>
        * {
            margin: 0;
        }

        html, body {
            min-height: 100vh;
        }

        body {
            background: #232323;
            color: #fff;
            font-family: Helvetica, Arial, sans-serif;
        }

        .text-success {
            color: #28a745;
        }

        .text-danger {
            color: #dc3545;
        }

        .modal__background {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .modal__window {
            box-sizing: border-box;
            padding: 29px;
            border: 1px solid #999;
            border-radius: 15px;
        }

        @media all and (min-width: 576px) {
            .modal__window {
                padding: 49px 79px 29px;
            }
        }

        .auth-form {
            display: flex;
            flex-direction: column;
            letter-spacing: 1px;
        }

        .auth-form__label {
            margin-bottom: 40px;
            position: relative;
        }

        .auth-form__input {
            position: relative;
            width: 240px;
            height: 40px;
            background: transparent;
            color: #ccc;
            box-sizing: border-box;
            font-size: 16px;
            outline: none;
            border-top: none;
            border-left: none;
            border-right: none;
            border-bottom: none;
            box-shadow: 0 1px 0 0 #666;
        }

        .auth-form__input.focus {
            box-shadow: 0 2px 0 0 #bbb;
        }

        .auth-form__submit {
            font-family: inherit;
            font-size: inherit;
            letter-spacing: inherit;
            cursor: pointer;
            border: 1px solid #ccc;
            height: 50px;
            border-radius: 10px;
            background: transparent;
            color: #ccc;
            outline: none;
        }

        .auth-form__submit:hover {
            background: #fff;
            border: 1px solid #fff;
            color: #232323;
        }
        
        .auth-form__bottom {
            margin-top: 30px;
            font-size: 12px;
            color: #ddd;
            text-align: center;
        }

        .auth-form__bottom a {
            color: #007bff;
        }

        .auth-form__bottom a:hover {
            color: #ddd;
        }
    </style>

    <script>
        async function authorize(e) {
            e.preventDefault();

            const input = document.querySelector('input');
            const clientId = input.value;

            if (!clientId) {
                return;
            }

            const message = clientId === 'aaa' ? 'USER_AUTHORIZED' : 'WRONG_AUTHORIZATION_CREDENTIALS';
            // Send message to parent window (Chainlit chat)
            if (window.opener) {
                window.opener.postMessage({
                    action: "handle_auth_result",
                    payload: {
                        status: message,
                        clientId: clientId
                    }
                }, "*");
                setTimeout(() => {
                    window.close();
                }, 500);
            }
        }
    </script>

    <div class="modal__background">
        <div class="modal__window">
            <form class="auth-form" name="form-auth" method="post" onsubmit="authorize(event)">
                <label class="auth-form__label">
                    <input class="auth-form__input input-password" name="client_id" placeholder="Client ID" required>
                </label>
                <input class="auth-form__submit" type="submit" value="Login">
            </form>
        </div>
    </div>
    """

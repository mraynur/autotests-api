from pydantic import BaseModel, Field, EmailStr, ConfigDict

class TokenSchema(BaseModel):
    """
    Описание структуры аутентификационных токенов.
    """
    model_config = ConfigDict(populate_by_name=True)

    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: EmailStr
    password: str

class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema

class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    model_config = ConfigDict(populate_by_name=True)

    refresh_token: str = Field(alias="refreshToken")

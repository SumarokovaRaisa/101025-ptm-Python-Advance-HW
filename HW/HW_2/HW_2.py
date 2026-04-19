from pydantic import BaseModel, EmailStr, ValidationError, Field, field_validator



class Address(BaseModel):
    city: str = Field(min_length=2)
    street: str = Field(min_length=3)
    house_number: int = Field(gt=0)

class User(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    address: Address
    is_employed: bool = Field(default=False)


    @field_validator("name")
    def validate_name(cls, value):
        if not all(part.isalpha() for part in value.split()):
            raise ValueError('Name must contain only letters')
        return value


def check_user_rules(user: User):
    if user.is_employed and not (18 <= user.age <= 65):
        raise ValueError("Employed users must be between 18 and 65 years old")

json_input = """{

    "name": "John Doe",

    "age": 30,

    "email": "john.doe@example.com",

    "is_employed": true,

    "address": {

        "city": "New York",

        "street": "5th Avenue",

        "house_number": 123

    }

}"""
json_invalid_1 = """{
     "name": "J",
    "age": 20,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""


json_invalid_2 = """{
     "name": "Jo",
    "age": 70,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""
def register_user(json_str: str):
    user = User.model_validate_json(json_str)
    check_user_rules(user)
    return user.model_dump_json()


try:
    result = register_user(json_input)
    print(result)
except ValidationError as e:
    print("ValidationError: ", e)

except ValueError as e:
    print(f"Business logic error:\n{e}")






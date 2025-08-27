from pydantic import BaseModel, Field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    weight: Annotated[float, Field(..., gt=0, lt=500, description='Weight of the user')]
    height: Annotated[float, Field(..., gt=0, lt=3, description='Height of the user in meters')]
    income_lpa: Annotated[float, Field(..., gt=0, description='Annual income of the user in LPA')]
    smoker: Annotated[bool, Field(..., description='Is the user smoker?')]
    city: Annotated[str, Field(..., description='The city from where the user belongs to')]
    occupation: Annotated[
        Literal['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'],
        Field(..., description='Occupation of the user')
    ]

    # ✅ BMI property
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)

    # ✅ Lifestyle risk
    @property
    def life_style(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

    # ✅ Age group
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    # ✅ City tier
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3
    
    # ✅ city normalize
    @field_validator('city')
    @classmethod
    def normalize_city(cls, v:str)->str:
        v = v.strip().title() 
        return v
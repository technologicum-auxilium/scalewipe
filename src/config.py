import os

class Config:
    AWS_REGION = os.environ.get('AWS_REGION', 'sa-east-1')

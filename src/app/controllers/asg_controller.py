import boto3
from fastapi import HTTPException
from src.config import Config
from src.app.models.asg_model import ASGTag

session = boto3.Session(region_name=Config.AWS_REGION)
client = session.client('autoscaling')

def update_asg(tag: ASGTag):
    response = client.describe_auto_scaling_groups()
    asg_names = []

    for asg in response['AutoScalingGroups']:
        asg_tags = {t['Key']: t['Value'] for t in asg['Tags']}
        if asg_tags.get(tag.Key) == tag.Value:
            asg_names.append(asg['AutoScalingGroupName'])

    if not asg_names:
        raise HTTPException(status_code=404, detail="No matching ASG found")

    for asg_name in asg_names:
        client.update_auto_scaling_group(
            AutoScalingGroupName=asg_name,
            MinSize=0,
            DesiredCapacity=0
        )

    return {'message': 'ASG(s) updated successfully'}

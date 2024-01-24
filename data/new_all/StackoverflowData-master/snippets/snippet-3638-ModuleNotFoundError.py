#Source: https://stackoverflow.com/questions/70895962/python-aws-boto3-returning-nonetype-error
#!/usr/bin/python3

import boto3
import botocore

boto3_session = create_boto3_session(profile_name='some_profile')
ec2_resource = boto3_session.resource("ec2", region_name='some_region')
ec2_instances = ec2_resource.instances.all()
for ec2_instance in ec2_instances:
    tags = getattr(ec2_instance, 'tags', [])
    for tag in tags:
        print(tag)
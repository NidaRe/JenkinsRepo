import boto3
import sys

region = sys.argv[1]
accesskey = sys.argv[2]
secretkey = sys.argv[3]

client = boto3.client('ec2',region_name=region, aws_access_key_id=accesskey,aws_secret_access_key=secretkey)

ins_data = client.describe_instances()
for step1 in ins_data['Reservations']:
	for step2 in step1['Instances']:
		print(step2['InstanceId'])


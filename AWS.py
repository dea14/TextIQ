from pprint import pprint
from boto import ec2

#use a cost-explorer API to calculate the total billing cost
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html
client = boto3.client('ce', name_of_region='region-name')

res = client.get_cost_and_usage(
    TimePeriod={
        'Start': '2020-01-01',
        'End': '2020-10-5'
    },
    Granularity='MONTHLY',
    Metrics=[
        'AmortizedCost',
    ]
)

print(res)


#store the access key and the secret key provided by AWS
#in variables
KEY_ID_AWS = 'XXXXXXXXXXXXXXXXXX'
SECRET_KEY_AWS = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

ec2conn = ec2.connection.EC2Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
all_instances = ec2conn.get_all_instances()
instances = [i for r in all_instances for i in r.instances]
for i in instances:
    pprint(i.__dict__)


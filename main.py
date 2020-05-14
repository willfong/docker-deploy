import boto3
import docker
import requests

'''
client = docker.DockerClient(base_url='unix://run/docker.sock')
containers = client.containers.list()
for container in containers:
    print(f"{container.id}\t{container.name}")

'''

def aws_region_id():
    response = requests.get(AWS_REGION_ID)
    return response.text[:-1]

def aws_instance_id():
    response = requests.get(AWS_INSTANCE_ID)
    return response.text

def aws_get_tags(id):
    filter = {'Name': 'resource-id', 'Values': [id]}
    response = aws_ec2_client.describe_tags(Filters=[filter])
    return response.get('Tags')

def aws_get_tag_value(tags, key):
    for tag in tags:
        if tag.get('Key') == key:
            return tag.get('Value')

def docker_containers():
    return docker_client.containers.list()

def main():
    instance_id = aws_instance_id()
    tags = aws_get_tags(instance_id)
    repository = aws_get_tag_value(tags, 'Repository')
    print(repository)
    containers = docker_containers()

# https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html

AWS_INSTANCE_ID="http://169.254.169.254/latest/meta-data/instance-id"
AWS_REGION_ID="http://169.254.169.254/latest/meta-data/placement/availability-zone"

aws_ec2_client = boto3.client('ec2', region_name=aws_region_id())
docker_client = docker.DockerClient(base_url='unix://run/docker.sock')

if __name__ == "__main__":
    main()

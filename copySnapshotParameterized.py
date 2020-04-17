import boto3
import sys

SOURCE_REGION = sys.argv[1]
DESTINATION_REGION = sys.argv[2]

# Connect to EC2 in Source region
source_client = boto3.client('ec2', region_name=SOURCE_REGION)

# Get a list of all snapshots, then sort them
snapshots = source_client.describe_snapshots(OwnerIds=['self'])
snapshots_sorted = sorted([(s['SnapshotId'], s['StartTime']) for s in snapshots['Snapshots']], key=lambda k: k[1])
latest_snapshot = snapshots_sorted[-1][0]

print ('Latest Snapshot ID is ' + latest_snapshot)

# Connect to EC2 in Destination region
destination_client = boto3.client('ec2', region_name=DESTINATION_REGION)

# Copy the snapshot
response = destination_client.copy_snapshot(
    SourceSnapshotId=latest_snapshot,
    SourceRegion=SOURCE_REGION,
    Description='This is my copied snapshot'
    )

print ('Copied Snapshot ID is ' + response['SnapshotId'])
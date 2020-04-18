import boto3
conn = boto3.client('ec2', region_name='us-east-2')
conn.copy_snapshot(Description='Snapshot copied from' , SourceSnapshotId='snap-07dbe42318924c5ad',DestinationRegion='us-east-1',SourceRegion='us-east-2')
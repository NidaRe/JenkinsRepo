import boto3
import sys

currentregion = sys.arv[1]
sourceregion = sys.argv[2]
destinationregion = sys.argv[3]
snapshotID = sys.argv[4]

conn = boto3.client('ec2', region_name=currentregion)
conn.copy_snapshot(Description='Snapshot copied from' , SourceSnapshotId=snapshotID,DestinationRegion=destinationregion,SourceRegion=sourceregion)
import boto3
import urllib.parse


def get_matching_s3_objects(bucket, prefix="", suffix=""):

    s3 = boto3.client("s3")
    paginator = s3.get_paginator("list_objects_v2")

    kwargs = {'Bucket': bucket}

    if isinstance(prefix, str):
        prefixes = (prefix, )
    else:
        prefixes = prefix

    for key_prefix in prefixes:
        kwargs["Prefix"] = key_prefix

        for page in paginator.paginate(**kwargs):
            try:
                contents = page["Contents"]
            except KeyError:
                return

            for obj in contents:
                key = obj["Key"]
                if key.endswith(suffix):
                    yield obj


def get_matching_s3_keys(bucket, prefix="", suffix=""):

    for obj in get_matching_s3_objects(bucket, prefix, suffix):
        key = obj["Key"]
        key_ae = urllib.parse.quote_plus(key, safe="/")
        print("https://"+bucket_n"."+region".amazonaws.com/"+key_ae)

region = input("Region :   ")
bucket_n = input("Bucket name :  ")
folder = input("Folder name   :  ")
get_matching_s3_keys(bucket_n, folder)


import boto3
import urllib.parse
import argparse

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


def get_matching_s3_keys(bucket, region, prefix="", suffix=""):

    url_root = f'https://{bucket}.{region}.amazonaws.com/'

    for obj in get_matching_s3_objects(bucket, prefix, suffix):
        key = obj["Key"]
        key_ae = urllib.parse.quote_plus(key, safe="/")
        print(url_root + key_ae)
        

def main():
    # Modify the defaults if you use the same region and bucket frequently
    parser = argparse.ArgumentParser(description='Process some command line arguments.')
    parser.add_argument('--region', type=str, required=False, default='YOUR-REGION', help='S3 region')
    parser.add_argument('--bucket', type=str, required=False, default='YOUR-BUCKET', help='S3 bucket')
    parser.add_argument('--folder', type=str, required=False, default='', help='Optional folder path within the bucket to enumerate')

    args = parser.parse_args()

    get_matching_s3_keys(args.bucket, args.region, args.folder)

if __name__ == "__main__":
    main()

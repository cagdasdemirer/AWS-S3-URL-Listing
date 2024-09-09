## AWS-S3-URL-Listing

A script that lists the URLs of all objects in a specific folder of a specific S3 bucket.

## Preparing
```python
pip install awscli
pip install boto3
```

#### AWS Configuration

See [Configuring the AWS CLI](https://docs.aws.amazon.com/en_us/cli/latest/userguide/cli-chap-configure.html).

Simplified steps:
 1. Make the IAM user part of a group that has the Administrator Access, Amazon S3 Full Access, and PowerUserAccess policies attached.
 2. Retrieve the AWS Access Key ID and the AWS Secrets Access Key for the IAM user.
 3. On the command line, run `aws configrure` enter the AWS Access Key ID and the AWS Secrets Access Key when prompted, along with your default region, if desired.

## Usage

```
python app.py --region YOUR-REGION --bucket YOUR-BUCKET --folder YOUR-FOLDER
```

If you're frequently working with a specific region and bucket, modify `app.py` with those defaults so you don't need to include them on the command line.

The `folder` value defaults to '', which then lists all objects within the bucket. A folder name can include sub-folders separated by /. If you have spaces in any folder name, put quotes around the entire folder value, such as:

```
python app.py --region YOUR-REGION --bucket YOUR-BUCKET --folder "images/marketing 2024"
```

## Note
This script was written for Virtual-hosted style URL. You can customize it according to the URL style you use by changing the `url_root` string on line 34.

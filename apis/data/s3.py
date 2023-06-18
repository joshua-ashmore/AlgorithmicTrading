"""API and data for S3 connection."""

import io

import boto3
import pandas as pd


class S3Client:
    """S3 client object with respective functions."""

    def __init__(
        self,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        region_name: str = "eu-west-2",
    ):
        """Init function."""
        self.client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
        )

    def save_params_to_s3(self, data, key: str, bucket: str):
        """Save params to s3 bucket."""
        if len(data) > 0:
            dataframe = pd.DataFrame(data)
            with io.StringIO() as csv_buffer:
                dataframe.to_csv(csv_buffer, index=False)

                response = self.client.put_object(
                    Bucket=bucket,
                    Key=key,
                    Body=csv_buffer.getvalue(),
                )

            status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

            if status != 200:
                raise BaseException("Could not return data from S3.")

    def read_from_s3(self, key: str, bucket: str):
        """Read from s3 bucket."""
        content_object = self.client.get_object(
            Bucket=bucket,
            Key=key,
        )
        file_content = content_object["Body"].read().decode("utf-8")
        dataframe = pd.read_csv(io.StringIO(file_content))
        return dataframe.to_dict("records")

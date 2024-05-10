from pyspark.sql import SparkSession



if __name__ == "__main__":
    spark = (SparkSession.builder.appName('Unstructured_Data_Realtime_Streaming')
            .config('spark.jars.packages',
                     'org.apache.adoop:hadoop-aws:3.3.1',
                     'org.amazon:aws-java-sdk-bundle:1.11.469')
            .config('spark.hadoop.fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')
            .config('spark.hadoop.fs.s3a.access.key', 'configuration.get("AWS_ACCESS_KEY")')
            .config('spark.hadoop.fs.s3a.secret.key', 'configuration.get("AWS_SECRET_KEY")')
            .config('spark.hadoop.fs.s3a.aws.credentials.provider', 
                    'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')
            .getOrCreate())
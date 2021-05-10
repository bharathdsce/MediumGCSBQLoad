from google.cloud import bigquery

def main(event, context):
    project_id = <your project name>
    bq_dataset = <BQ Dataset ID>
    bq_table = <BQ Table Name>
    file_name = event["name"]
    bucket_name = event["bucket"]
    gcs_uri = "gs://{bucket_name}/{file_name}".format(bucket_name, file_name)
    table_id = "{project_id}.{bq_dataset}.{bq_table}".format(project_id, bq_dataset, bq_table)

    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(
        schema=[bigquery.SchemaField("first_name", "STRING"),
                bigquery.SchemaField("last_name", "STRING"),
                bigquery.SchemaField("age", "INT64")],
        skip_leading_rows=1, source_format=bigquery.SourceFormat.CSV)

    load_job = client.load_table_from_uri(
        gcs_uri, table_id, job_config=job_config
    )

    load_job.result()

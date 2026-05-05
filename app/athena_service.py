import boto3
import time

athena = boto3.client('athena', region_name='us-east-1')

DATABASE = "shopcloud_db"
OUTPUT = "s3://shopcloud-bucket/athena-results/"

def run_query(sql: str):
    try:
        response = athena.start_query_execution(
            QueryString=sql,
            QueryExecutionContext={
                'Database': DATABASE
            },
            ResultConfiguration={
                'OutputLocation': OUTPUT
            }
        )

        query_id = response['QueryExecutionId']

        status = "RUNNING"
        timeout = 30
        elapsed = 0

        while status in ["RUNNING", "QUEUED"]:
            time.sleep(1)
            elapsed += 1

            result = athena.get_query_execution(QueryExecutionId=query_id)
            status = result['QueryExecution']['Status']['State']

            if elapsed >= timeout:
                return {
                    "status": "timeout",
                    "query_id": query_id
                }

        if status != "SUCCEEDED":
            return {
                "status": "error",
                "state": status,
                "query_id": query_id
            }

        results = athena.get_query_results(QueryExecutionId=query_id)

        rows = []

        for row in results['ResultSet']['Rows'][1:]:  
            rows.append([col.get('VarCharValue', '') for col in row['Data']])

        return {
            "status": "success",
            "query_id": query_id,
            "data": rows
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


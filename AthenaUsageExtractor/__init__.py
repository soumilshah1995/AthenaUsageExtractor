try:
    import boto3
    import uuid
    import json
    import re
    import os
    import io
    import pandas as pd
    import dateparser

except Exception as e:
    print("Error :{} ".format(e))

def flatten_dict(data, parent_key="", sep="_"):
    """Flatten data into a single dict"""
    try:
        items = []
        for key, value in data.items():
            new_key = parent_key + sep + key if parent_key else key
            if type(value) == dict:
                items.extend(flatten_dict(value, new_key, sep=sep).items())
            else:
                items.append((new_key, value))
        return dict(items)
    except Exception as e:
        return {}

def create_workgroup_history(day, workgroup):
    print("**", day)
    file_name = "workgroup_{}_{}_queries.json".format(workgroup, day)
    records = ""
    athena = boto3.client(
        "athena",
        aws_access_key_id=os.getenv("DEV_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("DEV_SECRET_KEY"),
        region_name=os.getenv("DEV_REGION"),
    )
    paginator = athena.get_paginator("list_query_executions").paginate(
        WorkGroup=workgroup
    )
    for page in paginator:
        query_executions = athena.batch_get_query_execution(
            QueryExecutionIds=page["QueryExecutionIds"]
        )
        for query in query_executions["QueryExecutions"]:
            if "CompletionDateTime" not in query["Status"]:
                continue
            query_day = query["Status"]["CompletionDateTime"].strftime("%Y-%m-%d")

            if day == query_day:
                json_payload = {}
                json_payload["QueryExecutionId"] = query.get("QueryExecutionId")
                json_payload["Query"] = query.get("Query")
                json_payload["StatementType"] = query.get("StatementType")
                json_payload["WorkGroup"] = query.get("WorkGroup")
                for key, value in flatten_dict(
                        query.get("ResultConfiguration")
                ).items():
                    json_payload[key] = value.__str__()
                for key, value in flatten_dict(
                        query.get("QueryExecutionContext")
                ).items():
                    json_payload[key] = value.__str__()
                for key, value in flatten_dict(query.get("EngineVersion")).items():
                    json_payload[key] = value.__str__()
                for key, value in flatten_dict(query.get("Statistics")).items():
                    json_payload[key] = value.__str__()
                for key, value in flatten_dict(query.get("Status")).items():
                    json_payload[key] = value.__str__()
                for key, value in flatten_dict(query.get("Statistics")).items():
                    json_payload[key] = value.__str__()
                records = records + json.dumps(json_payload) + "\n"
            elif query_day < day:
                return records
    return records


class AthenaUsageExtractor(object):
    def __init__(self, aws_access_key, aws_secret_key, aws_region):
        self.aws_access_key  = aws_access_key
        self.aws_secret_key  =aws_secret_key
        self.aws_region = aws_region

        self.athena_client = boto3.client(
            "athena",
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_key,
            region_name=self.aws_region

        )

    def _get_data(self, date, workgroup):

        """
        private method to return data
        :param day: 'YYYY-MM-DD'
        :return: Array
        """
        day = date
        paginator = self.athena_client.get_paginator("list_query_executions").paginate(WorkGroup=workgroup)
        for page in paginator:
            query_executions = self.athena_client.batch_get_query_execution(
                QueryExecutionIds=page["QueryExecutionIds"]
            )
            for query in query_executions["QueryExecutions"]:
                if "CompletionDateTime" not in query["Status"]:
                    continue
                query_day = query["Status"]["CompletionDateTime"].strftime("%Y-%m-%d")

                if day == query_day:
                    json_payload = {}
                    json_payload["QueryExecutionId"] = query.get("QueryExecutionId")
                    json_payload["Query"] = query.get("Query")
                    json_payload["StatementType"] = query.get("StatementType")
                    json_payload["WorkGroup"] = query.get("WorkGroup")
                    for key, value in flatten_dict(
                            query.get("ResultConfiguration")
                    ).items():
                        json_payload[key] = value.__str__()
                    for key, value in flatten_dict(
                            query.get("QueryExecutionContext")
                    ).items():
                        json_payload[key] = value.__str__()
                    for key, value in flatten_dict(query.get("EngineVersion")).items():
                        json_payload[key] = value.__str__()
                    for key, value in flatten_dict(query.get("Statistics")).items():
                        json_payload[key] = value.__str__()
                    for key, value in flatten_dict(query.get("Status")).items():
                        json_payload[key] = value.__str__()
                    for key, value in flatten_dict(query.get("Statistics")).items():
                        json_payload[key] = value.__str__()
                        yield json_payload

                elif query_day < day:
                    return None
        return None

    def get_usage_for_date(self, date , workgroup):
        """

        :param date: STR '(YYYY-MM-DD)'
        :param workgroup:  'primary'
        :return: Generator Object
        """
        date = dateparser.parse(date).strftime("%Y-%m-%d").__str__()
        response = self._get_data(workgroup=workgroup, date=date)
        return response


# def main():
#     helper = AthenaUsageExtractor(
#         aws_region='us-east-1',
#         aws_access_key='XXXX',
#         aws_secret_key='XXXXX'
#     )
#     response = helper.get_usage_for_date(date='2022-08-12', workgroup='primary')
#     while True:
#         try:
#             data = next(response)
#             print(data)
#         except StopIteration as e:
#             break
#         except Exception as e:
#             break
#
# main()

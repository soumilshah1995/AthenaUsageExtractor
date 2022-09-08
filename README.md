# Athena Usage Extractor 

[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)]

* Athena helps you analyze unstructured, semi-structured, and structured data stored in Amazon S3. Examples include CSV, JSON, or columnar data formats such as Apache Parquet and Apache ORC. You can use Athena to run ad-hoc queries using ANSI SQL, without the need to aggregate or load the data into Athena.
        
* Athena usage is simple python library that allows you to extract all usage information 


## Installation

[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)]


# AthenaUsageExtractor

* Athena helps you analyze unstructured, semi-structured, and structured data stored in Amazon S3. Examples include CSV, JSON, or columnar data formats such as Apache Parquet and Apache ORC. You can use Athena to run ad-hoc queries using ANSI SQL, without the need to aggregate or load the data into Athena.
    
* Athena usage is simple python library that allows you to extract all usage information 
    

## Installation
ac
```bash
pip install athena-usage-metrics-extractor
```
## Usage

```python
import sys
from AthenaUsageExtractor import AthenaUsageExtractor


def main():
    helper = AthenaUsageExtractor(
        aws_region='us-east-1',
        aws_access_key='XXXXX',
        aws_secret_key='XXXXX'
    )
    response = helper.get_usage_for_date(date='2022-08-12', workgroup='primary')
    while True:
        try:
            data = next(response)
            print(data)
        except StopIteration as e:
            break
        except Exception as e:
            break

main()

```
## Json format Returned 
```json
{
   "QueryExecutionId":"490024e6-3e89-4ec4-9ffd-b1302a77d33d",
   "Query":"<YOU WILL GET THE QUERY USER RAN >",
   "StatementType":"DML",
   "WorkGroup":"primary",
   "OutputLocation":"<AWS S3 Output Path >",
   "Database":"default",
   "SelectedEngineVersion":"AUTO",
   "EffectiveEngineVersion":"Athena engine version 2",
   "EngineExecutionTimeInMillis":"14045",
   "DataScannedInBytes":"59597591861",
   "TotalExecutionTimeInMillis":"14292",
   "QueryQueueTimeInMillis":"214",
   "QueryPlanningTimeInMillis":"960",
   "ServiceProcessingTimeInMillis":"33",
   "State":"SUCCEEDED",
   "SubmissionDateTime":"2022-08-12 13:56:07.837000-04:00",
   "CompletionDateTime":"2022-08-12 13:56:22.129000-04:00"
}
```

## Authors

* **Soumil Nitin Shah** 


## Soumil Nitin Shah 
Bachelor in Electronic Engineering |
Masters in Electrical Engineering | 
Master in Computer Engineering |

* Website : https://soumilshah.herokuapp.com
* Github: https://github.com/soumilshah1995
* Linkedin: https://www.linkedin.com/in/shah-soumil/
* Blog: https://soumilshah1995.blogspot.com/
* Youtube : https://www.youtube.com/channel/UC_eOodxvwS_H7x2uLQa-svw?view_as=subscriber
* Facebook Page : https://www.facebook.com/soumilshah1995/
* Email : shahsoumil519@gmail.com
* projects : https://soumilshah.herokuapp.com/project


I earned a Bachelor of Science in Electronic Engineering and a double master’s in Electrical and Computer Engineering. I have extensive expertise in developing scalable and high-performance software applications in Python. I have a YouTube channel where I teach people about Data Science, Machine learning, Elastic search, and AWS. I work as data collection and processing Team Lead at Jobtarget where I spent most of my time developing Ingestion Framework and creating microservices and scalable architecture on AWS. I have worked with a massive amount of data which includes creating data lakes (1.2T) optimizing data lakes query by creating a partition and using the right file format and compression. I have also developed and worked on a streaming application for ingesting real-time streams data via kinesis and firehose to elastic search

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


import boto3
import json

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Parse the request body from string to JSON
    requestBody = json.loads(event['body'])

    # Now you can access properties of the request body like this:
    operation = requestBody['operation']

    try:
        if operation == 'add_course':
            return add_course(requestBody, context)
        elif operation == 'query_course':
            return query_course(requestBody, context)
        elif operation == 'query_profile':
            return query_profile(requestBody, context)
        elif operation == 'add_student_course':
            return add_student_course(requestBody, context)
        elif operation == 'delete_student_course':
            return delete_student_course(requestBody, context)
        elif operation == 'add_profile':
            return add_profile(requestBody, context)
        elif operation == 'delete_course':
            return delete_course(requestBody, context)
        elif operation == 'delete_profile':
            return delete_profile(requestBody, context)
        else:
            return {
                'statusCode': 400,
                'body': 'Invalid operation',
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
                }
            }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'status code': 500,
            'body': 'Internal Server Error',
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            }
        }

def add_course(requestBody, context):
    try:
        client.put_item(
            TableName="Courses",
            Item={
                'name': {'S': requestBody["name"]},
                'description': {'S': requestBody["description"]},
                'secdatetime': {'SS': requestBody["secdatetime"]},
                'students': {'NS': requestBody["students"]},
                'teachers': {'NS': requestBody["teachers"]},
            }
        )
        response = {
            'statusCode': 200,
            'body': 'Successfully created course!',
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            },
        }
        return response
    except Exception as e:
        print(f"Error: {e}")
        return {
            'status code': 500,
            'body': 'Internal Server Error',
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            }
        }

def query_course(requestBody, context):
    try:
        data = client.query(
            TableName='Courses',
            KeyConditionExpression='#name = :value',
            ExpressionAttributeValues={':value': {'S': requestBody["name"]}},
            ExpressionAttributeNames={'#name': 'name'}
        )
        response = {
            'statusCode': 200,
            'body': json.dumps(data),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            },
        }
        return response
    except Exception as e:
        print(f"Error: {e}")
        return {
            'status code': 500,
            'body': 'Internal Server Error',
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            }
        }


def query_profile(requestBody, context):
    try:
        data = client.query(
            TableName='Profiles',
            KeyConditionExpression='#peoplesoftID = :value',
            ExpressionAttributeValues={':value': {'N': requestBody["peoplesoftID"]}},
            ExpressionAttributeNames={'#peoplesoftID': 'peoplesoftID'}
        )
        response = {
            'statusCode': 200,
            'body': json.dumps(data),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            },
        }
        return response
    except Exception as e:
        print(f"Error: {e}")
        return {
            'status code': 500,
            'body': 'Internal Server Error',
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            }
        }

def add_student_course(requestBody, context):
    try:
        response = client.update_item(
            TableName='Profiles',
            Key={'peoplesoftID': {'N': requestBody["peoplesoftID"]}},
            AttributeUpdates={
                'courses': {
                    'Action': 'ADD',
                    'Value': {'SS': [requestBody["name"]]}
                }
            }
        )
        courseName = requestBody["name"][:requestBody["name"].find(".")]
        response = client.update_item(
            TableName='Courses',
            Key={'name': {'S': courseName}},
            AttributeUpdates={
                'students': {
                    'Action': 'ADD',
                    'Value': {'NS': [requestBody["peoplesoftID"]]}
                }
            }
        )
        
        response = {
            'statusCode': 200,
            'body': 'successfully added student to course!',
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            },
        }
        return response
    except Exception as e:
        print(f"Error: {e}")
        return {
            'status code': 500,
            'body': 'Internal Server Error',
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            }
        }

def delete_student_course(requestBody, context):
    try:
        response = client.update_item(
            TableName='Profiles',
            Key={'peoplesoftID': {'N': requestBody["peoplesoftID"]}},
            AttributeUpdates={
                'courses': {
                    'Action': 'DELETE',
                    'Value': {'SS': [requestBody["name"]]}
                }
            }
        )
        courseName = requestBody["name"][:requestBody["name"].find(".")]
        response = client.update_item(
            TableName='Courses',
            Key={'name': {'S': courseName}},
            AttributeUpdates={
                'students': {
                    'Action': 'DELETE',
                    'Value': {'NS': [requestBody["peoplesoftID"]]}
                }
            }
        )
        
        response = {
            'statusCode': 200,
            'body': 'successfully deleted student from course!',
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            },
        }
        return response
    except Exception as e:
        print(f"Error: {e}")
        return {
            'status code': 500,
            'body': 'Internal Server Error',
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            }
        }
def add_profile(requestBody, context):
    try:
        data = client.put_item(
            TableName="Profiles",
            Item={
                'peoplesoftID': {'N': requestBody["peoplesoftID"]},
                'username': {'S': requestBody["username"]},
                'courses': {'SS': requestBody["courses"]},
                'email': {'S': requestBody["email"]},
                'NetID': {'S': requestBody["NetID"]},
                'password': {'S': requestBody["password"]},
                'permissions': {'N': requestBody["permissions"]},
            }
        )
        response = {
            'statusCode': 200,
            'body': json.dumps({'message': 'Successfully created profile!'}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            },
        }
        return response
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            },
        }

def delete_course(requestBody, context):
    try:
        response = client.delete_item(
            TableName='Courses',
            Key={'name': {'S': requestBody["name"]}}
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Course deleted successfully'),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            }
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Internal Server Error'),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            }
        }
        
def delete_profile(requestBody, context):
    try:
        response = client.delete_item(
            TableName='Profiles',
            Key={'peoplesoftID': {'N': requestBody["peoplesoftID"]}}
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Profile deleted successfully'),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            }
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Internal Server Error'),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            }
        }

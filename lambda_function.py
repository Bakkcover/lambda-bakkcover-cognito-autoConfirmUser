import boto3

def lambda_handler(event, context):
    # get email of new account
    email = event['request']['userAttributes']['email']
    
    # check if email has already been used
    client = boto3.client('cognito-idp')
    response = client.list_users(
        UserPoolId='ap-southeast-1_8ZjfRj8c6',
        AttributesToGet=['email']
        )

    for user in response['Users']:
        for attr in user['Attributes']:
            if attr['Name'] == 'email':
                existing_email = attr['Value']
                
                if email == existing_email:
                    raise Exception("Email address already in-use.")
                        
                break
    
    # sets the user pool autoConfirmUser flag to true
    # without any validation
    event['response']['autoConfirmUser'] = True
    event['response']['autoVerifyEmail'] = True
    
    print(event)

    # Return to Amazon Cognito
    return event

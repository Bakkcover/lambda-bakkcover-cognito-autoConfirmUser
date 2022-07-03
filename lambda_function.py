def lambda_handler(event, context):
    # sets the user pool autoConfirmUser flag to true
    # without any validation
    event['response']['autoConfirmUser'] = True
    
    print(event)

    # Return to Amazon Cognito
    return event

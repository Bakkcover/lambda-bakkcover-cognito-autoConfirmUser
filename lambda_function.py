def lambda_handler(event, context):
    # sets the user pool autoConfirmUser flag to true
    # without any validation
    event['response']['autoConfirmUser'] = True

    # test if auto-deploy works
    print(event)

    # Return to Amazon Cognito
    return event

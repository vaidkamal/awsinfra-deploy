import aws_cdk as core
import aws_cdk.assertions as assertions

from awsinfra_deploy.awsinfra_deploy_stack import AwsinfraDeployStack

# example tests. To run these tests, uncomment this file along with the example
# resource in awsinfra_deploy/awsinfra_deploy_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsinfraDeployStack(app, "awsinfra-deploy")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

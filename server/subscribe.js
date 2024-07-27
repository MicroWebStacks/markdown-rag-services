import { SNSClient, SubscribeCommand } from '@aws-sdk/client-sns';
import * as dotenv from 'dotenv'
dotenv.config()
import { fileURLToPath } from 'url';

import * as dotenv from 'dotenv'
dotenv.config()

const snsClient = new SNSClient({ 
  region: process.env.aws_region,
  credentials: { 
    accessKeyId: process.env.aws_access_key_id,
    secretAccessKey: process.env.aws_secret_access_key 
  } 
});

export const subscribeApp = async (topicArn,endpoint) => {
    const response = await snsClient.send(
      new SubscribeCommand({
        Protocol: "application",
        TopicArn: topicArn,
        Endpoint: endpoint,
      }),
    );
    console.log(response);
    return response;
  };
// snippet-end:[sns.JavaScript.subscriptions.subscribeAppV3]
  
// Invoke main function if this file was run directly.
if (process.argv[1] === fileURLToPath(import.meta.url)) {
    subscribeApp(
        process.env.SNS_TOPIC_ARN,
        process.env.SNS_ENDPOINT
    );
}

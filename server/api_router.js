import express from 'express';
import { SNSClient, ConfirmSubscriptionCommand } from '@aws-sdk/client-sns';
import * as dotenv from 'dotenv'
dotenv.config()

async function handleSNSMessage(req,res){
  const messageType = req.headers['x-amz-sns-message-type'];

  if (messageType === 'SubscriptionConfirmation') {
    const params = {
      Token: req.body.Token,
      TopicArn: req.body.TopicArn,
    };
    console.log(`setting Token '${params.Token}' and TopicArn '${params.TopicArn}'`)
    try {
      const data = await snsClient.send(new ConfirmSubscriptionCommand(params));
      console.log("Subscription confirmed:", data);
      res.status(200).send('Subscription confirmed');
    } catch (err) {
      console.error("Error confirming subscription:", err);
      res.status(500).send('Error');
    }
  } else if (messageType === 'Notification') {
    console.log("Message received:", req.body.Message);
    res.status(200).send('Message received');
  } else {
    res.status(400).send('Unknown message type');
  }
}

const apiHandler = async (req, res, next) => {
  console.log(`Received "${req.method}" request for "${req.path}"`);
  if (req.headers['x-amz-sns-message-type']) {
    handleSNSMessage(req, res);
  }else{
    res.status(200).json({ message: 'OK' });
  }
};

const snsClient = new SNSClient({ 
  region: process.env.aws_region,
  credentials: { 
    accessKeyId: process.env.aws_access_key_id,
    secretAccessKey: process.env.aws_secret_access_key 
  } 
});

const apiRouter = express.Router();

apiRouter.use(express.json());

apiRouter.get("/*", apiHandler);  // If you expect GET requests
apiRouter.post("/*", apiHandler);  // SNS uses POST requests for messages, consider adding this

export {
    apiRouter
};

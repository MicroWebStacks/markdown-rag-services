import express from 'express';
import fetch from 'node-fetch';  // You may need to install node-fetch using pnpm if not already available

const apiHandler = async (req, res, next) => {
  console.log(`Received ${req.method} request for ${req.path}`);

  // Log query parameters and body if available
  if (req.query && Object.keys(req.query).length > 0) {
    console.log('Query Parameters:', req.query);
  }
  if (req.body && Object.keys(req.body).length > 0) {
    console.log('Request Body:', req.body);
  }

  // Log all header keys
  console.log('Header Keys:', Object.keys(req.headers));


  // Check if this is an SNS Message
  if (req.headers['x-amz-sns-message-type']) {
    // Handle SNS messages
    handleSNSMessage(req.body, res);
  } else {
    // If not an SNS message, continue as normal
    res.status(200).json({ message: 'OK' });
  }
};

const handleSNSMessage = async (snsMessage, res) => {
  console.log("snsMessage")
  console.log(snsMessage)
  switch (snsMessage.Type) {
    case 'SubscriptionConfirmation':
      // Confirm subscription by visiting the SubscribeURL from the SNS message
      const confirmationResponse = await fetch(snsMessage.SubscribeURL);
      const confirmationData = await confirmationResponse.text();
      console.log('Subscription confirmation response:', confirmationData);
      res.status(200).json({ message: 'Subscription confirmed' });
      break;
    case 'Notification':
      // Handle notifications here
      console.log('Received notification:', snsMessage.Message);
      res.status(200).json({ message: 'Notification processed' });
      break;
    default:
      res.status(400).json({ message: 'Invalid SNS message type' });
      break;
  }
};

const apiRouter = express.Router();

apiRouter.use(express.json());

apiRouter.get("/*", apiHandler);  // If you expect GET requests
apiRouter.post("/*", apiHandler);  // SNS uses POST requests for messages, consider adding this

export {
    apiRouter
};

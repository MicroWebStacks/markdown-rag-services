import express from 'express'

const apiHandler = (req, res, next) => {
  // Logging the method, path, and possibly query or params
  console.log(`Received ${req.method} request for ${req.path}`);
  if (req.query && Object.keys(req.query).length > 0) {
    console.log('Query Parameters:', req.query);
  }
  if (req.params && Object.keys(req.params).length > 0) {
    console.log('Path Parameters:', req.params);
  }
  if (req.body && Object.keys(req.body).length > 0) {
    console.log('Request Body:', req.body);
  }

  // Always respond with status 200 and message "OK"
  res.status(200).json({ message: 'OK' });
};

const apiRouter = express.Router()

apiRouter.use(express.json());

apiRouter.get("/*",apiHandler)

export{
    apiRouter
}
